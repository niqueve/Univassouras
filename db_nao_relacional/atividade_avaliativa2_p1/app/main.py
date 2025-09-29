
from datetime import datetime, timezone
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError

from .ws_manager import manager
from .database import db
from .routes import messages
from .models import MessageOut

# -------------------------------------------------------------------------setup
app = FastAPI(title="Chat Refatorado")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------------------rotas
app.include_router(messages.router, prefix="/rooms", tags=["Messages"])
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", include_in_schema=False)
async def index():
    return FileResponse("app/static/index.html")


# ---------------------------------------------------------------- WebSocket Endpoint 
@app.websocket("/ws/{room}")
async def ws_room(ws: WebSocket, room: str):
    await manager.connect(room, ws)
    try:
        cursor = db()["messages"].find({"room": room}).sort("_id", -1).limit(20)
        items = [MessageOut(**d) async for d in cursor]
        items.reverse()
        await ws.send_json({
            "type": "history",
            "items": [msg.model_dump(mode="json") for msg in items]
        })

        while True:
            payload = await ws.receive_json()
            
            username = str(payload.get("username", "anon"))[:50]
            content = str(payload.get("content", "")).strip()
            
            if not content:
                continue 

            doc = {
                "room": room,
                "username": username,
                "content": content,
                "created_at": datetime.now(timezone.utc),
            }
            res = await db()["messages"].insert_one(doc)
            doc["_id"] = res.inserted_id

            message_out = MessageOut(**doc)
            await manager.broadcast(
                room, {"type": "message", "item": message_out.model_dump(mode="json")}
            )
            
    except WebSocketDisconnect:
        manager.disconnect(room, ws)