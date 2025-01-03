from contextlib import asynccontextmanager
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient  # Initialize MongoDB client
from dotenv import load_dotenv


# Load environment variables
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create database connection
    try:
        # Initialize AsyncIOMotorClient
        app.mongodb_client = AsyncIOMotorClient('mongodb://mongodb:27017')
        app.mongodb = app.mongodb_client.portfolio_db
        # Verify connection
        await app.mongodb.command('ping')
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e

    yield

    # Shutdown: Close database connection
    app.mongodb_client.close()
    print("MongoDB connection closed")

# Create FastAPI app with lifespan handler
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return {"message": "Portfolio System API"}


@app.get("/test-db")
async def test_db():
    try:
        # Simple database operation to test connection
        collections = await app.mongodb.list_collection_names()
        return {"status": "success", "collections": list(collections)}
    except Exception as e:
        return {"status": "error", "message": str(e)}
