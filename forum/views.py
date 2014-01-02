#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from forum.models import Subject
from forum.models import Thread

def index(request):
	subjects = Subject.objects.order_by('dateModified')
	template = loader.get_template('forum/index.html')
	context = RequestContext(request, {
	    'subjects':subjects,
	    })
	return HttpResponse(template.render(context))

def threads(request, subjectId):
	
	
	threads=Subject.objects.get(id=subjectId).thread_set.all()
	subjectTitle=Subject.objects.get(id=subjectId)

	template = loader.get_template('forum/threads.html')
	context = RequestContext(request, 
	    {'threads':threads,
	    'subjectTitle':subjectTitle,
	    'subjectId':subjectId}
	  )
	
	return HttpResponse(template.render(context))