from django.contrib import admin
from django.urls import path, include
from .views import Home, SignUp


app_name = "account"

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('signup', SignUp.as_view(), name='signup'),
]