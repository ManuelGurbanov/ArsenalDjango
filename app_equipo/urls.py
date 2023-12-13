# app_equipo/urls.py

from django.urls import path
from .views import agregar_jugador, eliminar_jugador, editar_jugador
from .views import lista_jugadores

from .views import crear_partido
from .views import lista_partidos

urlpatterns = [
    path('agregar-jugador/', agregar_jugador, name='agregar_jugador'),
    path('..', lista_jugadores, name='jugadores'),
    path('eliminar-jugador/<int:jugador_id>/', eliminar_jugador, name='eliminar_jugador'),
    path('editar-jugador/<int:jugador_id>/', editar_jugador, name='editar_jugador'),

    path('crear_partido/', crear_partido, name='crear_partido'),
    path('lista_partidos/', lista_partidos, name='partidos'),
]
