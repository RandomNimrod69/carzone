from django.shortcuts import render
from cars.models import Car  # Correct import of the Car model

# Create your views here.

def home(request):
    featured_cars = Car.objects.order_by('-data_adaugare').filter(is_featured=True)
    data = {
        'featured_cars': featured_cars
    }
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'pages/cars/cars.html')
