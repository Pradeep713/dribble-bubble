import logging

from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers, validators
from rest_framework_simplejwt.tokens import RefreshToken
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from dj_rest_auth.models import api_settings


class UserRegistrationSerializer(RegisterSerializer):
    role = serializers.ChoiceField(
        choices=User.USER_TYPE,
    )
    username = None
    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'role',
        )
        extra_kwargs = {'password' : {'write_only': True} }

    def create(self, validated_data):
        auth_user = User.objects.create_user(**validated_data)
        return auth_user

    def get_cleaned_data(self):
        data =  super().get_cleaned_data()
        data['role'] = self.validated_data.get('role', 3)
        return data


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128, write_only = True)
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'role',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'role',
        ]

