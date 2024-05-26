from fastapi import APIRouter, WebSocket, Request, WebSocketDisconnect, BackgroundTasks, HTTPException
import uuid
from ..socket.connection import ConnectionManager

chat = APIRouter()
manager = ConnectionManager()


@chat.post("/token")
async def token_generator(name, request:Request):
    print(request)
    if name == "":
        raise HTTPException(status_code=400, detail={
            "loc": "name", "msg": "Enter a valid name"
        })
    
    token = str(uuid.uuid4())

    data = {"name": name, "token": token}
    
    return data


@chat.post("/refresh_token")
async def refresh_token(request:Request):
    print("refersh token")
    return {"msg":"token_refreshed"}


@chat.websocket("/chat")
async def websocket_endpoint(websocket:WebSocket):
    await manager.connect(websocket)
    print("hello")
    try:
        while True:
            data = await websocket.receive_text()
            print(data)
            await manager.send_personal_message(f"Response from bot", websocket)

    except WebSocketDisconnect:
        manager.disconnect(websocket)


