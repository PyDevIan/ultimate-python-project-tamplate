# Dynamic config from environment variables
from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    app_name: str = "Copier Scaffold App"
    env: str = "development"
    openai_api_key: str | None = None

    class Config:
        env_file = Path(__file__).parent / ".env"


settings = Settings()
