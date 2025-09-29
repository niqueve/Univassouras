from typing import Optional
from motor.motor_asyncio import AsyncIOMotorClient
from .config import settings

_client: Optional[AsyncIOMotorClient] = None

def db () -> AsyncIOMotorClient:

    global _client
    if _client is None:
        if not settings.MONGO_URL:
            raise RuntimeError("Defina MONGO_URL no .env (string do MongoDB Atlas).")
        _client = AsyncIOMotorClient(settings.MONGO_URL)
    return _client[settings.MONGO_DB]

def close_db_connection ():
    global _client
    if _client:
        _client.close()
