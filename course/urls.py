from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('course.views',
                        (r'^$', 'index'),
                        (r'^(?P<department>\w+)(?P<number>\d\d\d)/$', 'show'),
                        (r'^(?P<department>\w+)(?P<number>\d\d\d)\?status=(?P<status>.*)/$', 'show'),
                        (r'^register/(?P<crn1>\d+)/$', 'register'),
                        (r'^register/(?P<crn1>\d+)\&(?P<crn2>\d+)/$', 'register'),
)
