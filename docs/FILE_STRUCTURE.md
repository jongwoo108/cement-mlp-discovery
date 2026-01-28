# FILE_STRUCTURE.md

> 전체 파일 구성 및 경로 참조

---

## 📁 프로젝트 디렉토리 트리

```
C:/cement_final/
│
├── 📓 notebooks/                        # Jupyter 노트북 (메인 워크플로우)
│   └── 01_Environment_Setup.ipynb      # ✅ 완료 - 환경 + C3S 최적화 + 수화
│
├── 🔬 structures/                       # 결정 구조 파일 (.cif)
│   ├── C3S_initial.cif                 # Materials Project의 초기 C3S
│   ├── C3S_optimized.cif               # BFGS 최적화 후 (Fmax < 0.05)
│   ├── C3S_hydration_initial.cif       # MD 전 C3S + 5 H2O
│   └── C3S_hydration_final.cif         # 1 ps 수화 시뮬레이션 후
│
├── 🎬 trajectories/                     # MD 시뮬레이션 궤적
│   ├── c3s_optimization.traj           # 최적화 궤적 (5 프레임)
│   └── hydration.traj                  # 수화 MD (1000 프레임, 1 ps)
│
├── 📊 figures/                          # 그래프 및 시각화
│   ├── C3S_optimization_analysis.png   # 4-panel 최적화 분석
│   ├── hydration_analysis.png          # 6-panel 수화 분석
│   ├── md_progress_realtime.png        # 실시간 MD 진행
│   ├── rdf_analysis.png                # 4-panel RDF 분석
│   ├── hydration_cao_evolution.png     # Ca-O 거리 변화
│   └── paper/                          # 출판용 그림 (비어있음)
│
├── 📈 results/                          # 수치 결과 및 데이터
│   ├── rdf_data.csv                    # RDF 데이터
│   ├── bond_analysis.json              # 결합 길이 통계
│   ├── coordination_analysis.json      # 배위수 분포
│   ├── ca_si_ratio_screening.csv       # Ca/Si 비율 결과
│   └── hydration_trajectory.csv        # 수화 궤적 데이터
│
├── 📝 paper/                            # 원고 파일
│   ├── manuscript/                     # LaTeX 소스 (비어있음)
│   ├── supplementary/                  # 보충 정보 (비어있음)
│   └── submission/                     # 최종 제출 (비어있음)
│
├── 📋 logs/                             # 시뮬레이션 로그
│   ├── hydration.log                   # MD 시뮬레이션 로그 (1.3 KB)
│   └── research_log.txt                # 수동 연구 노트 (선택)
│
├── 📚 docs/                             # 문서 (이 폴더)
│   ├── INDEX.md                        # 메인 문서 인덱스
│   ├── PROJECT_OVERVIEW.md             # 프로젝트 배경
│   ├── ENVIRONMENT_SETUP.md            # 설정 가이드
│   ├── FILE_STRUCTURE.md               # 이 파일
│   ├── WORKFLOW_01_OPTIMIZATION.md     # C3S 최적화 가이드
│   ├── WORKFLOW_02_HYDRATION.md        # 수화 시뮬레이션 가이드
│   ├── WORKFLOW_02_STRUCTURE_ANALYSIS.md # 구조 분석 가이드
│   ├── RESULTS_SUMMARY.md              # 주요 결과
│   ├── API_REFERENCE.md                # 코드 패턴
│   ├── TROUBLESHOOTING.md              # 일반적인 문제
│   └── SESSION_RESUME_TEMPLATE.md      # AI 에이전트용
│
├── 🗄️ archive/                          # 오래된/백업 파일
│   └── (비어있음 - 더 이상 사용하지 않는 파일용)
│
├── environment.yml                      # Conda 환경 사양
├── README.md                            # 프로젝트 README
├── .gitignore                           # Git 무시 규칙
└── LICENSE                              # MIT 라이선스 (선택)
```

---

## 🗂️ 파일 카테고리

### 1. Jupyter 노트북 (`notebooks/`)

**목적**: 메인 계산 워크플로우

| 파일 | 상태 | 설명 | 크기 |
|------|------|------|------|
| `01_Environment_Setup.ipynb` | ✅ 완료 | 환경 확인, C3S 최적화, 수화 시뮬레이션 | ~364 KB |
| `02_C3S_Structure_Analysis.ipynb` | ✅ 완료 | RDF, 결합 분석, 배위수, 수화 궤적 | ~50 KB |
| `03_CSH_Gel_Formation.ipynb` | ⏳ 다음 | C-S-H 젤 형성 시뮬레이션 | - |
| `04_Results_Analysis.ipynb` | 📅 예정 | 최종 분석 및 그림 | - |

---

### 2. 구조 파일 (`structures/`)

**목적**: CIF 형식의 결정 구조

| 파일 | 원자 수 | 목적 | 생성자 |
|------|---------|------|--------|
| `C3S_initial.cif` | 27 | MP의 초기 C3S | Materials Project |
| `C3S_optimized.cif` | 27 | 최적화된 구조 | BFGS 최적화기 |
| `C3S_hydration_initial.cif` | 42 | C3S + 5 H2O | 수동 조립 |
| `C3S_hydration_final.cif` | 42 | MD 시뮬레이션 후 | MolecularDynamics |

**주요 특성**:
```python
# C3S_optimized.cif
화학식: Ca3SiO5
공간군: 삼사정계
에너지: -199.4266 eV (-7.3862 eV/atom)
부피: ~XXX Å³
```

---

### 3. 궤적 (`trajectories/`)

**목적**: 시간에 따른 원자 위치 궤적

| 파일 | 프레임 | 시간 | 크기 | 목적 |
|------|--------|------|------|------|
| `c3s_optimization.traj` | 5 | - | 10.3 KB | BFGS 최적화 경로 |
| `hydration.traj` | 1000 | 1 ps | ~50 KB | 수화 MD 시뮬레이션 |

**궤적 읽기**:
```python
from ase.io.trajectory import Trajectory

# 궤적 로드
traj = Trajectory(str(FOLDERS['trajectories'] / 'hydration.traj'))

# 프레임 접근
initial = traj[0]      # 첫 번째 프레임
final = traj[-1]       # 마지막 프레임
middle = traj[500]     # 500번째 프레임

# 반복
for atoms in traj[::10]:  # 매 10 프레임
    # 프레임 처리
    pass
```

---

### 4. 그림 (`figures/`)

**목적**: 시각화 및 그래프

| 파일 | 유형 | 패널 | DPI | 크기 |
|------|------|------|-----|------|
| `C3S_optimization_analysis.png` | 다중 패널 | 2×2 | 200 | ~164 KB |
| `hydration_analysis.png` | 다중 패널 | 2×3 | 200 | ~XXX KB |
| `md_progress_realtime.png` | 다중 패널 | 2×2 | 200 | ~XXX KB |
| `rdf_analysis.png` | 다중 패널 | 2×2 | 300 | ~200 KB |
| `hydration_cao_evolution.png` | 다중 패널 | 2×2 | 300 | ~150 KB |

**명명 규칙**:
```
{주제}_{설명}.png
```

예시:
- `C3S_optimization_analysis.png`
- `ca_si_ratio_comparison.png`
- `rdf_analysis.png`

---

### 5. 결과 (`results/`)

**목적**: 수치 데이터 (CSV, JSON, TXT)

**현재 파일**:
```
results/
├── rdf_data.csv                    # RDF 데이터 (pair, distance, rdf)
├── bond_analysis.json              # 결합 길이 통계
│   {Ca-O: {mean, std, count}, Si-O: {...}}
├── coordination_analysis.json      # 배위수
│   {Ca-O: {mean, std, distribution}, Si-O: {...}}
├── ca_si_ratio_screening.csv       # Ca/Si 비율 연구 결과
├── hydration_trajectory.csv        # 수화 궤적 데이터
│   컬럼: time_ps, ca_o_distance, ca_o_count
└── (추가 생성 예정)
```

---

### 6. 로그 (`logs/`)

**목적**: 시뮬레이션 로그 및 연구 노트

| 파일 | 형식 | 목적 | 크기 |
|------|------|------|------|
| `hydration.log` | 텍스트 | MD 시뮬레이션 로그 (에너지, T 등) | 1.3 KB |
| `c3s_opt.log` | 텍스트 | 최적화 로그 (생성 시) | ~1 KB |
| `research_log.txt` | 텍스트 | 수동 노트 (선택) | 가변 |

**로그 형식** (`hydration.log`):
```
Time[ps]  Etot[eV]    Epot[eV]    Ekin[eV]   T[K]
0.0000    -199.4266   -199.4266    0.0000    0.0
0.0010    -199.4230   -199.4245    0.0015    12.3
...
```

---

### 7. 문서 (`docs/`)

**목적**: 인간과 AI 에이전트를 위한 프로젝트 문서

| 파일 | 목적 | 상태 |
|------|------|------|
| `INDEX.md` | 문서 인덱스 | ✅ |
| `PROJECT_OVERVIEW.md` | 프로젝트 컨텍스트 및 목표 | ✅ |
| `ENVIRONMENT_SETUP.md` | 설치 가이드 | ✅ |
| `FILE_STRUCTURE.md` | 이 파일 | ✅ |
| `WORKFLOW_01_OPTIMIZATION.md` | 최적화 워크플로우 | ✅ |
| `WORKFLOW_02_HYDRATION.md` | 수화 워크플로우 | ✅ |
| `WORKFLOW_02_STRUCTURE_ANALYSIS.md` | 구조 분석 워크플로우 | ✅ |
| `RESULTS_SUMMARY.md` | 주요 결과 | ✅ |
| `API_REFERENCE.md` | 코드 패턴 | ✅ |
| `TROUBLESHOOTING.md` | 일반적인 문제 | ✅ |

---

## 🔑 주요 경로 변수

### Python 코드 패턴

```python
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

# 필요시 폴더 생성
for folder in FOLDERS.values():
    folder.mkdir(parents=True, exist_ok=True)
```

### 사용 예시

```python
# 구조 읽기
from ase.io import read
atoms = read(FOLDERS['structures'] / 'C3S_optimized.cif')

# 구조 쓰기
from ase.io import write
write(FOLDERS['structures'] / 'new_structure.cif', atoms)

# 궤적 저장
from ase.io.trajectory import Trajectory
traj = Trajectory(str(FOLDERS['trajectories'] / 'simulation.traj'), 'w')
traj.write(atoms)

# 그림 저장
import matplotlib.pyplot as plt
plt.savefig(FOLDERS['figures'] / 'plot.png', dpi=300, bbox_inches='tight')

# 결과 저장
import pandas as pd
df.to_csv(FOLDERS['results'] / 'data.csv', index=False)
```

---

## 📏 파일 크기 가이드라인

### 목표 크기

| 카테고리 | 목표 크기 | 이유 |
|----------|-----------|------|
| 구조 (.cif) | < 10 KB | 작은 시스템 (< 100 원자) |
| 궤적 (.traj) | 10 KB - 1 MB | 1000 프레임 적절 |
| 그림 (.png) | 100-500 KB | 고품질 (dpi=200-300) |
| 결과 (.csv) | < 1 MB | 테이블 데이터 압축 잘 됨 |
| 노트북 (.ipynb) | 100 KB - 1 MB | 출력 포함 |

### 대용량 파일 (> 100 MB)

매우 큰 파일의 경우:
- `archive/` 또는 외부 저장소에 저장
- 압축 사용 (`.tar.gz`, `.zip`)
- `docs/DATA_DICTIONARY.md`에 위치 문서화

---

## 🔄 파일 생명주기

### 생성 흐름

```
노트북 셀
    ↓
데이터/구조 생성
    ↓
적절한 폴더에 저장
    ↓
노트북 출력에 문서화
    ↓
중요한 경우 docs/에 참조
```

### 명명 규칙

```python
# 타임스탬프 기반 (실행용)
f"simulation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.traj"

# 설명적 (분석용)
"C3S_optimized.cif"
"ca_si_ratio_1.7_optimized.cif"

# 버전 관리 (필요시)
"structure_v1.cif"
"structure_v2.cif"
```

---

## 🗂️ .gitignore 구성

**권장 `.gitignore`**:

```gitignore
# 대용량 궤적 파일
*.traj
trajectories/

# Jupyter 체크포인트
.ipynb_checkpoints/
__pycache__/

# 민감 정보
.mp_api_key
api_keys.txt

# OS
.DS_Store
Thumbs.db
desktop.ini

# 선택: 결과 (매우 큰 경우)
# results/*.csv
```

---

## 📋 파일 매니페스트

### 현재 파일 (2026-01-28)

```
총 파일: 25+
총 크기: ~1 MB

구성:
- 노트북: 2 (~414 KB)
- 구조: 4 (~2 KB)
- 궤적: 2 (~11 KB)
- 그림: 5 (~550 KB)
- 결과: 5 (~50 KB)
- 로그: 1 (1.3 KB)
- 문서: 10 (~30 KB)
- 설정: 3 (~5 KB)
```

---

## 🔍 파일 찾기 명령

### Windows (PowerShell)

```powershell
# 모든 CIF 파일 찾기
Get-ChildItem -Path C:\cement_final -Recurse -Filter *.cif

# 오늘 수정된 파일 찾기
Get-ChildItem -Path C:\cement_final -Recurse | Where-Object {$_.LastWriteTime -gt (Get-Date).Date}

# 폴더 크기 계산
Get-ChildItem -Path C:\cement_final -Directory | ForEach-Object {
    $size = (Get-ChildItem -Path $_.FullName -Recurse | Measure-Object -Property Length -Sum).Sum / 1MB
    [PSCustomObject]@{Folder=$_.Name; SizeMB=[math]::Round($size,2)}
}
```

### Python

```python
from pathlib import Path

# 특정 유형의 모든 파일 찾기
cif_files = list(Path("C:/cement_final").rglob("*.cif"))

# 파일 크기 가져오기
for file in Path("C:/cement_final/structures").iterdir():
    if file.is_file():
        print(f"{file.name}: {file.stat().st_size / 1024:.1f} KB")
```

---

## 📚 관련 문서

- [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) - 프로젝트 컨텍스트
- [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) - 설정 가이드
- [API_REFERENCE.md](API_REFERENCE.md) - 코드 패턴
- [RESULTS_SUMMARY.md](RESULTS_SUMMARY.md) - 주요 결과

---

**최종 업데이트**: 2026-01-28
**상태**: 활성
**버전**: 1.0.0
