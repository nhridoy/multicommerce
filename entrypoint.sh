#!/bin/bash
# Save this file with LF format instead of CRLF.
# If you are using VS Code you can easily do that at the bottom right corner of the window

# Collect static files
# echo "Collecting static files...."
# python manage.py collectstatic --noinput || exit 1

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Creating Superuser"
python manage.py init

# Start server
echo "Starting server"

gunicorn --preload core.wsgi:application --bind 0.0.0.0:8000 --timeout 600 --workers 3