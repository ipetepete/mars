from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'schedule'
urlpatterns = [
    # eg: /schedule/
    # The whole schedule
    path('', views.list_full, name='list_full'),
    path('list/', views.SlotList.as_view(), name='list'),
    #!path('$', views.SlotList.as_view(), name='list'),
    path('about', TemplateView.as_view(template_name="schedule/about.html")),
    path('empty', views.list_empty, name='list_empty'),
    path('today', views.SlotTodayList.as_view(), name='today_list'),
    path('calendar',
         login_required(TemplateView.as_view(
             template_name="schedule/fullcalendar.html"))),
    # By Month;  Example: /2012/aug/
    path('<int:year>/<month>/',views.SlotMonthList.as_view(),name="month_list"),

    # eg: /schedule/propid/ct13m/2014-12-25/  => smarts
    #  kp4m/2014-01-01 =>  2013B-0142 
    path('dbpropid/<telescope>/<instrument>/<date>/<hdrpid>/',
        views.dbpropid, name='dbpropid'),
    path('propid/<telescope>/<instrument>/<date>/',
        views.getpropid, name='getpropid'),
    path('setpropid/<telescope>/<instrument>/<date>/<propid>/',
        views.setpropid, name='setpropid'),
    path('batchaddpropids/', views.batch_add_propids, name='batch_add_propids'),
    path('slot/<tele>/<date>/', views.SlotGet.as_view(), name='getslot'),
    path('slot_detail/<int:pk>/',views.SlotDetail.as_view(), name='slot-detail'),
    path('api/occurrences/', views.occurrences, name="occurances"),
    path('upload/',  views.upload_file, name='upload_file'),
    path('delete_all_schedule_i_really_mean_it/',
         views.delete_schedule, name='delete_schedule'),
    re_path('update/(?P<day>\d{4}-\d{2}-\d{2})/',
            views.update_date, name='update_date'),
    re_path('update/(?P<semester>\d{4}[AB])/',    
            views.update_semester, name='update_semester'),
]

