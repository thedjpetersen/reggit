from django.conf.urls.defaults import *
from regfe import main
from django.conf import settings

urlpatterns = patterns('',
                        (r'^$', 'main.views.index'),
                        (r'^login/$', 'main.views.login'),
                        (r'^logout/$', 'main.views.logout'),
                        (r'^main/$', 'main.views.main'),
)
