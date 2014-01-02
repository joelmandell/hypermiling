#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from forumthread.models import Subject
from forumthread.models import Thread

def index(request):
	subjects = Subject.objects.order_by('dateModified')
	template = loader.get_template('forum/index.html')
	context = RequestContext(request, {
	    'subjects':subjects,
	    })
	return HttpResponse(template.render(context))

def subject(request, subjectid):
	output=u"<h2>Hej på dig här kommer trådar som tillhör id {0}</h2>".format(subjectid)
	all_threads=Subject.objects.get(id=subjectid).thread_set.all()

	for t in all_threads:
		output+=u"{0} <br />".format(t.threadTitle) 
	return HttpResponse(output)