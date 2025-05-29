#!/usr/bin/env bash
# build.sh

echo "Apply migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput
