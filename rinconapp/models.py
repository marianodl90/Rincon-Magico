import time
from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    

    def __str__(self):
        return f"{self.nombre}{self.telefono}"
    

    

class Plaza(models.Model):
    nombre_plaza = models.CharField(max_length=100)
    pago = models.DecimalField(max_digits= 10, decimal_places=2)
   

    def __str__(self):
        return f"{self.nombre_plaza}{self.pago}"
    

class Reserva(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, default=1)
    plaza = models.ForeignKey(Plaza, on_delete=models.CASCADE, default=1)
    fecha_evento = models.DateField(default=timezone.now)
    hora_evento = models.TimeField()
    direccion_evento = models.CharField(max_length=255, default="Por definir")

    def __str__(self):
        return f"{self.cliente}{self.plaza}{self.fecha_evento}{self.hora_evento}{self.direccion_evento}"