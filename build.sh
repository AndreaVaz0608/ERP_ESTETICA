#!/usr/bin/env bash
# build.sh

echo "Apply migrations"
python manage.py migrate --noinput

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Create superuser if not exists"
python manage.py shell << END
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superusuário {username} criado.")
    else:
        print(f"Superusuário {username} já existe.")
else:
    print("Variáveis de ambiente para superusuário não definidas.")
END
