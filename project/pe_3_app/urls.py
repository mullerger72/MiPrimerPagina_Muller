from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profesor/create", views.profesor_create, name="profesor_create"),
    path("profesor/list", views.profesor_list, name="profesor_list"),
    path("alumno/create", views.alumno_create, name="alumno_create"),
    path("alumno/list", views.alumno_list, name="alumno_list"),
]
