"""
Visualization Functions

시각화 함수
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
from pathlib import Path


def plot_screening_comparison(
    results: Dict[str, Dict],
    save_path: Optional[Path] = None,
    figsize: tuple = (14, 10)
) -> plt.Figure:
    """
    스크리닝 결과 비교 차트
    
    4개 패널: CO2 저감, Ca 활성, Si 안정성, 종합 점수
    """
    materials = list(results.keys())
    n_materials = len(materials)
    
    # 데이터 추출
    co2_reductions = [results[m]['co2_reduction'] for m in materials]
    ca_rates = [results[m]['analysis']['ca_leaching']['rate_per_ps'] for m in materials]
    si_cns = [results[m]['analysis']['si_coordination']['mean_cn'] for m in materials]
    total_scores = [results[m]['score']['total_score'] for m in materials]
    
    # 색상
    colors = plt.cm.Set2(np.linspace(0, 1, n_materials))
    
    fig, axes = plt.subplots(2, 2, figsize=figsize)
    
    # (a) CO2 저감률
    ax = axes[0, 0]
    bars = ax.bar(materials, co2_reductions, color=colors)
    ax.set_ylabel('CO₂ Reduction (%)')
    ax.set_title('(a) CO₂ Reduction Potential')
    ax.set_ylim(0, 100)
    for bar, val in zip(bars, co2_reductions):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val:.0f}%', ha='center', va='bottom', fontsize=9)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # (b) Ca 용출 속도
    ax = axes[0, 1]
    bars = ax.bar(materials, ca_rates, color=colors)
    ax.set_ylabel('Ca Leaching Rate (Ca/ps)')
    ax.set_title('(b) Ca Leaching Activity')
    for bar, val in zip(bars, ca_rates):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.2f}', ha='center', va='bottom', fontsize=9)
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # (c) Si 배위수
    ax = axes[1, 0]
    bars = ax.bar(materials, si_cns, color=colors)
    ax.axhline(y=4.0, color='r', linestyle='--', label='Ideal SiO₄ (CN=4)')
    ax.set_ylabel('Si Coordination Number')
    ax.set_title('(c) Si Coordination Stability')
    ax.set_ylim(0, 6)
    ax.legend()
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # (d) 종합 점수
    ax = axes[1, 1]
    bars = ax.bar(materials, total_scores, color=colors)
    ax.axhline(y=70, color='g', linestyle='--', alpha=0.5, label='Grade A')
    ax.axhline(y=50, color='orange', linestyle='--', alpha=0.5, label='Grade B')
    ax.set_ylabel('Screening Score')
    ax.set_title('(d) Overall Screening Score')
    ax.set_ylim(0, 100)
    ax.legend()
    for bar, val in zip(bars, total_scores):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{val:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    plt.setp(ax.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig


def plot_evolution(
    results: Dict[str, Dict],
    save_path: Optional[Path] = None,
    figsize: tuple = (15, 4)
) -> plt.Figure:
    """
    시간 변화 그래프
    
    3개 패널: Ca 용출, Si CN, C-S-H 쌍
    """
    fig, axes = plt.subplots(1, 3, figsize=figsize)
    
    materials = list(results.keys())
    colors = plt.cm.tab10(np.linspace(0, 1, len(materials)))
    
    for mat, color in zip(materials, colors):
        analysis = results[mat]['analysis']
        
        # Ca 용출
        ca_counts = analysis['ca_leaching'].get('leached_counts', [])
        if ca_counts:
            time_ps = np.linspace(0, 10, len(ca_counts))
            axes[0].plot(time_ps, ca_counts, label=mat, color=color)
        
        # Si CN
        cn_evol = analysis['si_coordination'].get('cn_evolution', [])
        if cn_evol:
            time_ps = np.linspace(0, 10, len(cn_evol))
            axes[1].plot(time_ps, cn_evol, label=mat, color=color)
        
        # C-S-H 쌍
        pairs_evol = analysis['csh_formation'].get('pairs_evolution', [])
        if pairs_evol:
            time_ps = np.linspace(0, 10, len(pairs_evol))
            axes[2].plot(time_ps, pairs_evol, label=mat, color=color)
    
    axes[0].set_xlabel('Time (ps)')
    axes[0].set_ylabel('Leached Ca')
    axes[0].set_title('Ca Leaching Evolution')
    axes[0].legend(loc='best', fontsize=8)
    
    axes[1].set_xlabel('Time (ps)')
    axes[1].set_ylabel('Si CN')
    axes[1].set_title('Si CN Evolution')
    axes[1].axhline(y=4.0, color='gray', linestyle='--', alpha=0.5)
    axes[1].legend(loc='best', fontsize=8)
    
    axes[2].set_xlabel('Time (ps)')
    axes[2].set_ylabel('Ca-Si Pairs (<3.5Å)')
    axes[2].set_title('C-S-H Precursor Formation')
    axes[2].legend(loc='best', fontsize=8)
    
    plt.tight_layout()
    
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    
    return fig
