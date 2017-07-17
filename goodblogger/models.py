from django.db import models

# Create your models here.
class Topic(models.Model):
    """A topic that a blog post can have"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """How to represent an instance as a string"""
        return self.text
