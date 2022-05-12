#!/bin/bash

python manage.py migrate
echo from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('root', 's.sazono23@gmail.com', 'saw654366') | python manage.py shell
python manage.py runserver 0.0.0.0:8000 --insecure