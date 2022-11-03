from django.db import models

# Create your models here.
class Persona(models.Model):    
    nombre = models.CharField(max_length=100,verbose_name='Nombre')
    apellido = models.CharField(max_length=150,verbose_name='Apellido')
    email = models.EmailField(max_length=150,verbose_name='Email')
    dni = models.IntegerField(verbose_name='DNI')

class Estudiante(models.Model):    
    persona = models.OneToOneField(Persona,on_delete=models.CASCADE,primary_key=True)
    matricula = models.CharField(max_length=10,verbose_name='Matricula')

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    descripcion = models.TextField(null=True, verbose_name='Descripción')
    #fecha_inicio = models.DateField(verbose_name='Fecha de inicio')
    #portada = models.ImageField(upload_to='imagenes/',null=True,verbose_name='Portada')
    categoria = models.ForeignKey(Categoria,on_delete=models.CASCADE)    
    #estudiantes = models.ManyToManyField(Estudiante) #tabla intermedia automatica de django
    estudiantes = models.ManyToManyField(Estudiante, through='Inscripcion')

class Inscripcion(models.Model):
    ESTADOS = [
        (1,'Inscripto'),
        (2,'Cursando'),
        (3,'Egresado'),
    ]
    fecha_creacion = models.DateField(verbose_name='Fecha de creacion')
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    estado = models.IntegerField(choices=ESTADOS,default=1)

    def __str__(self):
        return self.id