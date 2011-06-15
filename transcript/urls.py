from django.conf.urls.defaults import *

urlpatterns = patterns('transcript.views',
                      (r'^$', 'index'),
                      (r'^report_card/$','report_card')
        
        )
