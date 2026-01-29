# AI 기반 저탄소 시멘트 대체재 발견 연구 계획서

> **목표**: 산업 폐기물 기반 시멘트 대체재를 AI 시뮬레이션으로 발견하고,  
> 2026 AI Co-Scientist Challenge Korea 논문으로 제출

**작성일**: 2026-01-29  
**대회**: 2026 AI Co-Scientist Challenge Korea  
**상태**: 계획 수립

---

## 1. 연구 개요

### 1.1 연구 제목 (예정)

```
AI-Driven Discovery of Carbon-Neutral Cement Alternatives 
from Industrial Waste Using Machine Learning Potentials
```

**한글**: 기계학습 포텐셜을 활용한 산업 폐기물 기반 탄소중립 시멘트 대체재의 AI 기반 발견

### 1.2 연구 배경

- 시멘트 산업: 전 세계 CO₂ 배출량의 **8%** 차지
- 기존 C3S (트리칼슘 실리케이트): 고온 소성으로 대량 CO₂ 발생
- 산업 폐기물 활용: 폐기물 처리 + 탄소 저감의 이중 효과

### 1.3 연구 목적

1. **방법론 기여**: CHGNet 기반 자동화 스크리닝 파이프라인 개발
2. **과학적 발견**: 산업 폐기물 기반 유망 대체재 발견 및 검증
3. **정량적 분석**: CO₂ 저감률, C-S-H 형성 능력 정량화

### 1.4 핵심 기여 (Contributions)

| # | 기여 | 설명 |
|---|------|------|
| 1 | **자동화 파이프라인** | 새 재료 추가 시 코드 수정 없이 테스트 가능한 시스템 |
| 2 | **대규모 스크리닝** | 20+ 산업 폐기물 기반 후보 체계적 평가 |
| 3 | **유망 대체재 발견** | CO₂ 저감률 70%+ 달성 가능한 후보 식별 |
| 4 | **AI-인간 협업** | 도메인 비전문가도 활용 가능한 워크플로우 |

---

## 2. 연구 방법론

### 2.1 전체 워크플로우

```
┌─────────────────────────────────────────────────────────────────┐
│                    AI Co-Scientist Workflow                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [1] 후보 수집          [2] 자동 시뮬레이션      [3] 분석/발견  │
│  ┌──────────┐          ┌──────────────┐        ┌──────────┐    │
│  │산업폐기물│    →     │   CHGNet     │   →    │ 순위화   │    │
│  │데이터베이스│         │   MD 시뮬    │        │ Top N    │    │
│  └──────────┘          └──────────────┘        └──────────┘    │
│       │                       │                      │          │
│       ▼                       ▼                      ▼          │
│  Materials Project      구조 최적화            유망 후보        │
│  문헌 조사              수화 반응              심화 분석        │
│  조성 정의              Ca 용출/Si CN          논문 결과        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 기술 스택

| 구성요소 | 도구 | 역할 |
|----------|------|------|
| ML Potential | CHGNet | DFT 수준 정확도, 1000× 빠른 속도 |
| 시뮬레이션 | ASE + MD | 분자동역학 시뮬레이션 |
| 가속화 | CUDA/GPU | RTX 4070 Laptop GPU |
| 데이터 | Materials Project API | 구조 데이터베이스 |
| 분석 | NumPy, Pandas | 데이터 처리 |
| 시각화 | Matplotlib | 그래프 생성 |

### 2.3 평가 지표

| 지표 | 설명 | 기준 (C3S) |
|------|------|-----------|
| CO₂ 저감률 | 제조 과정 탄소 배출 감소 | 0% (기준) |
| Ca 용출 속도 | 수화 반응 활성 | 0.10 Ca/ps |
| Si 배위수 | 구조 안정성 (이상: 4.0) | 4.0 |
| C-S-H 쌍 | 결합재 형성 능력 | 8 pairs |

### 2.4 스크리닝 점수 공식

```
Score = w₁×(CO₂ 저감) + w₂×(Ca 활성) + w₃×(Si 안정) + w₄×(C-S-H 형성)

가중치: w₁=0.30, w₂=0.20, w₃=0.25, w₄=0.25
```

### 2.5 Baseline 설정 (C3S 기준점)

#### 2.5.1 왜 C3S가 Baseline인가?

| 이유 | 설명 |
|------|------|
| **산업 표준** | 포틀랜드 시멘트의 주성분 (50-70%) |
| **높은 반응성** | 빠른 수화 반응, C-S-H 젤 형성 |
| **CO₂ 주범** | 1450°C 소성 → 대량 CO₂ 발생 |
| **비교 기준** | 모든 대체재는 C3S 대비 평가 |

#### 2.5.2 C3S 구조 및 조성

```
화학식: Ca₃SiO₅ (3CaO·SiO₂)
약칭: C3S (Tricalcium Silicate, Alite)

원자 구성:
- Ca: 9 atoms
- Si: 3 atoms  
- O: 15 atoms
- Total: 27 atoms

특성:
- Ca/Si ratio: 3.0
- 결정계: 단사정계 (Monoclinic)
- 밀도: ~3.15 g/cm³
```

#### 2.5.3 C3S Baseline 시뮬레이션

| 단계 | 파라미터 | 예상 결과 |
|------|----------|----------|
| **1. 구조 최적화** | Fmax < 0.05 eV/Å | E/atom ≈ -7.39 eV |
| **2. 수화 시스템** | +10 H₂O molecules | 42 atoms total |
| **3. MD 시뮬레이션** | 10 ps, 300K, NVT | trajectory 생성 |
| **4. 분석** | Ca/Si/C-S-H | 기준값 도출 |

#### 2.5.4 C3S 기준값 (Reference Values)

| 지표 | C3S 기준값 | 측정 방법 | 의미 |
|------|-----------|----------|------|
| **CO₂ 저감률** | 0% | 정의상 기준 | 비교 기준점 |
| **Ca 용출 속도** | 0.10-0.40 Ca/ps | 3.0Å 이상 이동 Ca 수 / 시간 | 수화 반응 활성 |
| **Si 배위수** | 4.0 | O 원자 수 (cutoff 2.5Å) | SiO₄ 사면체 안정성 |
| **C-S-H 쌍** | 6-8 pairs | Ca-Si 거리 < 3.5Å | 결합재 형성 능력 |
| **에너지** | -7.39 eV/atom | CHGNet 계산 | 열역학적 안정성 |

#### 2.5.5 대체재 평가 기준

```
대체재 점수 계산:

1. CO₂ 저감 점수 (25점 만점)
   score_co2 = (대체재 CO₂ 저감률 / 100) × 25

2. Ca 활성 점수 (25점 만점)
   - C3S 대비 Ca 용출 속도 비교
   - 너무 낮으면 감점 (반응성 부족)
   - 너무 높으면 감점 (구조 불안정)
   score_ca = f(Ca_rate / C3S_Ca_rate)

3. Si 안정성 점수 (25점 만점)
   - Si CN이 4.0에 가까울수록 높은 점수
   score_si = 25 × (1 - |Si_CN - 4.0| / 4.0)

4. C-S-H 형성 점수 (25점 만점)
   - C3S 대비 C-S-H 쌍 수 비교
   score_csh = min(25, (CSH_pairs / C3S_CSH_pairs) × 25)

총점 = score_co2 + score_ca + score_si + score_csh (100점 만점)
```

#### 2.5.6 합격 기준 (Pass Criteria)

| 등급 | 점수 범위 | 의미 | 후속 조치 |
|------|----------|------|----------|
| **A (우수)** | 70+ | C3S 대체 가능 | 심화 분석 (100 ps) |
| **B (양호)** | 50-69 | 조건부 대체 가능 | 조성 최적화 검토 |
| **C (보통)** | 30-49 | 보조재로 활용 | 혼합 사용 검토 |
| **D (미달)** | <30 | 부적합 | 제외 |

---

## 3. 실험 설계

### 3.1 후보 재료 목록 (20+ 종)

#### Tier 1: 철강 산업 부산물

| # | 재료 | 조성 | 출처 | 예상 CO₂↓ |
|---|------|------|------|----------|
| 1 | Blast Furnace Slag (BFS) | Ca-Si-Al-Mg-O | 고로 | 80-90% |
| 2 | Steel Slag (SS) | Ca-Si-Fe-Mg-O | 제강 | 70-80% |
| 3 | Electric Arc Furnace Slag | Ca-Si-Fe-Al-O | 전기로 | 70-80% |
| 4 | Ladle Slag | Ca-Al-Si-Mg-O | 정련 | 75-85% |

#### Tier 2: 석탄 화력 부산물

| # | 재료 | 조성 | 출처 | 예상 CO₂↓ |
|---|------|------|------|----------|
| 5 | Fly Ash Class F | Si-Al-Fe-Ca-O | 무연탄 | 80-90% |
| 6 | Fly Ash Class C | Ca-Si-Al-O | 아역청탄 | 80-90% |
| 7 | Bottom Ash | Si-Al-Fe-Ca-O | 보일러 바닥 | 70-80% |
| 8 | Pond Ash | Si-Al-Fe-Ca-O | 저장지 | 70-80% |

#### Tier 3: 금속 제련 부산물

| # | 재료 | 조성 | 출처 | 예상 CO₂↓ |
|---|------|------|------|----------|
| 9 | Copper Slag | Fe-Si-Ca-Al-O | 구리 제련 | 70-80% |
| 10 | Lead-Zinc Slag | Fe-Si-Ca-Zn-O | 연아연 제련 | 65-75% |
| 11 | Nickel Slag | Fe-Si-Mg-O | 니켈 제련 | 70-80% |
| 12 | Red Mud | Fe-Al-Si-Ti-O | 알루미늄 정련 | 60-70% |

#### Tier 4: 실리카 풍부 폐기물

| # | 재료 | 조성 | 출처 | 예상 CO₂↓ |
|---|------|------|------|----------|
| 13 | Silica Fume | Si-O | 반도체/실리콘 | 85-90% |
| 14 | Rice Husk Ash | Si-K-O | 쌀겨 소각 | 90%+ |
| 15 | Sugarcane Bagasse Ash | Si-Al-Ca-O | 사탕수수 | 90%+ |
| 16 | Palm Oil Fuel Ash | Si-K-Ca-O | 팜유 생산 | 85-90% |

#### Tier 5: 기타 산업 폐기물

| # | 재료 | 조성 | 출처 | 예상 CO₂↓ |
|---|------|------|------|----------|
| 17 | Waste Glass | Si-Na-Ca-O | 폐유리 | 70-80% |
| 18 | Ceramic Waste | Si-Al-O | 폐도자기 | 60-70% |
| 19 | Phosphogypsum | Ca-S-O | 비료 생산 | 50-60% |
| 20 | Coal Gangue | Si-Al-Fe-O | 석탄 채굴 | 65-75% |
| 21 | Metakaolin | Si-Al-O | 점토 소성 | 70-80% |

### 3.2 시뮬레이션 파라미터

```yaml
# config/simulation.yaml

baseline:
  material: C3S
  reference_energy: -7.39 eV/atom

optimization:
  fmax: 0.05 eV/Å
  max_steps: 500
  optimizer: BFGS

hydration:
  n_water: 10
  box_expansion: 1.5×

md_simulation:
  screening:
    duration: 10 ps
    temperature: 300 K
    timestep: 1 fs
    ensemble: NVT
  
  deep_analysis:
    duration: 100 ps
    temperature: 300 K
    timestep: 1 fs

analysis:
  ca_leaching_threshold: 3.0 Å
  si_coordination_cutoff: 2.5 Å
  csh_pair_cutoff: 3.5 Å
```

### 3.3 컴퓨팅 자원

| 항목 | 사양 |
|------|------|
| GPU | NVIDIA RTX 4070 Laptop (8GB) |
| CPU | Intel Core i7-13700H |
| RAM | 32GB DDR5 |
| Storage | 1TB NVMe SSD |
| CUDA | 12.x |
| Python | 3.11 |

### 3.4 예상 실행 시간

| 단계 | 재료당 | 20개 재료 |
|------|--------|----------|
| 구조 최적화 | ~30s | ~10min |
| 수화 시스템 생성 | ~10s | ~3min |
| MD 10ps | ~15min | ~5h |
| 분석 | ~30s | ~10min |
| **총계** | ~16min | **~5.5h** |

---

## 4. 프로젝트 구조

### 4.1 폴더 구조

```
cement_final/
├── src/                          # 핵심 라이브러리
│   ├── __init__.py
│   ├── core/
│   │   ├── calculator.py         # CHGNet 초기화
│   │   ├── optimizer.py          # 구조 최적화
│   │   └── md.py                 # MD 시뮬레이션
│   ├── analysis/
│   │   ├── ca_leaching.py
│   │   ├── si_coordination.py
│   │   ├── csh_formation.py
│   │   └── scoring.py            # 스크리닝 점수
│   ├── database/
│   │   ├── candidates.py         # 후보 관리
│   │   └── materials_project.py  # MP API
│   ├── pipeline/
│   │   ├── screening.py          # 자동화 루프
│   │   └── config.py             # 설정 파싱
│   └── visualization/
│       └── plots.py
│
├── config/
│   ├── simulation.yaml
│   ├── candidates.yaml
│   └── evaluation.yaml
│
├── notebooks/
│   ├── archive/                  # 기존 노트북 (참고용)
│   └── pipeline/                 # 새 파이프라인
│       ├── 01_Setup_Validation.ipynb
│       ├── 02_Baseline_Reference.ipynb
│       ├── 03_Candidate_Database.ipynb
│       ├── 04_Screening_Pipeline.ipynb
│       ├── 05_Results_Analysis.ipynb
│       └── 06_Paper_Figures.ipynb
│
├── data/
│   ├── candidates/               # 후보 구조
│   ├── trajectories/             # MD 궤적
│   └── results/                  # 스크리닝 결과
│
├── paper/                        # 논문 작성
│   ├── template_2026.tex
│   ├── figures/
│   ├── tables/
│   └── references.bib
│
└── docs/                         # 문서
```

### 4.2 노트북 상세

| # | 노트북 | 목적 | 예상 시간 |
|---|--------|------|----------|
| 01 | Setup_Validation | 환경 검증, 모듈 테스트 | 10min |
| 02 | Baseline_Reference | C3S 기준점 확립 | 20min |
| 03 | Candidate_Database | 20+ 후보 구조 생성 | 2h |
| 04 | Screening_Pipeline | 전체 스크리닝 실행 | 5-6h |
| 05 | Results_Analysis | 순위화, 시각화 | 1h |
| 06 | Paper_Figures | 논문용 그래프 생성 | 1h |

---

## 5. 예상 결과 (논문 산출물)

### 5.1 주요 테이블

#### Table 1: 후보 재료 스크리닝 결과

| Rank | Material | CO₂↓(%) | Ca Rate | Si CN | C-S-H | Score |
|------|----------|---------|---------|-------|-------|-------|
| 1 | ? | ? | ? | ? | ? | ? |
| 2 | ? | ? | ? | ? | ? | ? |
| ... | ... | ... | ... | ... | ... | ... |
| 20 | ? | ? | ? | ? | ? | ? |

*실험 후 채워질 예정*

#### Table 2: Top 5 후보 상세 분석

| Property | #1 | #2 | #3 | #4 | #5 | C3S (ref) |
|----------|-----|-----|-----|-----|-----|-----------|
| Formula | ? | ? | ? | ? | ? | Ca₃SiO₅ |
| CO₂ Reduction | ?% | ?% | ?% | ?% | ?% | 0% |
| ... | ... | ... | ... | ... | ... | ... |

### 5.2 주요 그래프

#### Figure 1: 스크리닝 결과 개요
- (a) CO₂ 저감률 비교 (bar chart)
- (b) Ca 용출 활성 비교
- (c) Si 배위수 안정성
- (d) 종합 점수 순위

#### Figure 2: Top 후보 시간 변화
- (a) Ca 용출 진행
- (b) Si CN 변화
- (c) C-S-H 쌍 형성

#### Figure 3: 조성-성능 상관관계
- Ca/Si 비율 vs 성능
- Al 함량 영향

### 5.3 핵심 발견 (예상)

```
[실험 후 작성]
- "X 재료가 CO₂ 저감 Y%를 달성하면서 C-S-H 형성 능력 유지"
- "철강 슬래그 계열이 전반적으로 우수한 성능"
- "실리카 풍부 폐기물은 추가 활성화제 필요"
```

---

## 6. 논문 구조 (AI Co-Scientist Challenge 양식)

### 6.1 논문 목차

```
1. Introduction
   1.1 Background (시멘트 CO₂ 문제)
   1.2 Related Work (기존 대체재 연구)
   1.3 Contributions (본 연구 기여)

2. Methods
   2.1 Machine Learning Potential (CHGNet)
   2.2 Automated Screening Pipeline
   2.3 Evaluation Metrics
   2.4 Candidate Materials

3. Results
   3.1 Screening Results Overview
   3.2 Top Candidates Analysis
   3.3 Composition-Performance Correlation

4. Discussion
   4.1 Comparison with Literature
   4.2 Practical Implications
   4.3 Limitations

5. Conclusion
   5.1 Summary
   5.2 Future Work

References
Appendix
```

### 6.2 체크리스트 대응

| # | 항목 | 대응 계획 |
|---|------|----------|
| 1 | Claims | Methods와 Results에서 기여 명시 |
| 2 | Limitations | Discussion 섹션에 포함 |
| 4 | Reproducibility | GitHub 코드 + 파라미터 명시 |
| 5 | Open Access | GitHub 공개, 데이터 공유 |
| 6 | Experimental Details | Methods에 상세 기술 |
| 8 | Compute Resources | Methods에 GPU/시간 명시 |
| 10 | Broader Impacts | 탄소 저감 사회적 가치 |

---

## 7. 실행 로드맵

### Phase 1: 기반 구축 (Day 1-2)

```
□ 프로젝트 구조 재정리
  - notebooks/archive/ 이동
  - src/ 폴더 생성
  - config/ 설정 파일 작성

□ 핵심 함수 모듈화
  - 기존 04번 노트북에서 추출
  - src/core/, src/analysis/ 구현

□ 01_Setup_Validation.ipynb
  - 환경 검증
  - 모듈 import 테스트
```

### Phase 2: 데이터베이스 구축 (Day 3-4)

```
□ 02_Baseline_Reference.ipynb
  - C3S 기준점 확립
  - 평가 기준 저장

□ 03_Candidate_Database.ipynb
  - 20+ 후보 조성 정의
  - Materials Project 구조 다운로드
  - 수동 구조 생성 (필요시)
```

### Phase 3: 스크리닝 실행 (Day 5-6)

```
□ 04_Screening_Pipeline.ipynb
  - 전체 후보 자동 스크리닝
  - 진행 상황 모니터링
  - 에러 핸들링

□ 실행 (예상 5-6시간)
  - GPU 사용 확인
  - 중간 결과 저장
```

### Phase 4: 분석 및 시각화 (Day 7)

```
□ 05_Results_Analysis.ipynb
  - 순위화
  - 통계 분석
  - Top 후보 선별

□ 06_Paper_Figures.ipynb
  - Figure 1-3 생성
  - Table 1-2 생성
```

### Phase 5: 논문 작성 (Day 8-10)

```
□ paper/ 폴더 구성
  - template_2026.tex 작성
  - figures/ 복사
  - references.bib 정리

□ 섹션별 작성
  - Abstract
  - Introduction
  - Methods
  - Results
  - Discussion
  - Conclusion

□ 체크리스트 작성
  - 15개 항목 답변
```

### Phase 6: 최종 검토 (Day 11-12)

```
□ 논문 검토
  - 페이지 제한 (9페이지) 확인
  - 그래프/표 품질 확인

□ 코드 정리
  - GitHub 공개 준비
  - README 작성

□ 제출
```

---

## 8. 하이브리드 접근법 상세

### 8.1 기존 코드 활용

| 기존 (04번 노트북) | 새 위치 | 수정 사항 |
|-------------------|---------|----------|
| `run_hydration_md()` | `src/core/md.py` | 설정 파일 기반 |
| `analyze_ca_leaching()` | `src/analysis/ca_leaching.py` | 일반화 |
| `analyze_si_coordination()` | `src/analysis/si_coordination.py` | cutoff 설정 가능 |
| `calculate_screening_score()` | `src/analysis/scoring.py` | 가중치 설정 가능 |
| 시각화 코드 | `src/visualization/plots.py` | 템플릿화 |

### 8.2 새로 작성

| 모듈 | 기능 | 우선순위 |
|------|------|---------|
| `src/database/candidates.py` | 후보 CRUD | 높음 |
| `src/pipeline/screening.py` | 자동화 루프 | 높음 |
| `src/pipeline/config.py` | YAML 파싱 | 중간 |
| `src/database/materials_project.py` | MP API | 중간 |

---

## 9. 리스크 및 대응

| 리스크 | 확률 | 영향 | 대응 |
|--------|------|------|------|
| GPU 메모리 부족 | 중 | 중 | 배치 크기 조절 |
| MP API 제한 | 낮 | 중 | 수동 구조 생성 |
| 시뮬레이션 실패 | 중 | 낮 | 에러 핸들링, 건너뛰기 |
| 유의미한 결과 없음 | 낮 | 높 | 조성 범위 확대 |
| 시간 초과 | 중 | 중 | 후보 수 조절 (15개로) |

---

## 10. 성공 기준

### 10.1 최소 성공 기준 (Minimum Viable)

- [ ] 15+ 후보 스크리닝 완료
- [ ] Top 5 유망 후보 식별
- [ ] 논문 초안 완성

### 10.2 목표 성공 기준 (Target)

- [ ] 20+ 후보 스크리닝 완료
- [ ] CO₂ 70%+ 저감 후보 3개 이상 발견
- [ ] 논문 제출 완료
- [ ] 코드 GitHub 공개

### 10.3 확장 성공 기준 (Stretch)

- [ ] 25+ 후보 스크리닝
- [ ] Top 3 후보 100ps 심화 분석
- [ ] 실험 검증 방향 제시

---

## 11. 결론

### 11.1 연구 요약

본 연구는 CHGNet 기반 자동화 파이프라인을 구축하여 20+ 산업 폐기물 기반 시멘트 대체재 후보를 체계적으로 스크리닝하고, 유망 저탄소 대체재를 발견하는 것을 목표로 합니다.

### 11.2 예상 기여

1. **방법론**: 재사용 가능한 AI 기반 재료 스크리닝 파이프라인
2. **발견**: 산업 폐기물 활용 유망 시멘트 대체재
3. **영향**: 시멘트 산업 탄소 저감에 기여

### 11.3 다음 단계

이 계획서 승인 후:
1. 프로젝트 구조 재정리
2. src/ 모듈 구현
3. 01번 노트북 작성 시작

---

**작성일**: 2026-01-29  
**버전**: 2.0  
**상태**: 검토 대기
