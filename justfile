default: fmt fix

# Project management commands
project := "project"

start-project name:
    uv run django-admin startproject {{name}}

start-app name:
    cd ./{{project}} && uv run manage.py startapp {{name}}

shell:
    cd ./{{project}} && uv run manage.py shell -i ipython

serve:
    cd ./{{project}} && uv run manage.py runserver

make-migration app:
    cd ./{{project}} && uv run manage.py makemigrations {{app}}

make-migrations:
    cd ./{{project}} && uv run manage.py makemigrations

migrate:
    cd ./{{project}} && uv run manage.py migrate

create-superuser:
    cd ./{{project}} && uv run manage.py createsuperuser

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
