from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from ..models import user_models
from ..services import user_services
from ..serializers.user_serializers import UserSerializer
from django.http import JsonResponse
from rest_framework import status


class UserService():
    def get_comment_fk():
        return False