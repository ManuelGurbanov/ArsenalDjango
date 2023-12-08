# app_socios/urls.py

from django.urls import path
from .views import agregar_jugador, eliminar_jugador, editar_jugador
from .views import lista_jugadores

urlpatterns = [
    path('agregar-jugador/', agregar_jugador, name='agregar_jugador'),
    path('lista-jugadores/', lista_jugadores, name='jugadores'),
    path('eliminar-jugador/<int:jugador_id>/', eliminar_jugador, name='eliminar_jugador'),
    path('editar-jugador/<int:jugador_id>/', editar_jugador, name='editar_jugador'),
]
