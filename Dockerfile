FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . /app/
COPY entrypoint.sh /app/entrypoint.sh

RUN pip install poetry

RUN poetry install --with dev --no-interaction --no-ansi

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000
CMD ["uvicorn", "backend.asgi:application", "--host", "0.0.0.0", "--port", "8080", "--workers", "4"]
