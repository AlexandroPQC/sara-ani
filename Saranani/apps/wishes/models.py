from django.db import models

class Wishlist(models.Model):
    user = models.ForeignKey('users.User', blank=True, null=True)
    event = models.ManyToManyField('events.Event', blank=True)
    date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.id)
