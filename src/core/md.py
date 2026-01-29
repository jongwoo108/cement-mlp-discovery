"""
Molecular Dynamics Simulation

분자동역학 시뮬레이션 함수
"""

import time
from typing import Optional, Callable
from pathlib import Path

from ase import Atoms, units
from ase.md.nvtberendsen import NVTBerendsen
from ase.io.trajectory import Trajectory

from .calculator import get_calculator


def run_md_simulation(
    atoms: Atoms,
    name: str,
    duration_ps: float = 10.0,
    temperature: float = 300.0,
    timestep_fs: float = 1.0,
    save_interval: int = 10,
    trajectory_dir: Optional[Path] = None,
    use_gpu: bool = True,
    progress_callback: Optional[Callable] = None,
    progress_interval: float = 1.0,
    verbose: bool = True
) -> dict:
    """
    NVT MD 시뮬레이션 실행
    
    Parameters
    ----------
    atoms : Atoms
        시뮬레이션할 시스템
    name : str
        시스템 이름 (파일 저장용)
    duration_ps : float
        시뮬레이션 시간 (ps)
    temperature : float
        온도 (K)
    timestep_fs : float
        타임스텝 (fs)
    save_interval : int
        궤적 저장 간격 (스텝)
    trajectory_dir : Path, optional
        궤적 저장 디렉토리
    use_gpu : bool
        GPU 사용 여부
    progress_callback : Callable, optional
        진행 상황 콜백 함수
    progress_interval : float
        진행 상황 업데이트 간격 (ps)
    verbose : bool
        출력 여부
    
    Returns
    -------
    dict
        시뮬레이션 결과 메타데이터
    """
    from src import TRAJECTORIES_DIR
    
    start_time = time.time()
    
    # 계산기 설정
    calc = get_calculator(use_gpu)
    atoms.calc = calc
    
    # 궤적 파일 경로
    if trajectory_dir is None:
        trajectory_dir = TRAJECTORIES_DIR
    trajectory_dir = Path(trajectory_dir)
    trajectory_dir.mkdir(parents=True, exist_ok=True)
    
    traj_file = trajectory_dir / f"{name}_hydration.traj"
    
    # 총 스텝 수
    total_steps = int(duration_ps * 1000 / timestep_fs)
    steps_per_interval = int(progress_interval * 1000 / timestep_fs)
    n_intervals = int(duration_ps / progress_interval)
    
    if verbose:
        print(f"Running MD for {name} ({duration_ps} ps)...")
        print(f"  Total: {total_steps:,} steps ({duration_ps} ps)")
    
    # MD 설정
    dyn = NVTBerendsen(
        atoms,
        timestep=timestep_fs * units.fs,
        temperature_K=temperature,
        taut=100 * units.fs
    )
    
    # 궤적 저장
    traj = Trajectory(str(traj_file), 'w', atoms)
    dyn.attach(traj.write, interval=save_interval)
    
    # 진행 상황 표시하며 실행
    for i in range(n_intervals):
        interval_start = time.time()
        dyn.run(steps_per_interval)
        interval_time = time.time() - interval_start
        
        if verbose:
            current_ps = (i + 1) * progress_interval
            progress = current_ps / duration_ps
            elapsed = time.time() - start_time
            eta = elapsed / progress - elapsed if progress > 0 else 0
            
            bar_len = 20
            filled = int(bar_len * progress)
            bar = "█" * filled + "░" * (bar_len - filled)
            
            print(f"\r  Progress: [{bar}] {progress*100:.1f}% | "
                  f"{current_ps:.1f}/{duration_ps} ps | "
                  f"ETA: {eta:.0f}s", end="", flush=True)
        
        if progress_callback:
            progress_callback(i + 1, n_intervals)
    
    traj.close()
    
    elapsed_time = time.time() - start_time
    
    if verbose:
        print(f"\n  ✓ Completed in {elapsed_time:.0f}s")
        print(f"  ✓ Saved: {traj_file.name}")
    
    # 메타데이터
    metadata = {
        "name": name,
        "trajectory_file": str(traj_file),
        "duration_ps": duration_ps,
        "temperature_K": temperature,
        "timestep_fs": timestep_fs,
        "total_steps": total_steps,
        "elapsed_time": elapsed_time,
        "atoms_count": len(atoms)
    }
    
    return metadata
