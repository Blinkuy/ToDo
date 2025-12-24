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

compose-up:
	docker compose up --build -d

compose-down:
	docker compose down

migrate:
	alembic revision --autogenerate -m "auto migration"
	alembic upgrade head

downgrade:
	alembic downgrade -1

upgrade:
	alembic upgrade head

setup: install compose-up upgrade run
	@echo "setup completed"