from django.urls import path
from . import views

urlpatterns = [
    path('enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('bandeja/', views.bandeja_entrada, name='bandeja_entrada'),
]
