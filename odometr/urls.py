from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<car_id>[0-9]+)/$', views.car, name='car'),
    url(r'^(?P<car_id>[0-9]+)/checkpoints/$', views.checkpoints, name='checkpoints'),
]
