from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from cars.models import Car
from django.db.models import Q

def cars(request):
    cars = Car.objects.order_by('-data_adaugare')
    paginator = Paginator(cars, 3)
    page = request.GET.get('page')


    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    judet_search = Car.objects.values_list('judet', flat=True).distinct()
    an_search = Car.objects.values_list('an', flat=True).distinct()
    caroserie_search = Car.objects.values_list('caroserie', flat=True).distinct()
   



    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'judet_search': judet_search,
        'an_search': an_search,
        'caroserie_search': caroserie_search,
    }

    return render(request, 'cars/cars.html', data)

def car_detail(request, id): 
    single_car = get_object_or_404(Car, pk=id)
    data = {
        'single_car': single_car,
    }
    return render(request, 'cars/car_detail.html', data)

def search(request):
    # Start with all cars ordered by the date added
    cars = Car.objects.order_by('-data_adaugare')


     # Pagination setup
    paginator = Paginator(cars, 10)  # Show 10 cars per page
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)

    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    judet_search = Car.objects.values_list('judet', flat=True).distinct()
    an_search = Car.objects.values_list('an', flat=True).distinct()
    caroserie_search = Car.objects.values_list('caroserie', flat=True).distinct()
    cutie_search = Car.objects.values_list('cutie', flat = True).distinct

    # Check if 'keyword' is in GET parameters
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Filter cars where the 'description' field contains the keyword
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            # Filter cars by model
            cars = cars.filter(model__iexact=model)

    if 'judet' in request.GET:
        judet = request.GET['judet']
        if judet:
            # Filter cars by location (judet)
            cars = cars.filter(judet__iexact=judet)

    if 'an' in request.GET:
        an = request.GET['an']
        if an:
            # Filter cars by year
            cars = cars.filter(an__iexact=an)

    if 'caroserie' in request.GET:
        caroserie = request.GET['caroserie']
        if caroserie:
            # Filter cars by car body style
            cars = cars.filter(caroserie__iexact=caroserie)

    # Check for price range
    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if min_price and max_price:
            # Filter cars by price range
            cars = cars.filter(pret__gte=min_price, pret__lte=max_price)

    # Prepare the context for rendering
    data = {
        'cars': cars,
        'model_search': model_search,
        'judet_search': judet_search,
        'an_search': an_search,
        'caroserie_search': caroserie_search,
        'cutie_search': cutie_search,
    }

    # Render the response
    return render(request, 'cars/search.html', data)
