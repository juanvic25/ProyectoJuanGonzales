from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='profile')
    telefono = models.CharField(max_length=25, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True)
    foto = models.ImageField(upload_to='fotos_user', null=True, blank=True)