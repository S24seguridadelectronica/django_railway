from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_home, name='home'),  # Asegúrate de tener al menos una ruta definida
]
