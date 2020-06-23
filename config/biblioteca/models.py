from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=35)
    codigo=models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.nombre)

class Libro(models.Model):
    titulo=models.CharField(max_length=35)
    editorial=models.CharField(max_length=35)
    paginas=models.IntegerField(default='1')
    codigo=models.AutoField(primary_key=True)
    autor=models.ForeignKey(Autor, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.titulo)

class Ejemplar(models.Model):
    localizacion=models.CharField(max_length=35)
    codigo=models.AutoField(primary_key=True)
    libro=models.ForeignKey(Libro, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.libro)

class Usuario(models.Model):
    nombre=models.CharField(max_length=35)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=35)
    codigo=models.AutoField(primary_key=True)
    ejemplares=models.ManyToManyField(Ejemplar)
    def __str__(self):
        return str(self.nombre)