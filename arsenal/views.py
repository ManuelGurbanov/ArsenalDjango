from django.views.generic import TemplateView
from app_equipo.models import Jugador, Partido
from django.shortcuts import render

class InicioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jugadores'] = Jugador.objects.all()
        return context
    
class StatsView(TemplateView):
    template_name = "stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partidos'] = Partido.objects.all()
        return context

class SocioView(TemplateView):
    template_name = "socio.html"

class ContactoView(TemplateView):
    template_name = "contacto.html"