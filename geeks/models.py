from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class flight_Details(models.Model):
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
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    gender = models.CharField(max_length=20)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.Charfield(max_length=20)
    Pincode = models.IntegerField()
    is_admin = models.BooleanField()

    def __str__(self):
        return self.firstname + " " + self.lastname
              
class booking(models.Model):
    f_id = models.Foreignkey(flight_Details)
    u_id = models.ManyToManyField(user)
    p_id = models.Foreignkey(passenger)  
    #booking_number = models.IntegerField()
    pnr = models.IntegerField()
    booking_time = TimeField()
    number_of_passengers = models.IntegerField()
    
class airports(models.Model):
    Airport_name = models.CharField(max_length = 10)
    Country = models.CharField(max_length = 10 )
    
class passenger:
    name = models.CharField(max_lenght = 10 )
    address = models.CharField(max_length = 10)
    contact_number = models.Charfield(max_length = 10)
    email_id = models.EmailField(max_length = 10)
    Gender = models.CharField(max_length = 10)
    Age = models.IntegerField()
    user_id = models.Foreignkey(user)
    
class passenger_Booking:
    booking = models.ForeignKey(booking)
    passenger = models.ManyToManyField(passenger)
