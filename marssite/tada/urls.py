from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'dal'
urlpatterns = [
    path('prefix/', views.prefix, name='prefix'),
    path('obs/', views.obstype, name='obstype'),
    path('proc/', views.proctype, name='proctype'),
    path('prod/', views.prodtype, name='prodtype'),
    path('rawreq/', views.rawreq, name='rawreq'),
    path('fnreq/', views.filenamereq, name='filenamereq'),
    path('ingestreq/', views.ingestreq, name='ingestreq'),
    path('ingestrec/', views.ingestrec, name='ingestrec'),
    path('supportreq/', views.supportreq, name='supportreq'),
    path('floatreq/', views.floatreq, name='floatreq'),
    path('hdrfuncs/', views.hdrfuncs, name='hdrfuncs'),
    path('errcodes/', views.errcodes, name='errcodes'),
]
