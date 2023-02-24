from django.shortcuts import render
import datetime

# Create your views here.
def index(request):
    """Page for count to new year y/n"""
    now = datetime.datetime.now()
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })
