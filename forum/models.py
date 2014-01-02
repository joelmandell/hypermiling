from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
	subjectTitle = models.CharField(max_length=45)
	subjectDescription = models.CharField(max_length=100)
	dateModified = models.DateTimeField();
	def __unicode__(self):
		return self.subjectTitle

class Thread(models.Model):
	subjects = models.ManyToManyField(Subject)
	user = models.ForeignKey(User)
	threadTitle = models.CharField(max_length=45)
	threadText = models.CharField(max_length=3000)
	dateModified = models.DateTimeField()
	def __unicode__(self):
		return self.threadTitle

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	user = models.ForeignKey(User)
	text = models.CharField(max_length=3000)
	dateModified = models.DateField()
	def __unicode__(self):
		return self.text
