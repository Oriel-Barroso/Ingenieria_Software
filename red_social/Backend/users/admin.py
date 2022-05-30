from django.contrib import admin
from users.models import user_models

# le estamos dando acseso al administrador para que pueda editar y crear modelos de UserProfile
admin.site.register(user_models.Users)
