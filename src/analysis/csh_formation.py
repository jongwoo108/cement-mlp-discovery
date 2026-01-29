"""
C-S-H Formation Analysis

C-S-H 젤 형성 분석 함수
"""

import numpy as np
from typing import Dict, List
from pathlib import Path

from ase.io import read


def analyze_csh_formation(
    trajectory_path: Path,
    ca_si_cutoff: float = 3.5
) -> Dict:
    """
    C-S-H 형성 분석 (Ca-Si 근접 쌍 수)
    
    Parameters
    ----------
    trajectory_path : Path
        궤적 파일 경로
    ca_si_cutoff : float
        Ca-Si 근접 판정 거리 (Å)
    
    Returns
    -------
    dict
        분석 결과
    """
    # 궤적 로딩
    trajectory = read(trajectory_path, index=':')
    
    if len(trajectory) == 0:
        return {
            'initial_pairs': 0,
            'final_pairs': 0,
            'max_pairs': 0,
            'min_distance': 0.0,
            'pairs_evolution': []
        }
    
    # 첫 프레임에서 Ca, Si 인덱스 식별
    first_frame = trajectory[0]
    symbols = first_frame.get_chemical_symbols()
    ca_indices = [i for i, s in enumerate(symbols) if s == 'Ca']
    si_indices = [i for i, s in enumerate(symbols) if s == 'Si']
    
    if len(ca_indices) == 0 or len(si_indices) == 0:
        return {
            'initial_pairs': 0,
            'final_pairs': 0,
            'max_pairs': 0,
            'min_distance': 0.0,
            'pairs_evolution': []
        }
    
    # 각 프레임에서 Ca-Si 근접 쌍 수 계산
    pairs_evolution = []
    all_min_distances = []
    
    for frame in trajectory:
        positions = frame.get_positions()
        cell = frame.get_cell()
        
        ca_positions = positions[ca_indices]
        si_positions = positions[si_indices]
        
        # Ca-Si 쌍 계산
        n_pairs = 0
        frame_min_dist = float('inf')
        
        for ca_pos in ca_positions:
            for si_pos in si_positions:
                diff = si_pos - ca_pos
                # 최소 이미지 규약 (간단 버전)
                if cell.any():
                    for i in range(3):
                        if cell[i, i] > 0:
                            while diff[i] > cell[i, i] / 2:
                                diff[i] -= cell[i, i]
                            while diff[i] < -cell[i, i] / 2:
                                diff[i] += cell[i, i]
                dist = np.linalg.norm(diff)
                
                if dist < ca_si_cutoff:
                    n_pairs += 1
                
                frame_min_dist = min(frame_min_dist, dist)
        
        pairs_evolution.append(int(n_pairs))
        if frame_min_dist < float('inf'):
            all_min_distances.append(frame_min_dist)
    
    min_distance = min(all_min_distances) if all_min_distances else 0.0
    
    return {
        'initial_pairs': pairs_evolution[0],
        'final_pairs': pairs_evolution[-1],
        'max_pairs': max(pairs_evolution),
        'min_distance': float(min_distance),
        'pairs_evolution': pairs_evolution
    }
