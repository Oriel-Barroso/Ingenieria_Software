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
<<<<<<< HEAD
        data = JSONParser().parse(req)
        serialazer = UserSerializer(data=data)
        print("hola",data)
=======

        res = JSONParser().parse(req)
        serialazer = UserSerializer(data=res)
        
>>>>>>> login
        if serialazer.is_valid():
            serialazer.save()
            return JsonResponse(serialazer.data, status=status.HTTP_201_CREATED)

        return JsonResponse(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    @csrf_exempt 
<<<<<<< HEAD
    @api_view(('POST', ))
    def log_user(req):
        if req.method == 'POST':
            data = JSONParser().parse(req)
            username = data['username']
            password = data['password']
            if user_models.User.objects.filter(username=username, password=password).exists():
                user = user_models.User.objects.get(username=username)
                serializer = UserSerializer(user)
                return JsonResponse(serializer.data, status=200, safe=False)
            return JsonResponse('No existe', safe=False, status=400)
=======
    @api_view(('POST',))
    def get_user(request):

        users = JSONParser().parse(request) 

        user = user_models.Users.objects.get(username=users['username'], password=users['password'])

        response = UserSerializer(user)
        
        return JsonResponse(response.data ,safe= False, status=200)

        
>>>>>>> login
