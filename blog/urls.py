from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('', views.home_view, name='home'),  # Ejemplo de ruta para la vista de inicio

]
