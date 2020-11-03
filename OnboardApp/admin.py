from django.contrib import admin
from .models import Pais,Lugar,Contacto
# Register your models here.
class LugaresAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","disponible","pais"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["disponible","pais"]
    list_per_page = 10

admin.site.register(Pais)
admin.site.register(Lugar,LugaresAdmin)
admin.site.register(Contacto)