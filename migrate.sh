#!/bin/bash
# Script pour appliquer les migrations sur Render
echo "Running Django migrations..."
python3 manage.py makemigrations
python3 manage.py migrate --noinput
echo "Migrations applied successfully!"
