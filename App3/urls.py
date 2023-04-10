from django.contrib import admin
from django.urls import path
from PreEntrega3.views import *
from App3 import *
from .views import agregar_equipo

urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar-equipo/', agregar_equipo, name="agregar_equipo"),
    path('jugadores/', lista_jugadores, name="jugadores"),
    path('representantes/', representantes, name="representantes"),
]
