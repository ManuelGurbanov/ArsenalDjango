from django.shortcuts import render

# Create your views here.
from .models import Jugador
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
        form = JugadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jugadores')  # Asegúrate de que esté 'jugadores' aquí
    else:
        form = JugadorForm()

    return render(request, 'index.html', {'form': form})


def lista_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'index.html', {'jugadores': jugadores})

from django.shortcuts import get_object_or_404

def eliminar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, id=jugador_id)
    
    if request.method == 'POST':
        jugador.delete()
        return redirect('jugadores')  # O redirige a la vista que muestra la lista de jugadores
    
    return render(request, 'eliminar_jugador.html', {'jugador': jugador})