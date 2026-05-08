from abc import ABC, abstractmethod # Clases abstractas

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad 

    @property
    def id_entidad(self):
        """Este es un 'getter': permite leer el ID pero no cambiarlo fácilmente"""
        return self._id_entidad

    @abstractmethod
    def mostrar_detalle(self):
        """Método obligatorio para quien herede de esta clase"""
        pass