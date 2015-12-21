from django.conf.urls import patterns, url
from relimgApp import views
from django.conf import settings

urlpatterns = patterns(
	'',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<anime_id>\d+)/$', views.details, name='details'),
	url(r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_URL_IMAGE,})
)