from django.db import models
from geoposition.fields import GeopositionField

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    webpage = models.CharField(max_length=100)
    age_restriction = models.PositiveIntegerField(blank=True, null=True)
    category = models.ManyToManyField('Category')
    PlaceSchedule = models.ManyToManyField('PlaceSchedule', blank=True)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(blank=True, max_length=100)
    address = models.CharField(blank=True, max_length=300)
    description = models.CharField(blank=True, max_length=300)
    position = GeopositionField(blank=True, null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    event_start = models.DateTimeField(null=True, blank=True)
    event_end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.event_start)

class PlaceSchedule(models.Model):
    schedules = models.ManyToManyField('Schedule', blank=True)
    places = models.ForeignKey('Place', blank=True, null=True)

    # def __str__(self):
    #     return str(self.places)

class Galery(models.Model):
    name = models.CharField(blank=True, max_length=100)
    attachment = models.CharField(blank=True, max_length=200)
    parent = models.ForeignKey('Event', blank=True, null=True)

    def __str__(self):
        return self.name
