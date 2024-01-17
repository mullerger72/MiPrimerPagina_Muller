from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola Mundo")

def saludo2(request):
    nombre = input ("Ingresa tu Nombre: ")
    return HttpResponse(f"Hola <h1> {nombre} </h1>")