# app_socios/urls.py

from django.urls import path
from .views import agregar_jugador  # Importa tu vista
from .views import lista_jugadores

urlpatterns = [
    # Otras URL de app_socios...
    path('agregar-jugador/', agregar_jugador, name='agregar_jugador'),
    path('lista-jugadores/', lista_jugadores, name='jugadores'),
]
