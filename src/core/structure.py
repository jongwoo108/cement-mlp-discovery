"""
Structure Creation and Manipulation

구조 생성 및 조작 함수
"""

import numpy as np
from typing import Optional, Dict, Tuple
from pathlib import Path

from ase import Atoms
from ase.io import read, write
from ase.build import molecule


def load_structure(path: Path) -> Atoms:
    """구조 파일 로딩"""
    return read(path)


def save_structure(atoms: Atoms, path: Path) -> None:
    """구조 파일 저장"""
    write(path, atoms)


def get_composition(atoms: Atoms) -> Dict[str, int]:
    """원자 조성 반환"""
    from collections import Counter
    return dict(Counter(atoms.get_chemical_symbols()))


def add_water_molecules(
    atoms: Atoms,
    n_water: int = 10,
    min_distance: float = 2.5,
    box_expansion: float = 1.5,
    max_attempts: int = 1000
) -> Atoms:
    """
    구조에 물 분자 추가
    
    Parameters
    ----------
    atoms : Atoms
        원본 구조
    n_water : int
        추가할 물 분자 수
    min_distance : float
        최소 원자간 거리 (Å)
    box_expansion : float
        셀 확장 비율
    max_attempts : int
        각 물 분자당 최대 시도 횟수
    
    Returns
    -------
    Atoms
        물 분자가 추가된 구조
    """
    # 원본 복사
    system = atoms.copy()
    
    # 셀 확장 (필요시)
    cell = system.get_cell()
    if cell.any():
        new_cell = cell * box_expansion
        system.set_cell(new_cell, scale_atoms=False)
    else:
        # 셀이 없으면 생성
        positions = system.get_positions()
        max_pos = positions.max(axis=0)
        min_pos = positions.min(axis=0)
        size = (max_pos - min_pos) * box_expansion + 10.0
        system.set_cell(size)
        # 중앙 정렬
        center = size / 2
        current_center = (max_pos + min_pos) / 2
        system.translate(center - current_center)
    
    system.set_pbc(True)
    
    # 물 분자 템플릿
    water = molecule('H2O')
    
    cell_lengths = system.get_cell().lengths()
    added = 0
    
    for _ in range(n_water):
        for attempt in range(max_attempts):
            # 랜덤 위치
            pos = np.random.rand(3) * cell_lengths * 0.8 + cell_lengths * 0.1
            
            # 랜덤 회전
            angle = np.random.rand() * 2 * np.pi
            
            # 물 분자 복사 및 위치 설정
            new_water = water.copy()
            new_water.rotate(angle, 'z')
            new_water.translate(pos)
            
            # 거리 체크
            existing_positions = system.get_positions()
            water_positions = new_water.get_positions()
            
            min_dist = float('inf')
            for wp in water_positions:
                for ep in existing_positions:
                    dist = np.linalg.norm(wp - ep)
                    min_dist = min(min_dist, dist)
            
            if min_dist >= min_distance:
                system += new_water
                added += 1
                break
        
        if added < _ + 1:
            print(f"  Warning: Could only add {added}/{n_water} water molecules")
            break
    
    return system


def create_hydration_system(
    atoms: Atoms,
    n_water: int = 10,
    save_path: Optional[Path] = None,
    verbose: bool = True
) -> Atoms:
    """
    수화 시스템 생성
    
    Parameters
    ----------
    atoms : Atoms
        원본 구조
    n_water : int
        물 분자 수
    save_path : Path, optional
        저장 경로
    verbose : bool
        출력 여부
    
    Returns
    -------
    Atoms
        수화 시스템
    """
    if verbose:
        print(f"  Adding {n_water} water molecules...")
    
    hydrated = add_water_molecules(atoms, n_water=n_water)
    
    if verbose:
        comp = get_composition(hydrated)
        print(f"  Result: {hydrated.get_chemical_formula()}")
        print(f"  Atoms: {len(hydrated)}")
        print(f"  Composition: {comp}")
    
    if save_path:
        save_structure(hydrated, save_path)
        if verbose:
            print(f"  ✓ Saved: {save_path.name}")
    
    return hydrated


def create_model_structure(
    composition: Dict[str, int],
    volume: float,
    name: str = "model"
) -> Atoms:
    """
    주어진 조성으로 모델 구조 생성 (무작위 배치)
    
    Parameters
    ----------
    composition : dict
        원소별 원자 수 (예: {'Ca': 6, 'Si': 4, 'O': 16})
    volume : float
        목표 셀 부피 (Å³)
    name : str
        구조 이름
    
    Returns
    -------
    Atoms
        생성된 구조
    """
    # 총 원자 수
    total_atoms = sum(composition.values())
    
    # 셀 크기 (정육면체)
    cell_length = volume ** (1/3)
    
    # 원자 목록 생성
    symbols = []
    for element, count in composition.items():
        symbols.extend([element] * count)
    
    # 무작위 위치 생성
    positions = np.random.rand(total_atoms, 3) * cell_length * 0.8 + cell_length * 0.1
    
    # Atoms 객체 생성
    atoms = Atoms(
        symbols=symbols,
        positions=positions,
        cell=[cell_length, cell_length, cell_length],
        pbc=True
    )
    
    return atoms
