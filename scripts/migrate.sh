#!/bin/sh

makemigrations.sh

echo 'Executing migrate...'
python manage.py migrate --noinput
