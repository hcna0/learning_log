from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    """The Home Page for Learning Log."""
    return HttpResponse("Hello, Visitor. Welcome to Learning Log.")
    # return render(request, 'learning_logs/index.html')

