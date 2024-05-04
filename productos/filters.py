import django_filters 
from django.db.models import Q
from .models import Producto

class ProductoFilter(django_filters.FilterSet):
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')

    class Meta:
        model = Producto
        fields = []

    def filter_by_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(nombre__icontains=value) |
            Q(codigo_sku__icontains=value) |
            Q(codigo_barra__icontains=value) |
            Q(precio_venta_usd__icontains=value) |
            Q(observaciones__icontains=value)
        )