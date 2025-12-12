from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./app.db"
    SECRET_KEY: str = "dev-secret-key-change-in-production"
    # All fields should have defaults
    class Config:
        env_file = ".env"