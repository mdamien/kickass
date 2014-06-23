from settings.base import *

from settings.secrets import *

INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

USE_X_FORWARDED_HOST = True

DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['utc.io',]
