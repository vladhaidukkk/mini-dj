default: fmt fix

# Project management commands
serve:
    uv run ./project/manage.py runserver

# Code quality commands
fmt:
    uv run ruff format

lint:
    uv run ruff check

fix:
    uv run ruff check --fix

type:
    uv run pyright

# Testing commands
test:
    uv run pytest -v

cov:
    uv run pytest -v --cov

cov-xml:
    uv run pytest -v --cov --cov-report=xml
