from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'saranani',
        'USER': 'alexandro',
        'PASSWORD' : 'admin',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS =  [BASE_DIR.child('static')]

SOCIAL_AUTH_FACEBOOK_KEY = '125745471234326'
SOCIAL_AUTH_FACEBOOK_SECRET = '1baa17647010f976c88dc66097ea9ab9'
#
# SOCIAL_AUTH_TWITTER_KEY = 'K4xxxxxxxxxxxxxxxxxxxxxx'
# SOCIAL_AUTH_TWITTER_SECRET = '7hexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
