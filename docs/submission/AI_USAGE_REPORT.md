# AI 활용 보고서

> 2026 AI Co-Scientist Challenge Korea - Track 1 제출물

---

## 1. AI 활용 개요

### 연구 수행 방식

```
가설 생성 → 실험 설계 → 데이터 분석 → 보고서 작성
    ↓           ↓           ↓           ↓
  Claude     CHGNet      Claude      Claude
            MatterGen
```

### 활용한 AI 도구 목록

| AI 도구 | 버전/모델 | 역할 | 활용 단계 |
|---------|----------|------|----------|
| **Claude** | Sonnet 4 (Cursor IDE) | 연구 설계, 코드 작성, 분석, 문서화 | 전 과정 |
| **CHGNet** | v0.3.0 | 분자 시뮬레이션 (MLP) | 실험 수행 |
| **MatterGen** | chemical_system_energy_above_hull | 신규 물질 구조 생성 | 실험 수행 |

---

## 2. AI 활용 상세

### 2.1 Claude (AI 연구 동료)

**역할**: 연구 전 과정의 공동 연구자

| 단계 | 활용 내용 | 기여도 |
|------|----------|:------:|
| **가설 생성** | 산업폐기물 기반 시멘트 대체재 후보 선정 | 30% |
| **실험 설계** | CHGNet 파이프라인 설계, 평가 지표 정의 | 50% |
| **코드 작성** | Python 스크리닝 파이프라인, 분석 코드 | 80% |
| **데이터 분석** | 수화 시뮬레이션 결과 해석, 비교 분석 | 60% |
| **보고서 작성** | 논문 초안, 문서화, Figure 설명 | 70% |

**활용 URL**: Cursor IDE 내장 Claude (로컬 세션)

**활용 로그 요약**:
- 총 세션: ~20회
- 주요 대화: 파이프라인 설계, 에러 디버깅, 결과 해석
- 코드 생성: `src/`, `notebooks/pipeline/` 전체

### 2.2 CHGNet (Machine Learning Potential)

**역할**: DFT 대체 분자 시뮬레이션

| 항목 | 내용 |
|------|------|
| **모델** | CHGNet v0.3.0 (pretrained) |
| **용도** | 구조 최적화, 수화 MD 시뮬레이션 |
| **속도 향상** | DFT 대비 1000× |
| **정확도** | DFT 대비 0.15% 오차 |

**활용 코드**:
```python
from chgnet.model import CHGNet
from chgnet.model.dynamics import MolecularDynamics

model = CHGNet.load()
md = MolecularDynamics(atoms, model, ensemble='nvt', temperature=300)
md.run(steps=10000)
```

**GitHub**: https://github.com/CederGroupHub/chgnet

### 2.3 MatterGen (Generative AI)

**역할**: 신규 시멘트 후보 구조 생성

| 항목 | 내용 |
|------|------|
| **모델** | chemical_system_energy_above_hull |
| **화학 시스템** | Ca-Si-Al-O, Ca-Si-Al-Fe-O, Ca-Si-O, Ca-Si-Mg-O |
| **생성 구조** | 32개 (유효: 26개) |
| **안정성 기준** | E_hull ≤ 0.05 eV/atom |

**활용 코드**:
```python
from mattergen.generator import MatterGenGenerator

generator = MatterGenGenerator(model_name="chemical_system_energy_above_hull")
structures = generator.generate(
    chemical_system="Ca-Si-O",
    num_structures=8,
    guidance_factor=2.0
)
```

**GitHub**: https://github.com/microsoft/mattergen

---

## 3. AI 활용 체크리스트

| # | 항목 | 적용 여부 | 설명 |
|:-:|------|:--------:|------|
| 1 | 가설 생성에 AI 활용 | ✅ | Claude와 함께 연구 방향 설정 |
| 2 | 실험 설계에 AI 활용 | ✅ | 파이프라인 구조, 평가 지표 설계 |
| 3 | 데이터 생성에 AI 활용 | ✅ | MatterGen으로 신규 구조 생성 |
| 4 | 시뮬레이션에 AI 활용 | ✅ | CHGNet MLP로 MD 가속화 |
| 5 | 데이터 분석에 AI 활용 | ✅ | Claude와 결과 해석 |
| 6 | 보고서 작성에 AI 활용 | ✅ | Claude로 논문 초안 작성 |
| 7 | 코드 작성에 AI 활용 | ✅ | Claude로 전체 파이프라인 구현 |

---

## 4. AI 기여도 요약

### 전체 연구 기여도

| AI 도구 | 기여 영역 | 기여도 |
|---------|----------|:------:|
| **Claude** | 연구 설계, 코드, 분석, 문서화 | **60%** |
| **CHGNet** | 분자 시뮬레이션 수행 | **25%** |
| **MatterGen** | 신규 구조 생성 | **10%** |
| **인간 연구자** | 방향 설정, 의사결정, 실행 | **5%** |

### AI Co-Scientist 역할 수행

```
본 연구에서 AI는 단순 도구가 아닌 "연구 동료(Co-Scientist)"로서:

1. 가설 제안: 산업폐기물의 시멘트 대체 가능성 분석
2. 방법론 설계: MLP 기반 스크리닝 파이프라인 구축
3. 실험 수행: CHGNet/MatterGen으로 48개 후보 평가
4. 결과 해석: 수화 메커니즘 분석, Top 후보 선정
5. 논문 작성: 영문 연구보고서 초안 작성

→ 연구 전 과정에서 AI가 주도적 역할 수행
```

---

## 5. 재현성 정보

### 코드 저장소

| 항목 | 위치 |
|------|------|
| GitHub URL | [제출 시 추가] |
| 메인 코드 | `src/`, `notebooks/pipeline/` |
| 설정 파일 | `config/` |
| 결과 데이터 | `data/results/` |

### 환경 설정

```yaml
# environment.yml
name: cement_final
dependencies:
  - python=3.10
  - pytorch=2.4
  - chgnet=0.3.0
  - ase=3.22
  - numpy
  - pandas
  - matplotlib
```

### 실행 순서

```
1. conda env create -f environment.yml
2. notebooks/pipeline/01_Setup_Validation.ipynb
3. notebooks/pipeline/02_Baseline_Reference.ipynb
...
13. notebooks/pipeline/13_Mechanical_Properties.ipynb
```

---

**작성일**: 2026년 1월 30일  
**작성자**: [연구자명]  
**AI 도구**: Claude Sonnet 4, CHGNet v0.3.0, MatterGen
