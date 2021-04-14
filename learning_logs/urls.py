from django.conf.urls import url
from django.urls import path

from . import views

""" Defines URL schemes for learning_logs """

urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # output all topics
    path('topics/', views.topics, name='topics'),
    # page, with all information about topic
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # page for add new topic
    path('new_topic', views.new_topic, name='new_topic'),
    # page for topic addition
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # page for editing
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

]