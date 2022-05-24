from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from app1.models import user_models
from app1.serializers import user_serializers

class Users():
    @csrf_exempt 
    @api_view(('GET',))
    def get_user(req, username):
        user = user_models.Users.objects.filter(username=username).values()
        print(user, 'PRINT DEL USUARIO')

        response = user_serializers.UsersSerializer(user)
        return HttpResponse(response, status=200)

    @csrf_exempt 
    @api_view(('GET',))
    def get_all_users(req):
        user = user_models.Users.objects.all().values()
        return HttpResponse(user, status=200)