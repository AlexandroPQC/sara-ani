from django.shortcuts import render
from django.views.generic import TemplateView

from apps.events.models import Event

class IndexView(TemplateView):
    template_name = 'home/index.html'
