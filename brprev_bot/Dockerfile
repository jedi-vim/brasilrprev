FROM python:3.6.9

WORKDIR /app

RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

RUN PATH=$PATH:$HOME/.poetry/bin

COPY poetry.lock /app

COPY pyproject.toml /app

RUN $HOME/.poetry/bin/poetry config virtualenvs.create false && $HOME/.poetry/bin/poetry install --no-dev --no-interaction --no-ansi

COPY . /app/

EXPOSE 4000
