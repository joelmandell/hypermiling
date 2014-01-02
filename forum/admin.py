from django.contrib import admin
from forum.models import Subject
from forum.models import Thread

admin.site.register(Subject)
admin.site.register(Thread)