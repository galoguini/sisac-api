from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre_apellido', 'tipo_identificacion', 
                'numero_identificacion', 'otro_identificacion', 
                'condicion_iva', 'pais', 'provincia', 'localidad', 
                'domicilio', 'email', 'telefono']

    def validate(self, data):
        tipo_identificacion = data.get('tipo_identificacion')
        otro_identificacion = data.get('otro_identificacion')

        if tipo_identificacion == 'OTRO' and not otro_identificacion:
            raise serializers.ValidationError({
                'otro_identificacion': ['Este campo es requerido.']
            })
        
        if tipo_identificacion != 'OTRO' and otro_identificacion:
            raise serializers.ValidationError({
                'otro_identificacion': ['Este campo obligatoriamente debe ser vacío.']
            })

        return data