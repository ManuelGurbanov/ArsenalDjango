
from django.contrib import admin
from django.urls import path

from django.urls import include
from .views import InicioView, StatsView, SocioView, ContactoView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name="landing_page"),
    path('stats/', StatsView.as_view(), name="stats"),
    path('socio/', SocioView.as_view(), name="socio"),
    path('contacto/', ContactoView.as_view(), name="contacto"),
    path('app_equipo/', include('app_equipo.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)