from django.conf.urls import url
from .views import EventListView, EventView, EditEvent, DeleteEvent

urlpatterns = [
    # url(r'^$', IndexView.as_view())
    url(r'^events/$', EventListView.as_view(), name='events'),
    url(r'^events/new$', EventView, name='new_event'),
    url(r'^events/(?P<id_event>\d+)/$', EditEvent, name='edit_event'),
    url(r'^events/delete/(?P<id_event>\d+)/$', DeleteEvent, name='delete_event'),
]
