from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField

# Create your models here.
class Car(models.Model):

    state_choice =  (
        ('AT', 'Austria'),
        ('BE', 'Belgium'),
        ('BG', 'Bulgaria'),
        ('HR', 'Croatia'),
        ('CY', 'Cyprus'),
        ('CZ', 'Czech Republic'),
        ('DK', 'Denmark'),
        ('EE', 'Estonia'),
        ('FI', 'Finland'),
        ('FR', 'France'),
        ('DE', 'Germany'),
        ('GR', 'Greece'),
        ('HU', 'Hungary'),
        ('IE', 'Ireland'),
        ('IT', 'Italy'),
        ('LV', 'Latvia'),
        ('LT', 'Lithuania'),
        ('LU', 'Luxembourg'),
        ('MT', 'Malta'),
        ('NL', 'Netherlands'),
        ('PL', 'Poland'),
        ('PT', 'Portugal'),
        ('RO', 'Romania'),
        ('SK', 'Slovakia'),
        ('SI', 'Slovenia'),
        ('ES', 'Spain'),
        ('SE', 'Sweden'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))

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
    ('two', 'Two doors'),
    ('four', 'Four doors'),
    ('hatchback', 'Hatchback'),
    ('convertible', 'Convertible'),
    )
    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=150)
    city = models.CharField(max_length=150)
    colour = models.CharField(max_length=150)
    model = models.CharField(max_length=150)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=150)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/',)
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=150)
    engine = models.CharField(max_length=150)
    transmission = models.CharField(max_length=150)
    interior = models.CharField(max_length=150)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=100)
    passengers = models.IntegerField()
    interior = models.CharField(max_length=150)
    vin_no = models.CharField(max_length=150)
    mileage = models.CharField(max_length=150)
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title
