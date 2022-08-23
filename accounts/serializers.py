from dataclasses import field, fields
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model= Staff
        fields=('id','name','age','gender','department','dob')

    """def create(self, validated_data):
        staff = Staff.objects.create_user(validated_data['name'], validated_data['age'])

        return staff"""
