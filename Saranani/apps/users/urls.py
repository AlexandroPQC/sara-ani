from django.conf.urls import url
from .views import UserDetailView

urlpatterns = [
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user_detail'),
]
