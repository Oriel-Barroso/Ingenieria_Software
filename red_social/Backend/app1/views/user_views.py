import email
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from app1.models import user_models
from app1.serializers.user_serializers import UserSerializer


class Users():
    @csrf_exempt 
    @api_view(('GET',))
    def get_user(req, username):
        user = user_models.Users.objects.filter(username=username).values()
        print(user, 'PRINT DEL USUARIO')
        return Response(user[0]["email"], status=200)


    @csrf_exempt 
    @api_view(('GET',))
    def get_all_users(req):
        user = user_models.Users.objects.all().values()
        return Response(user, status=200)

  
