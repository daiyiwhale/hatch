"""
Django settings for hatch project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secre!
SECRET_KEY = os.getenv('HATCH_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
# turning off debug means ALLOWED_HOSTS must be configured
DEBUG = True
# debugging python-social-auth
SOCIAL_AUTH_RAISE_EXCEPTIONS = True
ALLOWED_HOSTS = []

ADMINS = (
    ('daiyi', 'daiyitastic@gmail.com'),
)

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
#    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'incubator.apps.IncubatorConfig',
    # django-user-accounts (https://django-user-accounts.readthedocs.org)
    'account',
    # pinax-theme-bootstrap
    'pinax_theme_bootstrap',
    'bootstrapform',
    # python-social-auth
    'social.apps.django_app.default',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # django-user-accounts
    'account.middleware.LocaleMiddleware',
    'account.middleware.TimezoneMiddleware',
)

ROOT_URLCONF = 'hatch.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                # TEMPLATE_CONTEXT_PROCESSORS
                # django-user-accounts
                'account.context_processors.account',
                # pinax-theme-bootstrap
                'django.core.context_processors.request',
                'pinax_theme_bootstrap.context_processors.theme',
                # python-social-auth
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'hatch.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hatchdb',
        'USER': 'daiyi',
        'PASSWORD': os.getenv('HATCH_DB_PW'),
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

# URL prefix for static files, eg "convox.org/hatch'/static/'"
STATIC_URL = '/h/static/'

# absolute path to static file directory collected by python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL for media, eg "convox.org/hatch'/media'"
MEDIA_URL = '/h/media/'

# absolute path to user-uploaded files
MEDIA_ROOT = '/srv/media/hatch_media'

# python-social-auth settings
SOCIAL_AUTH_URL_NAMESPACE = 'social'
USER_MODEL = 'account.Account'
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('HATCH_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('HATCH_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')
SOCIAL_AUTH_LOGIN_REDIRECT_URL = os.getenv('HATCH_SOCIAL_AUTH_LOGIN_REDIRECT_URL')
SOCIAL_AUTH_LOGIN_URL = os.getenv('HATCH_SOCIAL_AUTH_LOGIN_URL')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/fitness.activity.read',
]

# django-user-accounts settings
ACCOUNT_SIGNUP_REDIRECT_URL = os.getenv('HATCH_ACCOUNT_REDIRECT_URL')
ACCOUNT_LOGIN_REDIRECT_URL = os.getenv('HATCH_ACCOUNT_REDIRECT_URL')
ACCOUNT_LOGOUT_REDIRECT_URL =  os.getenv('HATCH_ACCOUNT_REDIRECT_URL')
