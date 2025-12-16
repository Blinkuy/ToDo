FROM python:3.11-slim

WORKDIR /app

# зависимости
COPY pyproject.toml uv.lock /app/

RUN pip install --upgrade pip \
    && pip install uv \
    && uv sync

# ВАЖНО: копируем alembic
COPY alembic.ini /app/alembic.ini
COPY alembic /app/alembic
COPY tests /app/tests

# код приложения
COPY src /app/src

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--reload"]
