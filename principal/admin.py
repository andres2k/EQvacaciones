from django.contrib import admin
from .models import Asociado, Vacacion, Feriado

# Register your models here.
admin.site.register(Asociado)
admin.site.register(Vacacion)
admin.site.register(Feriado)