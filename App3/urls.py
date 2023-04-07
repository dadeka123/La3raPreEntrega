from django.contrib import admin
from django.urls import path
from PreEntrega3.views import *
from App3 import *

urlpatterns = [
    path('', inicio),
    path('equipos/', lista_equipos),
    path('jugadores/', lista_jugadores),
    path('representantes/', representantes),
    path('agrega-jugador/<nombre>/<equipo>', agregar_jugador),
]
