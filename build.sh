#!/usr/bin/env bash
# Instala dependências
pip install -r requirements.txt

# Coleta arquivos estáticos
python manage.py collectstatic --no-input

# Aplica migrações
python manage.py migrate
