"""marssite URL Configurationinc
"""
#from django.conf.urls import include, url
from django.urls import include, path
#from django.conf.urls import url
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
    #path('home', include('water.urls', namespace='water')),
    #path('favicon.ico$', 'django.views.static.server',  {'document_root': '/var/mars/Mars_icon.jpg'}),

    path('users/', include('users.urls', namespace='users')),
    #!path('siap/', include('siap.urls', namespace='siap')),
    path('dal/', include('dal.urls', namespace='dal')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    #!path('provisional/', include('provisional.urls', namespace='provisional')),
    #path('tada/', include('tada.urls', namespace='tada')),
    path('audit/', include('audit.urls', namespace='audit')),
    path('natica/', include('natica.urls')),
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('portal/', include('portal.urls', namespace='portal')),
    #!path('api-auth/',  include('rest_framework.urls', namespace='rest_framework')),
    #path('api/', include(router.urls)),
    path('api/', api_root, name='api_root'),
    path('api-docs/', schema_view),
    path('docs/', include('docs.urls', namespace='docs')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
