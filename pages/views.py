from django.shortcuts import render, redirect
from cars.models import Car  # Correct import of the Car model

# Create your views here.

def home(request):
    # Query for featured cars, ordered by 'data_adaugare' in descending order
    featured_cars = Car.objects.filter(is_featured=True).order_by('-data_adaugare')

    # Query for all cars, ordered by 'data_adaugare' in descending order
    all_cars = Car.objects.order_by('-data_adaugare')

    # Fetch distinct values for each dropdown
    model_search = Car.objects.values_list('model', flat=True).distinct()
    judet_search = Car.objects.values_list('judet', flat=True).distinct()
    an_search = Car.objects.values_list('an', flat=True).distinct()
    caroserie_search = Car.objects.values_list('caroserie', flat=True).distinct()

    # Prepare the context data
    data = {
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'judet_search': judet_search,
        'an_search': an_search,
        'caroserie_search': caroserie_search,
    }

    # Render the template with the context data
    return render(request, 'home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cars(request):
    return render(request, 'pages/cars/cars.html')

def login(request):
    return render (request, 'accounts/login.html')

def register(request):
    return render (request, 'accounts/register.html')

def dashboard(request):
    return render (request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')

