"""
Django settings for marssite project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#!import warnings
#!
#!warnings.filterwarnings(
#!    'error', r"DateTimeField .* received a naive datetime",
#!    RuntimeWarning, r'django\.db\.models\.fields',
#!)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'siap',
    'schedule',
    'provisional',
    'water',
    'rest_framework',
    'rest_framework_swagger',
    'django_nvd3',
    'django_tables2',
    'audit',  # tada audit/status REST API
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
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

ROOT_URLCONF = 'marssite.urls'

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
                #'django.core.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'marssite.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'MST'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    #'/static/',
    '/var/www/static/',
    )
STATIC_ROOT = '/var/www/mars/static/'

SWAGGER_SETTINGS = {
#!    'exclude_namespaces': [],
#!    'api_version': '0.1',
#!    'api_path': '/',
    'enabled_methods': [
        'get',
        'post',
#!        'put',
#!        'patch',
#!        'delete'
    ],
#!    'api_key': '',
#!    'is_authenticated': False,
#!    'is_superuser': False,
#!    'permission_denied_handler': None,
#!    'resource_access_handler': None,
#!    'base_path':'localhost:8000/docs',
    'info': {
        'title': 'MARS prototype API documentation',
        'description': ('This is documentation for the '
                        'MARS (Metadata Archive Retrival Services) '
                        'prototype server.  '
                        # '<br />'
                        # 'You can find out more about Swagger at '
                        # '<a href="http://swagger.wordnik.com">'
                        # 'http://swagger.wordnik.com</a> '
                        # 'or on irc.freenode.net, #swagger. '
        ),
#        'license': 'Apache 2.0',
#        'licenseUrl': 'http://www.apache.org/licenses/LICENSE-2.0.html',
    },
#!    #! 'doc_expansion': 'none',
#!    'doc_expansion': 'full',
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    #!'DEFAULT_PERMISSION_CLASSES': [
    #!    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #!]
}

MEDIA_ROOT = '/var/mars/'

CONN_MAX_AGE = 7200 # keep DB connections for 2 hours

from .settings_local import *
