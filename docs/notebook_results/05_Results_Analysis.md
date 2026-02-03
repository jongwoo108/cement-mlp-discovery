# Top 5 후보 심층 분석 결과

> **실행일**: 2026-01-29  
> **노트북**: `notebooks/pipeline/05_Results_Analysis.ipynb`  
> **문서번호**: 05 (노트북 번호와 동일)  
> **상태**: ✅ 완료

---

## 1. 분석 개요

### 1.1 목적
04_Screening_Pipeline에서 선정된 Top 5 후보에 대한 심층 분석 및 C3S Baseline과의 상세 비교

### 1.2 분석 항목

| 분석 | 설명 | 목적 |
|------|------|------|
| RDF 분석 | Radial Distribution Function | 원자쌍 거리 분포 파악 |
| 결합 분석 | Bond Analysis | 배위수 통계 |
| Baseline 비교 | C3S 대비 성능 | 대체 가능성 평가 |
| 통계 분석 | 상관관계 분석 | 핵심 성능 지표 파악 |

### 1.3 Top 5 후보

| 순위 | 재료 | 점수 | 등급 | CO₂ 저감 |
|:----:|------|:----:|:----:|:--------:|
| 1 | **FlyAshC** | 90.3 | A | 85% |
| 2 | **EAFSlag** | 89.4 | A | 75% |
| 3 | **WasteGlass** | 84.7 | A | 75% |
| 4 | **CopperSlag** | 79.0 | A | 75% |
| 5 | **SteelSlag** | 78.9 | A | 75% |

---

## 2. C3S Baseline 비교

### 2.1 주요 지표 비교

| 재료 | CO₂↓ | Ca Rate | Si CN | C-S-H 쌍 | 점수 | 등급 |
|------|:----:|:-------:|:-----:|:--------:|:----:|:----:|
| **C3S (Baseline)** | 0% | 0.000 | 3.50 | 12 | 100.0 | REF |
| FlyAshC | 85% | 0.300 | 3.54 | 7 | 90.3 | A |
| EAFSlag | 75% | 0.300 | 3.30 | 12 | 89.4 | A |
| WasteGlass | 75% | 0.200 | 3.55 | 6 | 84.7 | A |
| CopperSlag | 75% | 0.100 | 2.94 | 7 | 79.0 | A |
| SteelSlag | 75% | 0.200 | 2.63 | 6 | 78.9 | A |

### 2.2 해석

**Ca 용출 속도 (Ca Rate)**
- C3S baseline은 0.000 Ca/ps (용출 없음)
- Top 5 후보 모두 C3S보다 높은 Ca 용출 활성
- FlyAshC, EAFSlag가 가장 높은 Ca 용출 (0.300 Ca/ps)

**Si 배위수 (Si CN)**
- 이상적인 값: 4.0 (SiO₄ 사면체)
- FlyAshC (3.54), WasteGlass (3.55): C3S와 유사한 안정성
- SteelSlag (2.63): 가장 낮음 → 구조 재배열 활발

**C-S-H 쌍 형성**
- EAFSlag: C3S와 동일한 12쌍 (최고)
- FlyAshC, CopperSlag: 7쌍
- WasteGlass, SteelSlag: 6쌍

---

## 3. RDF (Radial Distribution Function) 분석

### 3.1 분석 원자쌍

| 원자쌍 | 의미 | 첫 번째 피크 위치 |
|--------|------|:-----------------:|
| Ca-O | Ca 용출 및 수화 반응 | 2.3-2.5 Å |
| Si-O | SiO₄ 사면체 구조 | 1.6-1.7 Å |
| Ca-Si | C-S-H 형성 지표 | 3.0-3.5 Å |

### 3.2 RDF 분석 결과

![Top 5 RDF Analysis](../figures/top5_rdf_analysis.png)

**Ca-O RDF 해석**
- 첫 번째 피크 높이가 낮을수록 Ca 용출 활발
- EAFSlag, SteelSlag: 낮은 피크 → 활발한 Ca 용출
- FlyAshC: 중간 피크 → 적절한 Ca 방출

**Si-O RDF 해석**
- 첫 번째 피크 (~1.6 Å): Si-O 공유 결합
- 피크가 높고 좁을수록 SiO₄ 사면체 안정
- WasteGlass, FlyAshC: 안정한 Si 구조

**Ca-Si RDF 해석**
- 피크 존재 (~3.2 Å): Ca-Si 상호작용
- EAFSlag: 가장 높은 피크 → 강한 C-S-H 형성 경향

---

## 4. 결합 분석 (Bond Analysis)

### 4.1 Ca 배위수

| 재료 | Mean | Std | Min | Max |
|------|:----:|:---:|:---:|:---:|
| C3S | 5.22 | 0.63 | 4 | 6 |
| FlyAshC | 5.50 | 0.50 | 5 | 6 |
| EAFSlag | 5.40 | 1.02 | 4 | 7 |
| WasteGlass | 5.00 | 0.00 | 5 | 5 |
| CopperSlag | 4.50 | 0.50 | 4 | 5 |
| SteelSlag | 5.50 | 1.12 | 4 | 7 |

### 4.2 Si 배위수

| 재료 | Mean | Std | Min | Max |
|------|:----:|:---:|:---:|:---:|
| C3S | 4.00 | 0.00 | 4 | 4 |
| FlyAshC | 3.60 | 0.49 | 3 | 4 |
| EAFSlag | 3.50 | 0.50 | 3 | 4 |
| WasteGlass | 3.67 | 0.47 | 3 | 4 |
| CopperSlag | 3.00 | 0.71 | 2 | 4 |
| SteelSlag | 2.67 | 0.47 | 2 | 3 |

### 4.3 해석

- **C3S**: Si CN = 4.00 (완벽한 SiO₄ 사면체)
- **FlyAshC**: Si CN = 3.60 (안정한 구조 유지)
- **SteelSlag**: Si CN = 2.67 (구조 분해 진행 → 반응성 높음)

---

## 5. 시간에 따른 변화 분석

![Top 5 Evolution Comparison](../figures/top5_evolution_comparison.png)

### 5.1 Ca 용출 변화
- **EAFSlag, FlyAshC**: 초기 급격한 Ca 용출 후 안정화
- **WasteGlass, SteelSlag**: 점진적 Ca 용출
- **C3S (baseline)**: 거의 용출 없음

### 5.2 Si CN 변화
- 대부분 안정적 유지 (3.0-4.0 범위)
- **SteelSlag**: 초기 하락 후 안정화

### 5.3 C-S-H 쌍 형성
- **EAFSlag**: 지속적 증가 → 우수한 C-S-H 형성 능력
- **FlyAshC**: 초기 급증 후 안정화

---

## 6. 통계 분석

### 6.1 전체 통계

| 구분 | Score Mean | Score Std | CO₂↓ Mean | CO₂↓ Std |
|------|:----------:|:---------:|:---------:|:--------:|
| 전체 16개 후보 | 61.5 | 17.0 | 78.0% | 7.9% |
| **Top 5** | **84.5** | **4.9** | **77.0%** | **4.0%** |

### 6.2 상관관계 분석

![Metric Correlation Heatmap](../figures/metric_correlation_heatmap.png)

**Score와의 상관관계**

| 지표 | 상관계수 | 강도 | 방향 |
|------|:--------:|:----:|:----:|
| C-S-H 쌍 | **0.935** | **Strong** | + |
| Ca Rate | **0.651** | **Moderate** | + |
| CO₂ 저감 | 0.225 | Weak | + |
| Si CN | -0.258 | Weak | - |

### 6.3 핵심 발견

1. **C-S-H 형성이 가장 중요한 성능 지표** (r = 0.935)
   - C-S-H 쌍이 많을수록 점수 높음
   - EAFSlag가 12쌍으로 최고

2. **Ca 용출 활성이 두 번째로 중요** (r = 0.651)
   - Ca 용출이 C-S-H 형성의 전제 조건
   - Ca Rate > 0인 후보만 좋은 성적

3. **CO₂ 저감과 성능은 약한 상관관계** (r = 0.225)
   - 높은 CO₂ 저감이 높은 성능을 보장하지 않음
   - 성능과 환경 효과의 균형 필요

4. **Si CN은 약한 음의 상관관계** (r = -0.258)
   - 낮은 Si CN이 반드시 나쁜 것은 아님
   - 구조 재배열 = 반응성 증가

---

## 7. 레이더 차트 비교

![Top 5 Radar Comparison](../figures/top5_radar_comparison.png)

**종합 평가**
- **FlyAshC**: 가장 균형 잡힌 성능
- **EAFSlag**: C-S-H 형성 최강
- **WasteGlass**: 안정적인 Si 구조
- **CopperSlag/SteelSlag**: Ca 풍부, 추가 처리 권장

---

## 8. 결론

### 8.1 Top 5 후보 최종 평가

| 순위 | 재료 | 강점 | 약점 | 권장 용도 |
|:----:|------|------|------|----------|
| 1 | **FlyAshC** | 균형 잡힌 성능, 높은 CO₂↓ | - | OPC 대체 30-50% |
| 2 | **EAFSlag** | 최고의 C-S-H 형성 | MD 불안정성 | OPC 대체 20-40% |
| 3 | **WasteGlass** | 안정한 Si 구조, 순환경제 | Ca 부족 | 미분말 혼합 10-20% |
| 4 | **CopperSlag** | Fe 함량으로 강도↑ | Ca 보충 필요 | 골재/혼합재 15-25% |
| 5 | **SteelSlag** | Ca 풍부, 국내 생산량↑ | Si 불안정 | 도로/기초 20-30% |

### 8.2 핵심 메시지

1. **Ca 용출 활성이 C-S-H 형성의 핵심**
   - Ca Rate > 0인 후보가 우수한 성적
   - Ca 부족 재료는 Ca 보충 필요

2. **EAFSlag가 C-S-H 형성에서 C3S와 동등**
   - 12쌍으로 baseline과 동일
   - 75% CO₂ 저감 동시 달성

3. **Top 5 모두 A등급 (75점 이상)**
   - 실용화 가능성 높음
   - 혼합 사용으로 성능 최적화 가능

---

## 9. 생성된 파일

### 9.1 결과 파일 (`data/results/`)
```
deep_analysis_results.json     # 심층 분석 전체 결과
top5_comparison.csv            # Top 5 비교 테이블
```

### 9.2 시각화 (`figures/`)
```
top5_rdf_analysis.png          # RDF 비교 차트
top5_radar_comparison.png      # 레이더 차트
top5_evolution_comparison.png  # 시간 변화 그래프
metric_correlation_heatmap.png # 상관 행렬 히트맵
```

---

## 10. 다음 단계

### Phase 4: 논문 Figure 생성
- `06_Paper_Figures.ipynb` 실행
- 논문용 고품질 Figure 생성 (Figure 1-4)

### 추가 연구 제안
1. **장시간 시뮬레이션** (100 ps)
   - Top 3 후보 (FlyAshC, EAFSlag, WasteGlass)
   - 완전한 C-S-H 성장 관찰

2. **혼합 시스템 연구**
   - FlyAshC + BFS 조합
   - EAFSlag + SilicaFume 조합

3. **실험 검증**
   - 압축 강도 테스트
   - XRD, SEM 분석

---

**작성일**: 2026-01-29  
**상태**: ✅ Phase 3 심층 분석 완료
