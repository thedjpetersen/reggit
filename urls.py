from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('',
                        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),

                        (r'^$', 'main.views.index'),
                        (r'^login/$', 'main.views.login'),
                        (r'^logout/$', 'main.views.logout'),
                        (r'^main/$', 'main.views.main'),
                        (r'^transcript/$', include('transcript.urls')),
                        (r'^schedule/$', include('schedule.urls')),
                        (r'^scheduler/$', 'main.views.scheduler'),
                        (r'^course/', include('course.urls')),
)
