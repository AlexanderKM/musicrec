from django.conf.urls import patterns, url

from bands import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bands/$', views.search, name='search'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^bands/(?P<band_id>\d+)/$', views.bandName, name='bandName'),
)