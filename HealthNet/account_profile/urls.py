from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^edit-patient/$', views.edit_p, name='edit-patient'),
    url(r'^edit-doctor/$', views.edit_d, name='edit-doctor')
]
