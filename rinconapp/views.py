from django.shortcuts import render
from .models import Cliente, Reserva
from rinconapp.forms import ReservaFormulario

def lista_clientes(request):
    cliente = Cliente.objects.all()
    return render(request, "rinconapp/cliente.html", {'cliente': cliente})


def mostrar_calendario_reservas(request):
    return render(request, "rinconapp/calendario.html")

def vista_padre(request):
    return render(request, 'rinconapp/padre.html')

def reserva_formulario(request):
    """
    if request.method == 'POST':
        cliente = Cliente(nombre =request.POST['nombre'], apellido=request.POST['apellido'], telefono=request.POST['telefono'], email=request.POST['email'])
        reserva = Reserva(fecha=request.POST['fecha'], plaza=request.POST['plaza'], direccion=request.POST['direccion'],
                          seña=request.POST['seña'])
        cliente.save()
        reserva.save()
        return render(request, 'rinconapp/reserva.html')
    
    return render(request, 'rinconapp/reserva.html')

    """
    if request.method == 'POST':
        mi_formulario = ReservaFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            cliente = Cliente(nombre=informacion['nombre'], apellido=informacion['apellido'], telefono=informacion['telefono'], email=informacion['email'])
            cliente.save()

            reserva = Reserva(fecha=informacion['fecha'], plaza=informacion['plaza'], direccion=informacion['direccion'])
            reserva.save()

            return render(request, 'rinconapp/reserva.html')    
    
    return render(request, 'rinconapp/reserva.html')

