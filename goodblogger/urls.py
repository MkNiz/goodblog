"""Defines URL patterns for the goodblogger app"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home
    url(r'^$', views.index, name='index'),

    # All Topics
    url(r'^topics/$', views.topics, name='topics'),
    # Topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # New Topic
    url(r'^new_topic/$', views.new_topic, name='new_topic')
]
