from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import JsonResponse
from app1.models import user_models
from app1.serializers.user_serializers import UserSerializer

class Users():
   
    @csrf_exempt 
    @api_view(('GET',))
    def get_all_users(req):
<<<<<<< HEAD
        user = user_models.Users.objects.all().values()
        return HttpResponse(user, status=200)
    
=======
        user = user_models.Users.objects.all()
        response = UserSerializer(user, many = True)
        return JsonResponse(response.data, safe=False, status=200)
>>>>>>> login


