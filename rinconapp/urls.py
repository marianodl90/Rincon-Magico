from django.urls import path
from .views import lista_clientes, mostrar_reservas

urlpatterns =[
    path('clientes/', lista_clientes, name='lista_clientes'),
    path('reservas/', mostrar_reservas, name='mostrar_reservas'),
]