from django.conf.urls import patterns, include, url
from django.contrib import admin
from engine1 import engine1_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kasner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', engine1_views.index),
    url(r'^kasner/$', engine1_views.kasner),
    url(r'^add_form/$', engine1_views.add_form),
    url(r'^add/$', engine1_views.add),
    url(r'^about$', engine1_views.about),
    url(r'^another_page$', engine1_views.another_page),
    url(r'^search_stats$', engine1_views.search_stats),
    url(r'^stats-tabs$', engine1_views.stats_tabs),
    url(r'^stats_browsers$', engine1_views.stats_browsers),
    url(r'^stats_terms$', engine1_views.stats_terms),
)
