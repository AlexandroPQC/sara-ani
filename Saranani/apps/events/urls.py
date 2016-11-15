from django.conf.urls import url
from .views import EventListView, EventView

urlpatterns = [
    # url(r'^$', IndexView.as_view())
    url(r'^events/$', EventListView.as_view(), name='events'),
    url(r'^events/new$', EventView, name='new_event'),
]
