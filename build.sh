#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Clear any existing static files
python manage.py collectstatic --clear --no-input

# Collect static files
python manage.py collectstatic --no-input

# Run database migrations
python manage.py migrate 