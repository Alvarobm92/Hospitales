from django.forms import ModelForm
from models import Paciente, Ingreso, Review

class PacienteForm(ModelForm):
    class Meta:
        model = Paciente
        exclude = ('user',)

class IngresoForm(ModelForm):
    class Meta:
        model = Ingreso
        exclude = ('user',)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ('user',)