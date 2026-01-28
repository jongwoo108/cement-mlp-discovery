# API_REFERENCE.md

> 시멘트 연구를 위한 재사용 가능한 코드 패턴 및 함수

---

## 📚 코드 라이브러리

이 문서는 프로젝트 전반에서 사용되는 표준화된 코드 패턴을 포함합니다. 일관성을 유지하기 위해 이 스니펫을 복사하여 사용하세요.

---

## 🔧 1. 프로젝트 설정

### 표준 임포트

```python
# ========================================
# 시멘트 연구를 위한 표준 임포트
# ========================================
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import os
import time
from datetime import datetime

# ASE
from ase import Atoms
from ase.io import read, write
from ase.build import bulk, molecule
from ase.optimize import BFGS
from ase.io.trajectory import Trajectory

# CHGNet
import torch
from chgnet.model import CHGNet
from chgnet.model.dynamics import CHGNetCalculator, MolecularDynamics

# Materials Project
from pymatgen.io.ase import AseAtomsAdaptor
from mp_api.client import MPRester

# 분석
from scipy.spatial.distance import cdist
from scipy.signal import find_peaks
import psutil
```

### 프로젝트 설정

```python
# ========================================
# 프로젝트 설정
# ========================================
from pathlib import Path
import os

# 프로젝트 루트
WORK_DIR = Path("C:/cement_final")
os.chdir(WORK_DIR)

# 폴더 구조
FOLDERS = {
    'notebooks': WORK_DIR / "notebooks",
    'structures': WORK_DIR / "structures",
    'trajectories': WORK_DIR / "trajectories",
    'figures': WORK_DIR / "figures",
    'results': WORK_DIR / "results",
    'paper': WORK_DIR / "paper",
    'logs': WORK_DIR / "logs",
    'docs': WORK_DIR / "docs",
    'archive': WORK_DIR / "archive",
}

# 폴더 생성
for folder in FOLDERS.values():
    folder.mkdir(parents=True, exist_ok=True)

print(f"✅ 작업 디렉토리: {WORK_DIR}")
```

### GPU 설정

```python
# ========================================
# GPU 설정 확인
# ========================================
import torch

USE_GPU = torch.cuda.is_available()

if USE_GPU:
    gpu_name = torch.cuda.get_device_name(0)
    gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1e9
    print(f"🎮 GPU: {gpu_name}")
    print(f"   메모리: {gpu_memory:.1f} GB")
    DEVICE = 'cuda'
else:
    print("💻 CPU 모드")
    DEVICE = 'cpu'

# 재현성을 위한 시드 설정
torch.manual_seed(42)
if USE_GPU:
    torch.cuda.manual_seed(42)
```

---

## 🔬 2. CHGNet 작업

### CHGNet 모델 로드

```python
# ========================================
# CHGNet 로드
# ========================================
from chgnet.model import CHGNet

print("🔧 CHGNet 로딩 중...")
start = time.time()
chgnet = CHGNet.load()
load_time = time.time() - start

print(f"   ✅ {load_time:.1f}초 만에 로드됨")

# 전역 저장
globals()['CHGNET_MODEL'] = chgnet
```

### CHGNet 계산기 생성

```python
# ========================================
# CHGNet 계산기
# ========================================
from chgnet.model.dynamics import CHGNetCalculator

def get_chgnet_calculator(model=None, use_device=None):
    """
    일관된 설정으로 CHGNet 계산기 생성.

    Args:
        model: CHGNet 모델 (None이면 전역 사용)
        use_device: 'cuda' 또는 'cpu' (None이면 자동 감지)

    Returns:
        CHGNetCalculator 인스턴스
    """
    if model is None:
        model = globals().get('CHGNET_MODEL', CHGNet.load())

    if use_device is None:
        use_device = 'cuda' if torch.cuda.is_available() else 'cpu'

    calc = CHGNetCalculator(
        model=model,
        use_device=use_device
    )

    return calc

# 사용법
atoms.calc = get_chgnet_calculator()
```

---

## 🏗️ 3. 구조 작업

### 구조 로드

```python
# ========================================
# 구조 로드
# ========================================
from ase.io import read

def load_structure(filename, folder='structures'):
    """
    파일에서 구조 로드.

    Args:
        filename: 구조 파일명
        folder: 폴더 이름 (기본값: 'structures')

    Returns:
        ASE Atoms 객체
    """
    filepath = FOLDERS[folder] / filename

    if not filepath.exists():
        raise FileNotFoundError(f"구조를 찾을 수 없음: {filepath}")

    atoms = read(str(filepath))
    print(f"✅ 로드됨: {filename}")
    print(f"   원자: {len(atoms)}")
    print(f"   화학식: {atoms.get_chemical_formula()}")

    return atoms

# 사용법
c3s = load_structure('C3S_optimized.cif')
```

### 구조 저장

```python
# ========================================
# 구조 저장
# ========================================
from ase.io import write

def save_structure(atoms, filename, folder='structures', overwrite=False):
    """
    파일로 구조 저장.

    Args:
        atoms: ASE Atoms 객체
        filename: 출력 파일명
        folder: 폴더 이름 (기본값: 'structures')
        overwrite: 덮어쓰기 허용 (기본값: False)

    Returns:
        저장된 파일 경로
    """
    filepath = FOLDERS[folder] / filename

    if filepath.exists() and not overwrite:
        print(f"⚠️  파일 존재: {filename}")
        response = input("   덮어쓰기? (y/n): ")
        if response.lower() != 'y':
            print("   취소됨")
            return None

    write(str(filepath), atoms)
    print(f"✅ 저장됨: {filename}")
    print(f"   위치: {filepath}")

    return filepath

# 사용법
save_structure(atoms, 'my_structure.cif', overwrite=True)
```

### 구조 정보

```python
# ========================================
# 구조 정보
# ========================================
def print_structure_info(atoms, name="구조"):
    """
    포괄적인 구조 정보 출력.

    Args:
        atoms: ASE Atoms 객체
        name: 표시할 구조 이름
    """
    from collections import Counter

    print("="*70)
    print(f"{name} 정보")
    print("="*70)

    # 기본 정보
    print(f"\n📦 기본:")
    print(f"   화학식: {atoms.get_chemical_formula()}")
    print(f"   총 원자: {len(atoms)}")
    print(f"   부피: {atoms.get_volume():.2f} Å³")
    print(f"   밀도: {len(atoms)/atoms.get_volume()*1.66:.2f} g/cm³ (대략)")

    # 조성
    composition = Counter(atoms.get_chemical_symbols())
    print(f"\n🔬 조성:")
    for element, count in sorted(composition.items()):
        print(f"   {element}: {count}")

    # 셀
    cell = atoms.get_cell()
    print(f"\n📐 셀 파라미터:")
    print(f"   a: {cell[0,0]:.3f} Å")
    print(f"   b: {cell[1,1]:.3f} Å")
    print(f"   c: {cell[2,2]:.3f} Å")

    # 계산기
    if atoms.calc is not None:
        print(f"\n⚡ 계산기: {atoms.calc.__class__.__name__}")
        try:
            energy = atoms.get_potential_energy()
            print(f"   에너지: {energy:.4f} eV")
            print(f"   원자당 에너지: {energy/len(atoms):.4f} eV")
        except:
            print(f"   (에너지 사용 불가)")

    print("="*70)

# 사용법
print_structure_info(c3s, "C3S 최적화")
```

---

## ⚙️ 4. 구조 최적화

### BFGS 최적화

```python
# ========================================
# BFGS를 이용한 구조 최적화
# ========================================
from ase.optimize import BFGS
import time

def optimize_structure(atoms, fmax=0.05, steps=200,
                      trajectory=None, logfile=None):
    """
    BFGS를 사용하여 구조 최적화.

    Args:
        atoms: ASE Atoms 객체 (계산기 연결 필요)
        fmax: 힘 수렴 조건 (eV/Å)
        steps: 최대 최적화 단계
        trajectory: 궤적 파일 경로 (선택)
        logfile: 로그 파일 경로 (선택)

    Returns:
        최적화 결과를 담은 dict
    """
    print("="*70)
    print("구조 최적화")
    print("="*70)

    # 초기 상태
    print(f"\n⚡ 초기 상태:")
    initial_energy = atoms.get_potential_energy()
    initial_forces = atoms.get_forces()
    initial_fmax = np.abs(initial_forces).max()

    print(f"   에너지: {initial_energy:.4f} eV")
    print(f"   원자당 에너지: {initial_energy/len(atoms):.4f} eV")
    print(f"   최대 힘: {initial_fmax:.4f} eV/Å")

    # 최적화기 설정
    print(f"\n🔧 설정:")
    print(f"   방법: BFGS")
    print(f"   목표 Fmax: {fmax} eV/Å")
    print(f"   최대 단계: {steps}")

    # 경로를 문자열로 변환
    traj_str = str(trajectory) if trajectory else None
    log_str = str(logfile) if logfile else None

    optimizer = BFGS(
        atoms,
        trajectory=traj_str,
        logfile=log_str
    )

    # 최적화
    print(f"\n🚀 최적화 중...")
    start_time = time.time()

    try:
        optimizer.run(fmax=fmax, steps=steps)
        success = True
    except Exception as e:
        print(f"⚠️  최적화 중단: {e}")
        success = False

    elapsed = time.time() - start_time

    # 최종 상태
    final_energy = atoms.get_potential_energy()
    final_forces = atoms.get_forces()
    final_fmax = np.abs(final_forces).max()

    # 결과
    print(f"\n✅ 완료!")
    print(f"   시간: {elapsed:.1f}초")
    print(f"   단계: {optimizer.get_number_of_steps()}")

    print(f"\n📊 최종 상태:")
    print(f"   에너지: {final_energy:.4f} eV")
    print(f"   원자당 에너지: {final_energy/len(atoms):.4f} eV")
    print(f"   최대 힘: {final_fmax:.4f} eV/Å")
    print(f"   ΔE: {final_energy - initial_energy:.4f} eV")

    if final_fmax < fmax:
        print(f"   ✅ 수렴!")
    else:
        print(f"   ⚠️  미수렴 (Fmax = {final_fmax:.4f} > {fmax})")

    print("="*70)

    return {
        'success': success and (final_fmax < fmax),
        'steps': optimizer.get_number_of_steps(),
        'time': elapsed,
        'initial_energy': initial_energy,
        'final_energy': final_energy,
        'energy_change': final_energy - initial_energy,
        'initial_fmax': initial_fmax,
        'final_fmax': final_fmax,
    }

# 사용법
results = optimize_structure(
    atoms,
    fmax=0.05,
    trajectory=FOLDERS['trajectories'] / 'optimization.traj',
    logfile=FOLDERS['logs'] / 'optimization.log'
)
```

---

## 🌊 5. 분자 동역학

### MD 시뮬레이션

```python
# ========================================
# 분자 동역학 시뮬레이션
# ========================================
from chgnet.model.dynamics import MolecularDynamics

def run_md_simulation(atoms, duration_ps=1.0, temperature=300,
                     ensemble='nvt', timestep=1.0,
                     trajectory=None, logfile=None,
                     use_device=None):
    """
    분자 동역학 시뮬레이션 실행.

    Args:
        atoms: ASE Atoms 객체
        duration_ps: 시뮬레이션 시간 (피코초)
        temperature: 온도 (켈빈)
        ensemble: 'nvt' 또는 'nve'
        timestep: MD 시간 간격 (펨토초)
        trajectory: 궤적 파일 경로
        logfile: 로그 파일 경로
        use_device: 'cuda' 또는 'cpu'

    Returns:
        MolecularDynamics 객체
    """
    print("="*70)
    print("분자 동역학 시뮬레이션")
    print("="*70)

    # 단계 계산
    steps = int(duration_ps * 1000 / timestep)

    print(f"\n⚙️  설정:")
    print(f"   시간: {duration_ps} ps ({steps:,} 단계)")
    print(f"   시간 간격: {timestep} fs")
    print(f"   온도: {temperature} K")
    print(f"   앙상블: {ensemble.upper()}")

    if use_device is None:
        use_device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f"   장치: {use_device.upper()}")

    # 경로 변환
    traj_str = str(trajectory) if trajectory else None
    log_str = str(logfile) if logfile else None

    # MD 객체 생성
    md = MolecularDynamics(
        atoms=atoms,
        model=chgnet,
        ensemble=ensemble,
        temperature=temperature,
        timestep=timestep,
        trajectory=traj_str,
        logfile=log_str,
        loginterval=50,
        use_device=use_device
    )

    # 실행
    print(f"\n🚀 시뮬레이션 시작...")
    start_time = time.time()

    try:
        md.run(steps=steps)
        success = True
    except Exception as e:
        print(f"\n⚠️  시뮬레이션 오류: {e}")
        success = False

    elapsed = time.time() - start_time

    # 결과
    if success:
        print(f"\n✅ 완료!")
        print(f"   시간: {elapsed:.1f}초 ({elapsed/60:.1f}분)")
        print(f"   속도: {steps/elapsed:.1f} 단계/초")

        # 외삽
        time_10ps = (10.0 / duration_ps) * elapsed
        print(f"\n📈 외삽:")
        print(f"   10 ps 소요 예상: ~{time_10ps/60:.1f}분")
        print(f"   50 ps 소요 예상: ~{time_10ps*5/60:.1f}분")

    print("="*70)

    return md

# 사용법
md = run_md_simulation(
    atoms=system,
    duration_ps=1.0,
    temperature=300,
    trajectory=FOLDERS['trajectories'] / 'hydration.traj',
    logfile=FOLDERS['logs'] / 'hydration.log'
)
```

---

## 📊 6. 분석 함수

### RDF (방사 분포 함수)

```python
# ========================================
# 방사 분포 함수
# ========================================
def calculate_rdf(atoms, element1, element2, rmax=10.0, nbins=200):
    """
    방사 분포 함수 g(r) 계산.

    Args:
        atoms: ASE Atoms 객체
        element1: 첫 번째 원소 기호 (예: 'Ca')
        element2: 두 번째 원소 기호 (예: 'O')
        rmax: 최대 거리 (Å)
        nbins: 빈 개수

    Returns:
        r (배열), g_r (배열)
    """
    from scipy.spatial.distance import cdist

    # 위치 가져오기
    symbols = atoms.get_chemical_symbols()
    positions = atoms.get_positions()

    indices1 = [i for i, s in enumerate(symbols) if s == element1]
    indices2 = [i for i, s in enumerate(symbols) if s == element2]

    if len(indices1) == 0 or len(indices2) == 0:
        raise ValueError(f"{element1} 또는 {element2} 원자를 찾을 수 없음")

    pos1 = positions[indices1]
    pos2 = positions[indices2]

    # 거리 계산
    distances = cdist(pos1, pos2).flatten()

    # 히스토그램
    hist, bin_edges = np.histogram(distances, bins=nbins, range=(0, rmax))
    r = (bin_edges[:-1] + bin_edges[1:]) / 2
    dr = bin_edges[1] - bin_edges[0]

    # 정규화
    volume = atoms.get_volume()
    n1 = len(indices1)
    n2 = len(indices2)
    density = n2 / volume

    shell_volume = 4 * np.pi * r**2 * dr
    g_r = hist / (n1 * density * shell_volume)

    return r, g_r

# 사용법
r, g_r = calculate_rdf(atoms, 'Ca', 'O', rmax=10.0)
plt.plot(r, g_r)
plt.xlabel('r (Å)')
plt.ylabel('g(r)')
plt.title('Ca-O 방사 분포 함수')
```

### 결합 거리 분석

```python
# ========================================
# 결합 거리 분석
# ========================================
def analyze_bonds(atoms, element1, element2, cutoff=3.5):
    """
    두 원소 간 결합 거리 분석.

    Args:
        atoms: ASE Atoms 객체
        element1: 첫 번째 원소
        element2: 두 번째 원소
        cutoff: 최대 결합 거리 (Å)

    Returns:
        통계를 담은 dict
    """
    from scipy.spatial.distance import cdist

    symbols = atoms.get_chemical_symbols()
    positions = atoms.get_positions()

    indices1 = [i for i, s in enumerate(symbols) if s == element1]
    indices2 = [i for i, s in enumerate(symbols) if s == element2]

    pos1 = positions[indices1]
    pos2 = positions[indices2]

    # 모든 거리 계산
    distances = cdist(pos1, pos2)

    # cutoff 이하 결합 찾기
    bonds = distances[distances < cutoff]

    if len(bonds) == 0:
        return {'found': False}

    # 통계
    results = {
        'found': True,
        'n_bonds': len(bonds),
        'mean': bonds.mean(),
        'std': bonds.std(),
        'min': bonds.min(),
        'max': bonds.max(),
        'median': np.median(bonds),
        'coordination': len(bonds) / len(indices1),  # atom1당
    }

    # 요약 출력
    print(f"\n{element1}-{element2} 결합 분석:")
    print(f"  발견된 결합: {results['n_bonds']}")
    print(f"  평균: {results['mean']:.3f} ± {results['std']:.3f} Å")
    print(f"  범위: {results['min']:.3f} - {results['max']:.3f} Å")
    print(f"  배위수: {results['coordination']:.2f}")

    return results

# 사용법
bond_stats = analyze_bonds(atoms, 'Ca', 'O', cutoff=3.0)
```

---

## 📊 7. 시각화

### 출판 품질 그림

```python
# ========================================
# 출판 품질 그림 생성
# ========================================
def create_publication_figure(figsize=(12, 8), dpi=300):
    """
    출판 설정으로 그림 생성.

    Args:
        figsize: 그림 크기 (인치)
        dpi: 해상도

    Returns:
        fig, axes
    """
    plt.rcParams.update({
        'font.size': 11,
        'font.family': 'sans-serif',
        'axes.labelsize': 12,
        'axes.titlesize': 13,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10,
        'legend.fontsize': 10,
        'figure.dpi': dpi,
        'savefig.dpi': dpi,
        'savefig.bbox': 'tight',
    })

    fig, axes = plt.subplots(figsize=figsize)
    return fig, axes

# 사용법
fig, ax = create_publication_figure()
ax.plot(x, y)
plt.savefig(FOLDERS['figures'] / 'paper' / 'figure1.png')
```

---

## 📚 관련 문서

- [WORKFLOW_01_OPTIMIZATION.md](WORKFLOW_01_OPTIMIZATION.md) - 최적화 워크플로우
- [WORKFLOW_02_HYDRATION.md](WORKFLOW_02_HYDRATION.md) - MD 워크플로우
- [RESULTS_SUMMARY.md](RESULTS_SUMMARY.md) - 결과 참조

---

**최종 업데이트**: 2026-01-28
**상태**: 활성 개발
**버전**: 1.0.0
