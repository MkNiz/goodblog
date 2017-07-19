from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'goodblogger/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    return render(request, 'goodblogger/topics.html', {'topics': topics})

def topic(request, topic_id):
    """Displays a single topic and its posts"""
    topic = Topic.objects.get(id=topic_id)
    posts = topic.post_set.order_by('-date_added')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'goodblogger/topic.html', context) 
