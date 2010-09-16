from django.conf.urls.defaults import *
from django.conf import settings


urlpatterns = patterns('karaage.people.views.user',
    url(r'^profile/$', 'profile', name='kg_user_profile'),
    url(r'^profile/accounts/$', 'profile_accounts', name='kg_user_profile_accounts'),
    url(r'^profile/software/$', 'profile_software', name='kg_user_profile_software'),
    url(r'^profile/edit/$', 'edit_profile', name='kg_profile_edit'),
    url(r'^change_password/$', 'password_change', name='kg_user_change_password'),
    url(r'^change_password/done/$', 'password_change_done', name='kg_user_password_done'),

)

urlpatterns += patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}),
    url(r'^apply/$', 'django.views.generic.simple.direct_to_template', {'template': 'apply.html'}, name="apply"),
    url(r'^aup/$', 'django.views.generic.simple.direct_to_template', {'template': 'aup.html'}, name="aup"),
    url(r'^users/', include('karaage.people.urls.user')),
    url(r'^institutes/', include('karaage.institutes.urls.user')),
    url(r'^projects/', include('karaage.projects.urls.user')),
    url(r'^software/', include('karaage.software.urls.user')),
    url(r'^reports/', include('karaage.projectreports.urls.user')),
    url(r'^requests/user/', include('karaage.requests.urls.user')),
    url(r'^requests/projects/', include('karaage.requests.urls.projects')),
    url(r'^applications/', include('karaage.applications.urls.user')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^usage/', include('karaage.usage.urls')),
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
