from django.urls import path
from .views import AltaClienteView, ListadoClientesView

urlpatterns = [
    path('alta/', AltaClienteView.as_view(), name='alta_clientes'),
    path('listado/', ListadoClientesView.as_view(), name='listado_clientes'),
]