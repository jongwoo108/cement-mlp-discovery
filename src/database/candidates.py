"""
Candidate Materials Database

후보 재료 데이터베이스 관리
"""

import json
from dataclasses import dataclass, asdict
from typing import Dict, List, Optional
from pathlib import Path


@dataclass
class Candidate:
    """후보 재료 데이터 클래스"""
    name: str
    composition: Dict[str, int]  # {'Ca': 6, 'Si': 4, 'Al': 2, 'O': 16}
    co2_reduction: float  # CO2 저감률 (%)
    source: str  # 출처 (예: "철강 슬래그")
    tier: int = 1  # 우선순위 (1-5)
    volume: float = 1000.0  # 목표 셀 부피 (Å³)
    notes: str = ""
    
    def to_dict(self) -> dict:
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Candidate':
        return cls(**data)
    
    @property
    def formula(self) -> str:
        """화학식 반환"""
        parts = []
        for elem, count in sorted(self.composition.items()):
            if count == 1:
                parts.append(elem)
            else:
                parts.append(f"{elem}{count}")
        return ''.join(parts)
    
    @property
    def total_atoms(self) -> int:
        """총 원자 수"""
        return sum(self.composition.values())


class CandidateDatabase:
    """후보 재료 데이터베이스"""
    
    def __init__(self, db_path: Optional[Path] = None):
        """
        Parameters
        ----------
        db_path : Path, optional
            데이터베이스 파일 경로
        """
        self.candidates: Dict[str, Candidate] = {}
        self.db_path = db_path
        
        if db_path and db_path.exists():
            self.load(db_path)
    
    def add(self, candidate: Candidate) -> None:
        """후보 추가"""
        self.candidates[candidate.name] = candidate
    
    def remove(self, name: str) -> None:
        """후보 제거"""
        if name in self.candidates:
            del self.candidates[name]
    
    def get(self, name: str) -> Optional[Candidate]:
        """후보 조회"""
        return self.candidates.get(name)
    
    def list_all(self) -> List[Candidate]:
        """전체 목록"""
        return list(self.candidates.values())
    
    def list_by_tier(self, tier: int) -> List[Candidate]:
        """티어별 목록"""
        return [c for c in self.candidates.values() if c.tier == tier]
    
    def save(self, path: Optional[Path] = None) -> None:
        """데이터베이스 저장"""
        save_path = path or self.db_path
        if save_path is None:
            raise ValueError("No path specified for saving")
        
        data = {name: c.to_dict() for name, c in self.candidates.items()}
        
        with open(save_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load(self, path: Path) -> None:
        """데이터베이스 로딩"""
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        self.candidates = {
            name: Candidate.from_dict(cdata) 
            for name, cdata in data.items()
        }
        self.db_path = path
    
    def __len__(self) -> int:
        return len(self.candidates)
    
    def __iter__(self):
        return iter(self.candidates.values())


# 기본 후보 재료 정의
DEFAULT_CANDIDATES = [
    # Tier 1: 철강 부산물
    Candidate(
        name="BFS",
        composition={'Ca': 6, 'Si': 4, 'Al': 2, 'Mg': 1, 'O': 16},
        co2_reduction=85,
        source="고로 슬래그",
        tier=1,
        volume=1200
    ),
    Candidate(
        name="SteelSlag",
        composition={'Ca': 8, 'Si': 3, 'Fe': 2, 'Mg': 1, 'O': 16},
        co2_reduction=75,
        source="제강 슬래그",
        tier=1,
        volume=1200
    ),
    Candidate(
        name="EAFSlag",
        composition={'Ca': 5, 'Si': 4, 'Fe': 3, 'Al': 1, 'O': 16},
        co2_reduction=75,
        source="전기로 슬래그",
        tier=1,
        volume=1200
    ),
    
    # Tier 2: 석탄 화력 부산물
    Candidate(
        name="FlyAshF",
        composition={'Si': 6, 'Al': 3, 'Fe': 1, 'Ca': 1, 'O': 16},
        co2_reduction=85,
        source="Fly Ash Class F",
        tier=2,
        volume=1000
    ),
    Candidate(
        name="FlyAshC",
        composition={'Ca': 4, 'Si': 5, 'Al': 2, 'O': 16},
        co2_reduction=85,
        source="Fly Ash Class C",
        tier=2,
        volume=1000
    ),
    Candidate(
        name="BottomAsh",
        composition={'Si': 5, 'Al': 3, 'Fe': 2, 'Ca': 1, 'O': 16},
        co2_reduction=75,
        source="바닥재",
        tier=2,
        volume=1100
    ),
    
    # Tier 3: 금속 제련 부산물
    Candidate(
        name="CopperSlag",
        composition={'Fe': 5, 'Si': 4, 'Ca': 2, 'Al': 1, 'O': 16},
        co2_reduction=75,
        source="구리 슬래그",
        tier=3,
        volume=1200
    ),
    Candidate(
        name="RedMud",
        composition={'Fe': 4, 'Al': 4, 'Si': 2, 'Ti': 1, 'O': 16},
        co2_reduction=65,
        source="적니 (알루미늄 정련)",
        tier=3,
        volume=1100
    ),
    Candidate(
        name="NickelSlag",
        composition={'Fe': 5, 'Si': 4, 'Mg': 2, 'O': 16},
        co2_reduction=75,
        source="니켈 슬래그",
        tier=3,
        volume=1200
    ),
    
    # Tier 4: 실리카 풍부 폐기물
    Candidate(
        name="SilicaFume",
        composition={'Si': 8, 'O': 16},
        co2_reduction=88,
        source="실리카 흄",
        tier=4,
        volume=800
    ),
    Candidate(
        name="RiceHuskAsh",
        composition={'Si': 8, 'K': 1, 'O': 16},
        co2_reduction=92,
        source="왕겨재",
        tier=4,
        volume=800
    ),
    Candidate(
        name="POFA",
        composition={'Si': 6, 'K': 2, 'Ca': 1, 'O': 16},
        co2_reduction=88,
        source="팜유 연료재",
        tier=4,
        volume=900
    ),
    
    # Tier 5: 기타
    Candidate(
        name="WasteGlass",
        composition={'Si': 6, 'Na': 2, 'Ca': 2, 'O': 16},
        co2_reduction=75,
        source="폐유리",
        tier=5,
        volume=1000
    ),
    Candidate(
        name="CeramicWaste",
        composition={'Si': 6, 'Al': 4, 'O': 16},
        co2_reduction=65,
        source="폐도자기",
        tier=5,
        volume=900
    ),
    Candidate(
        name="Metakaolin",
        composition={'Si': 4, 'Al': 4, 'O': 14},
        co2_reduction=75,
        source="메타카올린",
        tier=5,
        volume=800
    ),
    Candidate(
        name="CoalGangue",
        composition={'Si': 5, 'Al': 4, 'Fe': 1, 'O': 16},
        co2_reduction=70,
        source="석탄 맥석",
        tier=5,
        volume=1000
    ),
]


def create_default_database(save_path: Path) -> CandidateDatabase:
    """기본 후보 데이터베이스 생성"""
    db = CandidateDatabase()
    
    for candidate in DEFAULT_CANDIDATES:
        db.add(candidate)
    
    db.save(save_path)
    return db
