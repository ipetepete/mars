from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('index/', views.index, name='users'),
    path('',       views.index, name='users'),
]
