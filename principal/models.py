from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
class Asociado(models.Model):
	"""Modelo para los asociados"""
	class Meta:
		verbose_name_plural="Asociados"
	nombre = models.CharField(max_length=500)
	fecha_ingreso = models.DateField(default=timezone.now)
	imagen = models.CharField(max_length=500)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, )

	def __unicode__(self):
		return self.user.first_name + ' ' + self.user.last_name

class Vacacion(models.Model):
	"""Modelo para las vacaciones"""
	class Meta:
		verbose_name_plural="Vacaciones"
	asociado = models.ForeignKey(Asociado)
	fecha_desde = models.DateField(default=timezone.now)
	fecha_hasta = models.DateField(default=timezone.now)

	def __unicode__(self):
		return self.asociado.nombre + " : " + self.fecha_desde.strftime("%d/%m/%Y") + " al " + self.fecha_hasta.strftime("%d/%m/%Y")

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
