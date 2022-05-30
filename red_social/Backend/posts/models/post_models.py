from django.db import models
from django.db.models import SET_NULL
from users.models.user_models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='posts/img/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=SET_NULL, null=True)
