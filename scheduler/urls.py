from django.conf.urls.defaults import *
from reggit import main
from django.conf import settings

urlpatterns = patterns('scheduler.views',
                      (r'^$', 'index'),
)
