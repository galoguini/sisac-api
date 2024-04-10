from django.urls import path
from .views import AgregarProductoView, ListadoProductosView

urlpatterns = [
    path('agregar/', AgregarProductoView.as_view(), name='agregar_producto'),
    path('listado/', ListadoProductosView.as_view(), name='listado_productos'),
]