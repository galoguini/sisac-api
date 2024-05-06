from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from clientes.models import Cliente
from productos.models import Producto
from empresas.models import Empresa

class Presupuesto(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    fecha = models.CharField(max_length=10)
    vencimiento = models.CharField(max_length=10)
    moneda = models.CharField(max_length=3)
    cantidad = models.PositiveIntegerField(default=1)
    precio = models.DecimalField(max_digits=15, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return f'Presupuesto para {self.cliente} en {self.moneda}'