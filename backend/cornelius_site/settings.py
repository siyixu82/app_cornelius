"""
Django settings for cornelius_site project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'll@k$mk0@%b9)ms@nej_k9+tz!@8d14!jkjxp4!h+d_1$m%2e^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #our app
    'cornelius_app',

    #3rd party app
    'rest_framework',
    
    'django_nose',

    'django_extensions'

]

#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'


# Tell nose to measure coverage on the 'foo' and 'bar' apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=cornelius_app'
]

# REST_FRAMEWORK = {
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': (
#         'rest_framework.permissions.IsAuthenticated',
#     )
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'cornelius_site.urls'

#AUTH_USER_MODEL = 'cornelius_app.CorneliusUser'

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

WSGI_APPLICATION = 'cornelius_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#[START db_setup]
# if os.getenv('GAE_APPLICATION', None):
#     # Running on production App Engine, so connect to Google Cloud SQL using
#     # the unix socket at /cloudsql/<your-cloudsql-connection string>
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'HOST': '/cloudsql/cool-wharf-291516:us-central1:cornelius',
#             'USER': 'postgres',
#             'PASSWORD': 'cornelius1234',
#             'NAME': 'cornelius_db',
#         }
#     }
# else:
#     # Running locally so connect to either a local MySQL instance or connect 
#     # to Cloud SQL via the proxy.  To start the proxy via command line: 
#     #    $ cloud_sql_proxy -instances=[INSTANCE_CONNECTION_NAME]=tcp:3306 
#     # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#             'NAME': 'cornelius_db',
#             'USER': 'postgres',
#             'PASSWORD': 'cornelius1234',
#         }
#     }

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'Cornelius', 
        'USER': 'db_cornelius', 
        'PASSWORD': '1234',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}




# [END db_setup]

#


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'