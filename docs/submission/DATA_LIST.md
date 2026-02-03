# 활용 데이터 목록

> 2026 AI Co-Scientist Challenge Korea - Track 1 제출물

---

## 1. 데이터 개요

| 구분 | 개수 | 설명 |
|------|:----:|------|
| **입력 데이터** | 16개 | 산업폐기물 CIF 구조 파일 |
| **AI 합성 데이터** | 32개 | MatterGen 생성 구조 |
| **시뮬레이션 결과** | 48개 | CHGNet MD 궤적 및 분석 |
| **최종 결과** | 7개 | JSON/CSV 결과 파일 |

---

## 2. 입력 데이터 (공공 데이터)

### 2.1 산업폐기물 구조 데이터

| # | 재료명 | 파일명 | 데이터 성격 | 수집 경로 |
|:-:|--------|--------|:----------:|----------|
| 1 | Blast Furnace Slag | `BFS_optimized.cif` | 공공 | Materials Project |
| 2 | Steel Slag | `SteelSlag_optimized.cif` | 공공 | Materials Project |
| 3 | EAF Slag | `EAFSlag_hydration.cif` | 공공 | Materials Project |
| 4 | Fly Ash Class C | `FlyAshC_hydration.xyz` | 공공 | Materials Project |
| 5 | Fly Ash Class F | `FlyAshF_hydration.traj` | 공공 | Materials Project |
| 6 | Bottom Ash | `BottomAsh_optimized.cif` | 공공 | Materials Project |
| 7 | Copper Slag | `CopperSlag_optimized.cif` | 공공 | Materials Project |
| 8 | Nickel Slag | `NickelSlag_optimized.cif` | 공공 | Materials Project |
| 9 | Red Mud | `RedMud_optimized.cif` | 공공 | Materials Project |
| 10 | Silica Fume | `SilicaFume_optimized.cif` | 공공 | Materials Project |
| 11 | Rice Husk Ash | `RiceHuskAsh_optimized.cif` | 공공 | Materials Project |
| 12 | POFA | `POFA_optimized.cif` | 공공 | Materials Project |
| 13 | Waste Glass | `WasteGlass_optimized.cif` | 공공 | Materials Project |
| 14 | Ceramic Waste | `CeramicWaste_optimized.cif` | 공공 | Materials Project |
| 15 | Metakaolin | `Metakaolin_optimized.cif` | 공공 | Materials Project |
| 16 | Coal Gangue | `CoalGangue_optimized.cif` | 공공 | Materials Project |

**데이터 출처**: Materials Project (https://materialsproject.org)  
**라이선스**: CC-BY-4.0  
**저장 위치**: `structures/`

### 2.2 기준선 데이터 (C3S)

| 파일명 | 데이터 성격 | 수집 경로 |
|--------|:----------:|----------|
| `C3S_initial.cif` | 공공 | Materials Project |
| `C3S_optimized.cif` | 공공 | CHGNet 최적화 |
| `C3S_hydration_initial.cif` | 공공 | 시뮬레이션 생성 |
| `C3S_hydration_final.cif` | 공공 | 시뮬레이션 결과 |

---

## 3. AI 합성 데이터 (MatterGen 생성)

### 3.1 생성 구조 목록

| 화학 시스템 | 생성 수 | 유효 수 | 데이터 성격 | 생성 방법 |
|------------|:------:|:------:|:----------:|----------|
| Ca-Si-Al-O | 8 | 7 | **AI 합성** | MatterGen |
| Ca-Si-Al-Fe-O | 8 | 5 | **AI 합성** | MatterGen |
| Ca-Si-O | 8 | 8 | **AI 합성** | MatterGen |
| Ca-Si-Mg-O | 8 | 6 | **AI 합성** | MatterGen |
| **Total** | **32** | **26** | - | - |

**저장 위치**: `data/mattergen/`, `structures/mattergen_optimized/`

### 3.2 MatterGen 생성 파라미터

```yaml
model: chemical_system_energy_above_hull
batch_size: 4
guidance_factor: 2.0
stability_criterion: E_hull <= 0.05 eV/atom
temperature: 1.0
num_steps: 1000
```

---

## 4. 시뮬레이션 결과 데이터

### 4.1 MD 궤적 파일

| 카테고리 | 파일 수 | 형식 | 저장 위치 |
|----------|:------:|:----:|----------|
| 산업폐기물 수화 | 16 | .traj | `trajectories/` |
| MatterGen 수화 | 4 | .traj | `trajectories/` |
| C3S 기준선 | 2 | .traj | `trajectories/` |

**데이터 성격**: 시뮬레이션 생성 (CHGNet MD)

### 4.2 주요 궤적 파일

| 파일명 | 원자 수 | 시뮬레이션 시간 |
|--------|:------:|:--------------:|
| `BFS_hydration.traj` | ~50 | 2 ps |
| `EAFSlag_hydration.traj` | ~60 | 2 ps |
| `FlyAsh_hydration.traj` | ~55 | 2 ps |
| `c3s_optimization.traj` | 27 | - |
| `hydration.traj` | 42 | 10 ps |

---

## 5. 최종 결과 데이터

### 5.1 JSON 결과 파일

| 파일명 | 내용 | 데이터 성격 |
|--------|------|:----------:|
| `top_candidates.json` | 산업폐기물 Top 5 | 분석 결과 |
| `mattergen_validation.json` | MatterGen 검증 결과 | 분석 결과 |
| `mattergen_hydration.json` | MatterGen 수화 시뮬레이션 | 시뮬레이션 결과 |
| `final_comparison_hydration.json` | 최종 비교 데이터 | 분석 결과 |
| `mechanical_properties_hydrated.json` | 기계적 특성 | 시뮬레이션 결과 |
| `mattergen_improved_hydration.json` | Supercell 실험 결과 | 시뮬레이션 결과 |
| `pipeline_screening_results.json` | 전체 스크리닝 결과 | 분석 결과 |

**저장 위치**: `data/results/`

### 5.2 CSV 결과 파일

| 파일명 | 내용 | 행 수 |
|--------|------|:-----:|
| `final_ranking_hydration.csv` | 최종 순위 테이블 | 48 |

---

## 6. 데이터 분류 요약

### 6.1 성격별 분류

| 데이터 성격 | 파일 수 | 비율 |
|------------|:------:|:----:|
| **공공 데이터** | 20 | 30% |
| **AI 합성 데이터** | 32 | 47% |
| **시뮬레이션 생성** | 22 | 23% |
| **개인 데이터** | 0 | 0% |

### 6.2 수집 경로별 분류

| 수집 경로 | 파일 수 | 설명 |
|----------|:------:|------|
| Materials Project | 20 | 공공 구조 데이터베이스 |
| MatterGen | 32 | AI 생성 구조 |
| CHGNet MD | 22 | 시뮬레이션 결과 |

---

## 7. 데이터 접근 정보

### 7.1 공공 데이터 출처

| 출처 | URL | 라이선스 |
|------|-----|----------|
| Materials Project | https://materialsproject.org | CC-BY-4.0 |
| CHGNet | https://github.com/CederGroupHub/chgnet | BSD-3 |
| MatterGen | https://github.com/microsoft/mattergen | MIT |

### 7.2 프로젝트 데이터 구조

```
cement_final/
├── data/
│   ├── candidates/        # 입력 구조 (공공)
│   ├── mattergen/         # AI 합성 구조
│   └── results/           # 분석 결과 (JSON/CSV)
├── structures/            # CIF 파일
│   └── mattergen_optimized/
├── trajectories/          # MD 궤적 (.traj)
└── figures/               # 시각화 결과
```

---

## 8. 데이터 재현성

### 8.1 재현 가능 데이터

| 데이터 유형 | 재현 방법 |
|------------|----------|
| 공공 구조 | Materials Project API로 재다운로드 |
| MatterGen 구조 | 동일 파라미터로 재생성 (확률적) |
| 시뮬레이션 결과 | 노트북 재실행 (결정적) |

### 8.2 시드 정보

```python
# MatterGen 생성 시 사용된 시드
random_seed = None  # 기본값 사용 (확률적 생성)

# CHGNet MD 시뮬레이션
# Langevin dynamics는 온도 기반 확률적
```

---

**작성일**: 2026년 1월 30일  
**총 데이터 파일**: ~74개  
**총 용량**: ~500 MB (trajectories 포함)
