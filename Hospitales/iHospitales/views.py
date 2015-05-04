from django.shortcuts import render
from models import Hospital, Medico, Paciente, Ingreso


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context
from django.template.loader import get_template
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
#LISTA HOSPITALES
def hospitales(request):

    lista_hospitales = Hospital.objects.all()
    template = get_template('hospitales.html')
    variables = Context({
        'user': request.user,
        'hospitales':lista_hospitales

    })
    output = template.render(variables)
    return HttpResponse(output)

#Hospital especifico
def hospitales_detail(request, pk):
    try:
        hospital = Hospital.objects.get( codigo_hospital= pk)
    except:
        raise Http404('Hospital not found.')

    try:
        medicos = Medico.objects.filter(hospital = pk)[:10]
    except:
        raise Http404('Lista de medicos not found.')
    try:

       ingresos = Ingreso.objects.filter(hospital = pk)[:5]

    except:
        raise Http404('Lista de ingresos not found.')
    #try:

       #pacientes = Paciente.objects.filter(id = Ingreso.paciente).exclude(id = [x.paciente for x in ingresos])
       #Gallery.objects.filter(type = 2).filter(root_gallery__isnull = True).exclude(id__in = [x.id for x in request.user.usergallery_set()])
    #except:
        #raise Http404('Lista de pacientes not found.')

    lista_pacientes = []
    for paciente in ingresos:
        if paciente.paciente not in lista_pacientes:
            lista_pacientes.append(paciente.paciente)


    if request.user.is_anonymous():
        lista_pacientes = []
        ingresos = []

    template = get_template('hospitales_detail.html')
    variables = Context({
        'user': request.user,
        'hospital':hospital,
        'medicos': medicos,
        'pacientes': lista_pacientes,
        'ingresos': ingresos
    })
    output = template.render(variables)
    return HttpResponse(output)

#Lista medicos
def medicos(request, pk):
    lista_medicos = Medico.objects.filter(hospital = pk)
    template = get_template('medicos.html')
    variables = Context({
        'user': request.user,
        'medicos':lista_medicos

    })
    output = template.render(variables)
    return HttpResponse(output)

#Medico especifico
def medicos_detail(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')
    medico = Medico.objects.get(codigo_medico = pk)
    ingresos = Ingreso.objects.filter(medico = pk)
    lista_pacientes = []
    for paciente in ingresos:
        if paciente.paciente not in lista_pacientes:
            lista_pacientes.append(paciente.paciente)

    template = get_template('medicos_detail.html')
    variables = Context({
        'user': request.user,
        'medico':medico,
        'lista_pacientes':lista_pacientes

    })
    output = template.render(variables)
    return HttpResponse(output)

#Lista de ingresos de un hospital
def ingresos_hospital(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')
    lista_ingresos = Ingreso.objects.filter(hospital = pk)
    template = get_template('ingresos.html')
    variables = Context({
        'user': request.user,
        'ingresos':lista_ingresos

    })
    output = template.render(variables)
    return HttpResponse(output)

#Lista de ingresos de un medico
def ingresos_medico(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')
    lista_ingresos = Ingreso.objects.filter(medico = pk)
    template = get_template('ingresos.html')
    variables = Context({
        'user': request.user,
        'ingresos':lista_ingresos

    })
    output = template.render(variables)
    return HttpResponse(output)

#Detalles de un ingreso
def ingresos_detail(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')

    ingresos = Ingreso.objects.get(codigo_ingreso = pk)

    template = get_template('ingresos_detail.html')
    variables = Context({
        'user': request.user,

        'ingresos':ingresos

    })
    output = template.render(variables)
    return HttpResponse(output)

#Lista de pacientes de un hospital
def pacientes_hospital(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')

    lista_ingresos = Ingreso.objects.filter(hospital = pk)
    lista_pacientes = []
    for paciente in lista_ingresos:
        if paciente.paciente not in lista_pacientes:
            lista_pacientes.append(paciente.paciente)

    template = get_template('pacientes.html')
    variables = Context({
        'user': request.user,
        'pacientes':lista_pacientes

    })
    output = template.render(variables)
    return HttpResponse(output)

#Lista de pacientes de un medico
def pacientes_medico(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')
    ingresos = Ingreso.objects.filter(medico = pk)
    lista_pacientes = []
    for paciente in ingresos:
        if paciente.paciente not in lista_pacientes:
            lista_pacientes.append(paciente.paciente)
    template = get_template('pacientes.html')
    variables = Context({
        'user': request.user,
        'pacientes':lista_pacientes

    })
    output = template.render(variables)
    return HttpResponse(output)

#Detalles de un paciente
def pacientes_detail(request, pk):
    if request.user.is_anonymous():
        raise Http404('No tienes permisos')
    paciente = Paciente.objects.get(dni = pk)
    ingresos = Ingreso.objects.filter(paciente = pk )
    lista_medicos = []
    for ingreso in ingresos:
        if ingreso.medico not in lista_medicos:
            lista_medicos.append(ingreso.medico)
    lista_hospitales = []
    for ingreso in ingresos:
        if ingreso.hospital not in lista_hospitales:
            lista_hospitales.append(ingreso.hospital)

    template = get_template('pacientes_detail.html')
    variables = Context({

        'user': request.user,
        'paciente':paciente,
        'medicos': lista_medicos,
        'hospitales': lista_hospitales

    })
    output = template.render(variables)
    return HttpResponse(output)





#Lista de hospitales - JSON
def hospitalesjson(request):
    listajson = Hospital.objects.all()
    json_list = serializers.serialize(u"json", listajson)
    return HttpResponse(json_list, content_type=u"application/json")
#Lista de hospitales XML
def hospitalesxml(request):
    listaxml = Hospital.objects.all()
    xml_list = serializers.serialize(u"xml", listaxml)
    return HttpResponse(xml_list, content_type=u"application/xml")

#Lista de Medicos - JSON
def medicosjson(request):
    listajson = Medico.objects.all()
    json_list = serializers.serialize(u"json", listajson)
    return HttpResponse(json_list, content_type=u"application/json")

#Lista de medicos XML
def medicosxml(request):
    listaxml = Medico.objects.all()
    xml_list = serializers.serialize(u"xml", listaxml)
    return HttpResponse(xml_list, content_type=u"application/xml")


#Lista de pacientes - JSON
def pacientesjson(request):
    listajson = Paciente.objects.all()
    json_list = serializers.serialize(u"json", listajson)
    return HttpResponse(json_list, content_type=u"application/json")
#Lista de pacientes XML
def pacientesxml(request):
    listaxml = Paciente.objects.all()
    xml_list = serializers.serialize(u"xml", listaxml)
    return HttpResponse(xml_list, content_type=u"application/xml")

#Lista de ingresos - JSON
def ingresosjson(request):
    listajson = Ingreso.objects.all()
    json_list = serializers.serialize(u"json", listajson)
    return HttpResponse(json_list, content_type=u"application/json")
#Lista de ingresos XML
def ingresosxml(request):
    listaxml = Ingreso.objects.all()
    xml_list = serializers.serialize(u"xml", listaxml)
    return HttpResponse(xml_list, content_type=u"application/xml")


#LOGOUT
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/hospitales")

#HOME
def home(request):
    template = get_template('home.html')
    variables = Context({

    })
    output = template.render(variables)
    return HttpResponse(output)


