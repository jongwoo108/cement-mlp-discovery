# 📚 시멘트 연구 프로젝트 문서

> **탄소중립 시멘트 결합재의 AI 기반 계산 설계**

---

## 📑 문서 목차

이 `docs/` 폴더는 AI 에이전트와 연구자들이 프로젝트를 이해하고 계속할 수 있도록 포괄적인 문서를 포함합니다.

### 노트북 결과 문서 (번호 = 노트북 매칭)

1. **[01_Project_Overview.md](01_Project_Overview.md)** - 프로젝트 배경, 목표, 방법론
2. **[02_STRUCTURE_ANALYSIS.md](02_STRUCTURE_ANALYSIS.md)** - C3S 구조 분석 (RDF, 결합, 배위수)
3. **[03_CSH_FORMATION.md](03_CSH_FORMATION.md)** - C-S-H 젤 형성 시뮬레이션 (Ca 용출, Si 배위)
4. **[04_Alternative_Binders_Results.md](04_Alternative_Binders_Results.md)** - 대체 결합재 스크리닝 결과 ✅ Phase 2-1 완료

### 프로젝트 관리 문서

- **[PIPELINE_PLAN.md](PIPELINE_PLAN.md)** - AI 기반 대체재 발견 연구 계획서 (논문용) ⭐ NEW
- **[PHASE2_PLAN.md](PHASE2_PLAN.md)** - Phase 2 실행 계획서 (구버전)
- **[WORK_LOG.md](WORK_LOG.md)** - 완료된 작업 로그
- **[FILE_STRUCTURE.md](FILE_STRUCTURE.md)** - 파일 구조 및 경로
- **[RESULTS_SUMMARY.md](RESULTS_SUMMARY.md)** - 주요 결과 및 수치 데이터
- **[API_REFERENCE.md](API_REFERENCE.md)** - 코드 패턴 및 재사용 함수

### 빠른 참조

- **세션 재개**: [SESSION_RESUME_TEMPLATE.md](SESSION_RESUME_TEMPLATE.md) 참조
- **코드 예제**: [CODE_EXAMPLES.md](CODE_EXAMPLES.md) 참조
- **데이터 사전**: [DATA_DICTIONARY.md](DATA_DICTIONARY.md) 참조

---

## 🎯 AI 에이전트용

### 컨텍스트 로딩 우선순위

프로젝트 작업 재개 시 AI 에이전트는 다음 순서로 문서를 읽어야 합니다:

1. **PROJECT_OVERVIEW.md** - 전체 그림 이해
2. **FILE_STRUCTURE.md** - 필요한 파일 위치 파악
3. **RESULTS_SUMMARY.md** - 완료된 작업 확인
4. **관련 WORKFLOW_*.md** - 특정 작업 이해
5. **API_REFERENCE.md** - 확립된 코드 패턴 사용

### 주요 정보 요약

```python
# 프로젝트 루트
WORK_DIR = Path("C:/cement_final")

# 현재 상태 (Phase 2-1 완료)
- 환경: ✅ 완료 (cement_final conda env)
- 01_노트북: ✅ 완료 (C3S 최적화 + 수화)
- 02_노트북: ✅ 완료 (구조 분석, RDF, 결합)
- 03_노트북: ✅ 완료 (C-S-H 젤 형성, 10 ps MD)
- 04_노트북: ✅ 완료 (대체 결합재 스크리닝) ← NEW

# Phase 2-1 결과 (선별된 재료)
- Fly Ash: 54.6점, CO₂ 90% 저감
- Slag: 53.5점, CO₂ 80% 저감  
- Metakaolin: 32.6점, CO₂ 70% 저감

# Phase 2 진행 상황
- Phase 2-1: ✅ 완료 (04_노트북)
- Phase 2-2: ⏳ 대기 (05_노트북 - 장시간 MD 100 ps)
- Phase 2-2: ⏳ 대기 (06_노트북 - Ca/Si 비율 연구)
- Phase 2-3: ⏳ 대기 (07_노트북 - 종합 비교 분석)

# 상세 계획서
- docs/PHASE2_PLAN.md 참조
```

---

## 📊 문서 표준

### 파일 명명 규칙

```
CATEGORY_TOPIC.md
```

예시:
- `WORKFLOW_01_OPTIMIZATION.md`
- `RESULTS_SUMMARY.md`
- `API_REFERENCE.md`

### 마크다운 구조

모든 문서 파일은 다음 구조를 따릅니다:

```markdown
# 제목

> 간단한 설명

---

## 섹션 1

내용...

## 섹션 2

내용...

---

**최종 업데이트**: YYYY-MM-DD
**작성자**: 역할/이름
**상태**: 활성/완료/초안
```

---

## 🔄 업데이트 로그

| 날짜 | 문서 | 변경 사항 | 작성자 |
|------|------|-----------|--------|
| 2026-01-28 | 전체 | 초기 문서 생성 | Intern |
| 2026-01-28 | WORKFLOW_02_STRUCTURE_ANALYSIS.md | 02 노트북 문서 추가 | AI Co-Scientist |
| 2026-01-28 | RESULTS_SUMMARY.md | 구조 분석 결과 추가 | AI Co-Scientist |
| 2026-01-28 | WORK_LOG.md | 세션 4 추가 | AI Co-Scientist |
| 2026-01-29 | PHASE2_PLAN.md | Phase 2 실행 계획서 추가 | AI Co-Scientist |
| 2026-01-29 | 04_Alternative_Binders_Results.md | Phase 2-1 결과 문서 추가 | AI Co-Scientist |
| 2026-01-29 | INDEX.md | Phase 2-1 완료 반영, 파일명 정리 | AI Co-Scientist |

---

## 📝 문서 기여 방법

문서 업데이트 시:

1. **날짜 업데이트**: "최종 업데이트" 필드 변경
2. **로그 추가**: UPDATE_LOG.md에 변경 사항 기록
3. **상호 참조**: 관련 문서의 링크 업데이트
4. **버전 관리**: 명확한 메시지로 커밋

---

## 🔍 검색 가이드

특정 정보 찾기:

- **환경 설정**: ENVIRONMENT_SETUP.md
- **파일 위치**: FILE_STRUCTURE.md
- **코드 패턴**: API_REFERENCE.md
- **결과/데이터**: RESULTS_SUMMARY.md
- **오류**: TROUBLESHOOTING.md
- **워크플로우**: WORKFLOW_*.md

---

**최종 업데이트**: 2026-01-29
**관리자**: 연구팀
**버전**: 2.0.0 (Phase 2-1 완료)
