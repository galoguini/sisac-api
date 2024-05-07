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
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    observaciones = models.TextField(blank=True, null=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    numero_presupuesto = models.PositiveIntegerField(default=5000)

    def save(self, *args, **kwargs):
        if self.pk is None:
            ultimo_presupuesto = Presupuesto.objects.all().order_by('-numero_presupuesto').first()
            if ultimo_presupuesto is not None:
                self.numero_presupuesto = ultimo_presupuesto.numero_presupuesto + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f'Presupuesto numero {self.numero_presupuesto} de {self.cliente.nombre_apellido}'