import os
import sys

from env_var import STRIPE_API, SECRET_KEY_VAR, EMAIL, EASY_POST_KEY, DATABASE

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = SECRET_KEY_VAR


# stripe
API_KEY = STRIPE_API['key']
API_KEY2 = STRIPE_API['pwd']


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_URL = '/auth_login/'
AUTH_LOGIN = 'auth_login'

SERVER = 'http://localhost:8000'

DEFAULT_FROM_EMAIL = EMAIL['default_message']
EMAIL_HOST = EMAIL['host']
EMAIL_HOST_USER = EMAIL['host_user']
EMAIL_HOST_PASSWORD = EMAIL['password']
EMAIL_PORT = EMAIL['port']
EMAIL_USE_TLS = EMAIL['tls']

SESSION_COOKIE_AGE = 14000

# test key shipping for ups ect
EASY_POST = EASY_POST_KEY

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'home.views.get_home_variables',
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'product',
    'account',
    'subscription',
    'cart',
    'order',
    'shipping'

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'borroh.urls'

WSGI_APPLICATION = 'borroh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE['name'],
        'HOST': DATABASE['host'],
        'PORT': DATABASE['port'],
        'USER': DATABASE['user'],
        'PASSWORD': DATABASE['password']
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static','root')
MEDIA_URL = '/media/'   
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static','media')

TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR),'static','templates'),
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR),'static','static'),
)

