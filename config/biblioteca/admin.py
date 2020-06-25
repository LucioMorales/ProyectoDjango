from django.contrib import admin
from .models import *
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono', 'direccion', 'codigo',]
    list_display_links = ('nombre', 'telefono', 'direccion', 'codigo',)
    
    fieldsets = (
        ('Datos', {
          'fields': ('nombre',)  
        }),
        ('Contacto', {
            'fields': ('direccion', 'telefono')
        }),
    )

class LibroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'editorial',]
    list_display_links = ('titulo', 'editorial',)

class LibroInline(admin.StackedInline):
    model = Libro
    extra = 0
    fields = ['titulo', 'editorial', 'paginas']
    
class AutorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'codigo',]        
    list_display_links = ('nombre', 'codigo',)
    search_fields = ['nombre']
    inlines = [LibroInline]

class EjemplarAdmin(admin.ModelAdmin):
    list_display = ['localizacion', 'libro', 'codigo',]
    list_display_links = ('localizacion', 'libro', 'codigo',)
    search_fields = ['libro__titulo']

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Autor, AutorAdmin)

