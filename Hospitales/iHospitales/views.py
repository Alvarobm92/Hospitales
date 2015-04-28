from django.shortcuts import render
from models import Hospital


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
        hospital = Hospital.objects.get(hospital_id= pk)
        template = get_template('hospitales_detail.html')
        variables = Context({
            'hospital':hospital
        })
        output = template.render(variables)
        return HttpResponse(output)
    except:
        raise Http404('User not found.')
