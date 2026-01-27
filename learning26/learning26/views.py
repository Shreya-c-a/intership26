from django.http import HttpResponse
from django.shortcuts import render


def test(request):
    return HttpResponse("hello test")

def aboutus(request):
    return render(request, 'aboutus.html')
    
def contactus(request):
        return render(request, 'contactus.html')    
    
def home(request):
        return render(request, 'home.html')
        