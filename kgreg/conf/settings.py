# Django settings for kgreg project.
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgreg/templates",
)

ROOT_URLCONF = 'kgreg.conf.urls'

SITE_ID = 2

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/kgreg_media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/share/kgreg/media'

GRAPH_URL = '/kgreg_graphs/'

LOGIN_REDIRECT_URL = '/kgreg/profile/'

ALLOW_REGISTRATIONS = False

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

TEMPLATE_CONTEXT_PROCESSORS += ('karaage.context_processors.registration',)

execfile("/etc/karaage/registration_settings.py")

