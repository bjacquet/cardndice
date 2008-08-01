from django.db import models

from cardndice.games.models import Game
from cardndice.players.models import Player

# Create your models here.
class Match(models.Model):
    game = models.ForeignKey(Game, core=True)

    def __str__(self):
        return self.game.name

    class Meta:
        ordering = ["id"]

    class Admin:
        pass

class Result (models.Model):
    match = models.ForeignKey(Match)
    player = models.ForeignKey(Player, edit_inline=models.TABULAR, 
                               num_in_admin=3)
    result = models.IntegerField(default=0, core=True)

    def __str__(self):
        return self.player.name

    class Meta:
        ordering = ["-result"]

    class Admin:
        pass
