FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

ARG BASIC_AUTH_USERNAME_ARG
ARG BASIC_AUTH_PASSWORD_ARG

ENV BASIC_AUTH_USERNAME=$BASIC_AUTH_USERNAME_ARG
ENV BASIC_AUTH_PASSWORD=$BASIC_AUTH_PASSWORD_ARG

COPY ./pyproject.toml /usr/pyproject.toml

WORKDIR /usr

RUN uv sync

COPY ./app /usr/app
COPY ./models /usr/models

CMD ["uv", "run", "app/main.py"]
