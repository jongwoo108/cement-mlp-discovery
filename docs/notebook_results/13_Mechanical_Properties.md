# 13. Mechanical Properties - 기계적 특성 계산

> 13_Mechanical_Properties.ipynb 실행 결과

---

## 개요

MatterGen 생성 구조의 **수화 후 기계적 특성**을 계산하여 콘크리트 재료로서의 가능성을 평가했습니다.

### 계산 방법

```
MatterGen 구조 → 물 5개 추가 → MD 평형화 (500 steps) → Bulk Modulus 계산
```

### 평가 기준

| 등급 | 조건 | 의미 |
|:----:|------|------|
| **A** | K ≥ 36 GPa | 시멘트 수준 이상 |
| **B** | K ≥ 24 GPa | C-S-H 겔 수준 |
| **C** | K < 24 GPa | 기준 미달 |

---

## 기준값 (Reference)

| 재료 | Bulk Modulus (K) | Young's Modulus (E) |
|------|:----------------:|:-------------------:|
| **Portland Cement** | 45 GPa | 25 GPa |
| **C-S-H Gel** | 30 GPa | 20 GPa |

---

## 결과

### MatterGen 구조 기계적 특성

| 구조 | 화학식 | K (GPa) | E (GPa) | G (GPa) | K/K_cement | 등급 |
|------|--------|:-------:|:-------:|:-------:|:----------:|:----:|
| phase1_Ca_Si_Al_O_005 | **AlCa2O4Si** | 141.0 | 211.5 | 84.6 | 3.13 | **A** |
| phase2_Ca_Si_O_005 | **Ca2OSi** | 137.8 | 206.7 | 82.7 | 3.06 | **A** |
| phase2_Ca_Si_Mg_O_000 | CaMgOSi | 129.5 | 194.2 | 77.7 | 2.88 | **A** |
| phase1_Ca_Si_Al_O_006 | Al2CaO2Si | 129.2 | 193.8 | 77.5 | 2.87 | **A** |
| phase2_Ca_Si_Mg_O_007 | CaMgOSi | 127.1 | 190.6 | 76.2 | 2.82 | **A** |
| phase1_Ca_Si_Al_O_001 | AlCaOSi3 | 86.5 | 129.8 | 51.9 | 1.92 | **A** |
| phase1_Ca_Si_Al_Fe_O_007 | Al2CaFe2O | 81.1 | 121.6 | 48.6 | 1.80 | **A** |
| phase1_Ca_Si_Al_O_004 | AlCa2O4Si | 65.7 | 98.5 | 39.4 | 1.46 | **A** |
| phase2_Ca_Si_Mg_O_003 | Ca2MgOSi | 60.8 | 91.2 | 36.5 | 1.35 | **A** |
| phase1_Ca_Si_Al_O_007 | AlCa2OSi | 59.1 | 88.6 | 35.4 | 1.31 | **A** |

---

## 핵심 발견

### 1. 모든 구조가 A등급

- **10개 구조 모두 시멘트 기준(45 GPa) 이상**
- 최고: AlCa2O4Si (K = 141 GPa, 시멘트의 3.1배)
- 최저: AlCa2OSi (K = 59 GPa, 시멘트의 1.3배)

### 2. Portland Cement 대비 우수

| 비교 항목 | Portland Cement | MatterGen (평균) | 배율 |
|-----------|:---------------:|:----------------:|:----:|
| Bulk Modulus | 45 GPa | **101.8 GPa** | 2.3× |
| Young's Modulus | 25 GPa | **152.7 GPa** | 6.1× |

### 3. Top 3 후보

| 순위 | 화학식 | K (GPa) | 특징 |
|:----:|--------|:-------:|------|
| 1 | **AlCa2O4Si** | 141.0 | 최고 강도, Ca-Al-Si-O 시스템 |
| 2 | **Ca2OSi** | 137.8 | 단순 조성, Ca-Si-O 시스템 |
| 3 | **CaMgOSi** | 129.5 | Mg 포함, 다양한 원소 |

---

## 해석 및 한계

### 긍정적 측면

- MatterGen 구조가 **기계적 강도 측면에서 매우 우수**
- 고강도 저탄소 시멘트 개발 가능성 시사

### 한계점

- **수화 반응성이 낮음** (11번 노트북 결과)
- 기계적 특성이 우수해도 **수화가 안 되면 실제 사용 불가**
- **대안적 활성화 방법** 필요 (알칼리 활성화, 열처리 등)

### 향후 연구 방향

1. Ca-rich 구조 재생성 (Ca/Si ≥ 1.5)
2. 알칼리 활성화 시뮬레이션
3. 산업폐기물과 블렌딩 최적화
4. 실험적 합성 및 검증

---

## 데이터 파일

| 파일 | 위치 | 설명 |
|------|------|------|
| `mechanical_properties_hydrated.json` | `data/results/` | 전체 계산 결과 |

---

## 논문 활용

### Figure 제안

- 기계적 특성 바 차트 (MatterGen vs Portland Cement)
- Top 3 구조의 응력-변형 다이어그램

### 결론 문구 예시

> "MatterGen-generated structures exhibit exceptional mechanical properties  
> (K = 59-141 GPa), significantly exceeding Portland cement (45 GPa).  
> However, hydration reactivity optimization remains a key challenge  
> for practical application."

---

**생성일**: January 30, 2026  
**상태**: Complete
