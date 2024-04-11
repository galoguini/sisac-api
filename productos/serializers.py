from rest_framework import serializers
from .models import Producto
from decimal import Decimal

class ProductoSerializer(serializers.ModelSerializer):
    precio_venta_usd = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = Producto
        fields = ['nombre', 'codigo_sku', 'codigo_barra', 'categoria', 
                'tasa_iva', 'unidad_medida', 'precio_venta_usd', 'stock', 'observaciones']

    def validate_precio_venta_usd(self, value):
        if value is not None:
            str_value = str(value)
            if str_value in ['0', '0.0', '0,0']:
                return None
            try:
                return Decimal(str_value.replace(',', '.'))
            except ValueError:
                raise serializers.ValidationError("precio_venta_usd debe ser un número decimal.")
        return value
    
    def validate(self, data):
        print(data)
        stock = data.get('stock')
        categoria = data.get('categoria')

        if categoria == 'PRODUCTO' and not stock:
            raise serializers.ValidationError({
                'stock': ['Tiene que agregar stock para un producto.']
            })
        
        if categoria != 'PRODUCTO' and stock is not None:
            raise serializers.ValidationError({
                'stock': ['Este campo obligatoriamente debe ser vacío.']
            })

        return data