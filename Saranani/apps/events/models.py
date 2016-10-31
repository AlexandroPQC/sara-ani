from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    webpage = models.CharField(max_length=100)
    age_restriction = models.PositiveIntegerField(blank=True, null=True)
    category = models.ManyToManyField('Category')

class Category(models.Model):
    name = models.CharField(blank=True, max_length=100)
    description = models.CharField(blank=True, max_length=200)
    parent = models.ForeignKey('self', blank=True, null=True)
