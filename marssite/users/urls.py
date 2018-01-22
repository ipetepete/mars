from django.conf.urls import url
from . import views

app_name = 'users'
urlpatterns = [
    url(r'^admin/$', views.admin, name='admin'),
    url(r'^index/$', views.index, name='users'),
    url(r'^$',
        views.index, name='users'),
]
