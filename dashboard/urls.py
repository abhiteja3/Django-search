from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from search import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'my_proj.views.home', name='home'),
    # url(r'^my_proj/', include('my_proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
      url(r'^app/', include('app.urls',namespace="app")),
      url(r'^search/$', views.searchview),
      url(r'^search/full/$', views.fullview),
      url(r'^admin/', include(admin.site.urls)),
)
