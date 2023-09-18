from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

def index(request):
    return render(request, "flight/index.html", {"flight": Flight.objects.all})

def flight(request):
    flight = Flight.object.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passenger": flight.passengers.all,
        "non_passenger": Passenger.objects.exclude(flight=flight).all
    })

def book(request, flight_id):
    if request.medthod == "POST":
        flight = Flight.object.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=int(request.POST["passenger"]))
        passenger.flight.add(flight)
        return HttpResponseRedirect(reverse("flight", args=(flight_id)))