from django.urls import path
from app1.views import auth_views

urlpatterns = [
    path('registro/', auth_views.Auth.registro),
]