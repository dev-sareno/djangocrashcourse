from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.ApiMainView.as_view(), name='api-main'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]
