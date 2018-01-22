from django.conf.urls import url
from . import views

app_name = 'portal'
urlpatterns = [
    url(r'^search/?$',
        views.search, name='search'),
    url(r'^search/results/?$',
        views.search, name='search results'),
    url(r'^downloadselected/?$',
        views.download_selected, name='downloadselected'),
    url(r'^downloadsinglefile/?$',
        views.download_single_file, name='downloadsinglefile'),
    url(r'^staging/?$',
        views.staging, name='staging'),
    url(r'^stageall/?$',
        views.stageall, name='stageall'),
]
