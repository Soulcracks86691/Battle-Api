from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import random
import os

app = FastAPI(title="Bot API", description="API for Telegram Bot", version="1.0")

# CORS allow (sabko access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ MAIN ENDPOINTS ============

@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Bot API is working!",
        "time": datetime.now().isoformat()
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "uptime": "running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/v1/health")
def api_v1_health():
    return {
        "status": "healthy",
        "message": "API is working perfectly",
        "version": "v1",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/status")
def status():
    return {
        "status": "ok",
        "message": "Bot is connected",
        "api": "active"
    }

@app.get("/api/v1/status")
def api_status():
    return {
        "status": "ok",
        "uptime": "running",
        "bot": "connected"
    }

# ============ BOT KE LIYE EXTRA ============

@app.get("/api/v1/info")
def info():
    return {
        "name": "Bot API",
        "version": "1.0",
        "status": "active"
    }

@app.get("/ping")
def ping():
    return {"pong": True, "status": "alive"}

# ============ CATCH-ALL (kuch bhi ho 404 na aaye) ============
@app.get("/{path:path}")
def catch_all(path: str):
    return {
        "message": f"Endpoint /{path} not found",
        "suggestion": "Try /health or /api/v1/health",
        "status": "error"
    }, 404
