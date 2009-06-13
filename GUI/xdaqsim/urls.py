from django.conf.urls.defaults import *
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^xdaqsim/', include('xdaqsim.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
    (r'^tests/', include('xdaqsim.results.urls')),
    (r'^tests/plots/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_DOC_ROOT}),
    (r'^tests/js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.JS_ROOT}),
    (r'^tests/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.CSS_ROOT}),        
)
