from fastapi import APIRouter, HTTPException
from app.models.schemas import Message
from app.services.producer import publish_message

router = APIRouter()

@router.post("/enviar")
async def enviar(message: Message):
    try:
        await publish_message(message.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"status": "enviado", "mensagem": message.dict()}