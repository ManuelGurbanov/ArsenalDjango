from django.contrib import admin
from .models import Socio, Jugador, Partido

admin.site.register(Socio) 
admin.site.register(Jugador)
admin.site.register(Partido)