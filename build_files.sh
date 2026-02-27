#!/bin/bash

echo "===> STARTING CUSTOM BUILD SCRIPT"

# Ensure pip is up to date
python3 -m pip install --upgrade pip

# Install requirements
echo "===> Installing requirements..."
python3 -m pip install -r requirements.txt

# Run collectstatic
echo "===> Running collectstatic..."
python3 manage.py collectstatic --noinput --clear

echo "===> BUILD SCRIPT FINISHED"
