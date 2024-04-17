from rest_framework import serializers
from .models import Presupuesto
from clientes.models import Cliente
from productos.models import Producto  # Importa tu modelo Producto

class PresupuestoSerializer(serializers.ModelSerializer):
    cliente = serializers.SlugRelatedField(
        slug_field='nombre_apellido',  # El campo que quieres mostrar
        queryset=Cliente.objects.all(),  # Esto se reemplazará en __init__
    )
    producto = serializers.SlugRelatedField(  # Nuevo campo
        slug_field='nombre',  # El campo que quieres mostrar
        queryset=Producto.objects.all(),  # Esto se reemplazará en __init__
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and hasattr(request, "user"):
            self.fields['cliente'].queryset = Cliente.objects.filter(usuario=request.user)
            self.fields['producto'].queryset = Producto.objects.filter(usuario=request.user)  # Filtra los productos

    class Meta:
        model = Presupuesto
        fields = ['cliente', 'fecha', 'vencimiento', 'moneda', 'observaciones', 'producto']