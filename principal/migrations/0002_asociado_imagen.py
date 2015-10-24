# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asociado',
            name='imagen',
            field=models.CharField(default='/home/mauroc/Proyectos/EQvacaciones/static/image/3865119.png', max_length=500),
            preserve_default=False,
        ),
    ]
