from django import forms

class ReservaFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    telefono = forms.IntegerField()
    email = forms.EmailField()
    plaza = forms.CharField(max_length=100)
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    direccion = forms.CharField(max_length=100)
    seña = forms.IntegerField(min_value=0)

