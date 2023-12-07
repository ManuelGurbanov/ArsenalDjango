from django import forms
from .models import Jugador  # Asumiendo que tienes un modelo Jugador en models.py

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'edad', 'posicion']
