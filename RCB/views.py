from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def virat(request):
    return HttpResponse('<h1>Viratian is the best cricketer</h>')

def abd(request):
    return render(request, 'abd.html')