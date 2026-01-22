from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # --- frontend ---
    FRONTEND_URL: str = Field(
        default="http://localhost:3000",
        description="Frontend url for CORS"
    )

    # --- database ---
    DATABASE_URL: str = Field(
        ...,
        env="DATABASE_URL",
        description="Postgres database url from env"
    )

    DATABASE_URL_SYNC: str = Field(
        ...,
        env="DATABASE_URL_SYNC",
        description="Postgres url for alembic"
    )

    DATABASE_URL_TEST: str = Field(
        ...,
        env="DATABASE_URL_TEST",
        description="Postgres url for pytest"
    )

    # --- broker ---
    KAFKA_URL: str = Field(
        default="localhost:9092",
        description="Kafka broker url"
    )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
