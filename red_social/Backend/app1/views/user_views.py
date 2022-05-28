
from http.client import responses
import re
from urllib import request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from app1.models import user_models
from app1.serializers.user_serializers import UserSerializer


class Users():
    @csrf_exempt 
    @api_view(('GET', 'POST'))
    def get_user(request):
        users = JSONParser().parse(request) 
        user = user_models.Users.objects.get(username=users['username'], password=users['password'])
        response = UserSerializer(user)
        
        return JsonResponse(response.data ,safe= False, status=200)


    @csrf_exempt 
    @api_view(('GET',))
    def get_all_users(req):
        user = user_models.Users.objects.all().values()
        return Response(user, status=200)

  
