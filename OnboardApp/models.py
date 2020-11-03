from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural = "Paises"
    
    def __str__(self):
        return self.nombre

class Lugar(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    disponible = models.BooleanField()
    pais = models.ForeignKey(Pais,on_delete=models.PROTECT)
    imagen = models.ImageField(upload_to="lugares",null=True)
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Lugares"
        
    

opciones_consultas = [
    [0,"Consulta"],
    [1,"Reclamo"],
    [2,"Sugerencia"],
    [3,"Felicitaciones"]
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField(name="¿Desea recibir promociones/avisos a su email?")

    def __str__(self):
        return self.nombre
