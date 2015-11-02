# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_remove_asociado_imagen2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asociado',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='asociado',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Fecha Ingreso'),
        ),
        migrations.AlterField(
            model_name='asociado',
            name='imagen',
            field=models.CharField(max_length=500, verbose_name=b'imagen'),
        ),
        migrations.AlterField(
            model_name='vacacion',
            name='fecha_desde',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Fecha Desde'),
        ),
        migrations.AlterField(
            model_name='vacacion',
            name='fecha_hasta',
            field=models.DateField(default=django.utils.timezone.now, verbose_name=b'Fecha Hasta'),
        ),
    ]
