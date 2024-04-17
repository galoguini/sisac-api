from django.urls import path
from .views import ListarPresupuestosView, AgregarPresupuestoView, EditarPresupuestoView

urlpatterns = [
    path('listar/', ListarPresupuestosView.as_view(), name='listar_presupuestos'),
    path('agregar/', AgregarPresupuestoView.as_view(), name='agregar_presupuesto'),
    path('editar/<int:pk>/', EditarPresupuestoView.as_view(), name='editar_presupuesto'),
]