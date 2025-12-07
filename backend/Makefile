install:
	uv sync

run:
	uv run uvicorn todoapp.main:app --reload

lint:
	uv run ruff check .

format:
	uv run ruff format . --fix

precommit:
	uv run pre-commit run --all-files
