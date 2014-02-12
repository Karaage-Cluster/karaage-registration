from django.conf.urls import *
from django.conf import settings

urlpatterns = patterns('',
)

try:
    execfile("/etc/karaage/registration_override_urls.py")
except IOError:
    pass

import karaage.conf.urls
urlpatterns += karaage.conf.urls.urlpatterns

execfile("/etc/karaage/registration_urls.py")
