from django_countries import countries
from django.db.models import Q
import django_filters 
from .models import Cliente

class ClienteFilter(django_filters.FilterSet):
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')

    class Meta:
        model = Cliente
        fields = []

    def filter_by_keyword(self, queryset, name, value):
        for country_code, country_name in countries:
            if country_name.lower() == value.lower():
                value = country_code
                break

        return queryset.filter(
            Q(nombre_apellido__icontains=value) |
            Q(numero_identificacion__icontains=value) |
            Q(pais__icontains=value) |
            Q(provincia__icontains=value) |
            Q(localidad__icontains=value) |
            Q(email__icontains=value) |
            Q(telefono__icontains=value)
        )