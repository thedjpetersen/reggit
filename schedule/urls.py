from django.conf.urls.defaults import *

urlpatterns = patterns('schedule.views',
                      (r'^$', 'index'),
                      (r'^next_term/$', 'next_term'),
)
