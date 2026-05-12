from entidades import EntidadBase
from excepciones import ErrorServicio

class Servicio(EntidadBase):
    """Clase abstracta para los servicios de Software FJ."""
    def __init__(self, id_servicio, nombre_servicio, precio_base):
        super().__init__(id_servicio)
        self._nombre_servicio = nombre_servicio
        self._precio_base = precio_base

    def calcular_costo(self, cantidad):
        pass

    def mostrar_detalle(self):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas):
        return self._precio_base * horas

    def mostrar_detalle(self):
        return f"SALA: {self._nombre_servicio} | Precio/Hora: ${self._precio_base}"

class AlquilerEquipo(Servicio):
    def __init__(self, id_servicio, nombre_servicio, precio_base, deposito):
        super().__init__(id_servicio, nombre_servicio, precio_base)
        self.__deposito = deposito

    def calcular_costo(self, dias):
        return (self._precio_base * dias) + self.__deposito

    def mostrar_detalle(self):
        return f"EQUIPO: {self._nombre_servicio} | Diario: ${self._precio_base} | Depósito: ${self.__deposito}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, nivel_urgencia="Normal"):
        costo = self._precio_base * horas
        if nivel_urgencia == "Urgente":
            costo *= 1.5
        return costo

    def mostrar_detalle(self):
        return f"ASESORÍA: {self._nombre_servicio} | Precio/Hora Base: ${self._precio_base}"