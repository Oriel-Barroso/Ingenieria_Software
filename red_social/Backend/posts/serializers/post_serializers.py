from rest_framework import serializers
from ..models.post_models import Post
from users.serializers.user_serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Post
        fields = ['title', 'photo', 'created_at', 'published', 'user']
