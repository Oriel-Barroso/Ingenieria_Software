from rest_framework.viewsets import ModelViewSet
from ..serializers.post_serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from ..models.post_models import Post


class PostAPIViewSet(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    filter_backends = [DjangoFilterBackend]
