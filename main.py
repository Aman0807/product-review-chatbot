import os
import json
from fastapi import FastAPI, Request 
import uvicorn
from src.routes.chat import chat


app = FastAPI()
app.include_router(chat)


@app.get("/")
async def root():
    return {"msg": "API is online"}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)