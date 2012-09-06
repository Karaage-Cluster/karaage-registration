# Django settings for kgreg project.
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgreg/templates",
)

ROOT_URLCONF = 'kgreg.conf.urls'

SITE_ID = 2

STATIC_ROOT = '/var/lib/karaage-registration/static'
STATIC_URL = '/kgreg_media/'
ADMIN_MEDIA_PREFIX = '/kgreg_media/admin/'

LOGIN_REDIRECT_URL = '/users/profile/'
LOGIN_URL = '/users/accounts/login/'

ALLOW_REGISTRATIONS = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.context_processors.registration',)

AJAX_SELECT_BOOTSTRAP = False
AJAX_SELECT_INLINES = None

execfile("/etc/karaage/registration_settings.py")

