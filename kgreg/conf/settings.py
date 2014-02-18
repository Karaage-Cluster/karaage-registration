# Django settings for kgreg project.
from karaage.conf.settings import *

ROOT_URLCONF = 'kgreg.conf.urls'

SITE_ID = 2

STATIC_ROOT = '/var/lib/karaage-registration/static'
STATIC_URL = '/kgreg_media/'

ADMIN_IGNORED = True

execfile("/etc/karaage/registration_settings.py")

