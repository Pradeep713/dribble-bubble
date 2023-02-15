from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers, validators
from rest_framework_simplejwt.tokens import RefreshToken


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[
        validators.UniqueValidator(
            queryset=User.objects.all(),
            message="Sorry, This username is taken."
        )]
    )
    password = serializers.CharField(
        max_length = 128,
        write_only = True,
        required = True,
        style = {
            'input_type' : 'password',
            'placeholder' : 'password'
        }
    )
    role = serializers.ChoiceField(choices=User.USER_TYPE)
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

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 128, write_only = True)