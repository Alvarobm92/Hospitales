from django.contrib import admin

# Register your models here.

from models import Hospital, Medico, Paciente, Ingreso

admin.site.register(Hospital)
admin.site.register(Medico)
admin.site.register(Paciente)
admin.site.register(Ingreso)
