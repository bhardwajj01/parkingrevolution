from django.urls import path
from .views import (
    CityListAPIView, CityDetailAPIView,
    LocationListAPIView, LocationDetailAPIView,
    ParkingSpotListAPIView, ParkingSpotDetailAPIView,
    BookingListAPIView, BookingDetailAPIView,
    CarDetailDetailAPIView,CarDetailListAPIView,
    RegistrationAPIView,LoginAPIView,
    get_all_cities,get_locations_by_city,get_spot_numbers_by_location ,create_booking

)

urlpatterns = [
    path('cities/', CityListAPIView.as_view(), name='city-list'),
    path('cities/<int:pk>/', CityDetailAPIView.as_view(), name='city-detail'),

    path('locations/', LocationListAPIView.as_view(), name='location-list'),
    path('locations/<int:pk>/', LocationDetailAPIView.as_view(), name='location-detail'),

    path('parking-spots/', ParkingSpotListAPIView.as_view(), name='parking-spot-list'),
    path('parking-spots/<int:pk>/', ParkingSpotDetailAPIView.as_view(), name='parking-spot-detail'),
    
    path('bookings/', BookingListAPIView.as_view(), name='booking-list'),
    path('bookings/<int:pk>/', BookingDetailAPIView.as_view(), name='booking-detail'),
    
    path('cardetail/', CarDetailListAPIView.as_view(), name='car-list'),
    path('cardetail/<int:pk>/', CarDetailDetailAPIView.as_view(), name='car-detail'),

    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('get-all-cities/', get_all_cities, name='get_all_cities'),
    path('get-locations-by-city/', get_locations_by_city, name='get_locations_by_city'),
    path('create_booking/', create_booking, name='create_booking'),
    path('get-spot-numbers-by-location/', get_spot_numbers_by_location, name='get_spot_numbers_by_location'),

]
