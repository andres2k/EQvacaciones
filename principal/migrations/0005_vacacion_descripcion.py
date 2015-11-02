# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0004_auto_20151101_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacacion',
            name='descripcion',
            field=models.CharField(default='default', max_length=500, verbose_name=b'Descripcion'),
            preserve_default=False,
        ),
    ]
