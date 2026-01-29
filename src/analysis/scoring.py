"""
Screening Score Calculation

스크리닝 점수 계산 함수
"""

from typing import Dict, Optional


# 기본 가중치
DEFAULT_WEIGHTS = {
    'co2_reduction': 0.30,
    'ca_activity': 0.20,
    'si_stability': 0.25,
    'csh_formation': 0.25
}

# C3S 기준값 (baseline)
C3S_BASELINE = {
    'co2_reduction': 0.0,  # %
    'ca_leaching_rate': 0.10,  # Ca/ps
    'si_coordination': 4.0,
    'csh_pairs': 8
}


def calculate_screening_score(
    co2_reduction: float,
    ca_leaching_rate: float,
    si_coordination: float,
    csh_pairs: int,
    weights: Optional[Dict[str, float]] = None,
    baseline: Optional[Dict[str, float]] = None
) -> Dict:
    """
    스크리닝 종합 점수 계산
    
    Parameters
    ----------
    co2_reduction : float
        CO2 저감률 (%)
    ca_leaching_rate : float
        Ca 용출 속도 (Ca/ps)
    si_coordination : float
        평균 Si 배위수
    csh_pairs : int
        C-S-H 쌍 수
    weights : dict, optional
        항목별 가중치
    baseline : dict, optional
        기준값 (C3S)
    
    Returns
    -------
    dict
        각 항목별 점수 및 총점
    """
    if weights is None:
        weights = DEFAULT_WEIGHTS
    
    if baseline is None:
        baseline = C3S_BASELINE
    
    # 1. CO2 저감 점수 (25점 만점)
    # 높을수록 좋음
    score_co2 = min(25, (co2_reduction / 100) * 25)
    
    # 2. Ca 활성 점수 (25점 만점)
    # 적절한 용출 속도가 좋음 (너무 낮거나 높으면 감점)
    baseline_rate = baseline.get('ca_leaching_rate', 0.10)
    if baseline_rate > 0:
        rate_ratio = ca_leaching_rate / baseline_rate
        if rate_ratio < 0.1:
            # 너무 낮음 (반응성 부족)
            score_ca = 5.0
        elif rate_ratio > 3.0:
            # 너무 높음 (구조 불안정)
            score_ca = 10.0
        else:
            # 적절한 범위
            score_ca = min(25, 10 + rate_ratio * 10)
    else:
        score_ca = 5.0 if ca_leaching_rate == 0 else 15.0
    
    # 3. Si 안정성 점수 (25점 만점)
    # CN=4.0에 가까울수록 좋음
    ideal_cn = baseline.get('si_coordination', 4.0)
    cn_deviation = abs(si_coordination - ideal_cn)
    score_si = max(0, 25 * (1 - cn_deviation / ideal_cn))
    
    # 4. C-S-H 형성 점수 (25점 만점)
    # 높을수록 좋음
    baseline_csh = baseline.get('csh_pairs', 8)
    if baseline_csh > 0:
        score_csh = min(25, (csh_pairs / baseline_csh) * 25)
    else:
        score_csh = min(25, csh_pairs * 3)
    
    # 가중 합산은 하지 않고 단순 합산 (100점 만점)
    total_score = score_co2 + score_ca + score_si + score_csh
    
    return {
        'co2_score': round(score_co2, 1),
        'ca_score': round(score_ca, 1),
        'si_score': round(score_si, 1),
        'csh_score': round(score_csh, 1),
        'total_score': round(total_score, 1),
        'grade': _get_grade(total_score)
    }


def _get_grade(score: float) -> str:
    """점수에 따른 등급 반환"""
    if score >= 70:
        return 'A'
    elif score >= 50:
        return 'B'
    elif score >= 30:
        return 'C'
    else:
        return 'D'


def format_score_table(scores: Dict[str, Dict]) -> str:
    """점수 테이블 포맷팅"""
    header = f"{'Material':<15} {'CO2↓':>8} {'Ca활성':>8} {'Si안정':>8} {'C-S-H':>8} {'Total':>8} {'Grade':>6}"
    separator = "-" * 70
    
    lines = [header, separator]
    
    for name, score in scores.items():
        line = (f"{name:<15} "
                f"{score['co2_score']:>8.1f} "
                f"{score['ca_score']:>8.1f} "
                f"{score['si_score']:>8.1f} "
                f"{score['csh_score']:>8.1f} "
                f"{score['total_score']:>8.1f} "
                f"{score['grade']:>6}")
        lines.append(line)
    
    lines.append(separator)
    
    return '\n'.join(lines)
