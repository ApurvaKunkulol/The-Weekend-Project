__author__ = 'Janak'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^articles/$', views.getarticles, name='articles'),
    url(r'^sentiment/(?P<article_id>[0-9]+)/$', views.getsentiment, name='getsentiment'),
]

