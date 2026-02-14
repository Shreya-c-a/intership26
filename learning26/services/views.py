
# Create your views here.
from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm


def serviceList(request):
    services = Service.objects.all()
    return render(request, 'services/servicelist.html', {"services": services})

def createService(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
    else:
        form = ServiceForm()
    return render(request, 'services/createservice.html', {"form": form})

def deleteService(request, id): 
    Service.objects.filter(id=id).delete() 
    return redirect("servicelist")     


def updateService(request, id):
    service = Service.objects.get(id=id)
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
    else:
        form = ServiceForm(instance=service)
    return render(request, 'services/updateservice.html', {"form": form})