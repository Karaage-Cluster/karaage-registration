from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('karaage.people.views.user',
    url(r'^profile/$', 'profile', name='kg_user_profile'),
    url(r'^profile/accounts/$', 'profile_accounts', name='kg_user_profile_accounts'),
    url(r'^profile/software/$', 'profile_software', name='kg_user_profile_software'),
    url(r'^profile/edit/$', 'edit_profile', name='kg_profile_edit'),
    url(r'^login/$', 'login', name='login'),
    url(r'^change_password/$', 'password_change', name='kg_user_change_password'),
    url(r'^change_password/done/$', 'password_change_done', name='kg_user_password_done'),

)

urlpatterns += patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^apply/$', 'django.views.generic.simple.direct_to_template', {'template': 'apply.html'}, name="apply"),
    url(r'^aup/$', 'django.views.generic.simple.direct_to_template', {'template': 'aup.html'}, name="aup"),
    (r'^users/', include('karaage.people.urls.user')),
    (r'^institutes/', include('karaage.institutes.urls.user')),
    (r'^projects/', include('karaage.projects.urls.user')),
    (r'^software/', include('karaage.software.urls.user')),
    (r'^reports/', include('karaage.projectreports.urls.user')),
    (r'^requests/user/', include('karaage.requests.urls.user')),
    (r'^requests/projects/', include('karaage.requests.urls.projects')),
    (r'^pbs/', include('django_pbs.servers.urls')),
    url(r'^captcha/', include('captcha.urls')),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),

)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^kgreg_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )

execfile("/etc/karaage/registration_urls.py")
