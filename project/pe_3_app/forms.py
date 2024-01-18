from django import forms

from . import models

class ProfesorForms(forms.ModelForm):
    class Meta:
        model = models.Profesor
        fields = "__all__"