from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Hospitales.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hospitales/$', 'iHospitales.views.hospitales', name='hospitales'),
    url(r'^hospitales/(?P<pk>\d+)', 'iHospitales.views.hospitales_detail' , name='hospital_detail'),
    #url(r'^pacientes/$', 'iHospitales.views.pacientes', name='pacientes'),

)
