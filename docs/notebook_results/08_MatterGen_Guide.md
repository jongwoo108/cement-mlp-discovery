# MatterGen 사용 가이드

## AI 기반 저탄소 시멘트 대체재 발견

---

## 1. 환경 설정

### 필수 조건
- MatterGen 설치 (base 환경)
- 체크포인트 다운로드 완료 (Git LFS)
- GPU (CUDA) 사용 가능

### 환경 확인
```bash
# MatterGen 설치 확인
conda activate base
python -c "import mattergen; print('OK')"

# 체크포인트 확인
ls c:\cement_final\mattergen\checkpoints\
```

---

## 2. 실행 계획

### Phase 1: Top 5 기반 구조 다양화

| 시스템 | 기반 후보 | 모델 |
|--------|----------|------|
| Ca-Si-Al-O | FlyAshC | chemical_system_energy_above_hull |
| Ca-Si-Al-Fe-O | EAFSlag | chemical_system_energy_above_hull |

### Phase 2: C-S-H 핵심 조성 탐색

| 시스템 | 목적 | 모델 |
|--------|------|------|
| Ca-Si-O | 기본 칼슘 실리케이트 | chemical_system_energy_above_hull |
| Ca-Si-Mg-O | 마그네슘 치환 | chemical_system_energy_above_hull |

### Phase 3: 특성 기반 역설계

| 조건 | 목표 | 모델 |
|------|------|------|
| bulk_modulus=100 GPa | 높은 강도 | ml_bulk_modulus |

---

## 3. 실행 방법

### 방법 A: Python 스크립트 사용

```bash
# base 환경 활성화
conda activate base

# Phase 1 실행
cd c:\cement_final\mattergen
python c:\cement_final\scripts\run_mattergen.py --phase=1

# Phase 2 실행
python c:\cement_final\scripts\run_mattergen.py --phase=2

# Phase 3 실행
python c:\cement_final\scripts\run_mattergen.py --phase=3
```

### 방법 B: Jupyter 노트북 사용

1. `08_MatterGen_Generation.ipynb` 열기
2. 커널: Python 3 (base) 선택
3. 셀 순서대로 실행

### 방법 C: CLI 직접 사용

```bash
cd c:\cement_final\mattergen

mattergen-generate "c:\cement_final\data\mattergen\phase1_Ca_Si_Al_O" \
    --model_path="checkpoints/chemical_system_energy_above_hull" \
    --batch_size=4 \
    --num_batches=2 \
    --properties_to_condition_on="{'chemical_system': 'Ca-Si-Al-O', 'energy_above_hull': 0.05}" \
    --diffusion_guidance_factor=2.0
```

---

## 4. 출력 파일

### 생성 디렉토리 구조
```
c:\cement_final\data\mattergen\
├── phase1_Ca_Si_Al_O/
│   ├── generated_crystals_cif.zip
│   ├── generated_crystals.extxyz
│   └── generated_trajectories.zip
├── phase1_Ca_Si_Al_Fe_O/
├── phase2_Ca_Si_O_stable/
├── phase2_Ca_Si_Mg_O/
└── phase3_high_bulk_modulus/
```

### 파일 설명
- `generated_crystals_cif.zip`: CIF 형식 구조 파일
- `generated_crystals.extxyz`: Extended XYZ 형식
- `generated_trajectories.zip`: 생성 과정 기록

---

## 5. 검증 파이프라인

생성된 구조는 `09_MatterGen_Validation.ipynb`에서 검증:

1. **CHGNet 에너지 계산**: 안정성 확인
2. **구조 최적화**: fmax < 0.05 eV/A
3. **수화 시뮬레이션**: 물 분자 추가 후 MD
4. **Top 5 비교**: 동일 기준으로 점수화

---

## 6. 예상 소요 시간

| 작업 | 시간 |
|------|------|
| 모델 로딩 (첫 실행) | 2-5분 |
| 구조 생성 (8개) | 10-20분 |
| 전체 Phase 1+2+3 | 1-2시간 |

---

## 7. 문제 해결

### "No module named 'torch_geometric'"
- base 환경에서 실행 필요
- `conda activate base`

### "FileNotFoundError: gemnet-dT.json"
- config.yaml의 scale_file 경로 확인
- 절대 경로로 수정 필요

### 타임아웃
- 터미널에서 직접 실행 권장
- 또는 timeout 값 증가

---

## 8. 참고 자료

- [MatterGen GitHub](https://github.com/microsoft/mattergen)
- [MatterGen Paper (Nature 2025)](https://doi.org/10.1038/s41586-025-08628-5)
- 체크포인트: `c:\cement_final\mattergen\checkpoints\`
