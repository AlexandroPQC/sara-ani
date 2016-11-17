from django.shortcuts import render
from django.views.generic import DetailView

from .models import User
from apps.events.models import Event

class UserDetailView(DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        list_events =  Event.objects.filter(title = context['object'])
        tags = [ event.tag.all() for event in list_events ]
        context['ev_tags'] =  zip(list_events, tags )
        return context
