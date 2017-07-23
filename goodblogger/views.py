from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Post
from .forms import TopicForm, PostForm

# Create your views here.
def index(request):
    return render(request, 'goodblogger/index.html')

@login_required
def topics(request):
    """Show all of the user's topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    return render(request, 'goodblogger/topics.html', {'topics': topics})

@login_required
def topic(request, topic_id):
    """Displays a single topic and its posts"""
    topic = Topic.objects.get(id=topic_id)
    # Raise a 404 if the user doesn't own this topic
    if topic.owner != request.user:
        raise Http404
    posts = topic.post_set.order_by('-date_added')
    context = {'topic': topic, 'posts': posts}
    return render(request, 'goodblogger/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # Display the blank form if data is not POSTed
        form = TopicForm()
    else:
        # Utilize POST data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('blog:topics'))
    return render(request, 'goodblogger/new_topic.html', {'form': form})

@login_required
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

@login_required
def edit_post(request, post_id):
    """Edit an existing post"""
    post = Post.objects.get(id=post_id)
    topic = post.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Prepares the form with the instance's existing data
        form = PostForm(instance=post)
    else:
        # Accept data and make changes
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('blog:topic', args=[topic.id]))
    context = { 'post': post, 'topic': topic, 'form': form }
    return render(request, 'goodblogger/edit_post.html', context)
