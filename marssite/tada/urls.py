from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'dal'
urlpatterns = [
    url(r'^prefix/$', views.prefix, name='prefix'),
    url(r'^obs/$', views.obstype, name='obstype'),
    url(r'^proc/$', views.proctype, name='proctype'),
    url(r'^prod/$', views.prodtype, name='prodtype'),
    url(r'^rawreq/$', views.rawreq, name='rawreq'),
    url(r'^fnreq/$', views.filenamereq, name='filenamereq'),
    url(r'^ingestreq/$', views.ingestreq, name='ingestreq'),
    url(r'^ingestrec/$', views.ingestrec, name='ingestrec'),
    url(r'^supportreq/$', views.supportreq, name='supportreq'),
    url(r'^floatreq/$', views.floatreq, name='floatreq'),
    url(r'^hdrfuncs/$', views.hdrfuncs, name='hdrfuncs'),
    url(r'^errcodes/$', views.errcodes, name='errcodes'),
]
