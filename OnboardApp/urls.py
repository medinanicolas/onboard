from django.urls import path
from OnboardApp import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('galeria',views.galeria,name="Galeria"),
    path('reservas',views.reservas,name="Reservas"),
    path('registro',views.registro,name="Registro"),
    path('contacto',views.contacto,name="Contacto"),
    
]