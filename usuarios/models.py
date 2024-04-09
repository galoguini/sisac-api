from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Usuario(User):
    empresa_entidad = models.CharField(max_length=100)
    celular = models.CharField(max_length=40)