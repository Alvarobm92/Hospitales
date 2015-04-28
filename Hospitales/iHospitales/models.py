from django.db import models

# Create your models here.

class Hospital(models.Model):
    hospital_id = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=40)


class Medico(models.Model):
    medico_id = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)

class Paciente(models.Model):
    paciente_id = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)

class ingreso (models.Model):
    ingreso_id = models.CharField(max_length=40)
    hospital_id = models.ForeignKey(Hospital)
    medico_id = models.ForeignKey(Medico)
    paciente_id = models.ForeignKey(Paciente)