"""
Silicon Coordination Analysis

Si 배위수 분석 함수
"""

import numpy as np
from typing import Dict, List
from pathlib import Path

from ase.io import read


def analyze_si_coordination(
    trajectory_path: Path,
    cutoff: float = 2.5
) -> Dict:
    """
    Si 배위수 분석
    
    Parameters
    ----------
    trajectory_path : Path
        궤적 파일 경로
    cutoff : float
        Si-O 결합 판정 거리 (Å)
    
    Returns
    -------
    dict
        분석 결과
    """
    # 궤적 로딩
    trajectory = read(trajectory_path, index=':')
    
    if len(trajectory) == 0:
        return {
            'n_si': 0,
            'initial_cn': 0.0,
            'final_cn': 0.0,
            'mean_cn': 0.0,
            'cn_evolution': []
        }
    
    # 첫 프레임에서 Si, O 인덱스 식별
    first_frame = trajectory[0]
    symbols = first_frame.get_chemical_symbols()
    si_indices = [i for i, s in enumerate(symbols) if s == 'Si']
    o_indices = [i for i, s in enumerate(symbols) if s == 'O']
    
    if len(si_indices) == 0:
        return {
            'n_si': 0,
            'initial_cn': 0.0,
            'final_cn': 0.0,
            'mean_cn': 0.0,
            'cn_evolution': []
        }
    
    # 각 프레임에서 평균 Si 배위수 계산
    cn_evolution = []
    
    for frame in trajectory:
        positions = frame.get_positions()
        cell = frame.get_cell()
        
        si_positions = positions[si_indices]
        o_positions = positions[o_indices]
        
        # 각 Si의 배위수
        cn_per_si = []
        for si_pos in si_positions:
            # Si-O 거리 계산 (PBC 고려)
            distances = []
            for o_pos in o_positions:
                diff = o_pos - si_pos
                # 최소 이미지 규약 (간단 버전)
                if cell.any():
                    for i in range(3):
                        if cell[i, i] > 0:
                            while diff[i] > cell[i, i] / 2:
                                diff[i] -= cell[i, i]
                            while diff[i] < -cell[i, i] / 2:
                                diff[i] += cell[i, i]
                dist = np.linalg.norm(diff)
                distances.append(dist)
            
            # cutoff 이내의 O 원자 수
            cn = sum(1 for d in distances if d < cutoff)
            cn_per_si.append(cn)
        
        mean_cn = np.mean(cn_per_si) if cn_per_si else 0.0
        cn_evolution.append(float(mean_cn))
    
    return {
        'n_si': len(si_indices),
        'initial_cn': cn_evolution[0],
        'final_cn': cn_evolution[-1],
        'mean_cn': float(np.mean(cn_evolution)),
        'cn_evolution': cn_evolution
    }
