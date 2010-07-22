# Django settings for kgreg project.
from karaage.conf.settings import *

TEMPLATE_DIRS += (
    "/usr/share/kgreg/templates",
)

ROOT_URLCONF = 'kgreg.conf.urls'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/kgreg_media/'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = '/usr/share/kgreg/media'

execfile("/etc/karaage/registration_settings.py")
