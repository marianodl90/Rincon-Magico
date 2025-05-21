from django.urls import path
from . import views
from rinconapp.forms import formulario_reserva


urlpatterns =[
    path('inicio/', views.vista_padre, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('reserva/', views.reserva_formulario, name='reserva_formulario'),
    
]