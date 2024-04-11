from django.db import models
from usuarios.models import Usuario

# Create your models here.

class Producto(models.Model):
    CATEGORIAS = [
    ('SERVICIO', 'SERVICIO'),
    ('PRODUCTO', 'PRODUCTO'),
    ('OTRO', 'OTRO'),
    ]

    TASA = [
    ('IVA EXENTO', 'IVA EXENTO'),
    ('IVA NO GRAVADO', 'IVA NO GRAVADO'),
    ("0.0", 'IVA 0%'),
    ("2.5", 'IVA 2.5%'),
    ("5.0", 'IVA 5%'),
    ("10.5", 'IVA 10.5%'),
    ("21.0", 'IVA 21%'),
    ("27.0", 'IVA 27%'),
    ]

    MEDIDA = [
    ('UNIDAD', 'UNIDAD'),
    ('KILO', 'KILO'),
    ('LITRO', 'LITRO'),
    ('METRO', 'METRO'),
    ('OTRO', 'OTRO'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    codigo_sku = models.CharField(max_length=50, null=True, blank=True)
    codigo_barra = models.CharField(max_length=50, null=True, blank=True)
    categoria = models.CharField(max_length=10, choices=CATEGORIAS)
    tasa_iva = models.CharField(max_length=17, choices=TASA)
    unidad_medida = models.CharField(max_length=10, choices=MEDIDA)
    precio_venta_usd = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre