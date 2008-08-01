from django.conf.urls.defaults import *

from cardndice.players.models import Player

info_dict = {
    'queryset': Player.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
)
