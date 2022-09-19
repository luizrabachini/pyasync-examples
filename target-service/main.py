from asyncio import sleep
from datetime import datetime

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def status():
    return {"message": "OK"}


@app.get("/api/sleep/{sleep_time}")
async def api_sleep(sleep_time: int):
    started_at: int = datetime.now()
    await sleep(sleep_time)
    ended_at = int = datetime.now()
    return {
        "started_at": started_at,
        "ended_at": ended_at,
        "diff": ended_at - started_at
    }
