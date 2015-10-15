from django.db import models
from django.utils import timezone

# Create your models here.
class Asociado(models.Model):
	"""Modelo para los asociados"""
	class Meta:
		verbose_name_plural="Asociados"
	nombre = models.CharField(max_length=500)
	fecha_ingreso=models.DateField(default=timezone.now)

	def __unicode__(self):
		return self.nombre

class Vacacion(models.Model):
	"""Modelo para las vacaciones"""
	class Meta:
		verbose_name_plural="Vacaciones"
	asociado = models.ForeignKey(Asociado)
	fecha_desde = models.DateField(default=timezone.now)
	fecha_hasta = models.DateField(default=timezone.now)

	def __unicode__(self):
		return self.asociado.nombre + " : " + str(self.fecha_desde) + " to " + str(self.fecha_hasta)

class Feriado(models.Model):
	"""Modelo para los Feriados"""
	class Meta:
		verbose_name_plural="Feriados"
	fecha = models.DateField()
	descripcion = models.CharField(max_length=500)
	TIPOS = (('F', 'Fijo'), ('V' , 'Variable'))
	tipo_feriado = models.CharField(max_length=8, choices=TIPOS, default=TIPOS[0])

	def __unicode__(self):
		return self.descripcion
