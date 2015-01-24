from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'diogenes_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^diogenes/', include('diogenes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/', include('registration.backends.simple.urls')),
)
