from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def Dhoni(request):
    return HttpResponse('<h1><marquee>Msd is the best captain for csk</marquee></h1>')
def raina(request):
    return render(request, 'raina.html')
