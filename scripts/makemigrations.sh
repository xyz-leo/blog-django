#!/bin/sh

echo 'Executing makemigrations...'
python manage.py makemigrations --noinput
