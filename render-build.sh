#!/usr/bin/env bash
# exit on error
set -o errexit

echo "===> INSTALLING DEPENDENCIES"
pip install -r requirements.txt

echo "===> RUNNING COLLECTSTATIC"
python manage.py collectstatic --noinput

echo "===> RUNNING MIGRATIONS"
# Optional: only run if you want to apply migrations during build
# python manage.py migrate

echo "===> BUILD FINISHED"
