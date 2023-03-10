"""Defines URL patterns for 'learning_logs' application"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path("<str:name>", views.greet, name="greet"),
    path("double", views.double, name="double"),

    # Page that shows topics
    path('topics/', views.topics, name='topics'),

    # Page that shows individual topic and entries
    path('topics/<int:topic_id>', views.topic, name='topic'),

    # Page that adds a new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Page that adds a new entry to a topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    
    # Page that edits an existing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    
]