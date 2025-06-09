from django.shortcuts import render, redirect
from .models import Cliente, Plaza, Reserva
from rinconapp.forms import formulario_reserva
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseBadRequest
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required





def vista_padre(request):
    return render(request, 'rinconapp/padre.html')

@login_required
def lista_clientes(request):
    reservas = Reserva.objects.select_related('cliente', 'plaza').all()
    return render(request, "rinconapp/cliente.html", {'reservas': reservas})


@login_required
def reserva_formulario(request):
    if request.method == "POST":
        mi_formulario = formulario_reserva(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data

            cliente, _ = Cliente.objects.get_or_create(
                nombre=informacion['nombre'],
                telefono=informacion['telefono']
            )

            plaza, _ = Plaza.objects.get_or_create(
                nombre_plaza=informacion['nombre_plaza'],
                pago=informacion['pago']
            )

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


def eliminar_cliente_y_reserva(request,id):

    reserva = Reserva.objects.get(id=id)
    cliente = reserva.cliente
    Reserva.objects.filter(cliente=cliente).delete()
    cliente.delete()
    return redirect('lista_clientes')



def actualizar_cliente_y_reserva(request, id):
    reserva = Reserva.objects.get(id=id)
    cliente = reserva.cliente
    plaza = reserva.plaza

    if request.method == "POST":
        mi_formulario = formulario_reserva(request.POST)
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data

            cliente.nombre = datos["nombre"]
            cliente.telefono = datos["telefono"]
            cliente.save()

            plaza.nombre_plaza = datos["nombre_plaza"]
            plaza.pago = datos["pago"]
            plaza.save()

            reserva.fecha_evento = datos["fecha_evento"]
            reserva.hora_evento = datos["hora_evento"]
            reserva.direccion_evento = datos["direccion_evento"]
            reserva.save()

            return render(request, 'rinconapp/cliente.html', {"reserva":reserva})
        return HttpResponseBadRequest("Formulario inválido. LLene los campos con datos validos (horario xx : xx)")

        

    else:
        datos_iniciales = {
            "nombre": cliente.nombre,
            "telefono": cliente.telefono,
            "nombre_plaza": plaza.nombre_plaza,
            "pago": plaza.pago,
            "fecha_evento": reserva.fecha_evento,
            "hora_evento": reserva.hora_evento,
            "direccion_evento": reserva.direccion_evento
        }
        mi_formulario = formulario_reserva(initial=datos_iniciales)
    
    return render(request, "rinconapp/editar_cliente.html", {"mi_formulario": mi_formulario, "reserva": reserva})


#def login_cliente(request): "EJEMPLO DEL PROFESOR"

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) 
        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

        user = authenticate(username= usuario, password= contra)
        if user is not None:  #Es lo mismo que preguntar si existe el user
            login(request, user)
            return render(request, "rinconapp/inicio.html", {"mensaje" : f"Bienvenido/a: {usuario}"})
        else:
            return HttpResponse("Usuario no encontrado")

    form = AuthenticationForm()
    return render(request, "rinconapp/login.html", {"form": form})
        


    #EJEMPLO DEL PROFESOR PERO CON VALIDACION PARA USAR SIEMPRE UN FORMULARIO VALIDO. SI NO HAY FORMULARIO RETORNA NUEVAMENTE EL TEMPLATE DE LOGIN.
def login_cliente(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contra)

            if user is not None: #Es lo mismo que preguntar si existe el user
                login(request, user)
                return render(request, "rinconapp/inicio.html", {"mensaje": f"Bienvenido/a: {usuario}"})
            else:
                return render(request, "rinconapp/login.html", {
                    "form": form,
                    "error": "Usuario no encontrado o contraseña incorrecta."
                })
        else:
            return render(request, "rinconapp/login.html", {
                "form": form,
                "error": "Formulario inválido. Revisa los datos ingresados."
            })

    
    form = AuthenticationForm()
    return render(request, "rinconapp/login.html", {"form": form})

def logout_view(request):
    logout(request)
    return render(request, 'rinconapp/logout.html')

@login_required
def productos(request):
    return render(request, "rinconapp/productos.html")

def registro_cliente(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Cliente creado con exito")
        
    else:
        form = UserCreationForm()
        
    return render(request, "rinconapp/registro.html", {"form": form})
