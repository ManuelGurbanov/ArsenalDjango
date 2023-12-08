
from django.contrib import admin
from django.urls import path

from django.urls import include
from .views import InicioView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name="landing_page"),

    path('app_socios/', include('app_socios.urls')),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)