# Generated by Django 5.0.2 on 2024-02-29 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.BigIntegerField()),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=50)),
                ('telefono', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('placa', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('modelo', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.categoria')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personas.vendedor')),
            ],
        ),
    ]
