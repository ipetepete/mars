#from django.conf.urls import url
from django.urls import include, path
from . import views


app_name = 'dal'
urlpatterns = [
    path('search/', views.search_by_json, name='search_by_json'),
    path('ti-pairs/', views.tele_inst_pairs, name='tele_inst_pairs'),
    path('schema/', views.schema_view, name='api_schema'),
    path('get-categories/', views.get_categories_for_query, name='get_filters_for_query'),
    path('object-lookup/', views.object_lookup, name="object_lookup"),
]
