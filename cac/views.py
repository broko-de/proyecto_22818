from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hola_mundo(request):
    return HttpResponse('Hola Mundo Django 🦄')
    
def saludar(request,nombre='Fede'):
    return HttpResponse(f"""
        <h1>Hola mundo Django - Un gusto {nombre}</h1>
    """)

def ver_proyectos(request,anio,mes):
    return HttpResponse(f"""
        <h1>Proyectos del {mes}/{anio}</h1>
        <p>Listado de proyectos</p>
    """)
