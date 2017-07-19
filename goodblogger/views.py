from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
    return render(request, 'goodblogger/index.html')

def topics(request):
    """Show all topics"""
    topics = Topic.objects.order_by('date_added')
    return render(request, 'goodblogger/topics.html', {'topics': topics})
