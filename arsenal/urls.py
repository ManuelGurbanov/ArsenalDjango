
from django.contrib import admin
from django.urls import path
from .views import InicioView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', InicioView.as_view(), name="landing_page")
]
