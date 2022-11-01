from django.db import models

# Create your models here.
class Estudiante(models.Model):    
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    email = models.EmailField(max_length=100, verbose_name='Email',null=True)
    dni= models.IntegerField(verbose_name='DNI')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre
    
