from django.shortcuts import render

# Create your views here.
from .models import Jugador
from .models import Partido
def home(request):
    jugadores = Jugador.objects.all()
    data = {
        'jugadores': jugadores
    }

    return render(request, 'templates/index.html', data)

from django.shortcuts import redirect
from .forms import JugadorForm


def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm()

    return render(request, 'agregar_jugador.html', {'form': form})


def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'index.html', {'jugadores': jugadores})

from django.shortcuts import get_object_or_404

def eliminar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    
    if request.method == 'POST':
        jugador.delete()
        return redirect('jugadores') 
    
    return render(request, 'eliminar_jugador.html', {'jugador': jugador})


def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)

    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('jugadores')
    else:
        form = JugadorForm(instance=jugador)

    return render(request, 'editar_jugador.html', {'form': form, 'jugador': jugador})

from django.shortcuts import render, redirect
from .forms import PartidoForm

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_partidos')
    else:
        form = PartidoForm()

    return render(request, 'crear_partido.html', {'form': form})

def lista_partidos(request):
    partidos = Partido.objects.all()
    return render(request, 'lista_partidos.html', {'partidos': partidos})
