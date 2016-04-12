from django.conf.urls import url

from . import views


urlpatterns = [
    # eg: /siap/
    url(r'^$', views.index, name='index'),

    url(r'^tada/$', views.tada, name='tada'),

    # eg: /siap/prop/2011A-0525
    url(r'^prop/(?P<propid>.+)/$', views.filenames, name='filenames'),
    url(r'^propfiles/(?P<propid>.+)/$', views.FileListView.as_view(), name='pfiles'),

    # eg: /siap/detail/cp243352.fits.gz
    url(r'^detail/(?P<image_id>.+)/$', views.detail, name='detail'),

    # eg: /siap/get/nsa/local_filename.fits
    url(r'^get/nsa/(?P<fname>.+)/$', views.getnsa, name='getnsa'),
    # eg: /siap/get/acq/archive_filename.fits
    url(r'^get/acq/(?P<fname>.+)/$', views.getacq, name='getacq'),

    url(r'^fquery/$', views.query_by_json, name='query_by_json'),
    url(r'^squery$', views.query_by_str, name='query_by_str'),
    url(r'^query$', views.query, name='query'),
]
