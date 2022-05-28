from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from app1.models import user_models
from app1.services import user_services
from app1.serializers.user_serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status



class Auth():

    @csrf_exempt 
    @api_view(('POST',))
    def registro(req):

        res = JSONParser().parse(req)
        serialazer = UserSerializer(data=res)
        
        if serialazer.is_valid():
            serialazer.save()
            return JsonResponse(serialazer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    @csrf_exempt 
    @api_view(('POST',))
    def get_user(request):

        users = JSONParser().parse(request) 

        user = user_models.Users.objects.get(username=users['username'], password=users['password'])

        response = UserSerializer(user)
        
        return JsonResponse(response.data['username'] ,safe= False, status=200)

        
