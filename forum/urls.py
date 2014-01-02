#-*- coding: utf-8 -*-
from django.conf.urls import patterns, url

from forumthread import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^Subjects/(?P<subjectid>\d+)/$', views.subject, name='subject')
)