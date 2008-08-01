from django.db import models
from django import newforms as forms

# Create your models here.

from cardndice.players.models import Player

class Game(models.Model):
    name = models.CharField(maxlength=80, blank='null', unique='true')
    min_player = models.IntegerField(default=1)
    max_player = models.IntegerField(default=1)
    ownerId = models.ForeignKey(Player)

    def save(self):
        if self.max_player < self.min_player:
            return False
        if self.min_player < 1:
            return False
        super(Game, self).save()

    def __str__(self):
        return self.name

    class Admin:
        pass

    class Meta:
        ordering = ["name"]

class GameForm(forms.ModelForm):
    class Meta:
        model = Game

# class GameForm(forms.Form):
#     name = forms.CharField(label='Name', help_text='80 characters maximun')
#     min_player = forms.IntegerField(label='Min players',
#                                     help_text='Less or equal than Max players')
#     max_player = forms.IntegerField(label='Max players',
#                                     help_text='Greater or equal than Min players')
    
