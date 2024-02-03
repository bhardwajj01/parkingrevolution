from rest_framework import serializers
from rest_framework.exceptions import ValidationError
import re
from .models import City, Location, ParkingSpot, User, Booking, CarDetail
from django.db.models import Q
from django.contrib.auth.hashers import make_password, check_password



class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class ParkingSpotSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParkingSpot
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError('Password must be at least 8 characters long.')
        
        if not re.search(r'[a-zA-Z]', password):
            raise serializers.ValidationError('Password must contain at least one alphabet.')
        
        if not re.search(r'\d', password):
            raise serializers.ValidationError('Password must contain at least one digit.')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise serializers.ValidationError('Password must contain at least one special character.')
        
        return password

    def create(self, validated_data):
        email = validated_data['email']
        phone_number = validated_data['phone_number']

        if User.objects.filter(email=email).exists():
            raise ValidationError({'email': ['User with this email already exists.']})
        
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError({'phone_number': ['User with this phone_number already exists.']})

        user = User.objects.create(
            email=email,
            phone_number=phone_number,
            username=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.password = make_password(validated_data['password'])  
        user.save()
        return user




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Use get to directly retrieve the user based on email or phone number
        user = User.objects.filter(Q(email=username) | Q(phone_number=username)).first()

        if user:
            
            # Check the password manually
            if check_password(password, user.password):
                data['user'] = user
            else:
                raise serializers.ValidationError('Authentication failed. Please try again.')
        else:
            raise serializers.ValidationError('User with this email or phone number does not exist.')
        
        return data
    
