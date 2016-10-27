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

SOCIAL_AUTH_FACEBOOK_KEY = '1096064430509335'
SOCIAL_AUTH_FACEBOOK_SECRET = 'f2fa3b6d5b6ee204861181fe38aad548'
#
# SOCIAL_AUTH_TWITTER_KEY = 'K4xxxxxxxxxxxxxxxxxxxxxx'
# SOCIAL_AUTH_TWITTER_SECRET = '7hexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
