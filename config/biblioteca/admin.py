from django.contrib import admin
from .models import *
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'direccion', 'codigo',]

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'editorial', 'paginas', 'codigo', 'autor',]
    
class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['localizacion', 'codigo', 'libro',]

class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo',]        

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Autor, AutorAdmin)

