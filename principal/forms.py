from django import forms
from django.forms import ModelForm
from principal.models import Vacacion

class VacacionForm(ModelForm):
    class Meta:
        model = Vacacion
        fields = '__all__'
