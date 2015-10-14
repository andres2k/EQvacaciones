# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('fecha_ingreso', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Feriados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo_feriado', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_desde', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_hasta', models.DateTimeField(default=django.utils.timezone.now)),
                ('asociado', models.ForeignKey(to='principal.Asociado')),
            ],
        ),
    ]
