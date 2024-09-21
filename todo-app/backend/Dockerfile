FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

COPY . /app
WORKDIR /app
RUN uv sync

ENV PORT=8081
CMD uv run fastapi run --port $PORT