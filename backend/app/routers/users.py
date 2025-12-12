from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import get_db, get_current_user
from app.utils import get_jwt_token

router = APIRouter(
    prefix='/api/users',
    tags=['users'],
)

@router.get('/profile')
def read_user_me(current_user: User = Depends(get_current_user)):
    return current_user

@router.get('/')
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()