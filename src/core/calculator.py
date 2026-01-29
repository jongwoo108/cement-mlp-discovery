"""
CHGNet Calculator and Structure Optimization

CHGNet 기반 계산기 초기화 및 구조 최적화 함수
"""

import time
from typing import Optional, Tuple
from pathlib import Path

from ase import Atoms
from ase.optimize import BFGS
from ase.io import write


def get_calculator(use_gpu: bool = True):
    """
    CHGNet 계산기 초기화
    
    Parameters
    ----------
    use_gpu : bool
        GPU 사용 여부 (기본값: True)
    
    Returns
    -------
    CHGNetCalculator
        초기화된 CHGNet 계산기
    """
    from chgnet.model import CHGNetCalculator
    
    device = "cuda" if use_gpu else "cpu"
    calculator = CHGNetCalculator(use_device=device)
    
    return calculator


def optimize_structure(
    atoms: Atoms,
    fmax: float = 0.05,
    max_steps: int = 500,
    use_gpu: bool = True,
    save_path: Optional[Path] = None,
    verbose: bool = True
) -> Tuple[Atoms, dict]:
    """
    구조 최적화 수행
    
    Parameters
    ----------
    atoms : Atoms
        최적화할 ASE Atoms 객체
    fmax : float
        최대 힘 수렴 기준 (eV/Å)
    max_steps : int
        최대 최적화 스텝 수
    use_gpu : bool
        GPU 사용 여부
    save_path : Path, optional
        최적화된 구조 저장 경로
    verbose : bool
        진행 상황 출력 여부
    
    Returns
    -------
    Tuple[Atoms, dict]
        최적화된 구조와 메타데이터
    """
    start_time = time.time()
    
    # 계산기 설정
    calc = get_calculator(use_gpu)
    atoms.calc = calc
    
    # 초기 에너지
    initial_energy = atoms.get_potential_energy()
    
    # 최적화
    optimizer = BFGS(atoms, logfile=None)
    
    try:
        optimizer.run(fmax=fmax, steps=max_steps)
        converged = optimizer.converged()
    except Exception as e:
        converged = False
        if verbose:
            print(f"  Warning: Optimization error - {e}")
    
    # 최종 상태
    final_energy = atoms.get_potential_energy()
    final_fmax = atoms.get_forces().max()
    
    elapsed_time = time.time() - start_time
    
    # 메타데이터
    metadata = {
        "initial_energy": float(initial_energy),
        "final_energy": float(final_energy),
        "energy_per_atom": float(final_energy / len(atoms)),
        "fmax": float(final_fmax),
        "steps": optimizer.nsteps,
        "converged": converged,
        "elapsed_time": elapsed_time
    }
    
    if verbose:
        status = "✓" if converged else f"(not converged)"
        print(f"  Steps: {optimizer.nsteps}")
        print(f"  Time: {elapsed_time:.1f}s")
        print(f"  Energy: {initial_energy:.2f} → {final_energy:.2f} eV")
        print(f"  Fmax: {final_fmax:.4f} eV/Å {status}")
    
    # 저장
    if save_path:
        write(save_path, atoms)
        if verbose:
            print(f"\n✓ Saved: {save_path.name}")
    
    return atoms, metadata
