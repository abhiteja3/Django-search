from django.conf.urls import patterns, url

from search.views import search

urlpatterns = patterns('',
    url(r'^search/$', search.views.searchview),
    #url(r'^search/$', search.views.fullview),
)