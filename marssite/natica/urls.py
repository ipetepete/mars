from django.urls import include, path
from . import views

app_name = 'natica'
urlpatterns = [
    path('store/', views.store, name='store'),       # ESSENTIAL
    path('search/', views.search, name='search'),      # ESSENTIAL
    #path('retrieve/', views.retrieve, name='retrieve'),# ESSENTIAL

    path('', views.index, name='index'),
    #path('ingest/', views.ingest, name='ingest'),
    path('search2/', views.search2, name='search2'),
    path('prot/', views.prot, name='prot'),
    path('ana/', views.analysis, name='analysis'),
    path('query/', views.query, name='query'),

    path('prefix/', views.prefix, name='prefix'),
    path('obs/', views.obstype, name='obstype'),
    path('proc/', views.proctype, name='proctype'),
    path('prod/', views.prodtype, name='prodtype'),
    
]


