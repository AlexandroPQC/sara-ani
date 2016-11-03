from django.conf.urls import url
from .views import EventListView

urlpatterns = [
    # url(r'^$', IndexView.as_view())
    url(r'^events/$', EventListView.as_view(), name='events'),
]
