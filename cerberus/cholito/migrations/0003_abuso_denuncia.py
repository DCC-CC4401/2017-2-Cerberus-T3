# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-23 19:19
from __future__ import unicode_literals

import cholito.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cholito', '0002_auto_20171023_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abuso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Abuso',
                'verbose_name_plural': 'Abusos',
            },
        ),
        migrations.CreateModel(
            name='Denuncia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('Reportada', 'Reportada'), ('Consolidada', 'Consolidada'), ('Verificada', 'Verificada'), ('Cerrada', 'Cerrada'), ('Desechada', 'Desechada')], default='Reportada', max_length=15)),
                ('localizacion', models.CharField(max_length=300, verbose_name='Lugar de la denuncia')),
                ('sexo', models.CharField(blank=True, choices=[(None, 'No especifica'), ('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('color', models.CharField(blank=True, max_length=50)),
                ('herido', models.NullBooleanField(default=None)),
                ('abuso', models.ManyToManyField(blank=True, to='cholito.Abuso')),
                ('animal', models.ForeignKey(default=cholito.models.crear_tipo_de_animal_por_defecto, on_delete=django.db.models.deletion.CASCADE, to='cholito.TipoDeAnimal', verbose_name='Tipo de animal')),
            ],
            options={
                'verbose_name': 'Denuncia',
                'verbose_name_plural': 'Denuncias',
            },
        ),
    ]
