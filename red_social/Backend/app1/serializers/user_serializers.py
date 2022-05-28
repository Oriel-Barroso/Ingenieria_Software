from rest_framework import serializers
from app1.models.user_models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (  
                    'first_name',
                    'last_name',
                    'email',
                    'username',
                    'password'
                  )


