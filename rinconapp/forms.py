from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente
 
class formulario_reserva(forms.Form):
    nombre = forms.CharField(max_length=100, label="Nombre")
    apellido = forms.CharField(max_length=100, label="Apellido")
    telefono = forms.CharField(max_length=20, label="Teléfono")
    nombre_plaza = forms.CharField(max_length=100, label="Nombre de la Plaza")
    pago = forms.DecimalField(max_digits=10, decimal_places=2, label="Pago")
    fecha_evento = forms.DateField(label="Fecha del Evento")
    hora_evento = forms.TimeField(label="Hora del Evento")
    direccion_evento = forms.CharField(max_length=255, label="Dirección del Evento")

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.telefono}{self.nombre_plaza}{self.pago}{self.fecha_evento}{self.hora_evento}{self.direccion_evento}" 
    
    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get("nombre")
        apellido = cleaned_data.get("apellido")
        telefono = cleaned_data.get("telefono")

        if nombre and apellido and telefono:
            if Cliente.objects.filter(nombre=nombre, apellido=apellido, telefono=telefono).exists():
                raise forms.ValidationError("Este cliente ya está registrado.")

        return cleaned_data


class ClienteRegistroForm(UserCreationForm):
    username = forms.CharField(
        label="Usuario",  
        help_text="Requerido. Máximo 150 caracteres. Letras, números y @/./+/-/_ solamente."
    )
    email = forms.EmailField(
        label="Correo electrónico"
    )
    password1 = forms.CharField(
        label="Contraseña",  
        widget=forms.PasswordInput,
        help_text="Debe contener al menos 8 caracteres, no ser común ni solo numérica."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña", 
        widget=forms.PasswordInput,
        help_text="Reingrese la misma contraseña para confirmar."
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields} 

