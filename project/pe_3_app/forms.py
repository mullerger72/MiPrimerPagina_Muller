from django import forms

from . import models

class ProfesorForms(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"

class AlumnoForms(forms.ModelForm):
    class Meta:
        model = models.Alumno
        fields = "__all__"

class CursoForms(forms.ModelForm):
    class Meta:
        model = models.Curso
        fields = "__all__"