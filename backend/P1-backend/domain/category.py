
import uuid
from dataclasses import dataclass, field, asdict
from typing import Optional, List, Any

from events.category_events import (
    CategoryCreated,
    CategoryUpdate,
    CategoryActivated,
    CategoryDeactivated
)

MAX_NAME = 255

@dataclass
class Category:
    name: str
    description: str = ""
    is_active: bool = True
    id: Optional[str] = field(default=None)
    events: List[Any] = field(default_factory=list, init=False, repr=False)

    #-------------------------------------------construtor inteligente
    def __post_init__(self):
        if not self.id:
            self.id = str(uuid.uuid4())
        self.name = self._validate_name(self.name)
        self.description = self.description or ""
        self.is_active = bool(self.is_active)

        self.events.append(
            CategoryCreated(
                category_id=self.id,
                name=self.name,
                description=self.description
            )
        )

    @staticmethod
    def _validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise ValueError("name deve ser uma string")
        n = name.strip()
        if not n:
            raise ValueError("name é obrigatório")
        if len(n) > MAX_NAME:
            raise ValueError(f"name deve ter no máximo {MAX_NAME} caracteres")
        return n

    #--------------------------comportamentos do domínio
    def update(self, *, name: Optional[str]=None, description: Optional[str]=None) -> None:
        if name is not None:
            self.name = self._validate_name(name)
        if description is not None:
            self.description = description

        self.events.append(
            CategoryUpdate(
                category_id=self.id,
                name=self.name,
                description=self.description
            )
        )

    def activate(self) -> None:
        self.is_active = True
        
        self.events.append(
            CategoryActivated (
                category_id=self.id)
        )

    def deactivate(self) -> None:
        self.is_active = False

        self.events.append(
            CategoryDeactivated(
                category_id=self.id
            )
        )

    #-----------------------------------------------------serialização
    def to_dict(self) -> dict:
        data = asdict(self)
        data.pop('events', None)
        data['class_name'] = self.__class__.__name__
        return data
    
    @classmethod
    def from_dict(cls, data: dict) -> "Category":
        data.pop('class_name', None)
        return cls(**data)

    #---------------------------------------------logs e depuração
    def __str__(self):
        return f"{self.name} | {self.description} | ({self.is_active})"
    
    def __repr__(self):
        return f"<Category {self.name} ({self.id})>"