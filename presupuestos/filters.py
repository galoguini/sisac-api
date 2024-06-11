import django_filters
from django.db.models import Q
from datetime import datetime
from .models import Presupuesto

class PresupuestoFilter(django_filters.FilterSet):
    fecha_inicio = django_filters.CharFilter(method='filter_fecha_inicio')
    fecha_fin = django_filters.CharFilter(method='filter_fecha_fin')
    palabra_clave = django_filters.CharFilter(method='filter_by_keyword')
    remitido = django_filters.BooleanFilter(method='filter_remitido')

    class Meta:
        model = Presupuesto
        fields = ['fecha', 'remitido']

    def filter_remitido(self, queryset, name, value):
        if value is True:
            return queryset.filter(remitido=True)
        return queryset

    def filter_fecha_inicio(self, queryset, name, value):
        try:
            fecha_inicio = datetime.strptime(value, '%d-%m-%Y')
            filtered_queryset = [
                presupuesto for presupuesto in queryset
                if datetime.strptime(presupuesto.fecha, '%d-%m-%Y') >= fecha_inicio
            ]
            return queryset.model.objects.filter(pk__in=[presupuesto.pk for presupuesto in filtered_queryset])
        except ValueError:
            return queryset

    def filter_fecha_fin(self, queryset, name, value):
        try:
            fecha_fin = datetime.strptime(value, '%d-%m-%Y')
            filtered_queryset = [
                presupuesto for presupuesto in queryset
                if datetime.strptime(presupuesto.fecha, '%d-%m-%Y') <= fecha_fin
            ]
            return queryset.model.objects.filter(pk__in=[presupuesto.pk for presupuesto in filtered_queryset])
        except ValueError:
            return queryset

    def filter_by_keyword(self, queryset, name, value):
        return queryset.filter(
            Q(cliente__nombre_apellido__icontains=value) |
            Q(cliente__numero_identificacion__icontains=value) |
            Q(cliente__pais__icontains=value) |
            Q(cliente__provincia__icontains=value) |
            Q(cliente__localidad__icontains=value) |
            Q(cliente__domicilio__icontains=value) |
            Q(cliente__email__icontains=value) |
            Q(cliente__telefono__icontains=value) |
            Q(productos__producto__nombre__icontains=value) |
            Q(productos__producto__codigo_sku__icontains=value) |
            Q(productos__producto__codigo_barra__icontains=value) |
            Q(productos__producto__categoria__icontains=value) |
            Q(productos__producto__precio_venta_usd__icontains=value) |
            Q(productos__producto__observaciones__icontains=value) |
            Q(observaciones__icontains=value)
        )
