from datetime import datetime

import httpx
from flask import Flask


app = Flask(__name__)


@app.route("/", methods=["GET"])
def status():
    return {"message": "OK"}


@app.route("/api/sync/resource", methods=["GET"])
def api_sync_resource():
    print("Received sync request")
    started_at = datetime.now()
    response: httpx.Response = httpx.get('http://localhost:8000/api/sleep/5', timeout=60)
    ended_at = datetime.now()
    return {
        "service": "sync",
        "started_at": started_at,
        "ended_at": ended_at,
        "diff": (ended_at - started_at).total_seconds(),
        "target_response": response.json()
    }
