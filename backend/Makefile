install:
	uv sync

run:
	uv run uvicorn src.main:app --reload

lint:
	uv run ruff check .

format:
	uv run ruff format . 

precommit:
	uv run pre-commit run --all-files

dc:
	docker compose up --build -d

dcd:
	docker compose down

dmigrate:
	docker compose exec backend uv run alembic revision --autogenerate -m "init"

dmigrateup:
	docker compose exec backend uv run alembic upgrade head

dtest:
	docker compose exec backend uv run pytest