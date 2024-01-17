from django.shortcuts import render

from . import models

def index(request):
    return render(request, "pe_3_app/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "pe_3_app/profesor_list.html")