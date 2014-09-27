from django.conf.urls import patterns, include, url
from django.contrib import admin
from engine1 import engine1_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kasner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', engine1_views.index),
)
