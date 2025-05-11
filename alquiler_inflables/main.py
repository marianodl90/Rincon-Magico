from paquete_cliente import Cliente
from paquete_cliente import Reserva



cliente_uno = Cliente("Mariano", "De Luis", 2604654891)
cliente_dos = Cliente("Belen", "De Luis", 2604658965)
cliente_tres = Cliente("Sebastian", "Castro", 2604416169)
cliente_cuatro = Cliente("Pablo", "Rodriguez", 2604788443)

print(cliente_uno)
reserva_uno = Reserva((2025,6,20,15,3), "Pelotero chico", "Los Sauces 3100", 30000)
cliente_uno.agregar_reserva(reserva_uno)
cliente_uno.mostrar_reserva()
cliente_uno.eliminar_reserva(0)

