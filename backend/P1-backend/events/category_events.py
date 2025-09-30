
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(frozen=True)
class CategoryCreated:
    category_id: str
    name: str
    description: str
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class CategoryUpdate:
    category_id: str
    name: str
    description: str
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class CategoryActivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class CategoryDeactivated:
    category_id: str
    timestamp: datetime = field(default_factory=datetime.utcnow)