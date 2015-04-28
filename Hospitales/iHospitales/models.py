from django.db import models

# Create your models here.

class Hospital(models.Model):
    nombre = models.CharField(max_length=40)
    ciudad = models.CharField(max_length=40)
    codigo_postal = models.CharField(max_length=40)
    def __unicode__(self):
        return self.nombre

class Medico(models.Model):
    nombre = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    hospital = models.ForeignKey(Hospital)
    def __unicode__(self):
        return self.nombre

class Paciente(models.Model):
    nombre = models.CharField(max_length=40)
    def __unicode__(self):
        return self.nombre

class Ingreso (models.Model):

    hospital = models.ForeignKey(Hospital)
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    #info = models.CharField(max_length=288)
    def __unicode__(self):
        return self.id