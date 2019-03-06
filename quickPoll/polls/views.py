from django.shortcuts import render
from .models import Poll



# Create your views here.

def search(request):

    polls= Poll.objects.all()
    context={'polls':polls}
    return render(request,'polls/search.html',context)



