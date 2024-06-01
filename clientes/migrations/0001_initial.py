# Generated by Django 5.0.3 on 2024-05-28 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_apellido', models.CharField(max_length=100)),
                ('tipo_identificacion', models.CharField(max_length=15)),
                ('numero_identificacion', models.CharField(max_length=40)),
                ('otro_identificacion', models.CharField(blank=True, max_length=40, null=True)),
                ('condicion_iva', models.CharField(max_length=30)),
                ('pais', models.CharField(max_length=100)),
                ('provincia', models.CharField(blank=True, max_length=100, null=True)),
                ('localidad', models.CharField(blank=True, max_length=100, null=True)),
                ('domicilio', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('telefono', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
