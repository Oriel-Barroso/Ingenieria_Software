from django.urls import path
from app1.views import view_notificaciones

urlpatterns = [
    path('mail/', view_notificaciones.send_email)
]