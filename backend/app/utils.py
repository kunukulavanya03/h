from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.dependencies import get_db
from app.config import settings
from jose import jwt
from passlib.context import CryptContext
from app.models import User

pwd_context = CryptContext(schemes=['bcrypt'], default='bcrypt')

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def authenticate_user(username: str, password: str):
    user = get_db().query(User).filter(User.username == username).first()
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict):
    access_token = jwt.encode(data, settings.SECRET_KEY, algorithm='HS256')
    return access_token

def get_jwt_token(token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user = get_db().query(User).filter(User.username == payload['sub']).first()
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token has expired')
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail='Could not validate token')
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail='Invalid token')