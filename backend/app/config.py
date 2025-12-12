from pydantic import BaseSettings
from app.dependencies import get_db

class Settings(BaseSettings):
    DATABASE_URL: str = 'sqlite:///./app.db'
    SECRET_KEY: str = 'dev-secret-key-change-in-production'
    JWT_SECRET_KEY: str = 'dev-jwt-secret-key-change-in-production'

    class Config:
        env_file = '.env'