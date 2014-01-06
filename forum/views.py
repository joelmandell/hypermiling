from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

from forum.models import Subject
from forum.models import Thread

def index(request):
  subjects = Subject.objects.order_by('dateModified')
  context = {
      'subjects':subjects,
      }
  return render(request, 'forum/index.html', context)

def threads(request, subjectId):
  try:
    subjectTitle = Subject.objects.get(id=subjectId)
    threads = Subject.objects.get(id=subjectId).thread_set.all()
  except Subject.DoesNotExist:
    raise Http404
  context = {'threads': threads, 'subjectTitle':subjectTitle, 'subjectId':subjectId}
  return render(request, 'forum/threads.html', context)

def thread(request, threadId):
  try:

    t=Thread.objects.get(id=threadId)
    title=t.threadTitle
    text=t.threadText
    user=t.user.username
    subjectId=Subject.objects.get(thread__id=threadId).id
    subjectTitle=Subject.objects.get(thread__id=threadId).subjectTitle
    posts=Thread.objects.get(id=threadId).post_set.all()
    
  except Thread.DoesNotExist:
    raise Http404
  
  context = {'title': title, 'text':text,'user':user, 'posts':posts,'subjectId':subjectId,'subjectTitle':subjectTitle}
  return render(request, 'forum/thread.html', context)


