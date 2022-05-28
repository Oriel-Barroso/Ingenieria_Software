from rest_framework import serializers
from ..models.user_models import Users


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = (  'user_ptr',
                    'first_name',
                    'last_name',
                    'email',
                    'username',
                    'password'
                  )


