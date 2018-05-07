#!/bin/sh

cd django/

source venv/bin/activate

git pull

rm -rf static

mkdir static

python manage.py collectstatic

sudo service nginx restart

killall -9 uwsgi

uwsgi django.ini

deactivate

cd ../