# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_auto_20151014_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asociado',
            name='fecha_ingreso',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feriado',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='feriado',
            name='tipo_feriado',
            field=models.CharField(default=(b'F', b'Fijo'), max_length=8, choices=[(b'F', b'Fijo'), (b'V', b'Variable')]),
        ),
        migrations.AlterField(
            model_name='vacacion',
            name='fecha_desde',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='vacacion',
            name='fecha_hasta',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
