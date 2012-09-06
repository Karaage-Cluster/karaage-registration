from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin


urlpatterns = patterns('',
)

try:
    execfile("/etc/karaage/registration_override_urls.py")
except IOError:
    pass


urlpatterns += patterns('karaage.people.views.user',
    url(r'^profile/$', 'profile', name='kg_user_profile'),
    url(r'^profile/accounts/$', 'profile_accounts', name='kg_user_profile_accounts'),
    url(r'^profile/software/$', 'profile_software', name='kg_user_profile_software'),
    url(r'^profile/projects/$', 'profile_projects', name='kg_user_profile_projects'),
    url(r'^profile/edit/$', 'edit_profile', name='kg_profile_edit'),
    url(r'^change_password/$', 'password_change', name='kg_user_change_password'),
    url(r'^change_password/done/$', 'password_change_done', name='kg_user_password_done'),
    url(r'^accounts/password_reset/$', 'password_reset', name='password_reset'),

)

urlpatterns += patterns('',
    url(r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'index.html'}, name='index'),
    url(r'^aup/$', 'django.views.generic.simple.direct_to_template', {'template': 'aup.html'}, name="aup"),
    url(r'^samllogin/$', 'karaage.views.saml_login', name="kg_saml_login"),
    url(r'^users/', include('karaage.people.urls.user')),
    url(r'^institutes/', include('karaage.institutes.urls.user')),
    url(r'^projects/', include('karaage.projects.urls.user')),
    url(r'^software/', include('karaage.software.urls.user')),
    url(r'^reports/', include('karaage.projectreports.urls.user')),
    url(r'^requests/user/', include('karaage.requests.urls.user')),
    url(r'^requests/projects/', include('karaage.requests.urls.projects')),
    url(r'^applications/', include('karaage.applications.urls.user')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^usage/', include('karaage.usage.urls.user')),
    url(r'^ajax_selects/', include('ajax_select.urls')),
    url(r'^xmlrpc/$', 'django_xmlrpc.views.handle_xmlrpc',),
    url(r'^pbs/', include('django_pbs.servers.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
from karaage.applications.saml import SAMLInstituteForm
from karaage.people.models import Institute
login_extra = {
    'samlform': SAMLInstituteForm(),
    'saml_enabled': Institute.active.filter(saml_entityid__isnull=False).exclude(saml_entityid=""),
}

from karaage.people.forms import SetPasswordForm
urlpatterns += patterns('django.contrib.auth.views',
    url(r'^accounts/login/$', 'login', {'extra_context': login_extra }, name='login'),
    url(r'^accounts/logout/$', 'logout', name='logout'),
    url(r'^accounts/password_reset/done/$', 'password_reset_done', name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'password_reset_confirm', {'set_password_form': SetPasswordForm}, name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', 'password_reset_complete', name='password_reset_complete'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^kgreg_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        (r'^karaage_graphs/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.GRAPH_ROOT}),
    )

execfile("/etc/karaage/registration_urls.py")
