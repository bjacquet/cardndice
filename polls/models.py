import datetime

from django.db import models

# Create your models here.
class Poll(models.Model):
    question = models.CharField(maxlength=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question

    def was_published_today(self):
        return self.pub_date.date() == datetime.date.today()
    was_published_today.short_description = 'Published today?'

    class Admin:
        fields = (
            (None, {'fields': ('question',)}),
            ('Date information', {'fields': ('pub_date',), 
                                  'classes': 'collapse'}),
        )
        list_display = ('question', 'pub_date', 'was_published_today')
        list_filter = ['pub_date']
        search_fields = ['question']
        date_hierarchy = 'pub_date'

    class Meta:
        ordering = ["-pub_date"]

class Choices(models.Model):
    poll = models.ForeignKey(Poll, edit_inline=models.TABULAR, num_in_admin=3)
    choice = models.CharField(maxlength=200, core=True)
    votes = models.IntegerField(core=True)

    def __str__(self):
        return self.choice

    class Meta:
        ordering = ["id"]
