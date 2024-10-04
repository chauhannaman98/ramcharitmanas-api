FROM python:3.12

ENV POETRY_VIRTUALENVS_CREATE=false\
    POETRY_VIRTUALENVS_IN_PROJECT=false\
    POETRY_NO_INTERACTION=1

WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ./

RUN pip install --upgrade --no-cache-dir poetry

RUN poetry install

EXPOSE 8000

COPY . .
