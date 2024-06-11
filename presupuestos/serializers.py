from rest_framework import serializers
from .models import Presupuesto, Cliente, Producto, PresupuestoProducto
from django.core.exceptions import ObjectDoesNotExist

class ClienteField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre_apellido

    def to_internal_value(self, data):
        try:
            cliente = Cliente.objects.get(id=int(data))
            return cliente
        except (ValueError, ObjectDoesNotExist, TypeError):
            try:
                cliente = Cliente.objects.get(nombre_apellido=data)
                return cliente
            except Cliente.DoesNotExist:
                raise serializers.ValidationError("Cliente con este ID o nombre no existe")

class ProductoField(serializers.RelatedField):
    def to_representation(self, value):
        return value.nombre

    def to_internal_value(self, data):
        try:
            producto = Producto.objects.get(id=int(data))
            return producto
        except (ValueError, ObjectDoesNotExist, TypeError):
            try:
                producto = Producto.objects.get(nombre=data)
                return producto
            except Producto.DoesNotExist:
                raise serializers.ValidationError("Producto con este ID o nombre no existe")
            

class PresupuestoProductoSerializer(serializers.ModelSerializer):
    producto = ProductoField(queryset=Producto.objects.all())

    class Meta:
        model = PresupuestoProducto
        fields = ['producto', 'cantidad', 'precio', 'descripcion']

class PresupuestoSerializer(serializers.ModelSerializer):
    cliente = ClienteField(queryset=Cliente.objects.all())
    productos = PresupuestoProductoSerializer(many=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            self.fields['cliente'].queryset = Cliente.objects.filter(usuario=request.user)
            self.fields['productos'].child.fields['producto'].queryset = Producto.objects.filter(usuario=request.user)

    def create(self, validated_data):
        productos_data = validated_data.pop('productos')
        presupuesto = Presupuesto.objects.create(**validated_data)
        for producto_data in productos_data:
            PresupuestoProducto.objects.create(presupuesto=presupuesto, **producto_data)
        return presupuesto

    class Meta:
        model = Presupuesto
        fields = ['id', 'cliente', 'fecha', 'vencimiento', 'moneda', 'observaciones', 'remitido', 'numero_presupuesto', 'productos']

