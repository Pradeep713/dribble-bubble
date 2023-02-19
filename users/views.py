from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from dj_rest_auth.registration.views import RegisterView

from .models import User
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserSerializer


class Home(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomSignUp(RegisterView):
    serializer_class = UserRegistrationSerializer

    def get_serializer_class(self):
        return UserRegistrationSerializer