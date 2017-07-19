from django import forms

from .models import Topic, Post

class TopicForm(forms.ModelForm):
    """Form for Topics"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class PostForm(forms.ModelForm):
    """Form for Posts"""
    class Meta:
        model = Post
        fields = ['title', 'text']
        labels = { 'title': 'Title', 'text': 'Content' }
        widgets = { 'text': forms.Textarea(attrs={ 'cols': 80 }) }
