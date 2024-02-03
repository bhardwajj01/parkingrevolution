from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework_simplejwt.tokens import RefreshToken
from .models import City, Location, ParkingSpot, Booking, CarDetail
from .serializers import (
    CitySerializer,
    LocationSerializer,
    ParkingSpotSerializer,
    BookingSerializer,
    RegistrationSerializer,
    LoginSerializer,
    UserSerializer,
    CarDetailSerializer,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view ,permission_classes ,authentication_classes

class CityListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: CitySerializer(many=True)},
        operation_description="Retrieve the list of cities."
    )
    def get(self, request, format=None):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CitySerializer,
        responses={201: CitySerializer()},
        operation_description="Create a new city."
    )
    def post(self, request, format=None):
        serializer = CitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CityDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: CitySerializer()},
        operation_description="Retrieve details of a city."
    )
    def get(self, request, pk, format=None):
        city = self.get_object(pk)
        if city is not None:
            serializer = CitySerializer(city)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=CitySerializer,
        responses={200: CitySerializer()},
        operation_description="Update details of a city."
    )
    def put(self, request, pk, format=None):
        city = self.get_object(pk)
        if city is not None:
            serializer = CitySerializer(city, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: "No Content"},
        operation_description="Delete a city."
    )
    def delete(self, request, pk, format=None):
        city = self.get_object(pk)
        if city is not None:
            city.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return City.objects.get(pk=pk)
        except City.DoesNotExist:
            raise NotFound("City not found with the specified ID", code=status.HTTP_404_NOT_FOUND)


class LocationListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: LocationSerializer(many=True)},
        operation_description="Retrieve the list of locations."
    )
    def get(self, request, format=None):
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=LocationSerializer,
        responses={201: LocationSerializer()},
        operation_description="Create a new location."
    )
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LocationDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: LocationSerializer()},
        operation_description="Retrieve details of a location."
    )
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=LocationSerializer,
        responses={200: LocationSerializer()},
        operation_description="Update details of a location."
    )
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        if location is not None:
            serializer = LocationSerializer(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: "No Content"},
        operation_description="Delete a location."
    )
    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        if location is not None:
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise NotFound("Location not found with the specified ID", code=status.HTTP_404_NOT_FOUND)


class ParkingSpotListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: ParkingSpotSerializer(many=True)},
        operation_description="Retrieve the list of parking spots."
    )
    def get(self, request, format=None):
        parking_spots = ParkingSpot.objects.all()
        serializer = ParkingSpotSerializer(parking_spots, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ParkingSpotSerializer,
        responses={201: ParkingSpotSerializer()},
        operation_description="Create a new parking spot."
    )
    def post(self, request, format=None):
        serializer = ParkingSpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ParkingSpotDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: ParkingSpotSerializer()},
        operation_description="Retrieve details of a specific parking spot."
    )
    def get(self, request, pk, format=None):
        parking_spot = self.get_object(pk)
        serializer = ParkingSpotSerializer(parking_spot)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ParkingSpotSerializer,
        responses={200: ParkingSpotSerializer()},
        operation_description="Update details of a specific parking spot."
    )
    def put(self, request, pk, format=None):
        parking_spot = self.get_object(pk)
        if parking_spot is not None:
            serializer = ParkingSpotSerializer(parking_spot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: "No Content"},
        operation_description="Delete a specific parking spot."
    )
    def delete(self, request, pk, format=None):
        parking_spot = self.get_object(pk)
        if parking_spot is not None:
            parking_spot.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return ParkingSpot.objects.get(pk=pk)
        except ParkingSpot.DoesNotExist:
            raise NotFound("ParkingSpot not found with the specified ID", code=status.HTTP_404_NOT_FOUND)






class CarDetailListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200:  CarDetailSerializer(many=True)},
        operation_description="Retrieve the list of car."
    )
    def get(self, request, format=None):
        locations = CarDetail.objects.all()
        serializer =  CarDetailSerializer(locations, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body= CarDetailSerializer,
        responses={201:  CarDetailSerializer()},
        operation_description="Create a new car."
    )
    def post(self, request, format=None):
        serializer =  CarDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarDetailDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200:  CarDetailSerializer()},
        operation_description="Retrieve details of a car."
    )
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer =  CarDetailSerializer(location)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body= CarDetailSerializer,
        responses={200:  CarDetailSerializer()},
        operation_description="Update details of a car."
    )
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        if location is not None:
            serializer = CarDetailSerializer(location, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        responses={204: "No Content"},
        operation_description="Delete a car."
    )
    def delete(self, request, pk, format=None):
        location = self.get_object(pk)
        if location is not None:
            location.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_object(self, pk):
        try:
            return CarDetail.objects.get(pk=pk)
        except CarDetail.DoesNotExist:
            raise NotFound("Car detail not found with the specified ID", code=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def create_booking(request, pk=1):
    user = request.user
    bookings = Booking.objects.filter(user_id=user.id)

    if bookings.exists():
        bookingdata = bookings.first()  
    else:
       bookingdata = Booking(user_id=user)  

    request.data['user_id'] = user.id

    serializer = BookingSerializer(bookingdata, data=request.data, context={"request": request})

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Booking created successfully'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_all_cities(request):
    cities = City.objects.all()
    serializer = CitySerializer(cities, many=True)
    return Response({'Cities': serializer.data}, status=status.HTTP_200_OK)



@api_view(['POST'])
def get_locations_by_city(request):
    city_id = request.data.get('city_id')
    if city_id is not None:
        locations = Location.objects.filter(city_id=city_id)
        serializer = LocationSerializer(locations, many=True)
        return Response({'Locations': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'city_id not provided in the request data'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def get_spot_numbers_by_location(request):
    location_id = request.data.get('location_id')
    if location_id is not None:
        spot_numbers = ParkingSpot.objects.filter(location_id=location_id, lsBooked=False)
        serializer = ParkingSpotSerializer(spot_numbers, many=True)
        return Response({'SpotNumbers': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'location_id not provided in the request data'}, status=status.HTTP_400_BAD_REQUEST)



class BookingListAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        responses={200: BookingSerializer(many=True)},
        operation_description="Retrieve a list of all bookings."
    )
    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=BookingSerializer,
        responses={201: BookingSerializer()},
        operation_description="Create a new booking."
    )
    def post(self, request, format=None):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'success': True, 'data': serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class BookingDetailAPIView(APIView):
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [JWTAuthentication]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Booking ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            200: BookingSerializer(),
            404: "Booking not found with the specified ID",
        },
        operation_description="Retrieve a booking by ID."
    )
    def get(self, request, pk, format=None):
        booking = self.get_object(pk)
        if booking is not None:
            serializer = BookingSerializer(booking)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Booking ID", type=openapi.TYPE_INTEGER),
        ],
        request_body=BookingSerializer,
        responses={
            200: BookingSerializer(),
            400: "Invalid input",
            404: "Booking not found with the specified ID",
        },
        operation_description="Update a booking by ID."
    )
    def put(self, request, pk, format=None):
        booking = self.get_object(pk)
        if booking is not None:
            serializer = BookingSerializer(booking, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)



    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('pk', openapi.IN_PATH, description="Booking ID", type=openapi.TYPE_INTEGER),
        ],
        responses={
            204: "Booking deleted successfully",
            404: "Booking not found with the specified ID",
        },
        operation_description="Delete a booking by ID."
    )
    def delete(self, request, pk, format=None):
        booking = self.get_object(pk)
        if booking is not None:
            booking.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get_object(self, pk):
        try:
            return Booking.objects.get(pk=pk)
        except Booking.DoesNotExist:
            raise Booking("Booking not found with the specified ID", code=status.HTTP_404_NOT_FOUND)


class RegistrationAPIView(APIView):

    @swagger_auto_schema(
        request_body=RegistrationSerializer,
        responses={
            201: "User registered successfully",
            400: "Invalid input",
        },
        operation_description="Register a new user."
    )
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'success': True,
                            'message': 'User created successfully'},
                             status=status.HTTP_201_CREATED)
        else:
            print("Validation errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(APIView):
    
    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: "Login successful",
            400: "Invalid credentials or input",
        },
        operation_description="Log in a user and generate access token."
    )
    
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'status': True,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'phone_number': user.phone_number,
                    'access_token': str(refresh.access_token),
                    'refresh_token': str(refresh),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'status': False, 'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'status': False, 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
