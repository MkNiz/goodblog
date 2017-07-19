from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm, PostForm

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

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # Display the blank form if data is not POSTed
        form = TopicForm()
    else:
        # Utilize POST data
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topics'))
    return render(request, 'goodblogger/new_topic.html', {'form': form})

def new_post(request, topic_id):
    """Add a new post"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # Display the blank form if data is not POSTed
        form = PostForm()
    else:
        # Utilize POST data
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic_id]))
    context = { 'topic': topic, 'form': form }
    return render(request, 'goodblogger/new_post.html', context)
