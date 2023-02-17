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

# class SignUp(CreateAPIView):
#     model = User
#     permission_classes = [
#         permissions.AllowAny
#     ]
#     serializer_class = UserRegistrationSerializer
#     queryset = User.objects.all()
#     renderer_classes = [JSONRenderer, TemplateHTMLRenderer]
#     template_name = 'users/signup.html'

    
#     # def create(self, request, *args, **kwargs):
#     #     return super().create(request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         serializer = UserRegistrationSerializer()
#         return Response({'serializer':serializer})

#     def post(self, request, *args, **kwargs):
#         user = self.create(request, *args, **kwargs)
#         return HttpResponseRedirect(reverse('login'))

class CustomSignUp(RegisterView):
    serializer_class = UserRegistrationSerializer