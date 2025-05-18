from django.shortcuts import render
from .models import Cliente, Reserva, Calendario

def lista_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, "rinconapp/cliente.html", {'cliente': cliente})


def mostrar_reservas(request):
    reserva = Reserva.objects.all()
    return render(request, "rinconapp/reserva.html", {'reserva': reserva})

def mostrar_calendario_reservas(request):
    return render(request, "rinconapp/calendario.html")

def vista_padre(request):
    return render(request, 'rinconapp/padre.html')

