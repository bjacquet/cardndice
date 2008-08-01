from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'cardndice.views.defaults.index'),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^polls/', include('cardndice.polls.urls')),
    (r'^games/', include('cardndice.games.urls')),
    (r'^players/', include('cardndice.players.urls')),
    (r'^matches/', include('cardndice.matches.urls')),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
)

handler404 = 'cardndice.views.defaults.page_not_found'
handler500 = 'cardndice.views.defaults.server_error'
