from django.shortcuts import render
from django.http import HttpResponse
from . import views
from cars.models import Car


def cars(request):
    return render(request, 'cars/cars.html') 
