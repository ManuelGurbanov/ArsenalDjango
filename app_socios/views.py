from django.shortcuts import render

# Create your views here.
from .models import Jugador
def home(request):
    jugadores = Jugador.objects.all()
    data = {
        'jugadores': jugadores
    }

    return render(request, 'templates/index.html', data)