from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    #url(r'^$', views.SubmittalList.as_view(), name='submittal_list'),
    url(r'^$', views.AuditRecordList.as_view(), name='sourcefile_list'),
    #url(r'^(?P<pk>[0-9]+)/$', views.SubmittalDetail.as_view(), name='submittal_detail'),
    #url(r'^add$', views.add_submit, name='submittal_add'),
    url(r'^source/$', views.source, name='source'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^delete/(?P<md5sum>.+)/$', views.delete, name='delete'),
    url(r'^reaudit/(?P<orig_md5sum>.+)/(?P<new_md5sum>.+)/$',
        views.re_audit, name='re_audit'),
    url(r'^refresh/$', views.refresh, name='refresh'),
    url(r'^fstop/(?P<md5sum>.+)/(?P<fstop>[:\w]+)/(?P<host>.+)/$',
        views.update_fstop, name='update_fstop'),
    #url(r'^fstop/(?P<md5sum>\w+)/(?P<fstop>[:\w]+)/)$',
    #    views.update_fstop, name='update_fstop'),
    #url(r'^fstop/(?P<md5sum>\w+)/(?P<fstop>[:\w]+)/(?P<host>.+)$',
    #    views.update_fstop, name='update_fstop'),
    url(r'^update/$', views.update, name='update'),
    url(r'^missing/$', views.not_ingested, name='not_ingested'),
    url(r'^failed/$', views.failed_ingest, name='failed_ingest'),
    url(r'^stagedarc/$',
        views.staged_archived_files, name='staged_archived_files'),
    url(r'^stagednoarc/$',
        views.staged_noarchived_files, name='staged_noarchived_files'),
    url(r'^agg/$', views.agg_domeday, name='agg'),
    #!url(r'^notchecknight/$', views.progress_count, name='progress_count'),
    #!url(r'^progress_plot/$', views.progress, name='progress'),
    url(r'^demo1/$', views.demo_multibarhorizontalchart,  name='demo1'),
    #!url(r'^hbar/$', views.hbar_svg,  name='hbar_svg'),
    url(r'^dupes/$', views.get_rejected_duplicates,  name='get_rejected_duplicates'),
    url(r'^miss/$', views.get_rejected_missing,  name='get_rejected_missing'),
    url(r'^recent/$', views.get_recent, name='get_recent'),
    url(r'^recentcnt/$', views.get_recent_count, name='get_recent_count'),
    url(r'^hideall/$', views.hide_all, name='hide_all'),
    url(r'^unhidecnt/$', views.get_unhide_count, name='get_unhide_count'),
    url(r'^marsclearlog/$', views.clear_mars_log, name='clear_mars_log'),
    url(r'^marslogcnt/$', views.get_mars_log_count, name='get_mars_log_count'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
