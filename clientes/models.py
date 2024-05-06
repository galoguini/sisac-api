from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Cliente(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_apellido = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=15)
    numero_identificacion = models.CharField(max_length=40)
    otro_identificacion = models.CharField(max_length=40, null=True, blank=True)
    condicion_iva = models.CharField(max_length=30)
    pais = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100, null=True, blank=True)
    localidad = models.CharField(max_length=100, null=True, blank=True)
    domicilio = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f"{self.tipo_identificacion} {self.numero_identificacion}"