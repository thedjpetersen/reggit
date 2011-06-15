from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('',
    (r'^$', 'main.views.index'),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.STATIC_DOC_ROOT}), 
    (r'^login/$', 'main.views.login'),
    (r'^logout/$', 'main.views.logout'),
    (r'^main/$', 'main.views.main'),
    (r'^transcript/', include('transcript.urls')),
    (r'^schedule/', include('schedule.urls')),
    (r'^', include('scheduler.urls')),
    (r'^course/', include('course.urls')),
    (r'^planner/', 'main.views.planner'),
)

