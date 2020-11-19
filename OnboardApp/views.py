from django.shortcuts import render, HttpResponse,redirect,get_object_or_404
from .models import Lugar,Resena
from .forms import ContactoForm,LugarForm,CustomUserCreationForm,ResenaForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.mixins import UserPassesTestMixin

# Create your views here.

def inicio(request):
    resenas = Resena.objects.all()
    lugares = Lugar.objects.all().order_by('-id')[:4]
    data = {
        'resenas':resenas,
        'lugares':lugares
    }

    return render(request, "OnboardApp/inicio.html",data)
    

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

@permission_required('OnboardApp.add_lugar')
def agregar_lugar(request):
    data = {
        'form': LugarForm()
    }
    if request.method == 'POST':
        formulario = LugarForm(data=request.POST,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Agregado correctamente")
            if request.user.has_perm('OnboardApp.view_lugares'):
                return redirect(to="Listar_lugares")
            else:
                return redirect(to="Inicio")
        else:
            data["form"] = formulario
 
    return render(request, "OnboardApp/lugares/agregar.html",data)

@login_required
def agregar_resena(request):
    data = {
        'form': ResenaForm()
    }
    if request.method == 'POST':
        formulario = ResenaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Reseña enviada")
        else:
            data["form"] = formulario
 
    return render(request, "OnboardApp/resenas/agregar.html",data)
@permission_required('OnboardApp.view_lugar')
def listar_lugares(request):
    lugares = Lugar.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(lugares,5)
        lugares = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity': lugares,
        'paginator': paginator
    }
    return render(request,"OnboardApp/lugares/listar.html",data)
@permission_required('OnboardApp.change_lugar')
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
@permission_required('OnboardApp.delete_lugar')
def eliminar_lugar(request,id):
    lugar = get_object_or_404(Lugar,id=id)
    lugar.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect(to="Listar_lugares")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Te has registrado correctamente")
            return redirect(to="Inicio")
        data["form"] = formulario
    return render(request, 'registration/registro.html',data)