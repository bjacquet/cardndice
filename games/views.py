from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django import newforms as forms

# Create your views here.

from cardndice.games.models import GameForm

def create_game(request):
    new_data = {}
    if request.POST:
        new_data = GameForm(request.POST)
        if new_data.is_valid():
            new_game = new_data.save() 
            return HttpResponseRedirect("/games/%i" % new_game.id)
    else:
        errors = new_nata = {}
    form = GameForm()
    return render_to_response('games/new_game.html', {'form': form})
