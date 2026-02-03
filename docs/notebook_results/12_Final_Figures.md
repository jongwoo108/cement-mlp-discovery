# 12. Final Figures - 논문용 그림 생성

> 12_Final_Figures.ipynb 실행 결과

---

## 생성된 Figure 목록

### Main Figures

| Figure | 파일명 | 설명 |
|--------|--------|------|
| **Fig 1** | Fig1_Pipeline_Overview | 연구 파이프라인 개요 다이어그램 |
| **Fig 2** | Fig2_Screening_Results | 산업폐기물 스크리닝 결과 |
| **Fig 3** | Fig3_Top5_Comparison | Top 5 후보 비교 |
| **Fig 4** | Fig4_Molecular_Analysis | 분자 수준 분석 |
| **Fig 5** | Fig5_Pipeline_Overview | MatterGen 포함 전체 파이프라인 |
| **Fig 6** | Fig6_MatterGen_Comparison | MatterGen vs 산업폐기물 비교 |
| **Fig 7** | Fig7_Recommendations | 연구 결과 및 권장사항 |

### Supplementary Figures

| Figure | 파일명 | 설명 |
|--------|--------|------|
| **Fig S1** | FigS1_Correlation_Heatmap | 상관관계 히트맵 |

---

## Figure 상세

### Fig 5: Complete Pipeline Overview

MatterGen을 포함한 전체 연구 파이프라인:

```
입력 → CHGNet 스크리닝 → MatterGen 생성 → 검증 → 최종 비교
```

### Fig 6: MatterGen vs Industrial Waste

산업폐기물 Top 5와 MatterGen 구조 비교:
- 수화 반응성 점수
- CO2 저감 잠재력
- 최종 순위

### Fig 7: Research Outcomes and Recommendations

주요 발견 사항:
1. 16개 산업폐기물 CHGNet 스크리닝 완료
2. Top 5 선정: FlyAshC, EAFSlag, WasteGlass, CopperSlag, SteelSlag
3. MatterGen으로 32개 신규 구조 생성 (26개 유효)
4. 최고 MatterGen 구조: Ca2Si2O6 (E/atom = -7.82 eV)

권장사항:
- **단기**: FlyAshC, EAFSlag 블렌드 시멘트 활용
- **중기**: MatterGen 구조 합성 및 실험 검증
- **장기**: AI 기반 물질 발견 확대

---

## 파일 위치

```
figures/paper/
├── Fig1_Pipeline_Overview.png (.pdf)
├── Fig2_Screening_Results.png (.pdf)
├── Fig3_Top5_Comparison.png (.pdf)
├── Fig4_Molecular_Analysis.png (.pdf)
├── Fig5_Pipeline_Overview.png (.pdf)
├── Fig6_MatterGen_Comparison.png (.pdf)
├── Fig7_Recommendations.png (.pdf)
└── FigS1_Correlation_Heatmap.png (.pdf)
```

---

## 사용법

논문에서 Figure 삽입 시:
- PNG: 웹/프레젠테이션용 (300 dpi)
- PDF: 논문 제출용 (벡터)

---

**생성일**: January 30, 2026  
**상태**: Complete
