from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    celular = models.CharField(max_length=40)
    empresa_seleccionada = models.ForeignKey('empresas.Empresa', on_delete=models.SET_NULL, blank=True, null=True, related_name='usuarios_seleccionados')