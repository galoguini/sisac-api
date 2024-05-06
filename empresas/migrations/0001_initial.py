# Generated by Django 5.0.3 on 2024-05-06 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_empresa', models.CharField(max_length=100)),
                ('nombre_fantasia', models.CharField(blank=True, max_length=100, null=True)),
                ('categoria_fiscal', models.CharField(max_length=25)),
                ('tipo_cuenta', models.CharField(max_length=20)),
                ('cuit', models.CharField(max_length=20)),
                ('nro_ingresos_brutos', models.CharField(max_length=20)),
                ('fecha_inicio_actividad', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=50)),
                ('localidad', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('CBU', models.CharField(blank=True, max_length=22, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
            ],
        ),
    ]
