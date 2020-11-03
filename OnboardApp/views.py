from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import Lugar
from .forms import ContactoForm,LugarForm
from django.contrib import messages

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
            messages.success(request,"Enviado correctamente")
            return redirect(to="Inicio")
        else:
            data["form"] =  formulario
    return render(request, "OnboardApp/contacto.html",data)

def reservas(request):

    return render(request, "OnboardApp/reservas.html")

def registro(request):

    return render(request, "OnboardApp/registro.html")

def agregar_lugar(request):
    data = {
        'form': LugarForm()
    }
    if request.method == 'POST':
        formulario = LugarForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado correctamente")
            return redirect(to="Listar_lugares")
        else:
            data["form"] = formulario
 
    return render(request, "OnboardApp/lugares/agregar.html",data)

def listar_lugares(request):
    lugares = Lugar.objects.all()
    data = {
        'lugares': lugares
    }
    return render(request,"OnboardApp/lugares/listar.html",data)

def modificar_lugar(request,id):

    lugar = get_object_or_404(Lugar,id=id)

    data = {
        'form': LugarForm(instance=lugar)
    }

    if request.method == 'POST':
        formulario = LugarForm(data=request.POST,instance=lugar,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="Listar_lugares")
        data["form"] = formulario


    return render(request,"OnboardApp/lugares/modificar.html",data)

def eliminar_lugar(request,id):
    lugar = get_object_or_404(Lugar,id=id)
    lugar.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="Listar_lugares")