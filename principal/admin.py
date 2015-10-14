from django.contrib import admin
from .models import Asociados, Vacaciones, Feriados

# Register your models here.
admin.site.register(Asociados)
admin.site.register(Vacaciones)
admin.site.register(Feriados)