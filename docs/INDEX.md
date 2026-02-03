# 문서 인덱스

> AI 기반 탄소중립 시멘트 바인더 전산 설계

---

## 빠른 링크

- **[FINAL_RESULTS.md](FINAL_RESULTS.md)** - 최종 연구 결과 요약
- **[RESEARCH_ROADMAP.md](RESEARCH_ROADMAP.md)** - 연구 로드맵 (추가 실험 계획)
- **[submission/FINAL_PAPER.md](submission/FINAL_PAPER.md)** - 제출용 논문 (영문)
- **[PIPELINE_PLAN.md](PIPELINE_PLAN.md)** - 연구 파이프라인 계획

---

## 📁 폴더 구조

```
docs/
├── planning/           ← 연구 계획 문서
├── notebook_results/   ← 노트북 실험 결과
├── submission/         ← 대회 제출물
└── (루트)              ← 핵심 참조 문서
```

---

## 📋 submission/ (제출물)

| 문서 | 설명 |
|------|------|
| [FINAL_PAPER.md](submission/FINAL_PAPER.md) | **최종 연구보고서 (영문)** |
| [PAPER_SUBMISSION.md](submission/PAPER_SUBMISSION.md) | 연구보고서 초안 |
| [PAPER_OUTLINE.md](submission/PAPER_OUTLINE.md) | 논문 Outline |
| [AI_USAGE_REPORT.md](submission/AI_USAGE_REPORT.md) | **AI 활용 보고서** |
| [DATA_LIST.md](submission/DATA_LIST.md) | **활용 데이터 목록** |

---

## 📊 notebook_results/ (실험 결과)

| 문서 | 노트북 | 설명 |
|------|:------:|------|
| [04_Screening_Results.md](notebook_results/04_Screening_Results.md) | 04 | 산업폐기물 스크리닝 결과 |
| [05_Results_Analysis.md](notebook_results/05_Results_Analysis.md) | 05 | 결과 분석 |
| [06_Paper_Figures.md](notebook_results/06_Paper_Figures.md) | 06 | 논문 Figure (1-4) |
| [08_MatterGen_Guide.md](notebook_results/08_MatterGen_Guide.md) | 08 | MatterGen 사용 가이드 |
| [11_Final_Comparison.md](notebook_results/11_Final_Comparison.md) | 11 | 최종 비교 (산업폐기물 vs MatterGen) |
| [12_Final_Figures.md](notebook_results/12_Final_Figures.md) | 12 | 최종 Figure (5-7, S1) |
| [13_Mechanical_Properties.md](notebook_results/13_Mechanical_Properties.md) | 13 | 기계적 특성 결과 |
| [14_Supercell_Experiment.md](notebook_results/14_Supercell_Experiment.md) | 14 | Supercell 실험 (부정적 결과) |
| [15_Ca_Si_Ratio_Results.md](notebook_results/15_Ca_Si_Ratio_Results.md) | 15 | Ca/Si 비율 효과 분석 |
| [16_Ca_Rich_MatterGen_Results.md](notebook_results/16_Ca_Rich_MatterGen_Results.md) | 16 | Ca-rich 구조 생성 |
| [17_Alkali_Activation_Results.md](notebook_results/17_Alkali_Activation_Results.md) | 17 | **알칼리 활성화 (MatterGen 활용 경로 발견!)** |

---

## 📝 planning/ (연구 계획)

| 문서 | 설명 |
|------|------|
| [01_Project_Overview.md](planning/01_Project_Overview.md) | 프로젝트 개요 및 목표 |
| [02_Structure_Analysis.md](planning/02_Structure_Analysis.md) | C3S 구조 분석 |
| [03_CSH_Formation.md](planning/03_CSH_Formation.md) | C-S-H 젤 형성 분석 |
| [04_Alternative_Binders.md](planning/04_Alternative_Binders.md) | 대체 바인더 초기 결과 |
| [05_Phase2_Plan.md](planning/05_Phase2_Plan.md) | 2단계 계획 |
| [06_Results_Summary.md](planning/06_Results_Summary.md) | 결과 요약 (초기) |
| [07_Work_Log.md](planning/07_Work_Log.md) | 작업 로그 |

---

## 📚 참조 문서 (루트)

| 문서 | 설명 |
|------|------|
| [FINAL_RESULTS.md](FINAL_RESULTS.md) | **최종 연구 결과 요약** |
| [RESEARCH_ROADMAP.md](RESEARCH_ROADMAP.md) | **연구 로드맵 (추가 실험 계획)** |
| [PIPELINE_PLAN.md](PIPELINE_PLAN.md) | 연구 파이프라인 전체 계획 |
| [API_REFERENCE.md](API_REFERENCE.md) | 코드 패턴 및 재사용 함수 |
| [FILE_STRUCTURE.md](FILE_STRUCTURE.md) | 프로젝트 파일 구조 |
| [README.md](README.md) | 문서 안내 |

---

## 핵심 결과 요약

### 최종 순위 (수화 반응 기반)

| 순위 | 재료 | 출처 | 최종 점수 | CO₂ 저감 |
|:----:|------|------|:---------:|:--------:|
| 1 | EAFSlag | 산업폐기물 | 77.8 | 75% |
| 2 | WasteGlass | 산업폐기물 | 75.7 | 75% |
| 3 | FlyAshC | 산업폐기물 | 75.1 | 85% |

### 출처별 비교

| 출처 | 평균 점수 | CO₂ 저감 |
|------|:---------:|:--------:|
| 산업폐기물 | 74.5 | 75-85% |
| MatterGen | 63.0 | 90% |

### 기계적 특성 (MatterGen)

| 지표 | Portland Cement | MatterGen (평균) |
|------|:---------------:|:----------------:|
| Bulk Modulus | 45 GPa | **101.8 GPa** |
| Young's Modulus | 25 GPa | **152.7 GPa** |

---

## 환경 정보

| 환경 | 용도 |
|------|------|
| `cement_final` | CHGNet 분석, 메인 파이프라인 |
| `base` | MatterGen 구조 생성 |

---

**최종 수정**: 2026년 1월 30일  
**버전**: 3.0.0 (폴더 구조 재정리)  
**상태**: 완료
