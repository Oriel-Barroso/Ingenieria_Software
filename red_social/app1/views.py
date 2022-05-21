import email
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

# Create your views here.
@csrf_exempt 
@api_view(('POST',))
def registro(req):
    data = JSONParser().parse(req)
    # print(data['firstname'])
    # print(data['lastname'])
    # print(data['username'])
    # print(data['email'])
    # print(data['password'])
    user = User.objects.create_user(first_name=data['firstname'],
                               last_name=data['lastname'],
                               email=data['email'],
                               username=data['username'],
                               password=data['password']
                              )
    user.save()
    return HttpResponse(user, status=200)