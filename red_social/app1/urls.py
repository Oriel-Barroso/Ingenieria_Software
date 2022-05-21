from django.urls import path
from app1 import views


urlpatterns = [
    path('registro/', views.registro),
    path('get_user/', views.get_user),
    path('get_all_users/', views.get_all_users),
]