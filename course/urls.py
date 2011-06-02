from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('course.views',
                        (r'^$', 'index'),
                        (r'^(?P<department>\w\w)(?P<course_number>\d\d\d)/$', 'show'),
                        (r'^(?P<department>\w\w\w)(?P<course_number>\d\d\d)/$', 'show'),
                        (r'^(?P<department>\w\w\w\w)(?P<course_number>\d\d\d)/$', 'show'),
)
