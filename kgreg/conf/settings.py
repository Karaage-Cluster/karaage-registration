# Django settings for kgreg project.
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgreg/templates",
)

ROOT_URLCONF = 'kgreg.conf.urls'

SITE_ID = 2

STATIC_ROOT = '/var/lib/karaage-registration/static'
STATIC_URL = '/kgreg_media/'

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.common.context_processors.registration',)

ADMIN_IGNORED = True

execfile("/etc/karaage/registration_settings.py")

