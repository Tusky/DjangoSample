import os
import sys

######################################################################
#                           BASE CONFIG                              #
######################################################################
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.environ.get('SECRET_KEY', 'not-so-secret-if-you-can-read-this')

DEBUG = os.environ.get('DEBUG', False) == 'True'
TESTING = True if 'test' in sys.argv else False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
WSGI_APPLICATION = 'djangosample.wsgi.application'
ROOT_URLCONF = 'djangosample.urls'

######################################################################
#                        APPLICATION CONFIG                          #
######################################################################
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize'
)

THIRD_PARTY_APPS = (
    'bootstrap4',
)

PROJECT_APPS = (
    'user',
    'blog'
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

######################################################################
#                       TEMPLATE CONFIGURATION                       #
######################################################################

STATIC_URL = '/static/'
LOGIN_URL = '/login/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'blog.context_processors.get_categories'
            ],
        },
    },
]


######################################################################
#                       DATABASE CONFIGURATION                       #
######################################################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if TESTING:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}

######################################################################
#                       INTERNATIONALIZATION                         #
######################################################################

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

######################################################################
#                        THIRD PARTY PACKAGE                         #
######################################################################
