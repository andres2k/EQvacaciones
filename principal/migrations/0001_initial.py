# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asociado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=500)),
                ('fecha_ingreso', models.DateField(default=django.utils.timezone.now)),
                ('imagen', models.CharField(max_length=500)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Asociados',
            },
        ),
        migrations.CreateModel(
            name='Feriado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('descripcion', models.CharField(max_length=500)),
                ('tipo_feriado', models.CharField(default=(b'F', b'Fijo'), max_length=8, choices=[(b'F', b'Fijo'), (b'V', b'Variable')])),
            ],
            options={
                'verbose_name_plural': 'Feriados',
            },
        ),
        migrations.CreateModel(
            name='Vacacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha_desde', models.DateField(default=django.utils.timezone.now)),
                ('fecha_hasta', models.DateField(default=django.utils.timezone.now)),
                ('asociado', models.ForeignKey(to='principal.Asociado')),
            ],
            options={
                'verbose_name_plural': 'Vacaciones',
            },
        ),
    ]
