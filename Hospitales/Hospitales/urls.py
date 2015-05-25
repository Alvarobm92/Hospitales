from django.conf.urls import patterns, include, url
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import UpdateView
from iHospitales.forms import PacienteForm , IngresoForm
from iHospitales.models import Paciente, Ingreso
from iHospitales.views import HospitalList, HospitalDetail, MedicoList, MedicoDetail, HospitalViewSet, MedicoViewSet, IngresoCreate, PacienteCreate
from iHospitales import views

from rest_framework import routers

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()
router.register(r'hospital', views.HospitalViewSet)
router.register(r'medico', views.MedicoViewSet)
router.register(r'paciente', views.PacienteViewSet)
router.register(r'ingreso', views.IngresoViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hospitales.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hospitales/$', 'iHospitales.views.hospitales', name='hospitales'), #Lista Hospitales
    url(r'^hospitales/(?P<pk>\w+)/$', 'iHospitales.views.hospitales_detail' , name='hospital_detail'),#Detalles Hospital
    url(r'^hospitales/(?P<pk>\w+)/medicos/$', 'iHospitales.views.medicos' , name='medicos'), #Lista de medicos de un Hospital
    url(r'medicos/(?P<pk>\w+)/$', 'iHospitales.views.medicos_detail' , name='medico_detail'), #Detalles de un medico
    url(r'^hospitales/(?P<pk>\w+)/ingresos/$', 'iHospitales.views.ingresos_hospital' , name='ingresos_hospital'), #Lista de ingresos de un hospital
    url(r'medicos/(?P<pk>\w+)/ingresos/$', 'iHospitales.views.ingresos_medico' , name='ingresos_medico'), #Lista de ingresos de un medico
    url(r'ingresos/(?P<pk>\w+)/$', 'iHospitales.views.ingresos_detail' , name='ingresos_detail'), #Detalles de un ingreso

    url(r'pacientes/(?P<pk>\w+)/$', 'iHospitales.views.pacientes_detail' , name='pacientes_detail'), #Detalles de un paciente
    url(r'^hospitales/(?P<pk>\w+)/pacientes/$', 'iHospitales.views.pacientes_hospital' , name='pacientes_hospital'), #Lista de pacientes de un hospital
    url(r'medicos/(?P<pk>\w+)/pacientes/$', 'iHospitales.views.pacientes_medico' , name='pacientes_medico'), #Lista de pacientes de un medico


    url(r'^api/hospitales.json$', 'iHospitales.views.hospitalesjson'),
    url(r'^api/hospitales.xml$', 'iHospitales.views.hospitalesxml'),
    url(r'^api/medicos.json$', 'iHospitales.views.medicosjson'),
    url(r'^api/medicos.xml$', 'iHospitales.views.medicosxml'),
    url(r'^api/pacientes.json$', 'iHospitales.views.pacientesjson'),
    url(r'^api/pacientes.xml$', 'iHospitales.views.pacientesxml'),
    url(r'^api/ingresos.json$', 'iHospitales.views.ingresosjson'),
    url(r'^api/ingresos.xml$', 'iHospitales.views.ingresosxml'),

    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'logout', 'iHospitales.views.logout'),
    url(r'^$', 'iHospitales.views.home'),

	url(r'^api/', include(router.urls)),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^paciente/create/$', PacienteCreate.as_view(), name='paciente_create'),
    url(r'^ingreso/create/$', IngresoCreate.as_view(), name='ingreso_create'),



url(r'^pacientes/(?P<pk>\w+)/edit/$',UpdateView.as_view(
            model=Paciente,
            form_class=PacienteForm,
            template_name='form.html'),
        name='paciente_edit'),

url(r'^ingresos/(?P<pk>\w+)/edit/$',UpdateView.as_view(
            model=Ingreso,
            form_class=IngresoForm,
            template_name='form.html'),
        name='ingreso_edit'),
)
