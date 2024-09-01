from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from . import views
from cars.models import Car


def cars(request):
    return render(request, 'cars/cars.html') 

def car_detail(request, id): 
    single_car = get_object_or_404(Car, pk=id)

    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)