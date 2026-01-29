"""
Configuration Management

설정 파일 관리
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional

from src import CONFIG_DIR


def load_config(config_name: str = "simulation") -> Dict[str, Any]:
    """
    설정 파일 로딩
    
    Parameters
    ----------
    config_name : str
        설정 파일 이름 (확장자 제외)
    
    Returns
    -------
    dict
        설정 데이터
    """
    config_path = CONFIG_DIR / f"{config_name}.yaml"
    
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    
    with open(config_path, 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    return config


def save_config(config: Dict[str, Any], config_name: str) -> None:
    """설정 파일 저장"""
    config_path = CONFIG_DIR / f"{config_name}.yaml"
    
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True)


# 기본 설정
DEFAULT_SIMULATION_CONFIG = {
    'baseline': {
        'material': 'C3S',
        'reference_energy': -7.39  # eV/atom
    },
    'optimization': {
        'fmax': 0.05,  # eV/Å
        'max_steps': 500
    },
    'hydration': {
        'n_water': 10,
        'box_expansion': 1.5
    },
    'md_simulation': {
        'screening': {
            'duration_ps': 10,
            'temperature_K': 300,
            'timestep_fs': 1
        },
        'deep_analysis': {
            'duration_ps': 100,
            'temperature_K': 300,
            'timestep_fs': 1
        }
    },
    'analysis': {
        'ca_leaching_threshold': 3.0,  # Å
        'si_coordination_cutoff': 2.5,  # Å
        'csh_pair_cutoff': 3.5  # Å
    }
}

DEFAULT_EVALUATION_CONFIG = {
    'scoring': {
        'weights': {
            'co2_reduction': 0.30,
            'ca_activity': 0.20,
            'si_stability': 0.25,
            'csh_formation': 0.25
        },
        'thresholds': {
            'min_total_score': 40,
            'min_co2_reduction': 50
        }
    },
    'baseline': {
        'material': 'C3S',
        'ca_leaching_rate': 0.10,
        'si_coordination': 4.0,
        'csh_pairs': 8
    },
    'grades': {
        'A': 70,
        'B': 50,
        'C': 30,
        'D': 0
    }
}


def create_default_configs() -> None:
    """기본 설정 파일 생성"""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    
    save_config(DEFAULT_SIMULATION_CONFIG, "simulation")
    save_config(DEFAULT_EVALUATION_CONFIG, "evaluation")
