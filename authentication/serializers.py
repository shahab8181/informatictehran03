from rest_framework import serializers
from .models import User, Otp


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name', 'phone_number', 'password'
        ]



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'phone_number', 'password'
        ]



class VerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Otp
        fields = [
            'phone_number', 'code'
        ]
        
