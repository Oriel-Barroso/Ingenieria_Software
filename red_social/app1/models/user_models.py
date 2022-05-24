from django.db import models
from django.contrib.auth.models import User

class Users(User):
    comentario_fk = models.CharField(max_length=70)
    