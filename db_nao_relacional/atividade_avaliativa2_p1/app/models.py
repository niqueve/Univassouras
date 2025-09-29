from datetime import datetime, timezone
from typing import List, Optional
from pydantic import BaseModel, Field, field_validator, ConfigDict
from bson import ObjectId

class PyObjectId (ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate (cls, v, _):
        if not ObjectId.is_valid (v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)
    
class MessageBase (BaseModel):
    username: str = Field(..., max_length=50)
    content: str = Field(..., max_lenght=1000)

    @field_validator ("content")
    def content_must_not_be_empty(cls, value):
        if not value.strip():
            raise ValueError("O conteúdo não pode ser vazio.")
        return value
    
class MessageIn(MessageBase):
    pass

class MessageOut(MessageBase):
    id: str = Field(alias="_id")
    room: str
    created_at: datetime

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
        json_enconders={ObjectId: str, datetime: lambda dt: dt.isoformat()}
    )

class MessageHistory(BaseModel):
    items: List[MessageOut]
    next_cursor: Optional[str] = None
    