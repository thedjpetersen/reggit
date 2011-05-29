from django.conf.urls.defaults import *
from reggie import main
from django.conf import settings

urlpatterns = patterns('',
                        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT}),

                        (r'^$', 'main.views.index'),
                        (r'^login/$', 'main.views.login'),
                        (r'^logout/$', 'main.views.logout'),
                        (r'^main/$', 'main.views.main'),
                        (r'^transcript/$', 'main.views.transcript'),
                        (r'^schedule/$', 'main.views.schedule'),
                        (r'^make_schedule/$', 'main.views.make_schedule'),
)
