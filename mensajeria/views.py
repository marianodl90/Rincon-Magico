from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import MensajeForm
from .models import Mensaje
from django.contrib.auth.decorators import login_required

@login_required
def enviar_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()
    return render(request, 'mensajeria/enviar_mensaje.html', {'form': form})

@login_required
def bandeja_entrada(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user).order_by('-fecha_envio')
    return render(request, 'mensajeria/bandeja_entrada.html', {'mensajes': mensajes})
