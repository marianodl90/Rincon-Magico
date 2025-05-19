from django.urls import path
from .views import lista_clientes, mostrar_calendario_reservas, vista_padre, reserva_formulario

urlpatterns =[
    path('inicio/', vista_padre, name='inicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('calendario/', mostrar_calendario_reservas, name= 'mostrar_calendario_reservas'),
    path('', reserva_formulario, name='reserva_formulario'),
    
]