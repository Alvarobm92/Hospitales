from django.shortcuts import render
from models import Hospital, Medico


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
        medicos = Medico.objects.filter(id = pk)
    except:
        raise Http404('Lista de medicos not found.')

    template = get_template('hospitales_detail.html')
    variables = Context({
        'hospital':hospital,
        'medicos': medicos
    })
    output = template.render(variables)
    return HttpResponse(output)
