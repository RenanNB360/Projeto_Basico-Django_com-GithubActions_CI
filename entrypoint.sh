#!/bin/sh

echo "Aplicando migrações..."
task migrate

echo "Coletando arquivos estáticos..."
python manage.py collectstatic --no-input

echo "Iniciando o servidor..."
exec uvicorn backend.asgi:application --host 0.0.0.0 --port 8080 --workers 4