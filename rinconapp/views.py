from django.shortcuts import render
from .models import Cliente, Plaza, Reserva
from rinconapp.forms import formulario_reserva


def vista_padre(request):
    return render(request, 'rinconapp/padre.html')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "rinconapp/cliente.html", {'clientes': clientes})



def reserva_formulario(request):
    if request.method == "POST":
        mi_formulario = formulario_reserva(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            # Buscar o crear cliente
            cliente, _ = Cliente.objects.get_or_create(
                nombre=informacion['nombre'],
                telefono=informacion['telefono']
            )

            # Buscar o crear plaza (opcional)
            plaza, _ = Plaza.objects.get_or_create(
                nombre_plaza=informacion['nombre_plaza'],
                pago=informacion['pago']
            )

            # Crear reserva
            reserva = Reserva(
                cliente=cliente,
                plaza=plaza,
                fecha_evento=informacion['fecha_evento'],
                hora_evento=informacion['hora_evento'],
                direccion_evento=informacion['direccion_evento']
            )
            reserva.save()

            return render(request, 'rinconapp/reserva.html')    

    return render(request, 'rinconapp/reserva.html')
