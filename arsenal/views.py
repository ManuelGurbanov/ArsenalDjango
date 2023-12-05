from django.views.generic import TemplateView
from app_socios.models import Jugador  # Asegúrate de importar tu modelo Jugador
class InicioView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['jugadors'] = Jugador.objects.all()
        return context