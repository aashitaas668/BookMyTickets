from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class flight_details(models.Model):
    airport_id = models.ForeignKey(airports)
    flight_number = models.IntegerField()
    airline_name = models.CharField(max_length=10)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    date_of_departure = models.DateField()
    date_of_arrival = models.DateField()
    source = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    available_seats = models.IntegerField()
    total_seats = models.IntegerField()
    price = models.Charfield(max_length=10)
   

    def __str__(self):
        return self.flight_number + " " + self.date_of_arrival

class user(AbstractUser):
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.Charfield(max_length=20)
    pincode = models.IntegerField()
    is_admin = models.BooleanField()

    def __str__(self):
        return self.first_name + " " + self.last_name
              
class booking(models.Model):
    f_id = models.Foreignkey(flight_Details)
    u_id = models.ManyToManyField(user)
    p_id = models.Foreignkey(passenger)  
    #booking_number = models.IntegerField()
    pnr = models.IntegerField()
    booking_time = TimeField()
    number_of_passengers = models.IntegerField()
    
class airports(models.Model):
    airport_name = models.CharField(max_length = 10)
    country = models.CharField(max_length = 10 )
    
class passenger:
    name = models.CharField(max_lenght = 10 )
    address = models.CharField(max_length = 10)
    contact_number = models.Charfield(max_length = 10)
    email_id = models.EmailField(max_length = 10)
    gender = models.CharField(max_length = 10)
    age = models.IntegerField()
    user_id = models.Foreignkey(user)
    
class passenger_booking:
    booking = models.ForeignKey(booking)
    passenger = models.ManyToManyField(passenger)
