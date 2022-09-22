from django.urls import path

from . import views

urlpatterns = [
    path('hola_mundo',views.hola_mundo ),
    path('saludar/',views.saludar ),
    path('saludar/<str:nombre>',views.saludar ),
    path('proyectos/<int:anio>/<int:mes>',views.ver_proyectos,name="ver_proyectos" ),
]