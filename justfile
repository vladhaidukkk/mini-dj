default: fmt fix

# Code quality commands
fmt:
    uv run ruff format

lint:
    uv run ruff check

fix:
    uv run ruff check --fix

types:
    uv run pyright
