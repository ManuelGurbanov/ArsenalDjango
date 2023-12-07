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