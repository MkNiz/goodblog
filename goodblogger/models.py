from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """A topic that a blog post can have"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """How to represent an instance as a string"""
        return self.text

class Post(models.Model):
    """A post in the blog"""
    topic = models.ForeignKey(Topic)
    title = models.CharField(max_length=128)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """How to represent an instance as a string"""
        return self.title
