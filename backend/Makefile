install:
	uv sync

run:
	uv run uvicorn src.main:app --reload

makemigrations:
	uv run alembic revision --autogenerate -m "$(MESSAGE)"

migrate:
	uv run alembic upgrade head

rollback:
	uv run alembic downgrade -1

docker-up:
	docker compose up --build -d

docker-down:
	docker compose down

lint:
	uv run ruff check .

format:
	uv run ruff format .

precommit:
	uv run pre-commit run --all-files

prerun: install docker-up migrate
	@echo "Application is ready to run"

kafka:
	faststream run  src.consumer.app:app 