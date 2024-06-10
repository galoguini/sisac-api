from django.db.models import Q
import django_filters 
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')

    class Meta:
        model = Cliente
        fields = []

    def filter_by_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(nombre_apellido__icontains=value) |
            Q(numero_identificacion__icontains=value) |
            Q(pais__icontains=value) |
            Q(provincia__icontains=value) |
            Q(localidad__icontains=value) |
            Q(email__icontains=value) |
            Q(telefono__icontains=value) |
            Q(domicilio__icontains=value) |
            Q(condicion_iva__icontains=value) |
            Q(tipo_identificacion__icontains=value) |
            Q(otro_identificacion__icontains=value) 
        )