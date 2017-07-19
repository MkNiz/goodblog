from django import forms

from .models import Topic

class TopicForm(forms.ModelForm):
    """Form for Topics"""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}
