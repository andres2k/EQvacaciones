from django.db import models
from django.utils import timezone

# Create your models here.
class Asociados(models.Model):
	"""Modelo para los asociados"""
	nombre = models.CharField(max_length=500)
	fecha_ingreso=models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.nombre		

class Vacaciones(models.Model):
	"""Modelo para las vacaciones"""
	asociado = models.ForeignKey(Asociados)
	fecha_desde = models.DateTimeField(default=timezone.now)
	fecha_hasta = models.DateTimeField(default=timezone.now)

	def __unicode__(self):
		return self.asociado.nombre, fecha_hasta

class Feriados(models.Model):
	"""Modelo para los Feriados"""
	fecha = models.DateTimeField()
	descripcion = models.CharField(max_length=500)
	tipo_feriado = models.CharField(max_length=10)

	def __unicode__(self):
		return self.descripcion		