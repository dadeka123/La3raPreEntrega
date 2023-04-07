from django.contrib import admin
from django.urls import path
from PreEntrega3.views import *
from App3 import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('equipos/', lista_equipos, name="equipos"),
    path('jugadores/', lista_jugadores, name="jugadores"),
    path('representantes/', representantes, name="representantes"),
    path('agrega-jugador/<nombre>/<equipo>', agregar_jugador, name="equipo"),
]
