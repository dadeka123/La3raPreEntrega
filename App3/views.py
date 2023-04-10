from django.shortcuts import render,redirect
from .models import Jugador, Equipo, Representante
from django.http import HttpResponse
from .forms import EquipoForm

# Create your views here.

def agregar_equipo(request):
    
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else:
        form = EquipoForm()
    return render(request, 'agregar_equipo.html', {'form': form})


# def jugadores(self, nombre, equipo):
    
#     jugadores = Jugador(nombre=nombre, equipo=equipo)
#     jugadores.save()
    
#     return HttpResponse(f"""
#     <p>El jugador {jugadores.nombre} se agregó al equipo {jugadores.equipo}</p>
#     """)
    
# def listar_equipos(self):
    
#     lista = Jugador.objects.all()
    
#     return render(self, "lista_equipos.html", {"lista_equipos": lista})

# def cursoFormulario(request):
    
#     print('metod: ', request.method)
#     print('metod: ', request.POST)
    
#     if request.method == 'POST':
        
#         jugadores = Jugador(nombre=request.POST['jugador'], equipo=request.POST['equipo'])
#         jugadores.save()
        
#         return render(request, "inicio.html")
    
#     return render(request, "cursoFormulario.html")

