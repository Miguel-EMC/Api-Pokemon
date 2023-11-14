from django.urls import path
from . import views

urlpatterns = [
    # URL para mostrar detalles de un Pokémon específico
    path('pokemon/<str:name>/', views.pokemon_detail, name='pokemon_detail'),

    # URL para mostrar la lista de Pokémon
    path('', views.pokemon_lista, name='pokemon_list'),
]
