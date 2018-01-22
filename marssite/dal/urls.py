from django.conf.urls import url
from . import views


app_name = 'dal'
urlpatterns = [
    # eg: /dal/
    #! url(r'^$', views.index, name='index'),

    url(r'^search/$',
        views.search_by_json, name='search_by_json'),
    url(r'ti-pairs/$', views.tele_inst_pairs, name='tele_inst_pairs'),
    url(r'schema/$', views.schema_view, name='api_schema'),
    url(r'^get-categories/?$', views.get_categories_for_query, name='get_filters_for_query'),
    url(r'^object-lookup/$', views.object_lookup, name="object_lookup"),
]
