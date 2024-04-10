from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
    ('SERVICIOS', 'SERVICIOS'),
    ('PRODUCTOS', 'PRODUCTOS'),
    ('OTRO', 'OTRO'),
    ]

    TASA = [
    (0, '0%'),
    (10.5, '10.5%'),
    (21, 'IVA 21%'),
    (27, '27%'),
    ]

    MEDIDA = [
    ('UNIDAD', 'UNIDAD'),
    ('KILO', 'KILO'),
    ('LITRO', 'LITRO'),
    ('METRO', 'METRO'),
    ('OTRO', 'OTRO'),
    ]

    # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    codigo_sku = models.CharField(max_length=50, null=True, blank=True)
    codigo_barra = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS, default='PRODUCTOS')
    tasa_iva = models.DecimalField(max_digits=5, decimal_places=2, choices=TASA, default=21)
    unidad_medida = models.CharField(max_length=10, choices=MEDIDA, default='UNIDAD')
    # cuenta_contable = models.CharField(max_length=50, null=True, blank=True)
    actividad = models.CharField(max_length=100, null=True, blank=True)
    # formulario_iva2002 = models.CharField(max_length=100, null=True, blank=True) # categoria formulario iva 2002
    precio_venta_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre