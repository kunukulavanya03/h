from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.dependencies import get_db
from app.routers import auth, data, users
from app.utils import get_jwt_token, authenticate_user
from app.config import settings
from app.schemas import User

app = FastAPI(
    title='FastAPI Application',
    description='A simple FastAPI application.',
    version='1.0.0',
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(data.router)

@app.get('/api/health')
def read_health():
    return {'status': 'ok'}