from django.db import models
from django.contrib.auth.models import User

class Usuario(User):
    celular = models.CharField(max_length=40, blank=True, null=True)
    empresa_seleccionada = models.ForeignKey('empresas.Empresa', on_delete=models.SET_NULL, blank=True, null=True, related_name='usuarios_seleccionados')