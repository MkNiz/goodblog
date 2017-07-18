"""Defines URL patterns for the goodblogger app"""

from django.conf.urls import url
from . import views

urlpatterns = [
    # Home
    url(r'^$', views.index, name='index')
]
