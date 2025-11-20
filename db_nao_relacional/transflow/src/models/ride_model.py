from pydantic import BaseModel, Field
from uuid import uuid4, UUID

class Passenger(BaseModel):
    name: str
    phone: str

class Driver(BaseModel):
    name: str
    score: float = Field(..., ge=0.0, le=5.0)

class Ride(BaseModel):
    ride_id: UUID = Field(default_factory=uuid4)
    passenger: Passenger
    driver: Driver
    origin: str
    destination: str
    fare: float = Field(..., gt=0.0)
    payment_method: str

    class Config:
        json_schema_extra = {
            "example": {
                "passenger": {"name": "Monique", "phone": "00000-0000"},
                "driver": {"name": "Carla", "score": 4.8},
                "origin": "Centro",
                "destination": "Inoã",
                "fare": 35.90,
                "payment_method": "Pix"
            }
        }
