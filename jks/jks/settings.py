"""
Django settings for jks project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    'rest_framework',
    'corsheaders',
    'django_cleanup.apps.CleanupConfig',
    'debug_toolbar',

    'jks_site',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'jks.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        # Deploy dirs
        # 'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'jks.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        # For deploy
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Almaty'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'
STATIC_URL = '/static_back/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_back')

# MEDIA_URL = '/media/'
MEDIA_URL = '/media_back/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_back')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ]
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]

# Email settings
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

BOT_TOKEN = os.environ.get('BOT_TOKEN')

LANGUAGES = (
    ('ru', 'Russian'),
    ('en', 'English'),
    ('kk', 'Kazakhstan'),
)

MODELTRANSLATION_LANGUAGES = ('ru', 'en', 'kk')
MODELTRANSLATION_TRANSLATION_REGISTRY = 'jks.translation'

JAZZMIN_SETTINGS = {
    "site_brand": "JKS admin",
    "welcome_sign": "Welcome to the JKS admin",
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"model": "jks_site.Manager"},
        {"model": "jks_site.Form"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        # {"app": "food_packaging_admin"},
    ],
    "show_sidebar": True,
    "show_ui_builder": True,
    "related_modal_active": True,
    "order_with_respect_to": ["jks_site.MainPage",
                              "jks_site.VideoProductionPage",
                              "jks_site.AboutUsPage",
                              "jks_site.ProjectsPage",
                              "jks_site.InfluencersPage",
                              "jks_site.Influencer",
                              "jks_site.DubStudioPage",
                              "jks_site.Studio",
                              "jks_site.AnimationStudioPage",
                              "jks_site.SeriesFilmsPage",
                              "jks_site.GameDevPage"
                              ],
    "changeform_format_overrides": {"jks_site.MainPage": "vertical_tabs",
                                    "jks_site.VideoProductionPage": "vertical_tabs",
                                    "jks_site.Partner": "vertical_tabs",
                                    "jks_site.Footer": "vertical_tabs",
                                    "jks_site.AboutUsPage": "vertical_tabs",
                                    "jks_site.ProjectsPage": "vertical_tabs",
                                    "jks_site.InfluencersPage": "vertical_tabs",
                                    "jks_site.Influencer": "vertical_tabs",
                                    "jks_site.DubStudioPage": "vertical_tabs",
                                    "jks_site.Studio": "vertical_tabs",
                                    "jks_site.AnimationStudioPage": "vertical_tabs",
                                    "jks_site.SeriesFilmsPage": "vertical_tabs",
                                    "jks_site.GameDevPage": "vertical_tabs"},
}

REDIS_HOST = 'redis'
REDIS_PORT = '6379'
CELERY_BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CORS_ALLOW_ALL_ORIGINS: True

# Deploy settings
# USE_X_FORWARDED_HOST = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# CSRF_TRUSTED_ORIGINS = ['https://*.foodpackaging.kz', 'https://*.foodpackaging.kz/api/v1/create']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file_format': {
            'format': '{levelname} - {asctime} - {module} - {filename} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'file_format',
            'filename': 'log_django.log',
        },
    },
    'loggers': {
        'main': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
