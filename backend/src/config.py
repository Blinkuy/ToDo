from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- frontend ---
    FRONTEND_URL: str = "http://localhost:3000"

    # --- database ---
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    DATABASE_URL_SYNC: str = Field(..., env="DATABASE_URL_SYNC")
    DATABASE_URL_TEST: str = Field(..., env="DATABASE_URL_TEST")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
