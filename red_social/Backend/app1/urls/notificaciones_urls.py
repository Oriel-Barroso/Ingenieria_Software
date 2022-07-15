from django.urls import path
from app1.views import view_notificaciones

urlpatterns = [
    path('mail/<str:asunto>/<str:mensaje>/<str:email_destino>/', view_notificaciones.send_email)
]