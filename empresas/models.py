from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Empresa(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    nombre_empresa = models.CharField(max_length=100)
    nombre_fantasia = models.CharField(max_length=100, blank=True, null=True)
    categoria_fiscal = models.CharField(max_length=25)
    tipo_cuenta = models.CharField(max_length=20)
    cuit = models.CharField(max_length=20)
    nro_ingresos_brutos = models.CharField(max_length=20)
    fecha_inicio_actividad = models.CharField(max_length=10)
    direccion = models.CharField(max_length=100)
    provincia = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    CBU = models.CharField(max_length=22, blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)

    def __str__(self):
        return self.nombre_empresa