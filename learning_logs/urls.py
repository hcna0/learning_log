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
]
