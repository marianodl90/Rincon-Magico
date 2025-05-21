from django import forms

class formulario_reserva(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.IntegerField()
    nombre_plaza = forms.CharField(max_length=100)
    pago = forms.CharField(max_length=100)
    fecha_evento = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    hora_evento = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    direccion_evento = forms.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre}{self.telefono}{self.nombre_plaza}{self.pago}{self.fecha_evento}{self.hora_evento}{self.direccion_evento}" 
