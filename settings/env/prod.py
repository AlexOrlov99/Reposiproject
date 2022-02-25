from settings.base import *  # noqa


DEBUG = False
WSGI_APPLICATION = None

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db_prod.sqlite3',
    }
}
ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]
INTERNAL_IPS = ['127.0.0.1']

INSTALLED_APPS += [
    'debug_toolbar'
]
MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]