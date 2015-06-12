from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
# Create your models here.

class Hospital(models.Model):
    codigo_hospital = models.CharField(max_length=10, primary_key= True )
    nombre = models.CharField(max_length=40)
    ciudad = models.TextField(max_length=40)
    codigo_postal = models.CharField(max_length=40)
    pais = models.CharField(max_length=40)
    Dep_destacados = models.CharField(max_length=40)
    telefono = models.IntegerField()
    capacidad = models.IntegerField()
    def __unicode__(self):
        return self.nombre

class Medico(models.Model):
    codigo_medico = models.CharField(max_length=10, primary_key= True )
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=40)
    especialidad = models.CharField(max_length=40)
    departamento = models.CharField(max_length=40)
    hospital = models.ForeignKey(Hospital)
    def __unicode__(self):
        return self.nombre

class Paciente(models.Model):
    dni = models.CharField(max_length=10, primary_key= True )
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    ciudad = models.CharField(max_length=40)
    pais =  models.CharField(max_length=40)
    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('pacientes_detail', kwargs={'pk': self.pk})


class Ingreso (models.Model):
    codigo_ingreso = models.CharField(max_length=10, primary_key= True )
    hospital = models.ForeignKey(Hospital)
    medico = models.ForeignKey(Medico)
    paciente = models.ForeignKey(Paciente)
    sintomas = models.CharField(max_length=140)
    #info = models.CharField(max_length=288)
    def __unicode__(self):
        return self.codigo_ingreso

    def get_absolute_url(self):
        return reverse('ingresos_detail', kwargs={'pk': self.pk})


class Review (models.Model):
    codigo_review =  models.CharField(max_length=5, primary_key= True )
    RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'))
    rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    hospital = models.ForeignKey(Hospital)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    def __unicode__(self):
        return self.codigo_review

    def get_absolute_url(self):
        return reverse('hospitales', kwargs={})