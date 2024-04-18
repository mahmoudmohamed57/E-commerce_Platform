from .common import *
import dj_database_url
import os

DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

DATABASES =  {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')
