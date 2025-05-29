from django import forms


class formulario_reserva(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=20)
    nombre_plaza = forms.CharField(max_length=100)
    pago = forms.DecimalField(max_digits=10, decimal_places=2)
    fecha_evento = forms.DateField()
    hora_evento = forms.TimeField()
    direccion_evento = forms.CharField(max_length=255)


    def __str__(self):
        return f"{self.nombre}{self.telefono}{self.nombre_plaza}{self.pago}{self.fecha_evento}{self.hora_evento}{self.direccion_evento}" 