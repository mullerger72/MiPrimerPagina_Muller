from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profesot/create", views.profesor_create, name="profesor_create"),
    path("profesot/list", views.profesor_list, name="profesor_list"),
]
