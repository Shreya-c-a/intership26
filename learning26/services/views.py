
# Create your views here.
from urllib import request
from django.shortcuts import get_object_or_404, render,redirect
from .models import Service
from .forms import ServiceForm


def serviceList(request):
    services = Service.objects.all()
    return render(request, 'services/servicelist.html', {"services": services})

def createService(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('servicelist')

    return render(request, 'services/createservice.html', {'form': form})


def deleteService(request, id):
    service = Service.objects.get(id=id)

    if request.method == "POST":
        service.delete()
        return redirect('servicelist')

    return render(request, 'services/servicedelete.html', {'service': service})


def updateService(request, id):
    service = get_object_or_404(Service, id=id)
    form = ServiceForm(request.POST or None, instance=service)

    if form.is_valid():
        form.save()
        return redirect('servicelist')

    return render(request, 'services/updateservice.html', {'form': form})