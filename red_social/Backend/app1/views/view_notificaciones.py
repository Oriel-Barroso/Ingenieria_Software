from django.conf import settings
from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from red_social import settings 

# Create your views here.

#Asunto: Tema a tratar -- Mensaje: Texto a enviar -- user_email: Es el mail que utilizaria el sistema
#Email_destino: Destino con el que se quiere comunicar
@csrf_exempt
@api_view(('POST',))
def send_email(request, asunto, mensaje, email_destino):
    user_email = settings.EMAIL_HOST_USER
    if asunto and mensaje and user_email:
        try:
            email = EmailMessage(asunto, mensaje, user_email, to=[email_destino])
            email.send(fail_silently=False)
            return HttpResponse("Mail enviado",status=200)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')