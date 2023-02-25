from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Topic
from .forms import TopicForm

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

def topic(request, topic_id):
    """Shows single topic and all entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries}
    return render(request, 'learning_logs/topic.html', context)


def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data & make form
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form. 
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
