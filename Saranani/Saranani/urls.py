"""Saranani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.views import logout, login

urlpatterns = [
    url(r'^', include('apps.home.urls')),
    url(r'^', include('apps.events.urls')),
    url(r'^', include('apps.users.urls', namespace='users')),
    url(r'^admin/', admin.site.urls),
    #   PYTHON SOCIAL AUTH
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^users/logout/$', logout, {'next_page': '/'}, name="user-logout"),
    url(r'^login/$', login, name='login'),

]
