#!/bin/sh

set -e

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Iniciando aplicação..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

echo "► Aplicando migrations..."
poetry run python manage.py migrate --noinput

echo "► Coletando arquivos estáticos..."
poetry run python manage.py collectstatic --noinput --clear

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Iniciando Gunicorn..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

exec poetry run gunicorn core.wsgi:application \
    --bind 0.0.0.0:8003 \
    --workers 1 \
    --threads 2 \
    --access-logfile - \
    --error-logfile - \
    --timeout 120
