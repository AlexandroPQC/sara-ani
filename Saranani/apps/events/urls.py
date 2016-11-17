from django.conf.urls import url
from .views import EventListView, EventView, EditEvent, DeleteEvent, EventUpdate, CreateEvent, EventDelete

urlpatterns = [
    url(r'^events/$', EventListView.as_view(), name='events'),
    url(r'^events/new$', CreateEvent.as_view(), name='new_event'),
    url(r'^events/(?P<pk>\d+)/$', EventUpdate.as_view(), name='edit_event'),
    url(r'^events/delete/(?P<pk>\d+)/$', EventDelete.as_view(), name='delete_event'),
]
