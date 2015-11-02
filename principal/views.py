from django.shortcuts import render
from principal.models import Asociado, Feriado, Vacacion
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from principal.forms import VacacionForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



# Create your views- here.(

def index(request):
    asociados=Asociado.objects.all()
    return render_to_response('index.html', {'asociados':asociados}) #con render_to_response le indicamos que vamos a usar una plantilla

def vacacion_usuario(request, id_asociado):
    dato = get_object_or_404(Asociado, pk=id_asociado)
    vacaciones = Vacacion.objects.filter(asociado=dato)
    return render_to_response('vacaciones.html', {'vacaciones':vacaciones, 'asociado':dato})

def nueva_vacacion(request):
    if request.POST:
        form = VacacionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = VacacionForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('nueva_vacacion.html', args)
