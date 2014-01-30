from django.conf.urls import *
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
)

try:
    execfile("/etc/karaage/registration_override_urls.py")
except IOError:
    pass


urlpatterns += patterns('',
    url(r'^$', 'karaage.legacy.simple.direct_to_template', {'template': 'index.html'}, name='index'),
    url(r'^aup/$', 'karaage.legacy.simple.direct_to_template', {'template': 'aup.html'}, name="aup"),
    url(r'^persons/', include('karaage.people.urls.user')),
    url(r'^profile/', include('karaage.people.urls.profile')),
    url(r'^institutes/', include('karaage.institutes.urls.user')),
    url(r'^projects/', include('karaage.projects.urls.user')),
    url(r'^software/', include('karaage.software.urls.user')),
    url(r'^applications/', include('karaage.applications.urls.user')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^usage/', include('karaage.usage.urls.user')),
    url(r'^ajax_selects/', include('ajax_select.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc',),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^kgreg_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^karaage_graphs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GRAPH_ROOT}),
    )

execfile("/etc/karaage/registration_urls.py")
