from django.contrib import admin
from .models import City, Location, ParkingSpot, User, Booking



admin.site.register(City)
admin.site.register(Location)
admin.site.register(ParkingSpot)
admin.site.register(User)
admin.site.register(Booking)