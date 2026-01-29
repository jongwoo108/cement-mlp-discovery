"""
Automated Screening Pipeline

자동화 스크리닝 파이프라인
"""

import json
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Callable

from src import STRUCTURES_DIR, TRAJECTORIES_DIR, RESULTS_DIR
from src.core import optimize_structure, run_md_simulation, create_hydration_system
from src.core.structure import create_model_structure, save_structure
from src.analysis import (
    analyze_ca_leaching, 
    analyze_si_coordination, 
    analyze_csh_formation,
    calculate_screening_score
)
from src.database.candidates import Candidate, CandidateDatabase


class ScreeningPipeline:
    """자동화 스크리닝 파이프라인"""
    
    def __init__(
        self,
        config: Dict,
        output_dir: Optional[Path] = None,
        verbose: bool = True
    ):
        """
        Parameters
        ----------
        config : dict
            시뮬레이션 설정
        output_dir : Path, optional
            출력 디렉토리
        verbose : bool
            상세 출력 여부
        """
        self.config = config
        self.output_dir = output_dir or RESULTS_DIR
        self.verbose = verbose
        
        self.results: Dict[str, Dict] = {}
        self.errors: Dict[str, str] = {}
        
    def run(
        self, 
        candidates: List[Candidate],
        progress_callback: Optional[Callable] = None
    ) -> Dict[str, Dict]:
        """
        전체 후보에 대해 스크리닝 실행
        
        Parameters
        ----------
        candidates : list
            후보 재료 목록
        progress_callback : Callable, optional
            진행 상황 콜백
        
        Returns
        -------
        dict
            스크리닝 결과
        """
        total = len(candidates)
        start_time = time.time()
        
        if self.verbose:
            print("=" * 60)
            print("AUTOMATED SCREENING PIPELINE")
            print("=" * 60)
            print(f"\nCandidates: {total}")
            print(f"Duration: {self.config['md_simulation']['screening']['duration_ps']} ps each")
            
            # 예상 시간 계산
            est_time_per_candidate = 15  # 분
            est_total = total * est_time_per_candidate
            print(f"Estimated time: ~{est_total} min ({est_total/60:.1f} hours)")
            print()
        
        candidate_times = []
        
        for i, candidate in enumerate(candidates):
            candidate_start = time.time()
            
            if self.verbose:
                # 전체 진행 바
                progress = (i) / total
                bar_len = 30
                filled = int(bar_len * progress)
                bar = "█" * filled + "░" * (bar_len - filled)
                
                print(f"\n{'='*60}")
                print(f"[{bar}] {i}/{total} ({progress*100:.0f}%)")
                print(f"{'='*60}")
                print(f"Material: {candidate.name} (Tier {candidate.tier})")
                print(f"Formula: {candidate.formula}")
                print(f"CO₂ Reduction: {candidate.co2_reduction}%")
                print("-" * 40)
                
                # ETA 계산
                if candidate_times:
                    avg_time = sum(candidate_times) / len(candidate_times)
                    remaining = total - i
                    eta_min = (avg_time * remaining) / 60
                    print(f"ETA: ~{eta_min:.0f} min remaining")
            
            try:
                result = self._process_candidate(candidate)
                self.results[candidate.name] = result
                
                candidate_elapsed = time.time() - candidate_start
                candidate_times.append(candidate_elapsed)
                
                if self.verbose:
                    score = result.get('score', {})
                    print(f"\n  ✓ {candidate.name} Complete!")
                    print(f"    Score: {score.get('total_score', 'N/A')}/100 (Grade {score.get('grade', 'N/A')})")
                    print(f"    Time: {candidate_elapsed/60:.1f} min")
                    
            except Exception as e:
                self.errors[candidate.name] = str(e)
                candidate_times.append(time.time() - candidate_start)
                if self.verbose:
                    print(f"\n  ✗ {candidate.name} Failed: {e}")
            
            if progress_callback:
                progress_callback(i + 1, total)
        
        elapsed = time.time() - start_time
        
        if self.verbose:
            # 최종 진행 바
            bar = "█" * 30
            print(f"\n{'='*60}")
            print(f"[{bar}] {total}/{total} (100%)")
            print(f"{'='*60}")
            print(f"COMPLETED: {len(self.results)}/{total} successful")
            if self.errors:
                print(f"FAILED: {len(self.errors)}")
            print(f"Total Time: {elapsed/60:.1f} min ({elapsed/3600:.2f} hours)")
            print("=" * 60)
        
        return self.results
    
    def _process_candidate(self, candidate: Candidate) -> Dict:
        """단일 후보 처리"""
        result = {
            'name': candidate.name,
            'formula': candidate.formula,
            'co2_reduction': candidate.co2_reduction,
            'source': candidate.source
        }
        
        # 1. 구조 생성
        atoms = create_model_structure(
            composition=candidate.composition,
            volume=candidate.volume,
            name=candidate.name
        )
        result['initial_atoms'] = len(atoms)
        
        # 2. 구조 최적화
        opt_config = self.config['optimization']
        optimized, opt_meta = optimize_structure(
            atoms,
            fmax=opt_config['fmax'],
            max_steps=opt_config['max_steps'],
            save_path=STRUCTURES_DIR / f"{candidate.name}_optimized.cif",
            verbose=self.verbose
        )
        result['optimization'] = opt_meta
        
        # 3. 수화 시스템 생성
        hyd_config = self.config['hydration']
        hydrated = create_hydration_system(
            optimized,
            n_water=hyd_config['n_water'],
            save_path=STRUCTURES_DIR / f"{candidate.name}_hydration.cif",
            verbose=self.verbose
        )
        result['hydrated_atoms'] = len(hydrated)
        
        # 4. MD 시뮬레이션
        md_config = self.config['md_simulation']['screening']
        md_meta = run_md_simulation(
            hydrated,
            name=candidate.name,
            duration_ps=md_config['duration_ps'],
            temperature=md_config['temperature_K'],
            timestep_fs=md_config['timestep_fs'],
            verbose=self.verbose
        )
        result['md_simulation'] = md_meta
        
        # 5. 분석
        traj_path = Path(md_meta['trajectory_file'])
        analysis_config = self.config['analysis']
        
        ca_result = analyze_ca_leaching(
            traj_path, 
            distance_threshold=analysis_config['ca_leaching_threshold']
        )
        si_result = analyze_si_coordination(
            traj_path,
            cutoff=analysis_config['si_coordination_cutoff']
        )
        csh_result = analyze_csh_formation(
            traj_path,
            ca_si_cutoff=analysis_config['csh_pair_cutoff']
        )
        
        result['analysis'] = {
            'ca_leaching': ca_result,
            'si_coordination': si_result,
            'csh_formation': csh_result
        }
        
        # 6. 점수 계산
        score = calculate_screening_score(
            co2_reduction=candidate.co2_reduction,
            ca_leaching_rate=ca_result['rate_per_ps'],
            si_coordination=si_result['mean_cn'],
            csh_pairs=csh_result['max_pairs']
        )
        result['score'] = score
        
        return result
    
    def save_results(self, filename: str = "screening_results.json") -> Path:
        """결과 저장"""
        output_path = self.output_dir / filename
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # numpy 타입 변환
        def convert(obj):
            if hasattr(obj, 'item'):
                return obj.item()
            elif hasattr(obj, 'tolist'):
                return obj.tolist()
            elif isinstance(obj, dict):
                return {k: convert(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert(v) for v in obj]
            return obj
        
        results_data = {
            'timestamp': datetime.now().isoformat(),
            'config': self.config,
            'results': convert(self.results),
            'errors': self.errors
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(results_data, f, indent=2, ensure_ascii=False)
        
        return output_path
    
    def get_rankings(self) -> List[Dict]:
        """점수 순위 반환"""
        rankings = []
        for name, result in self.results.items():
            rankings.append({
                'name': name,
                'score': result['score']['total_score'],
                'grade': result['score']['grade'],
                'co2_reduction': result['co2_reduction']
            })
        
        return sorted(rankings, key=lambda x: x['score'], reverse=True)
