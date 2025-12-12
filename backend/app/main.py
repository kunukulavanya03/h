from fastapi import FastAPI
from dotenv import load_dotenv
from app.routes import auth_router, users_router, items_router
from app.database import SessionLocal, engine
from app.models import Base

load_dotenv()

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router, prefix="/api/auth")
app.include_router(users_router, prefix="/api/users")
app.include_router(items_router, prefix="/api/items")

@app.get("/api/health")
def health_check():
    return {"status": "OK", "message": "Backend is up and running"}