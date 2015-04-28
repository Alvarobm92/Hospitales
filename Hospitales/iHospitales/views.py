from django.shortcuts import render
from models import Hospital, Medico, Paciente, Ingreso


from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template


# Create your views here.
def hospitales(request):
    lista_hospitales = Hospital.objects.all()
    template = get_template('hospitales.html')
    variables = Context({

        'hospitales':lista_hospitales

    })
    output = template.render(variables)
    return HttpResponse(output)


def hospitales_detail(request, pk):
    try:
        hospital = Hospital.objects.get( id= pk)
    except:
        raise Http404('Hospital not found.')

    try:
        medicos = Medico.objects.filter(hospital = pk)[:10]
    except:
        raise Http404('Lista de medicos not found.')
    try:

       ingresos = Ingreso.objects.filter(hospital = pk )[:5]
       pacientes = [ingreso.paciente for ingreso in ingresos]
    except:
        raise Http404('Lista de ingresos not found.')
    #try:

       #pacientes = Paciente.objects.filter(id = Ingreso.paciente).exclude(id = [x.paciente for x in ingresos])
       #Gallery.objects.filter(type = 2).filter(root_gallery__isnull = True).exclude(id__in = [x.id for x in request.user.usergallery_set()])
    #except:
        #raise Http404('Lista de pacientes not found.')

    template = get_template('hospitales_detail.html')
    variables = Context({
        'hospital':hospital,
        'medicos': medicos,
        'ingresos': ingresos
    })
    output = template.render(variables)
    return HttpResponse(output)

def medicos(request, pk):
    lista_medicos = Medico.objects.filter(hospital = pk)
    template = get_template('medicos.html')
    variables = Context({

        'medicos':lista_medicos

    })
    output = template.render(variables)
    return HttpResponse(output)

def medicos_detail(request, pk, pk2):
    medico = Medico.objects.get(id = pk2)
    template = get_template('medicos_detail.html')
    variables = Context({

        'medico':medico

    })
    output = template.render(variables)
    return HttpResponse(output)
