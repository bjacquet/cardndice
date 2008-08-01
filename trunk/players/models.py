from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(maxlength=80, blank='null', unique='true')
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Admin:
        pass
