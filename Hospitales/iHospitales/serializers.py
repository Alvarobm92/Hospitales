from models import Hospital, Medico, Paciente, Ingreso
from rest_framework import serializers


class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = ('codigo_postal', 'nombre', 'ciudad', 'codigo_postal', 'capacidad')


class MedicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ('codigo_medico', 'nombre', 'edad', 'ciudad', 'especialidad', 'departamento', 'hospital')

class PacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paciente
        fields = ('dni', 'nombre', 'edad', 'ciudad')

class IngresoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medico
        fields = ('codigo_ingreso', 'hospital', 'medico', 'paciente', 'sintomas')


##