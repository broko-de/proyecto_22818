from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse


# Create your views here.
def index(request):
    if(request.method=='GET'):
        titulo = 'Titulo cuando accedo por GET'
    else:
        titulo = f'Titulo cuando accedo por otro metodo {request.method}'
    parametetros_get = request.GET.get('nombre')
    return HttpResponse(f"""
        <h1>{titulo}</h1>
        <p>{parametetros_get}</p>
    """)


def quienes_somos(request):
    #return redirect('saludar_solito')
    return redirect(reverse('saludar', kwargs={'nombre': 'PepaPig'}))

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