"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dj_rest_auth.registration.views import RegisterView
from allauth.account.views import confirm_email
from users.serializers import UserRegistrationSerializer
from users.views import CustomSignUp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include("users.urls")),
    path('users/', include("rest_framework.urls")),
    path('users/dj-rest-auth/', include("dj_rest_auth.urls")),
    path('users/dj-rest-auth/registration/', CustomSignUp.as_view(), name = 'rest_register'),
    path('users/dj-rest-auth/registration/', include("dj_rest_auth.registration.urls")),
]
