from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'audit'
urlpatterns = [
    path('', views.AuditRecordList.as_view(), name='sourcefile_list'),
    path('source/', views.source, name='source'),
    path('submit/', views.submit, name='submit'),
    path('delete/<md5sum>/', views.delete, name='delete'),
    path('reaudit/<orig_md5sum>/<new_md5sum>/', views.re_audit, name='re_audit'),
    path('refresh/', views.refresh, name='refresh'),
    path('fstop/<md5sum>/<fstop>/<host>/',
         views.update_fstop, name='update_fstop'),
    path('update/', views.update, name='update'),
    path('query/<int:obsday>/<tele>/<inst>/<base>./',
        views.query, name='query'),
    path('missing/', views.not_ingested, name='not_ingested'),
    path('failed/', views.failed_ingest, name='failed_ingest'),
    path('stagedarc/',
        views.staged_archived_files, name='staged_archived_files'),
    path('stagednoarc/',
        views.staged_noarchived_files, name='staged_noarchived_files'),
    path('agg/', views.agg_domeday, name='agg'),
    #!path('notchecknight/', views.progress_count, name='progress_count'),
    #!path('progress_plot/', views.progress, name='progress'),
    path('demo1/', views.demo_multibarhorizontalchart,  name='demo1'),
    #!path('hbar/', views.hbar_svg,  name='hbar_svg'),
    path('dupes/', views.get_rejected_duplicates,  name='get_rejected_duplicates'),
    path('miss/', views.get_rejected_missing,  name='get_rejected_missing'),
    path('recent/', views.get_recent, name='get_recent'),
    path('recentcnt/', views.get_recent_count, name='get_recent_count'),
    path('hideall/', views.hide_all, name='hide_all'),
    path('unhidecnt/', views.get_unhide_count, name='get_unhide_count'),
    path('marsclearlog/', views.clear_mars_log, name='clear_mars_log'),
    path('marslogcnt/', views.get_mars_log_count, name='get_mars_log_count'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
