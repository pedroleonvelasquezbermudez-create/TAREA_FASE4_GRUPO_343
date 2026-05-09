from entidades import EntidadBase
from abc import abstractmethod

class Servicio(EntidadBase):
    def __init__(self, id_servicio, nombre_servicio, precio_base):
        super().__init__(id_servicio)
        self._nombre_servicio = nombre_servicio
        self._precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        """Método abstracto que cada hijo debe implementar de forma única"""
        pass

# --- Ejemplo de Servicio 1: Reserva de Salas ---
class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        # Aquí el polimorfismo: el costo es por hora
        return self._precio_base * horas

    def mostrar_detalle(self):
        return f"SALA: {self._nombre_servicio} | Precio por hora: ${self._precio_base}"