from django.shortcuts import render # type: ignore

# Create your views here.
def rohit(request):
    return render(request, 'rohit.html')