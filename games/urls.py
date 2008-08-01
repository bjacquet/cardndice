from django.conf.urls.defaults import *

from cardndice.games.models import Game, GameForm

info_dict = {
    'queryset': Game.objects.all(),
}

new_game_form = {
    'form': GameForm({'name': 'game name',
                      'min_player': 1,
                      'max_player': 1}),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', info_dict),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    (r'^new/$', 'cardndice.games.views.create_game'),
)
