from datetime import datetime

import httpx
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def status():
    return {"message": "OK"}


@app.get("/api/async/resource")
async def api_async_resource():
    print("Received async request")
    started_at = datetime.now()
    async with httpx.AsyncClient() as client:
        response: httpx.Response = await client.get('http://localhost:8000/api/sleep/5', timeout=60)
    ended_at = datetime.now()
    return {
        "service": "async",
        "started_at": started_at,
        "ended_at": ended_at,
        "diff": ended_at - started_at,
        "target_response": response.json()
    }


@app.get("/api/async/block/resource")
async def api_async_resource():
    print("Received async block request")
    started_at = datetime.now()
    response: httpx.Response = httpx.get('http://localhost:8000/api/sleep/5', timeout=60)
    ended_at = datetime.now()
    return {
        "service": "async",
        "started_at": started_at,
        "ended_at": ended_at,
        "diff": ended_at - started_at,
        "target_response": response.json()
    }
