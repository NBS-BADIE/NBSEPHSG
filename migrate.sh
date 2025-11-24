#!/bin/bash
echo "Running Django migrations..."
python3 manage.py makemigrations
python3 manage.py migrate --noinput
echo "Migrations applied successfully!"
