from datetime import datetime


class Reserva:
    def __init__(self, fecha, plaza:str, direccion:str, seña:int):
        self.fecha = datetime(*fecha)
        self.plaza = plaza
        self.direccion = direccion
        self.seña = seña
        
    def __str__(self):
        fecha_formateada = self.fecha.strftime('%d/%m/%Y %H:%M')
        return f"Se reservo {self.plaza} el dia {fecha_formateada} en la dirección {self.direccion}, y se pago de seña {self.seña} pesos"
    

