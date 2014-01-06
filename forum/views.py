from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.models import User

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
  try:
    subjectTitle = Subject.objects.get(id=subjectId)
    threads = Subject.objects.get(id=subjectId).thread_set.all()
  except Subject.DoesNotExist:
    raise Http404
  context = {'threads': threads, 'subjectTitle':subjectTitle, 'subjectId':subjectId}
  return render(request, 'forum/threads.html', context)

def thread(request, threadId):
  try:
    t=Thread.objects.get(id=threadId).all()
    title=t.threadTitle;
    posts=Thread.objects.get(id=threadId).post_set.all()
  except Subject.DoesNotExist:
    raise Http404
  context = {'threads': threads, 'subjectTitle':subjectTitle, 'subjectId':subjectId}
  return render(request, 'forum/threads.html', context)


