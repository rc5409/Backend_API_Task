from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str
    model: str = "gpt-3.5-turbo"

    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
