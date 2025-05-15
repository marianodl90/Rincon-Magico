from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}{self.apellido}{self.telefono}{self.email}"
    
class Reserva(models.Model):
    fecha = models.DateField()
    plaza = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    seña = models.IntegerField()

    def __str__(self):
        return f"{self.fecha}{self.plaza}{self.direccion}{self.seña}"
    

class Calendario(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"{self.fecha}{self.hora}"
    

