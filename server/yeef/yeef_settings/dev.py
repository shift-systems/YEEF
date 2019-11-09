from .base import *
ALLOWED_HOSTS = ['*']


MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')
MEDIA_URL = '/media/'

ENVIRONMENT = "development"
