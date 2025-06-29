from django.urls import path
from . import views
from rinconapp.forms import formulario_reserva



urlpatterns =[
    path('inicio/', views.vista_padre, name='inicio'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('reserva/', views.reserva_formulario, name='reserva_formulario'),
    path('eliminar/<int:id>', views.eliminar_cliente_y_reserva, name='eliminar_cliente_y_reserva'),
    path('actualizar/<int:id>', views.actualizar_cliente_y_reserva, name='actualizar_cliente_y_reserva'),
    path('login/', views.login_cliente, name='login_cliente'),
    path('productos/', views.productos, name='productos'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registro_cliente, name='registro_cliente'),
    path('me/', views.sobre_mi, name='sobre_mi'),
]

