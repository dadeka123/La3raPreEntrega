from django.shortcuts import render
from .models import Jugador, Equipo, Representante
from django.http import HttpResponse

# Create your views here.


def jugadores(self, nombre, equipo):
    
    jugadores = Jugador(nombre=nombre, equipo=equipo)
    jugadores.save()
    
    return HttpResponse(f"""
    <p>El jugador {jugadores.nombre} se agregó al equipo {jugadores.equipo}</p>
    """)
    
def listar_equipos(self):
    
    lista = Jugador.objects.all()
    
    return render(self, "lista_equipos.html", {"lista_equipos": lista})

