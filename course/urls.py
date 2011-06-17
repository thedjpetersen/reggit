from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('course.views',
                        (r'^$', 'index'),
                        (r'^(?P<department>\w+)(?P<number>\d\d\d)/$', 'show'),
)
