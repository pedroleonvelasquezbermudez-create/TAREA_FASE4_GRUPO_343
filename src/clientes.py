from entidades import EntidadBase
from excepciones import ErrorValidacion
from confi_logger import registrar_error

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, correo):
        # Constructor de la clase padre (EntidadBase)
        super().__init__(id_cliente)
        
        # Usamos validación inmediata para cumplir con la "estabilidad"
        if not nombre or not correo:
            mensaje = f"Intento de registro de cliente {id_cliente} con datos incompletos."
            registrar_error(mensaje)
            raise ErrorValidacion("El nombre y el correo son obligatorios.")
            
        self.__nombre = nombre  # Doble guion bajo (__) para encapsulación estricta (privado)
        self.__correo = correo
        self.__reservas_activas = []

    # Getters: para poder leer los datos privados de forma segura
    @property
    def get_nombre(self):
        return self.__nombre

    # Lo definimos como abstracto en EntidadBase
    def mostrar_detalle(self):
        return f"CLIENTE: {self.__nombre} | ID: {self.id_entidad} | Correo: {self.__correo}"