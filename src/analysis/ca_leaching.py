"""
Calcium Leaching Analysis

Ca 용출 분석 함수
"""

import numpy as np
from typing import Dict, List
from pathlib import Path

from ase.io import read


def analyze_ca_leaching(
    trajectory_path: Path,
    distance_threshold: float = 3.0
) -> Dict:
    """
    Ca 용출 분석
    
    Parameters
    ----------
    trajectory_path : Path
        궤적 파일 경로
    distance_threshold : float
        용출 판정 거리 기준 (Å)
    
    Returns
    -------
    dict
        분석 결과
    """
    # 궤적 로딩
    trajectory = read(trajectory_path, index=':')
    
    if len(trajectory) == 0:
        return {
            'n_ca': 0,
            'initial_leached': 0,
            'final_leached': 0,
            'max_leached': 0,
            'rate_per_ps': 0.0,
            'leached_counts': []
        }
    
    # 첫 프레임에서 Ca 인덱스 식별
    first_frame = trajectory[0]
    symbols = first_frame.get_chemical_symbols()
    ca_indices = [i for i, s in enumerate(symbols) if s == 'Ca']
    
    if len(ca_indices) == 0:
        return {
            'n_ca': 0,
            'initial_leached': 0,
            'final_leached': 0,
            'max_leached': 0,
            'rate_per_ps': 0.0,
            'leached_counts': []
        }
    
    # 초기 Ca 위치
    initial_ca_positions = first_frame.get_positions()[ca_indices]
    
    # 각 프레임에서 용출된 Ca 수 계산
    leached_counts = []
    
    for frame in trajectory:
        current_positions = frame.get_positions()[ca_indices]
        
        # 각 Ca의 이동 거리
        displacements = np.linalg.norm(
            current_positions - initial_ca_positions, axis=1
        )
        
        # 임계값 이상 이동한 Ca 수
        n_leached = np.sum(displacements > distance_threshold)
        leached_counts.append(int(n_leached))
    
    # 시뮬레이션 시간 추정 (프레임 수 기반, 10 fs 간격 가정)
    duration_ps = len(trajectory) * 0.01  # 10 fs = 0.01 ps
    
    # 용출 속도 계산
    if duration_ps > 0:
        rate_per_ps = (leached_counts[-1] - leached_counts[0]) / duration_ps
    else:
        rate_per_ps = 0.0
    
    return {
        'n_ca': len(ca_indices),
        'initial_leached': leached_counts[0],
        'final_leached': leached_counts[-1],
        'max_leached': max(leached_counts),
        'rate_per_ps': float(rate_per_ps),
        'leached_counts': leached_counts
    }
