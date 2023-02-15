from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from .models import User
from .serializers import UserRegistrationSerializer


class Home(TemplateView):
    template_name = "account/home.html"

class SignUp(CreateAPIView):
    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    
    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='account/signup.html')

    def post(self, request, *args, **kwargs):
        user = self.create(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('login'))