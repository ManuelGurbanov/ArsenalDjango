from django import forms
from .models import Jugador, Partido

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad', 'posicion', 'imagen_perfil']


class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = ['equipo_local', 'equipo_visitante', 'fecha']
