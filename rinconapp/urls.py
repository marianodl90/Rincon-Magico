from django.urls import path
from .views import lista_clientes, mostrar_reservas, mostrar_calendario_reservas, vista_padre

urlpatterns =[
    path('inicio/', vista_padre, name='inicio'),
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('reservas/', mostrar_reservas, name='mostrar_reservas'),
    path('calendario/', mostrar_calendario_reservas, name= 'mostrar_calendario_reservas'),

]