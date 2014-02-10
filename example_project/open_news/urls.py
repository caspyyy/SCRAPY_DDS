from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from open_news import views

urlpatterns = patterns('',
	url(r'^$', views.index2, name='index2'),
	url(r'^(?P<myID>\d+)/$', views.detail, name='detail'),
	url(r'^run_script/$', views.run_script, name='run_script'),
	url(r'^amchart/$', views.amchart, name='amchart'),
)
