from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from clientes.models import Cliente
from productos.models import Producto
from empresas.models import Empresa

class Presupuesto(models.Model):
    MONEDAS = [
        ('USD', 'Dólares'),
        ('ARS', 'Pesos Argentinos'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, blank=True, null=True)
    fecha = models.DateField(default=timezone.now)
    vencimiento = models.DateField(default=timezone.now)
    moneda = models.CharField(max_length=3, choices=MONEDAS)
    observaciones = models.TextField(blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.empresa:
            self.empresa = self.usuario.empresa_seleccionada
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Presupuesto para {self.cliente} en {self.moneda}'