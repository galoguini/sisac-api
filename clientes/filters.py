import django_filters 
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    class Meta:
        model = Cliente
        fields = ['nombre_apellido', 'numero_identificacion', 'pais', 'provincia', 'localidad', 'email', 'telefono']