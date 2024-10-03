from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Выставка котиков"
    DATABASE_URL: str = "sqlite+aiosqlite:///./fastapi.db"
    SECRET_KEY: str = "SECRET_KEY"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
