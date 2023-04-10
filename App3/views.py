from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EquipoForm, JugadorForm, RepresentanteForm

def agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Equipo agregado con éxito.')
            return redirect('inicio')
    else:
        form = EquipoForm()
    return render(request, 'agregar_equipo.html', {'form': form})

def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Jugador agregado con éxito.')
            return redirect('inicio')
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
        form = RepresentanteForm()
    return render(request, 'agregar_representante.html', {'form': form})
