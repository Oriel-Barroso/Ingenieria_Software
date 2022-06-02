from django.conf import settings
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from red_social import settings 

# Create your views here.
@csrf_exempt
@api_view(('POST',))
def send_email(request):
    subject = "Prueba"
    message = "Esto es una prueba, de nuevo"
    user_email = settings.EMAIL_HOST_USER
    if subject and message and user_email:
        try:
            email = EmailMessage(subject, message, user_email, to=['ORIEL_GOLD97@outlook.com','o.barroso@alumno.um.edu.ar'])
            email.send(fail_silently=False)
            return HttpResponse(f"Mail enviado (creo){user_email}",status=200)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')