from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic

# Create your views here.
def index(request):
    """The Home Page for Learning Log."""
    # return HttpResponse("Hello, Visitor. Welcome to Learning Log.")
    return render(request, 'learning_logs/index.html')

def greet(request, name):
    """Return Homepage matching url ending"""
    # return HttpResponse(f"Hello, {name.capitalize()}.")
    return render(request, 'learning_logs/greet.html', {
        "name": name.capitalize()
    })

def double(request):
    return HttpResponse("Hello Hello to you double two.")


def topics(request):
    """Shows all Topics"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)