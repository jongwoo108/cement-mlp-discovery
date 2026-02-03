"""
MatterGen 구조 생성 스크립트
계획에 따른 Phase별 구조 생성을 수행합니다.
"""

import os
import sys
from pathlib import Path

# 프로젝트 경로 설정
PROJECT_ROOT = Path(__file__).parent.parent
MATTERGEN_REPO = PROJECT_ROOT / 'mattergen'
OUTPUT_DIR = PROJECT_ROOT / 'data' / 'mattergen'

# MatterGen 경로를 Python 경로에 추가
sys.path.insert(0, str(MATTERGEN_REPO))
os.chdir(MATTERGEN_REPO)

print(f"Project Root: {PROJECT_ROOT}")
print(f"MatterGen Repo: {MATTERGEN_REPO}")
print(f"Output Dir: {OUTPUT_DIR}")

# MatterGen import
from mattergen.generator import CrystalGenerator

def generate_structures(
    model_name: str,
    output_name: str,
    properties: dict,
    batch_size: int = 4,
    num_batches: int = 2,
    guidance_factor: float = 2.0
):
    """
    MatterGen으로 구조 생성
    """
    output_path = OUTPUT_DIR / output_name
    output_path.mkdir(parents=True, exist_ok=True)
    
    checkpoint_path = MATTERGEN_REPO / 'checkpoints' / model_name
    
    print(f"\n{'='*60}")
    print(f"MatterGen Generation")
    print(f"{'='*60}")
    print(f"Model: {model_name}")
    print(f"Checkpoint: {checkpoint_path}")
    print(f"Output: {output_path}")
    print(f"Properties: {properties}")
    print(f"Total structures: {batch_size * num_batches}")
    print(f"{'='*60}\n")
    
    # Generator 초기화
    generator = CrystalGenerator(
        model_path=str(checkpoint_path),
        batch_size=batch_size,
        num_batches=num_batches,
        properties_to_condition_on=properties,
        diffusion_guidance_factor=guidance_factor
    )
    
    # 생성 실행
    generator.generate(output_dir=output_path)
    
    print(f"\n[SUCCESS] Generation complete!")
    print(f"Output saved to: {output_path}")
    
    # 생성된 파일 확인
    for f in output_path.iterdir():
        size = f.stat().st_size / 1024
        print(f"  - {f.name} ({size:.1f} KB)")
    
    return output_path


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='MatterGen structure generation')
    parser.add_argument('--phase', type=int, default=1, help='Phase number (1, 2, or 3)')
    args = parser.parse_args()
    
    if args.phase == 1:
        # Phase 1.1: Ca-Si-Al-O (FlyAshC 기반)
        generate_structures(
            model_name='chemical_system_energy_above_hull',
            output_name='phase1_Ca_Si_Al_O',
            properties={
                'chemical_system': 'Ca-Si-Al-O',
                'energy_above_hull': 0.05
            },
            batch_size=4,
            num_batches=2
        )
        
        # Phase 1.2: Ca-Si-Al-Fe-O (EAFSlag 기반)
        generate_structures(
            model_name='chemical_system_energy_above_hull',
            output_name='phase1_Ca_Si_Al_Fe_O',
            properties={
                'chemical_system': 'Ca-Si-Al-Fe-O',
                'energy_above_hull': 0.05
            },
            batch_size=4,
            num_batches=2
        )
    
    elif args.phase == 2:
        # Phase 2.1: Ca-Si-O (안정 구조)
        generate_structures(
            model_name='chemical_system_energy_above_hull',
            output_name='phase2_Ca_Si_O_stable',
            properties={
                'chemical_system': 'Ca-Si-O',
                'energy_above_hull': 0.0
            },
            batch_size=4,
            num_batches=2
        )
        
        # Phase 2.2: Ca-Si-Mg-O
        generate_structures(
            model_name='chemical_system_energy_above_hull',
            output_name='phase2_Ca_Si_Mg_O',
            properties={
                'chemical_system': 'Ca-Si-Mg-O',
                'energy_above_hull': 0.05
            },
            batch_size=4,
            num_batches=2
        )
    
    elif args.phase == 3:
        # Phase 3: 벌크 모듈러스 기반 역설계
        generate_structures(
            model_name='ml_bulk_modulus',
            output_name='phase3_high_bulk_modulus',
            properties={
                'ml_bulk_modulus': 100.0  # GPa
            },
            batch_size=4,
            num_batches=2
        )
    
    print("\n[DONE] All generations complete!")
