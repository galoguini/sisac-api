from django.urls import path
from .views import AgregarProductoView, ListadoProductosView, EliminarProductoView

urlpatterns = [
    path('agregar/', AgregarProductoView.as_view(), name='agregar_producto'),
    path('listado/', ListadoProductosView.as_view(), name='listado_productos'),
    path('eliminar/<int:pk>/', EliminarProductoView.as_view(), name='eliminar_producto'),
]