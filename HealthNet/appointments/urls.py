from django.conf.urls import url

from . import views
from .views import CreateAppointment, DeleteAppointment

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<appointment_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<appointment_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<pk>[0-9]+)/delete/$', DeleteAppointment.as_view(), name='delete'),
    url(r'^create/$', CreateAppointment.as_view(), name='create'),
]
