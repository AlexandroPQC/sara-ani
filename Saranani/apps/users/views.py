from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User
from apps.wishes.models import Wishlist

class UserDetailView(LoginRequiredMixin, DetailView):

    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['list_wishes'] =  Wishlist.objects.filter(user = context['object'])
        return context
