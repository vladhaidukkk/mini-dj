default: fmt fix

# Project management commands
project_name := "project"

start-project name:
    uv run django-admin startproject {{name}}

start-app name:
    cd ./{{project_name}} && uv run manage.py startapp {{name}}

serve:
    cd ./{{project_name}} && uv run manage.py runserver

migrate:
    cd ./{{project_name}} && uv run manage.py migrate

create-superuser:
    cd ./{{project_name}} && uv run manage.py createsuperuser

# Code quality commands
fmt:
    uv run ruff format

lint:
    uv run ruff check

fix:
    uv run ruff check --fix

check-types:
    uv run pyright

# Testing commands
test:
    uv run pytest -v

cov:
    uv run pytest -v --cov

cov-xml:
    uv run pytest -v --cov --cov-report=xml
