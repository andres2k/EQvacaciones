# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0002_auto_20151014_0204'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_desde', models.DateTimeField(default=django.utils.timezone.now)),
                ('fecha_hasta', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Vacaciones',
            },
        ),
        migrations.RenameModel(
            old_name='Asociados',
            new_name='Asociado',
        ),
        migrations.RenameModel(
            old_name='Feriados',
            new_name='Feriado',
        ),
        migrations.RemoveField(
            model_name='vacaciones',
            name='asociado',
        ),
        migrations.AlterModelOptions(
            name='asociado',
            options={'verbose_name_plural': 'Asociados'},
        ),
        migrations.AlterModelOptions(
            name='feriado',
            options={'verbose_name_plural': 'Feriados'},
        ),
        migrations.DeleteModel(
            name='Vacaciones',
        ),
        migrations.AddField(
            model_name='vacacion',
            name='asociado',
            field=models.ForeignKey(to='principal.Asociado'),
        ),
    ]
