from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre', 'codigo_sku', 'codigo_barra', 'categoria', 
                'tasa_iva', 'unidad_medida', 'actividad', 
                'precio_venta_usd', 'observaciones']