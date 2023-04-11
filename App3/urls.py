from django.contrib import admin
from django.urls import path
from PreEntrega3.views import *
from .views import agregar_equipo, agregar_jugador,agregar_representante

urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar-equipo/', agregar_equipo, name="agregar_equipo"),
    path('agregar-jugador/', agregar_jugador, name="agregar_jugador"),
    path('agregar-representante/', agregar_representante, name="agregar_representante"),
    path('busquedaEquipo/', busquedaEquipo, name="BusquedaEquipo"),
    path('buscar/', buscar, name="Buscar"),
]

