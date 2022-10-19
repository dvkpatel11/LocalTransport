from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import *

# Create your views here.
def index(request):
    return render(request, "buses/index.html", {
        "buses" :  Bus.objects.all(),
        "stations" : Station.objects.all(),
        "passengers" : Passenger.objects.all()
    })

def bus(request, bus_id):
    bus = Bus.objects.get(id=bus_id)
    return render(request, "buses/bus.html", {
        "bus" : bus,
        "passengers": bus.passengers.all(),
        "non_passengers" : Passenger.objects.exclude(buses=bus_id).all()
    })

def book(request, bus_id):
    if request.method == "POST":
        bus = Bus.objects.get(pk=bus_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.buses.add(bus)
        return HttpResponseRedirect(reverse("bus", args=(bus.id,)))