# tests/conftest.py
import pytest
from httpx import AsyncClient
from sqlalchemy import text
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.pool import StaticPool

from src.database.deps import get_session
from src.database.models import Base
from src.main import app

TEST_DB_URL = "sqlite+aiosqlite:///:memory:"

engine = create_async_engine(
    TEST_DB_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

TestingSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
)


@pytest.fixture()
async def session():
    # Создаём таблицы (для in-memory SQLite — безопасно делать каждый раз)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with TestingSessionLocal() as s:
        # Очищаем данные
        async with engine.begin() as conn:
            for table in reversed(Base.metadata.sorted_tables):
                await conn.execute(text(f"DELETE FROM {table.name}"))
        await s.commit()
        yield s


@pytest.fixture()
async def client(session):
    async def override_get_session():
        return session

    app.dependency_overrides[get_session] = override_get_session
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
    app.dependency_overrides.clear()
