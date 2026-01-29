"""
AI-Driven Cement Alternative Discovery Pipeline

산업 폐기물 기반 저탄소 시멘트 대체재 발견을 위한 
자동화 시뮬레이션 파이프라인
"""

__version__ = "1.0.0"
__author__ = "AI Co-Scientist"

from pathlib import Path

# 프로젝트 루트 경로
PROJECT_ROOT = Path(__file__).parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
RESULTS_DIR = PROJECT_ROOT / "results"
STRUCTURES_DIR = PROJECT_ROOT / "structures"
TRAJECTORIES_DIR = PROJECT_ROOT / "trajectories"
FIGURES_DIR = PROJECT_ROOT / "figures"
