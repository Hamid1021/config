"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
from decouple import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["hamid1021.pythonanywhere.com",'*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',


    'widget_tweaks',
    'extensions',
    'account.apps.AccountConfig',
    'sitemap.apps.SitemapConfig',
    'area.apps.OstanHaConfig',
    'image_optimizer',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        # 'NAME': 'mydatabase',
        # 'USER': 'mydatabaseuser',
        # 'PASSWORD': 'mypassword',
        # 'HOST': '127.0.0.1',
        # 'PORT': '5432',
    # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Hamid1021$default',
        'USER': 'Hamid1021',
        'PASSWORD': 'Dr.Darker1021',
        'HOST': 'Hamid1021.mysql.pythonanywhere-services.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'STRICT_ALL_TABLES',
        },
    }
}


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

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATICFILES_DIRS = [BASE_DIR / 'assets' ]

STATIC_URL = '/static/'
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / 'static/static/'
MEDIA_ROOT = BASE_DIR / 'static/media/'


REGISTRY_URL = "account:register"

AUTH_USER_MODEL = "account.User"

LOGIN_REDIRECT_URL = "/Login/"
LOGIN_URL = "/Login/"

SECRET_KEY = config('SECRET_KEY')



# EMAIL_BACKEND = 'config('SECRET_KEY')
# EMAIL_HOST = config('SECRET_KEY')
# EMAIL_HOST_USER = config('SECRET_KEY')
# EMAIL_HOST_PASSWORD = config('SECRET_KEY')
# DEFAULT_FROM_EMAIL = config('SECRET_KEY')
# EMAIL_PORT = 465
# # EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True


# EMAIL_BACKEND = config('SECRET_KEY')
# EMAIL_HOST = config('SECRET_KEY')
# EMAIL_HOST_USER = config('SECRET_KEY')
# EMAIL_HOST_PASSWORD = config('SECRET_KEY')
# EMAIL_PORT = 465
# DEFAULT_FROM_EMAIL = config('SECRET_KEY')
# # EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True


SEND_SMS_KEY = config('SEND_SMS_KEY')

SITE_ID = 1
OPTIMIZED_IMAGE_METHOD = 'pillow'