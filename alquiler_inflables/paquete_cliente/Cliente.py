from datetime import datetime
from paquete_cliente.Reserva import Reserva


class Persona:
    def __init__(self, nombre:str, apellido:str):
        self.nombre = nombre
        self.apellido = apellido
        

class Cliente (Persona):
    def __init__(self, nombre:str, apellido:str, telefono:int):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.reservas = []
  
    def __str__(self):
         return f"Reserva realizada \nEl nombre del cliente es {self.nombre} {self.apellido}, y su telefono es {self.telefono}"

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
        
    def mostrar_reserva(self):
        if not self.reservas:
            print("No existe reserva")
        else:
            print(self.reservas[-1])

            
    def eliminar_reserva(self, indice: int):
        if 0 <= indice < len(self.reservas):
            reserva_eliminada = self.reservas.pop(indice)
            print("Reserva eliminada")
        else:
            print("Índice de reserva inválido.")



