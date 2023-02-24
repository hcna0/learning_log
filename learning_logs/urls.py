"""Defines URL patterns for 'learning_logs' application"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path("single", views.single, name="single"),
    path("double", views.double, name="double"),
]
