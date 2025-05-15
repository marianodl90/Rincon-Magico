from django.shortcuts import render, get_object_or_404
from .models import Cliente, Reserva

def lista_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, "rinconapp/cliente.html", {'cliente': cliente})


def mostrar_reservas(request):
    reserva = Reserva.objects.all()
    return render(request, "rinconapp/reserva.html", {'reserva': reserva})

def mostrar_calendario_reservas(request):
    return render(request, "rinconapp/calendario.html")
