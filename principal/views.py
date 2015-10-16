from django.shortcuts import render
from principal.models import Asociado, Feriado, Vacacion
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse



# Create your views- here.(

def inicio(request):
    vacaciones=Vacacion.objects.all()
    return render_to_response('inicio.html', {'vacaciones':vacaciones}) #con render_to_response le indicamos que vamos a usar una plantilla

def vacacion_usuario(request, id_usuario):
    dato = get_object_or_404(Vacacion, pk=id_usuario)
    return render_to_response('vacaciones.html', {'vacaciones':dato})
