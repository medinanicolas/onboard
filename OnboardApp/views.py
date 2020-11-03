from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):

    return render(request, "OnboardApp/inicio.html")

def galeria(request):

    return render(request, "OnboardApp/galeria.html")

def contacto(request):

    return render(request, "OnboardApp/contacto.html")

def reservas(request):

    return render(request, "OnboardApp/reservas.html")

def registro(request):

    return render(request, "OnboardApp/registro.html")
