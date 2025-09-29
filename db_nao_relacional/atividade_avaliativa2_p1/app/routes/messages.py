from datetime import datetime, timezone
from fastapi import APIRouter, Query, HTTPException, Body
from bson import ObjectId
from bson.errors import InvalidId

from ..database import db
from ..models import MessageIn, MessageOut, MessageHistory

router = APIRouter()

@router.get("/{room}/messages", response_model=MessageHistory)
async def get_messages(
    room: str,
    limit: int = Query(20, ge=1, le=100),
    before_id: str | None = Query(None),
):
    query = {"room": room}
    if before_id:
        try:
            query["_id"] = {"$lt": ObjectId(before_id)}
        except InvalidId:
            raise HTTPException(status_code=400, detail="O 'before_id' fornecido não é um ObjectId válido.")
        
    cursor = db()["messages"].find(query).sort("_id", -1).limit(limit)
    docs = [MessageOut(**d) async for d in cursor]
    docs.reverse()

    next_cursor = docs[0].id if docs else None

    return {"items": docs, "next_cursor": next_cursor}

@router.post("/{room}/messages", response_model=MessageOut, status_code=201)
async def post_message(room: str, message: MessageIn):
    doc = {
        "room": room,
        "username": message.username,
        "content": message.content,
        "creat_at": datetime.now(timezone.utc),
    }
    res = await db()["messages"].insert_one(doc)

    doc["_id"] = res.inserted_id

    return MessageOut(**doc)