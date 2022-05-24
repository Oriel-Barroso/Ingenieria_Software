from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from app1.models import user_models
from app1.services import user_services
from app1.serializers.user_serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status

# class Auth():
#     @csrf_exempt 
#     @api_view(('POST',))
#     def registro(req):
#         data = JSONParser().parse(req)

#         isEmpty = user_services.UserService.get_comment_fk()
#         if(not isEmpty):
#             return HttpResponse("Ejemplo de error", status=500)

#         user = user_models.Users.objects.create_user(first_name=data['firstname'],
#                                         last_name=data['lastname'],
#                                         email=data['email'],
#                                         username=data['username'],
#                                         password=data['password'],
#                                     )
#         user.save()
#         return HttpResponse(user, status=200)


class Auth():

    @csrf_exempt 
    @api_view(('POST',))
    def registro(req):

        data = JSONParser().parse(req)
        serialazer = UserSerializer(data=data)
        print("hola",data)
        if serialazer.is_valid():

            serialazer.save()

            return JsonResponse(serialazer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serialazer.errors, status=status.HTTP_400_BAD_REQUEST)

            