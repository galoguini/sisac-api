# from rest_framework import serializers
# from .models import Presupuesto, PresupuestoProducto
# from clientes.models import Cliente
# from productos.models import Producto  
# from clientes.serializers import ClienteSerializer
# from productos.serializers import ProductoSerializer

# class ProductoPresupuestoSerializer(serializers.ModelSerializer):
#     producto = ProductoSerializer(read_only=True)
#     producto_id = serializers.IntegerField(write_only=True)

#     class Meta:
#         model = PresupuestoProducto
#         fields = ['producto', 'producto_id', 'cantidad', 'precio']

#     def to_representation(self, instance):
#         representation = super().to_representation(instance)
#         representation['producto'] = ProductoSerializer(instance.producto).data
#         return representation

# class PresupuestoSerializer(serializers.ModelSerializer):
#     cliente = ClienteSerializer(read_only=True)
#     productos = ProductoPresupuestoSerializer(many=True)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         request = self.context.get('request')
#         if request and hasattr(request, "user"):
#             self.fields['cliente'].queryset = Cliente.objects.filter(usuario=request.user)
#             self.fields['productos'].queryset = PresupuestoProducto.objects.filter(presupuesto__usuario=request.user)

#     class Meta:
#         model = Presupuesto
#         fields = ['id', 'cliente', 'fecha', 'vencimiento', 'moneda', 'productos', 'observaciones', 'numero_presupuesto']

#     def create(self, validated_data):
#         productos_data = validated_data.pop('productos')
#         presupuesto = Presupuesto.objects.create(**validated_data)
#         for producto_data in productos_data:
#             producto_id = producto_data.pop('producto_id')
#             producto = Producto.objects.get(id=producto_id)
#             PresupuestoProducto.objects.create(presupuesto=presupuesto, producto=producto, **producto_data)
#         return presupuesto


# serializers.py
# from rest_framework import serializers
# from .models import Presupuesto, PresupuestoProducto
# from productos.models import Producto

# class PresupuestoProductoSerializer(serializers.ModelSerializer):
#     producto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all())

#     class Meta:
#         model = PresupuestoProducto
#         fields = ['id' ,'producto', 'cantidad', 'precio']

# class PresupuestoSerializer(serializers.ModelSerializer):
#     productos = PresupuestoProductoSerializer(source='presupuestoproducto_set', many=True)

#     class Meta:
#         model = Presupuesto
#         fields = ['id', 'cliente', 'fecha', 'vencimiento', 'moneda', 'observaciones', 'productos']

#     def create(self, validated_data):
#         productos_data = validated_data.pop('productos')
#         presupuesto = Presupuesto.objects.create(**validated_data)
#         for producto_data in productos_data:
#             producto_id = producto_data.pop('producto').id  # Esto ya es el ID del producto
#             producto = Producto.objects.get(id=producto_id)
#             PresupuestoProducto.objects.create(presupuesto=presupuesto, producto=producto, **producto_data)
#         return presupuesto


# class PresupuestoProductoSerializer(serializers.ModelSerializer):
#     producto = serializers.SlugRelatedField(
#         slug_field='nombre',
#         queryset=Producto.objects.all()
#     )

#     class Meta:
#         model = PresupuestoProducto
#         fields = ['producto', 'cantidad', 'precio']



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

# class PresupuestoProductoSerializer(serializers.ModelSerializer):
#     producto = serializers.SlugRelatedField(slug_field='nombre', queryset=Producto.objects.all(),)

#     class Meta:
#         model = PresupuestoProducto
#         fields = ['producto', 'cantidad', 'precio']

class PresupuestoSerializer(serializers.ModelSerializer):
    # cliente = serializers.SlugRelatedField(
    #     slug_field='nombre_apellido',  
    #     queryset=Cliente.objects.all(),  
    # )
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
        fields = ['id', 'cliente', 'fecha', 'vencimiento', 'moneda', 'observaciones', 'numero_presupuesto', 'productos']

