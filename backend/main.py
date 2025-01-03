# backend/main.py
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient('mongodb://mongodb:27017')
    app.mongodb = app.mongodb_client.portfolio_db

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()