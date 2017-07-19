from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Topic
from .forms import TopicForm

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
