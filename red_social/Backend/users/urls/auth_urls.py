from django.urls import path
from ..views import auth_views

urlpatterns = [
    path('registro/', auth_views.Auth.registro),
    path('log_user/', auth_views.Auth.log_user),
]