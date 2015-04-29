from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hospitales.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hospitales/$', 'iHospitales.views.hospitales', name='hospitales'), #Lista Hospitales
    url(r'^hospitales/(?P<pk>\d+)/$', 'iHospitales.views.hospitales_detail' , name='hospital_detail'),#Detalles Hospital
    url(r'^hospitales/(?P<pk>\d+)/medicos/$', 'iHospitales.views.medicos' , name='medicos'), #Lista de medicos de un Hospital
    url(r'medicos/(?P<pk>\d+)/$', 'iHospitales.views.medicos_detail' , name='medico_detail'), #Detalles de un medico
    url(r'^hospitales/(?P<pk>\d+)/ingresos/$', 'iHospitales.views.ingresos_hospital' , name='ingresos_hospital'), #Lista de ingresos de un hospital
    url(r'medicos/(?P<pk>\d+)/ingresos/$', 'iHospitales.views.ingresos_medico' , name='ingresos_medico'), #Lista de ingresos de un medico
    url(r'ingresos/(?P<pk>\d+)/$', 'iHospitales.views.ingresos_detail' , name='ingresos_detail'), #Detalles de un ingreso

    url(r'pacientes/(?P<pk>\d+)/$', 'iHospitales.views.pacientes_detail' , name='pacientes_detail'), #Detalles de un paciente
    url(r'^hospitales/(?P<pk>\d+)/pacientes/$', 'iHospitales.views.pacientes_hospital' , name='pacientes_hospital'), #Lista de pacientes de un hospital
    url(r'medicos/(?P<pk>\d+)/pacientes/$', 'iHospitales.views.pacientes_medico' , name='pacientes_medico'), #Lista de pacientes de un medico


    #url(r'^pacientes/$', 'iHospitales.views.pacientes', name='pacientes'),

)
