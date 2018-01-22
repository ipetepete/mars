"""marssite URL Configurationinc
"""
#from django.conf.urls import include, url
from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User # ,Group
#from provisional.views import FitsnameViewSet
from rest_framework_swagger.views import get_swagger_view

#from schedule.views import ScheduleViewSet
from water.views import api_root
# Serializers define the API representation.
#!class UserSerializer(serializers.HyperlinkedModelSerializer):
#!    class Meta:
#!        model = User
#!        fields = ('url', 'username', 'email', 'is_staff')
#!
#!class GroupSerializer(serializers.HyperlinkedModelSerializer):
#!    class Meta:
#!        model = Group


schema_view = get_swagger_view(title='Rest API')


# ViewSets define the view behavior.
#!class UserViewSet(viewsets.ModelViewSet):
#!    queryset = User.objects.all()
#!    serializer_class = UserSerializer
#!class GroupViewSet(viewsets.ModelViewSet):
#!    queryset = Group.objects.all()
#!    serializer_class = GroupSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#!router.register(r'groups', GroupViewSet)

#router.register(r'fitsnames', FitsnameViewSet)
#router.register(r'schedules', ScheduleViewSet)

admin.site.site_header = 'MARS Administration'



urlpatterns = [
    path('', include('water.urls')),
    #url(r'^home', include('water.urls', namespace='water')),
    #url(r'^favicon.ico$', 'django.views.static.server',  {'document_root': '/var/mars/Mars_icon.jpg'}),

    url(r'^users/', include('users.urls', namespace='users')),
    #!url(r'^siap/', include('siap.urls', namespace='siap')),
    url(r'^dal/', include('dal.urls', namespace='dal')),
    url(r'^schedule/', include('schedule.urls', namespace='schedule')),
    #!url(r'^provisional/', include('provisional.urls', namespace='provisional')),
    url(r'^tada/', include('tada.urls', namespace='tada')),
    url(r'^audit/', include('audit.urls', namespace='audit')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^portal/', include('portal.urls', namespace='portal')),
    #!url(r'^api-auth/',  include('rest_framework.urls', namespace='rest_framework')),
    #url(r'^api/', include(router.urls)),
    url(r'^api/', api_root, name='api_root'),
    url(r'^api-docs/', schema_view),
    url(r'^docs/', include('docs.urls', namespace='docs')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
