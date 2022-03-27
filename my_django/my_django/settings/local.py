from distutils.debug import DEBUG
from .base import *

DEBUG=True
ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['MY_DJANGO_DATABASE_NAME'],
        'USER': os.environ['MY_DJANGO_DATABASE_USER'],
        'PASSWORD': os.environ['MY_DJANGO_DATABASE_PASS'],
        'HOST': os.environ['MY_DJANGO_DATABASE_HOST'],
        'PORT': os.environ['MY_DJANGO_DATABASE_PORT'],
    }
}