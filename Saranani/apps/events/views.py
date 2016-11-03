from django.shortcuts import render

from django.views.generic import ListView

from .models import Event

class EventListView(ListView):
    model = Event
    context_object_name = 'events'
