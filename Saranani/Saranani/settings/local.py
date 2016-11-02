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

SOCIAL_AUTH_FACEBOOK_KEY = ''
SOCIAL_AUTH_FACEBOOK_SECRET = ''
#
# SOCIAL_AUTH_TWITTER_KEY = 'K4xxxxxxxxxxxxxxxxxxxxxx'
# SOCIAL_AUTH_TWITTER_SECRET = '7hexxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'


GEOPOSITION_GOOGLE_MAPS_API_KEY = ''

GEOPOSITION_MAP_OPTIONS = {
    'minZoom': 14,
    'backgroundColor': 'grey',
    'fullscreenControl': 'true',
    'center' : {'lat' : -16.503816418559943, 'lng' : -68.12961772084236,},
    'panControl': 'true',
    'componentRestrictions': {'country': 'bo'}
}

GEOPOSITION_MARKER_OPTIONS = {
    'position' : {'lat' : -16.503816418559943, 'lng' : -68.12961772084236,},
}
