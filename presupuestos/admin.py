from django.contrib import admin
from .models import Presupuesto, PresupuestoProducto

# Register your models here.

admin.site.register(Presupuesto)
admin.site.register(PresupuestoProducto)