from django.urls import path,include
from OnboardApp import views

from .views import LugarViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('lugares',LugarViewSet)

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('galeria/',views.galeria,name="Galeria"),
    path('contacto/',views.contacto,name="Contacto"),
    path('agregar-lugar/',views.agregar_lugar,name='Agregar_lugar'),
    path('listar-lugares/',views.listar_lugares,name='Listar_lugares'),
    path('modificar-lugar/<id>/',views.modificar_lugar,name='Modificar_lugar'),
    path('eliminar-lugar/<id>/',views.eliminar_lugar,name='Eliminar_lugar'),
    path('registro/',views.registro,name='Registro'),
    path('agregar-resena/',views.agregar_resena,name='Agregar_resena'),
    path('api/',include(router.urls))
]