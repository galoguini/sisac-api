import django_filters
from django.db.models import Q
from .models import Presupuesto
from django_countries import countries

class PresupuestoFilter(django_filters.FilterSet):
    fecha = django_filters.DateFromToRangeFilter()
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')

    class Meta:
        model = Presupuesto
        fields = ['fecha']

    def filter_by_keyword(self, queryset, name, value):
        for country_code, country_name in countries:
            if country_name.lower() == value.lower():
                value = country_code
                break

        return queryset.filter(
            Q(cliente__nombre_apellido__icontains=value) |
            Q(cliente__numero_identificacion__icontains=value) |
            Q(cliente__pais__icontains=value) |
            Q(cliente__provincia__icontains=value) |
            Q(cliente__localidad__icontains=value) |
            Q(cliente__domicilio__icontains=value) |
            Q(cliente__email__icontains=value) |
            Q(cliente__telefono__icontains=value) |
            Q(producto__nombre__icontains=value) |
            Q(producto__codigo_sku__icontains=value) |
            Q(producto__codigo_barra__icontains=value) |
            Q(producto__categoria__icontains=value) |
            Q(producto__precio_venta_usd__icontains=value) |
            Q(producto__observaciones__icontains=value) |
            Q(observaciones__icontains=value)
        )