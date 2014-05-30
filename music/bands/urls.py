from django.conf.urls import patterns, url

from bands import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bands/(?P<band_id>\d+)/$', views.bandName, name='bandName'),
)