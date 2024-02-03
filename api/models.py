from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_number=models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class City(models.Model):
    cityName = models.CharField(max_length=255)

    def __str__(self):
        return self.cityName


class Location(models.Model):
    locationName = models.CharField(max_length=255)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)
    location_latitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
    location_longitude = models.CharField('Longitude', max_length=20, null=True, blank=True)

    def __str__(self):
        return self.locationName
    


class ParkingSpot(models.Model):
    spotNumber = models.CharField(max_length=50)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE)
    lsBooked = models.BooleanField(default=False)

    def __str__(self):
        return self.spotNumber

#     password = models.CharField(max_length=255)
# class User(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=12,unique=True)

#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
    
    
class CarDetail(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='car_details')
    number_plate = models.CharField(max_length=10)
    make_and_model = models.CharField(max_length=100)
    year = models.CharField(max_length=4)
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make_and_model} ({self.year})"
   

class Booking(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True, default=None)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True, default=None)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    spot_id = models.ForeignKey(ParkingSpot, on_delete=models.CASCADE, related_name='bookings')
    bookingDate = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()
   


    def __str__(self):
        return f"Booking #- {self.user_id.first_name} {self.user_id.last_name}"
    
