#!/bin/sh

# Apply database migrations
python src/manage.py migrate
python src/manage.py populate_tables

# Start Gunicorn server with optimized settings
NUM_WORKERS=$(($(nproc) * 2 + 1))
gunicorn --chdir src main.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers $NUM_WORKERS \
    --worker-class gevent \
    --worker-connections 2000 \
    --timeout 20 \
    --graceful-timeout 10 \
    --keep-alive 10 \
    --access-logfile access.log \
    --error-logfile error.log \
    --log-level info