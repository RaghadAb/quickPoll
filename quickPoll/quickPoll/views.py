from django.http import HttpResponse
import datetime
from django.shortcuts import render

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def home(request):
    context = {}
    return render(request, 'home.html', context)
