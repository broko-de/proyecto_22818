from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse

from django.template import loader

# Create your views here.
def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET - MODIFICO EL VALOR'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parametetros_get = request.GET.get('nombre')
    listado_cursos = [
        {
            'nombre':'Fullstack Java',
            'descripcion': 'Curso curso',
            'categoria':'Programación'
        },
        {
            'nombre':'Diseño UX/UI',
            'descripcion': '🎨',
            'categoria':'Diseño'
        },
        {
            'nombre':'Big Data',
            'descripcion': 'test test',
            'categoria':'Analisis de datos'
        },
    ]
    return render(request,'cac/index.html',{'titulo':titulo,'cursos':listado_cursos})
    # return HttpResponse(f"""
    #     <h1>{titulo}</h1>
    #     <p>{parametetros_get}</p>
    # """)


def quienes_somos(request):
    #return redirect('saludar_solito')
    #return redirect(reverse('saludar', kwargs={'nombre': 'PepaPig'}))
    template = loader.get_template('cac/quienes_somos.html')
    contexto = {'titulo':'Codo a Codo - Quienes Somos'}
    return HttpResponse(template.render(contexto,request))

def hola_mundo(request):
    return HttpResponse('Hola Mundo Django 🦄')
    
def saludar(request,nombre='Fede'):
    return HttpResponse(f"""
        <h1>Hola mundo Django - Un gusto {nombre}</h1>
    """)

def ver_proyectos(request,anio,mes=1):
    return HttpResponse(f"""
        <h1>Proyectos del {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)

def ver_proyectos_2022_08(request):
    return HttpResponse(f"""
        <h1>Proyectos del mes de agosto del 2022</h1>
        <p>Listado de proyectos</p>
    """)

def cursos_detalle(request, nombre_curso):
    """"
    ir a buscar en mi base datos el curso que tenga ese nombre: slug
    """
    return HttpResponse(f'{nombre_curso}')

def cursos(request, nombre_categoria):
    return HttpResponse(f'{nombre_categoria}')