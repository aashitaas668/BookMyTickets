from django.db import models

# Create your models here.
class Flight_Details(models.Model):
    flight_number = models.CharField(max_length=10)
    flight_name = models.CharField(max_length=30)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    airline_name = models.CharField(max_length=10)
    source = models.CharField(max_length=10)
    destination = models.CharField(max_length=10)
    source_airport = models.CharField(max_length=10)
    destination_airport = models.CharField(max_length=10)
    flight_duration = models.IntergerField()
    stops = models.IntegerField()
    remaining_seats = models.IntegerField()
    total_seats = models.IntegerField()
    price = models.Charfield(max_length=10)
    date_of_departure = models.DateField()
   

    def __str__(self):
        return self.flight_number + " " + self.op_airline

class User(models.Model):
    user_number = models.Charfield(max_length=10)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)
    password = models.CharField(max_length=20)
    is_admin = models.BooleanField()

    def __str__(self):
        return self.firstname + " " + self.lastname
        
    class Meta:
      abstract = True
class Booking(models.Model):
    booking_id = models.CharField(max_length = 10)
    booking_date = models.DateField()
    trip_date = models.Date_Field()
    flight_number = models.ForeignKey(Flight, on_delete=models.CASCADE)
    user_number = models.ForeignKey(Flight , on_delete=models.CASCADE)
    number_of_passengers = models.IntergerField()
    total_price = models.IntegerField()
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
