from django.urls import path
from app1.views import user_views, auth_views

urlpatterns = [
    path('get_user/', auth_views.Auth.get_user),
    path('get_all_users/', user_views.Users.get_all_users),
]