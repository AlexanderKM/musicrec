from django.conf.urls import patterns, url

from bands import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^bands/(?P<band_id>\d+)/$', views.bandName, name='bandName'),
    url(r'^statistics/$', views.statistics, name='statistics'),
)