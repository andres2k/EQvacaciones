# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_asociado_imagen2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asociado',
            name='imagen2',
        ),
    ]
