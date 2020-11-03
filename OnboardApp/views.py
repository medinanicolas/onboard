from django.shortcuts import render, HttpResponse
from .models import Lugar
from .forms import ContactoForm

# Create your views here.

def inicio(request):

    return render(request, "OnboardApp/inicio.html")

def galeria(request):
    lugares = Lugar.objects.all()
    data = {
        'lugares': lugares
    }
    return render(request, "OnboardApp/galeria.html",data)

def contacto(request):
    data = {
        'form':ContactoForm
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Formulario Enviado"
        else:
            data["form"] =  formulario
    return render(request, "OnboardApp/contacto.html",data)

def reservas(request):

    return render(request, "OnboardApp/reservas.html")

def registro(request):

    return render(request, "OnboardApp/registro.html")
