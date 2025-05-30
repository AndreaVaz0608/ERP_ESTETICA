from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-it0+nni@4oaa114@44xhnzs&9m!czzmhwe=g*7##&8+p44exyw')
DEBUG = os.getenv('DEBUG', '').lower() == 'true'

ALLOWED_HOSTS = [
    os.getenv("RENDER_EXTERNAL_HOSTNAME", "localhost"),
    ".onrender.com",
]

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'clientes',
    'import_export',
    'agendamentos',
    'servicos',
    'financeiro',
    'profissionais',
    'campanhas',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'erp_estetica.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'erp_estetica.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    "site_title": "ERP Estética",
    "site_header": "ERP Estética",
    "site_brand": "Clínica Silvia Vaz",
    "welcome_sign": "Bem-vinda, Silvia Vaz!",
    "copyright": "Silvia Vaz © 2024",
    "search_model": ["clientes.Cliente", "agendamentos.Agendamento", "servicos.Servico"],
    "site_logo": "logo_silvia_vaz.png",
    "site_icon": "logo_silvia_vaz.png",
    "icons": {
        "clientes.Cliente": "fas fa-user",
        "agendamentos.Agendamento": "fas fa-calendar-alt",
        "servicos.Servico": "fas fa-stethoscope",
    },
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["clientes", "agendamentos", "servicos"],
    "custom_links": {
        "servicos": [{
            "name": "Tabela de Preços",
            "url": "/admin/servicos/servico/",
            "icon": "fas fa-money-bill"
        }]
    },
    "custom_css": "custom_admin.css",
}
