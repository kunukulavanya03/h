from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import User

users_router = APIRouter()

@users_router.get("/")
def get_users():
    session = SessionLocal()
    users = session.query(User).all()
    return {"users": users, "total": len(users)}

@users_router.get("/{id}")
def get_user(id: int):
    session = SessionLocal()
    user = session.query(User).filter_by(id=id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}