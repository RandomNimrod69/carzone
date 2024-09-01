from django.db import models
from datetime import datetime

class Car(models.Model):

    county_choice = (
        ('DJ', 'Dolj'),
        ('MH', 'Mehedinti'),
        ('OT', 'Olt'),
        ('B', 'Bucuresti'),
    )

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year + 1)):
        year_choice.append((r, r))

    car_title = models.CharField(max_length=255)
    judet = models.CharField(choices=county_choice, max_length=100)
    culoare = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    an = models.IntegerField()
    conditie = models.CharField(max_length=100)
    pret = models.IntegerField()
    descriere = models.TextField()
    poza = models.ImageField(upload_to='photos/%Y/%m/%d/')
    poza_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    poza_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    poza_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    poza_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    optiuni = models.CharField(choices=features_choices, max_length=100)
    caroserie = models.CharField(max_length=100)
    motor = models.CharField(max_length=100)
    cutie = models.CharField(max_length=100)
    kilometraj = models.IntegerField()
    usi = models.CharField(choices=door_choices, max_length=100)
    pasageri = models.IntegerField()
    serie_Sasiu = models.CharField(max_length=100)
    consum = models.IntegerField()
    tip_combustibil = models.CharField(max_length=100)
    numar_propietari = models.CharField()
    is_featured = models.BooleanField(default=False)
    data_adaugare = models.DateTimeField(default=datetime.now, blank=True)
