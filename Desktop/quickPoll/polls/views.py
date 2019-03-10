from django.shortcuts import render
from .models import Poll,Options
from django.http import HttpResponse
from django.shortcuts import get_object_or_404



# Create your views here.

def search(request):

    polls= Poll.objects.all()
    context={'polls':polls}
    return render(request,'polls/search.html',context)



def option_Number(request, quiPoll_id):
    option=Poll.objects.get(id=quiPoll_id)

    if request.method=="POST":
        print("It's submitted!")
        print(request.POST)

    if request.method=="GET":
        print("Got it")
        print(request.GET)

    context={'option':option}
    return render(request,'polls/option_Number.html',context)

def vote (request, quiPoll_id):
    poll = get_object_or_404(Poll, id=quiPoll_id)

    return HttpResponse("def")



#uses the option_Number.html template , this enables the user to vote

