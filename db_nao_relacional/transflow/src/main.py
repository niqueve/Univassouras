from fastapi import FastAPI, Depends, HTTPException, status
from typing import List
from pymongo.collection import Collection
from redis import Redis
from contextlib import asynccontextmanager

from src.models.ride_model import Ride
from src.database.mongo_client import get_mongo_collection
from src.database.redis_client import get_redis_client
from src.producer import broker, publish_ride

@asynccontextmanager
async def lifespan(app: FastAPI):
    await broker.connect()
    print("Broker connected.")
    yield
    await broker.close()
    print("Broker closed.")

app = FastAPI(
    title="TransFlow API",
    description="API para gerenciamento de corridas",
    lifespan=lifespan
)

# -------------------------------------Endpoints (Mongo e RabbitMQ)

@app.post("/corridas", status_code=status.HTTP_202_ACCEPTED)
async def register_ride(ride: Ride):
    """
    Cadastrar uma nova corrida.
    A corrida será enviada para o processamento assíncrono (RabbitMQ).
    """
    try:
        await publish_ride(ride)

        return {
            "message": "Corrida recebida e sendo processada.",
            "ride_id": ride.ride_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao publicar corrida: {e}")
    
@app.get("/corridas", response_model=List[dict])
async def search_rides_for_payment(
    payment_method: str,
    db: Collection = Depends(get_mongo_collection)
):
    """Filtra corridas pela forma de pagamento"""
    rides = list(db.find({"payment_method": payment_method}, {"_id": 0}))
    if not rides:
        raise HTTPException(
            status_code=404,
            detail=f"Nenhuma corrida encontrada para a forma de pagamento: {payment_method}"
        )
    return rides

# ------------------------------endpoints (Redis)

@app.get("/saldo/{driver}")
async def check_balance(
    driver: str,
    redis_client: Redis = Depends(get_redis_client)
):
    """Consulta o saldo atual de um motorista no Redis."""
    balance = redis_client.get(f"saldo: {driver}")
    if balance is None:
        raise HTTPException(
            status_code=404,
            detail=f"Motorista '{driver}' não encontrado ou sem saldo."
        )
    return {"driver": driver, "balance": float(balance)}