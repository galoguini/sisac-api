from rest_framework import serializers
from .models import Usuario

class SendEmailSerializer(serializers.Serializer):
    destinatario = serializers.EmailField()
    asunto = serializers.CharField(max_length=255)
    mensaje = serializers.CharField()
    pdf = serializers.FileField()

class UpdateSMTPInfoSerializer(serializers.ModelSerializer):
    email_smtp = serializers.EmailField(required=True)
    smtp_app_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Usuario
        fields = ['email_smtp', 'smtp_app_password']

    def update(self, instance, validated_data):
        instance.email_smtp = validated_data.get('email_smtp', instance.email_smtp)
        if 'smtp_app_password' in validated_data:
            instance.smtp_app_password = validated_data['smtp_app_password']
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'first_name', 'last_name', 'email', 'celular', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        usuario = Usuario.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
            email=validated_data.get('email'),
            password=validated_data['password'],
            celular=validated_data.get('celular'),
        )
        return usuario