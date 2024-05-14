from django.urls import path
from .views import ListarPresupuestosView, AgregarPresupuestoView, EditarPresupuestoView, EliminarPresupuestoView, DetallePresupuestoView, ImpriPresupuestoView

urlpatterns = [
    path('listar/', ListarPresupuestosView.as_view(), name='listar_presupuestos'),
    path('agregar/', AgregarPresupuestoView.as_view(), name='agregar_presupuesto'),
    path('editar/<int:pk>/', EditarPresupuestoView.as_view(), name='editar_presupuesto'),
    path('eliminar/<int:numero_presupuesto>/', EliminarPresupuestoView.as_view(), name='eliminar_presupuesto'),
    path('detalle/<int:numero_presupuesto>/', DetallePresupuestoView.as_view(), name='detalle_presupuesto'),
    path('imprimir/<int:numero_presupuesto>/', ImpriPresupuestoView.as_view(), name='imprimir_presupuesto'),
]