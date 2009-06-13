from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('xdaqsim.results.views',
    (r'^admin/(.*)', admin.site.root),
    (r'^$', 'index'),
    (r'^(?P<test_id>\d+)/$', 'detail'),
    (r'^select/$', 'select'),
    (r'^plot/$', 'plot'),
    (r'^all/$', 'all'),
)
