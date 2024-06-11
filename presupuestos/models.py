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
    observaciones = models.TextField(blank=True, null=True)
    remitido = models.BooleanField(default=False)
    numero_presupuesto = models.PositiveIntegerField(default=5000)

    def save(self, *args, **kwargs):
        if self.pk is None:
            ultimo_presupuesto = Presupuesto.objects.filter(usuario=self.usuario).order_by('-numero_presupuesto').first()
            if ultimo_presupuesto is not None:
                self.numero_presupuesto = ultimo_presupuesto.numero_presupuesto + 1
            else:
                self.numero_presupuesto = 5000
        super().save(*args, **kwargs)

class PresupuestoProducto(models.Model):
    presupuesto = models.ForeignKey(Presupuesto, related_name='productos', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=20, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)