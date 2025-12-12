from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import User
from app.utils import get_password_hash, verify_password

auth_router = APIRouter()

@auth_router.post("/login")
def login(email: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"token": "your-jwt-token", "user": user}

@auth_router.post("/register")
def register(name: str, email: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter_by(email=email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already exists")
    new_user = User(name=name, email=email, password=get_password_hash(password))
    session.add(new_user)
    session.commit()
    return {"token": "your-jwt-token", "user": new_user}