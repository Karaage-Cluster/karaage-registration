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
    url(r'^persons/', include('karaage.people.urls.persons')),
    url(r'^profile/', include('karaage.people.urls.profile')),
    url(r'^groups/', include('karaage.people.urls.groups')),
    url(r'^institutes/', include('karaage.institutes.urls')),
    url(r'^projects/', include('karaage.projects.urls')),
    url(r'^machines/', include('karaage.machines.urls')),
    url(r'^software/', include('karaage.software.urls')),
    url(r'^applications/', include('karaage.applications.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^usage/', include('karaage.usage.urls')),
    url(r'^ajax_selects/', include('ajax_select.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc',),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^karaage_graphs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GRAPH_ROOT}),
    )

execfile("/etc/karaage/registration_urls.py")
