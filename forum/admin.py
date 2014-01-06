from django.contrib import admin
from forum.models import Subject
from forum.models import Thread
from forum.models import Post

admin.site.register(Subject)
admin.site.register(Thread)
admin.site.register(Post)