from django.shortcuts import redirect, render

from . import models
from . import forms

def index(request):
    return render(request, "pe_3_app/index.html")

def profesor_list(request):
    consulta = models.Profesor.objects.all()
    contexto = {"profesores": consulta}
    return render(request, "pe_3_app/profesor_list.html", contexto)

def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("profesor_list")
    else:
        form = forms.ProfesorForms()
    return render(request, "pe_3_app/profesor_create.html", {"form": form})

def alumno_list(request):
    consulta = models.Alumno.objects.all()
    contexto = {"alumnos": consulta}
    return render(request, "pe_3_app/alumno_list.html", contexto)

def alumno_create(request):
    if request.method == "POST":
        form = forms.AlumnoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("alumno_list")
    else:
        form = forms.AlumnoForms()
    return render(request, "pe_3_app/alumno_create.html", {"form": form})

def curso_list(request):
    consulta = models.Curso.objects.all()
    contexto = {"cursos": consulta}
    return render(request, "pe_3_app/curso_list.html", contexto)

def curso_create(request):
    if request.method == "POST":
        form = forms.CursoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_list")
    else:
        form = forms.CursoForms()
    return render(request, "pe_3_app/curso_create.html", {"form": form})
