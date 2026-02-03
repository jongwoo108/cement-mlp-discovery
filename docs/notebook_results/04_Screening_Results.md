# 자동화 파이프라인 스크리닝 결과

> **실행일**: 2026-01-29  
> **노트북**: `notebooks/pipeline/04_Screening_Pipeline.ipynb`  
> **문서번호**: 04 (노트북 번호와 동일)  
> **상태**: ✅ 완료 (16개 후보 전체)

---

## 1. 실험 개요

### 1.1 목적
AI 기반 자동화 스크리닝 파이프라인을 통한 16개 산업 부산물의 체계적 평가 및 탄소중립 시멘트 결합재 후보 선별

### 1.2 파이프라인 구성

```
후보 구조 생성 → CHGNet 최적화 → 수화 시스템 생성 → MD 시뮬레이션 → 분석 → 점수화
```

### 1.3 테스트 재료 (16개)

| 분류 | 재료 | 주요 성분 | CO₂ 저감(%) |
|------|------|----------|:-----------:|
| 제철 슬래그 | BFS (고로슬래그) | Ca-Si-Al-Mg | 85 |
| | SteelSlag (제강슬래그) | Ca-Si-Fe-Mg | 75 |
| | EAFSlag (전기로슬래그) | Ca-Si-Fe-Al | 75 |
| 비산재 | FlyAshF (F급) | Si-Al-Fe-Ca | 85 |
| | FlyAshC (C급) | Ca-Si-Al | 85 |
| | BottomAsh | Si-Al-Fe-Ca | 75 |
| 비철금속 슬래그 | CopperSlag | Fe-Si-Ca-Al | 75 |
| | NickelSlag | Fe-Si-Mg | 75 |
| 기타 산업부산물 | RedMud | Fe-Al-Si-Ti | 65 |
| | SilicaFume | Si | 88 |
| 농업 부산물 | RiceHuskAsh | Si-K | 92 |
| | POFA | Si-Ca-K | 88 |
| 폐기물 | WasteGlass | Si-Na-Ca | 75 |
| | CeramicWaste | Si-Al | 65 |
| 천연 포졸란 | Metakaolin | Si-Al | 75 |
| | CoalGangue | Si-Al | 70 |

### 1.4 시뮬레이션 조건

| 파라미터 | 값 |
|----------|-----|
| 시뮬레이션 시간 | 10 ps (각 재료) |
| 물 분자 수 | 10개 |
| 온도 | 300 K |
| 앙상블 | NVT (Berendsen) |
| 타임스텝 | 1 fs |
| MLP 모델 | CHGNet v0.3.0 |
| GPU | NVIDIA RTX 4070 Laptop |

---

## 2. 실행 결과 요약

### 2.1 총 실행 시간

| 항목 | 값 |
|------|-----|
| 시작 시간 | 09:02:03 |
| 완료 시간 | 17:24:48 |
| **총 소요 시간** | **약 8시간 23분** |
| 평균 후보당 시간 | ~31분 |

### 2.2 구조 최적화 결과

모든 16개 후보에서 최적화 수행 (CHGNet 사용):
- 대부분 300-500 스텝 내 완료
- 일부 무정형 구조는 완전 수렴하지 않음 (Fmax > 0.05 eV/Å)
- 최적화 시간: 10-52초/후보

### 2.3 MD 시뮬레이션

| 후보 | MD 시간 | "Isolated atom" 경고 |
|------|---------|:--------------------:|
| BFS | 604s | - |
| SteelSlag | 795s | 다수 |
| EAFSlag | 758s | 다수 |
| FlyAshF | 783s | - |
| FlyAshC | 935s | - |
| BottomAsh | 938s | - |
| CopperSlag | 911s | - |
| RedMud | 925s | 소수 |
| NickelSlag | 929s | - |
| SilicaFume | 875s | - |
| RiceHuskAsh | 728s | - |
| POFA | 597s | - |
| WasteGlass | 608s | - |
| CeramicWaste | 870s | - |
| Metakaolin | ~800s | - |
| CoalGangue | ~480s | - |

**참고**: "Isolated atom" 경고는 원자가 상호작용 cutoff(6Å) 밖으로 이동했음을 의미하며, 일부 슬래그 시스템에서 발생

---

## 3. 스크리닝 점수

### 3.1 평가 기준

| 항목 | 가중치 | 설명 | 기준 |
|------|:------:|------|------|
| CO₂ 저감 | 25% | 기존 OPC 대비 CO₂ 감축률 | 높을수록 좋음 |
| Ca 용출 활성 | 25% | Ca leaching rate | C3S 대비 비교 |
| Si 구조 안정성 | 25% | Si 평균 배위수 | CN=4에 가까울수록 좋음 |
| C-S-H 형성 | 25% | Ca-Si 근접 쌍 수 (< 4Å) | 많을수록 좋음 |

### 3.2 최종 순위

| 순위 | 재료 | 점수 | 등급 | CO₂↓ | Ca Rate | Si CN | C-S-H |
|:----:|------|:----:|:----:|:----:|:-------:|:-----:|:-----:|
| 1 | **FlyAshC** | **90.3** | **A** | 85% | 0.300 | 3.54 | 7 |
| 2 | **EAFSlag** | **89.4** | **A** | 75% | 0.300 | 3.30 | 12 |
| 3 | **WasteGlass** | **84.7** | **A** | 75% | 0.200 | 3.55 | 6 |
| 4 | **CopperSlag** | **79.0** | **A** | 75% | 0.100 | 2.94 | 7 |
| 5 | **SteelSlag** | **78.9** | **A** | 75% | 0.200 | 2.63 | 6 |
| 6 | POFA | 64.4 | B | 88% | 0.000 | 4.02 | 4 |
| 7 | FlyAshF | 63.2 | B | 85% | 0.000 | 3.41 | 5 |
| 8 | BFS | 60.9 | B | 85% | 0.500 | 2.74 | 4 |
| 9 | RiceHuskAsh | 51.1 | B | 92% | 0.000 | 3.70 | 0 |
| 10 | BottomAsh | 50.8 | B | 75% | 0.000 | 3.33 | 2 |
| 11 | SilicaFume | 50.2 | B | 88% | 0.000 | 3.71 | 0 |
| 12 | NickelSlag | 48.1 | C | 75% | 0.000 | 3.89 | 0 |
| 13 | Metakaolin | 44.8 | C | 75% | 0.000 | 3.36 | 0 |
| 14 | CoalGangue | 44.5 | C | 70% | 0.000 | 3.52 | 0 |
| 15 | CeramicWaste | 42.2 | C | 65% | 0.000 | 3.34 | 0 |
| 16 | RedMud | 42.0 | C | 65% | 0.000 | 3.32 | 0 |

### 3.3 등급 분포

| 등급 | 점수 범위 | 후보 수 | 재료 |
|:----:|:---------:|:-------:|------|
| **A** | 75-100 | 5 | FlyAshC, EAFSlag, WasteGlass, CopperSlag, SteelSlag |
| **B** | 50-74 | 6 | POFA, FlyAshF, BFS, RiceHuskAsh, BottomAsh, SilicaFume |
| **C** | 0-49 | 5 | NickelSlag, Metakaolin, CoalGangue, CeramicWaste, RedMud |

---

## 4. 상세 분석

### 4.1 Ca 용출 활성

**높은 Ca 용출** (C-S-H 형성에 유리):
- FlyAshC, EAFSlag: 0.300 Ca/ps
- WasteGlass, SteelSlag: 0.200 Ca/ps
- BFS: 0.500 Ca/ps (가장 높음, 그러나 Si 안정성 낮음)

**Ca 용출 없음** (활성화 필요):
- POFA, FlyAshF, RiceHuskAsh, SilicaFume 등
- 원인: Ca 함량 부족 또는 Ca가 구조에 강하게 결합

### 4.2 Si 배위수 (구조 안정성)

**이상적 CN (3.5-4.0)** - SiO₄ 사면체 유지:
- POFA: 4.02 (최고)
- NickelSlag: 3.89
- SilicaFume: 3.71
- RiceHuskAsh: 3.70

**낮은 CN (< 3.0)** - 구조 재배열 활발:
- SteelSlag: 2.63
- BFS: 2.74
- CopperSlag: 2.94

### 4.3 C-S-H 형성 지표

**가장 많은 Ca-Si 쌍 형성**:
1. EAFSlag: 12쌍 (최다)
2. FlyAshC, CopperSlag: 7쌍
3. WasteGlass, SteelSlag: 6쌍

**C-S-H 형성 없음** (Ca-Si 쌍 0):
- RiceHuskAsh, SilicaFume, NickelSlag, Metakaolin, CoalGangue, CeramicWaste, RedMud
- 원인: Ca 부족 또는 Ca-Si 상호작용 거리 부족

---

## 5. Top 5 후보 상세

### 5.1 FlyAshC (C급 비산재) - 1위, 90.3점

| 항목 | 값 | 평가 |
|------|-----|------|
| 조성 | Ca₄Si₅Al₂O₁₆ | Ca 풍부 |
| CO₂ 저감 | 85% | 우수 |
| Ca 용출 | 0.300/ps | 높음 |
| Si CN | 3.54 | 양호 |
| C-S-H 쌍 | 7 | 양호 |

**강점**: 높은 Ca 함량, 활발한 Ca 용출, 양호한 Si 구조
**적용**: 고로슬래그와 혼합 사용 시 시너지 기대

### 5.2 EAFSlag (전기로 슬래그) - 2위, 89.4점

| 항목 | 값 | 평가 |
|------|-----|------|
| 조성 | Ca₅Si₄Fe₃AlO₁₆ | Fe 함유 |
| CO₂ 저감 | 75% | 양호 |
| Ca 용출 | 0.300/ps | 높음 |
| Si CN | 3.30 | 양호 |
| C-S-H 쌍 | **12** | **최다** |

**강점**: 가장 많은 C-S-H 쌍 형성, 높은 Ca 활성
**주의**: MD 중 "isolated atom" 경고 다수 발생

### 5.3 WasteGlass (폐유리) - 3위, 84.7점

| 항목 | 값 | 평가 |
|------|-----|------|
| 조성 | Ca₂Si₆Na₂O₁₆ | Na 함유 |
| CO₂ 저감 | 75% | 양호 |
| Ca 용출 | 0.200/ps | 중간 |
| Si CN | 3.55 | 양호 |
| C-S-H 쌍 | 6 | 양호 |

**강점**: 폐기물 재활용, 양호한 Si 안정성
**적용**: 순환경제 관점에서 유리

### 5.4 CopperSlag (동 슬래그) - 4위, 79.0점

| 항목 | 값 | 평가 |
|------|-----|------|
| 조성 | Fe₅Si₄Ca₂AlO₁₆ | Fe 다량 |
| CO₂ 저감 | 75% | 양호 |
| Ca 용출 | 0.100/ps | 낮음 |
| Si CN | 2.94 | 중간 |
| C-S-H 쌍 | 7 | 양호 |

**강점**: Fe 함량으로 강도 향상 기대
**주의**: Ca 함량 낮아 추가 공급 필요 가능

### 5.5 SteelSlag (제강 슬래그) - 5위, 78.9점

| 항목 | 값 | 평가 |
|------|-----|------|
| 조성 | Ca₈Si₃Fe₂MgO₁₆ | Ca 최다 |
| CO₂ 저감 | 75% | 양호 |
| Ca 용출 | 0.200/ps | 중간 |
| Si CN | 2.63 | 낮음 |
| C-S-H 쌍 | 6 | 양호 |

**강점**: 높은 Ca 함량, 국내 생산량 풍부
**주의**: Si 배위수 낮음 (구조 불안정 가능)

---

## 6. 시각화 결과

### 6.1 스크리닝 비교 차트
![Pipeline Screening Comparison](../figures/pipeline_screening_comparison.png)

- **(a) CO₂ 저감률**: RiceHuskAsh(92%) > POFA/SilicaFume(88%) > FlyAsh(85%)
- **(b) Ca 용출 활성**: BFS > FlyAshC/EAFSlag > WasteGlass/SteelSlag
- **(c) Si 배위수**: POFA > NickelSlag > SilicaFume > RiceHuskAsh
- **(d) 종합 점수**: A등급 5개, B등급 6개, C등급 5개

### 6.2 시간 변화 그래프
![Pipeline Screening Evolution](../figures/pipeline_screening_evolution.png)

- **Ca 용출**: 대부분 초기 급격한 용출 후 안정화
- **Si CN**: 대부분 안정적 유지, 일부 슬래그에서 변동
- **C-S-H 쌍**: EAFSlag가 지속적으로 증가

---

## 7. 결론 및 해석

### 7.1 주요 발견

1. **Top 5 후보 확정**
   - FlyAshC, EAFSlag, WasteGlass, CopperSlag, SteelSlag
   - 모두 A등급 (75점 이상)
   - 공통점: Ca 용출 활성 + C-S-H 형성 능력

2. **C-S-H 형성의 핵심 요소**
   - Ca 용출 활성이 C-S-H 형성의 전제 조건
   - Ca Rate > 0인 후보만 C-S-H 쌍 형성
   - EAFSlag가 가장 많은 12쌍 형성

3. **CO₂ 저감과 성능의 균형**
   - 최고 CO₂ 저감(92% RiceHuskAsh)이 최고 성능이 아님
   - Ca 함량이 성능에 더 큰 영향

4. **B/C 등급 후보의 한계**
   - Ca 용출 없음 → C-S-H 형성 불가
   - 단독 사용보다 혼합재로 활용 권장

### 7.2 기술적 고찰

1. **Slag 시스템의 불안정성**
   - SteelSlag, EAFSlag에서 "isolated atom" 경고 다수
   - 원인: Fe-O 결합의 동적 거동
   - 대책: 더 큰 시스템 또는 더 긴 평형화 시간 필요

2. **Si 배위수 해석**
   - CN < 3: 구조 분해 진행 (Ca 용출과 연관)
   - CN ~ 4: 안정한 SiO₄ 사면체 유지
   - 낮은 CN이 반드시 나쁜 것은 아님 (반응성 증가)

3. **스크리닝 한계**
   - 10 ps는 초기 반응만 포착
   - 장기 C-S-H 성장은 관찰 불가
   - 실제 성능은 실험 검증 필요

### 7.3 실용화 권장 사항

| 순위 | 재료 | 권장 용도 | 혼합 비율 |
|:----:|------|----------|:---------:|
| 1 | FlyAshC | OPC 대체 | 30-50% |
| 2 | EAFSlag | OPC 대체 | 20-40% |
| 3 | WasteGlass | 미분말 혼합 | 10-20% |
| 4 | CopperSlag | 골재/혼합재 | 15-25% |
| 5 | SteelSlag | 도로/기초 | 20-30% |

---

## 8. 생성된 파일

### 8.1 구조 파일 (`structures/`)
```
BFS_optimized.cif, BFS_hydration.cif
SteelSlag_optimized.cif, SteelSlag_hydration.cif
EAFSlag_optimized.cif, EAFSlag_hydration.cif
FlyAshF_optimized.cif, FlyAshF_hydration.cif
FlyAshC_optimized.cif, FlyAshC_hydration.cif
BottomAsh_optimized.cif, BottomAsh_hydration.cif
CopperSlag_optimized.cif, CopperSlag_hydration.cif
RedMud_optimized.cif, RedMud_hydration.cif
NickelSlag_optimized.cif, NickelSlag_hydration.cif
SilicaFume_optimized.cif, SilicaFume_hydration.cif
RiceHuskAsh_optimized.cif, RiceHuskAsh_hydration.cif
POFA_optimized.cif, POFA_hydration.cif
WasteGlass_optimized.cif, WasteGlass_hydration.cif
CeramicWaste_optimized.cif, CeramicWaste_hydration.cif
Metakaolin_optimized.cif, Metakaolin_hydration.cif
CoalGangue_optimized.cif, CoalGangue_hydration.cif
```

### 8.2 궤적 파일 (`trajectories/`)
```
BFS_hydration.traj
SteelSlag_hydration.traj
EAFSlag_hydration.traj
FlyAshF_hydration.traj
FlyAshC_hydration.traj
BottomAsh_hydration.traj
CopperSlag_hydration.traj
RedMud_hydration.traj
NickelSlag_hydration.traj
SilicaFume_hydration.traj
RiceHuskAsh_hydration.traj
POFA_hydration.traj
WasteGlass_hydration.traj
CeramicWaste_hydration.traj
Metakaolin_hydration.traj
CoalGangue_hydration.traj
```

### 8.3 결과 파일 (`data/results/`)
```
pipeline_screening_results.json    # 상세 결과
pipeline_screening_summary.csv     # 요약 테이블
top_candidates.json                # Top 5 후보
```

### 8.4 시각화 (`figures/`)
```
pipeline_screening_comparison.png  # 비교 차트
pipeline_screening_evolution.png   # 시간 변화 그래프
```

---

## 9. 다음 단계

### Phase 4: 논문 작성
1. **05_Results_Analysis.ipynb**
   - Top 5 후보 심층 분석
   - RDF, 결합 분석
   
2. **06_Paper_Figures.ipynb**
   - 논문용 고품질 Figure 생성
   - Figure 1-4 완성

### 추가 연구 제안
1. **장시간 시뮬레이션** (100 ps)
   - Top 5 후보 대상
   - 완전한 C-S-H 성장 관찰

2. **혼합 시스템 연구**
   - FlyAshC + BFS 조합
   - EAFSlag + SilicaFume 조합

3. **실험 검증**
   - 압축 강도 테스트
   - XRD, SEM 분석

---

**작성일**: 2026-01-29  
**완료 시간**: 17:24:48  
**상태**: ✅ Phase 3 완료
