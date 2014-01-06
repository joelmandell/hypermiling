#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from forum import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<subjectId>\d+)/$', views.threads, name='threads')
)