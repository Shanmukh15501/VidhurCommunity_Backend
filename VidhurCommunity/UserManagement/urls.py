"""VidhurCommunity URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView
from rest_framework_simplejwt.views import TokenBlacklistView




urlpatterns = [
    
    path('v1/login', LoginUserView.as_view(), name='login-user'),
    path('v1/iamuser/', IamUserDetailsView.as_view(), name='login-user'),
    path('v1/api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('v1/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('v1/api/token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),





]
