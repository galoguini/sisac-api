from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nombre_apellido', 'tipo_identificacion', 
                'numero_identificacion', 'otro_identificacion', 
                'condicion_iva', 'pais', 'provincia', 'localidad', 
                'domicilio', 'email', 'telefono']