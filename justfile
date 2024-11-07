default: fmt fix

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
