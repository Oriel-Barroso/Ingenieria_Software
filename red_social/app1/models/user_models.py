from django.db import models
from django.contrib.auth.models import User


class Users(User, models.Model):
    comentario = models.CharField(max_length=70)
    pass
    
    
  

    
         