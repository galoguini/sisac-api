from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Producto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    codigo_sku = models.CharField(max_length=50, null=True, blank=True)
    codigo_barra = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.CharField(max_length=10)
    tasa_iva = models.CharField(max_length=17)
    unidad_medida = models.CharField(max_length=10)
    precio_venta_usd = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    def get_id(self):
        return self.id