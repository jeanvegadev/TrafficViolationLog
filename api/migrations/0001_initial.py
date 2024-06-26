# Generated by Django 4.2.11 on 2024-04-25 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('numero_identificatorio', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa_patente', models.CharField(max_length=6)),
                ('marca', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('propietario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.persona')),
            ],
        ),
    ]
