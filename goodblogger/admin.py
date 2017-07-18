from django.contrib import admin

# Register your models here.
from goodblogger.models import Topic, Post

admin.site.register(Topic)
admin.site.register(Post)
