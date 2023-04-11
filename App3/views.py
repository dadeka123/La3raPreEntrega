from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import EquipoForm, JugadorForm, RepresentanteForm
from .models import *

def agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Equipo agregado con éxito.")
            return redirect('inicio')
        else:
            messages.error(request, "Por favor corrija los errores en el formulario.")
    else:
        form = EquipoForm()
    return render(request, 'agregar_equipo.html', {'form': form})

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Jugador agregado con éxito.")
            return redirect('inicio')
        else:
            messages.error(request, "Por favor corrija los errores en el formulario.")
    else:
        form = JugadorForm()
    return render(request, 'agregar_jugador.html', {'form': form})

def agregar_representante(request):
    if request.method == 'POST':
        form = RepresentanteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Representante agregado con éxito.')
            return redirect('inicio')
        else:
            messages.error(request, "Por favor corrija los errores en el formulario.")
    else:
        form = RepresentanteForm()
    return render(request, 'agregar_representante.html', {'form': form})

def busquedaEquipo(request):
    return render(request, "busquedaEquipo.html")

def buscar(request):
    if request.GET.get("Equipo"):
        equipo_name = request.GET.get("Equipo")
        equipos = Equipo.objects.filter(nombre_equipo=equipo_name)
        return render(request, "resultadoBusqueda.html", {"equipos": equipos, "equipo_name": equipo_name})
    else:
        return HttpResponse(f'No enviaste info')
