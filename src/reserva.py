from datetime import datetime
from excepciones import ErrorServicio
from confi_logger import registrar_error

class Reserva:
    """
    Clase que gestiona la unión entre un Cliente y un Servicio.
    Aquí se aplica la lógica principal de manejo de excepciones.
    """
    def __init__(self, cliente, servicio, cantidad):
        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad
        self.fecha = datetime.now()

    def procesar_reserva(self):
        # Usamos .get_nombre sin paréntesis si lo definiste como @property
        # O simplemente usa una forma que no falle:
        nombre_cliente = str(self.cliente.get_nombre)
        
        print(f"\n--- Procesando Reserva para: {nombre_cliente} ---")
        try:
            # Simulamos una validación: si la cantidad es 0 o negativa, lanzamos error
            if self.cantidad <= 0:
                raise ErrorServicio("La cantidad de horas o días debe ser mayor a cero.")
            
            # Calculamos el costo usando polimorfismo
            total = self.servicio.calcular_costo(self.cantidad)
            
        except ErrorServicio as e:
            print(f"Error detectado: {e}")
            registrar_error(f"Fallo en reserva de {nombre_cliente}: {e}")
        
        except Exception as e:
            print(f"Error inesperado: {e}")
            registrar_error(f"Error crítico: {e}")
            
        else:
            # Esto solo se ejecuta si el bloque 'try' fue exitoso
            print(f"¡Reserva Exitosa!")
            print(f"Detalle: {self.servicio.mostrar_detalle()}")
            print(f"Total a pagar: ${total}")
            return True
            
        finally:
            # Esto se ejecuta SIEMPRE (haya error o no)
            print(f"Transacción finalizada a las: {self.fecha.strftime('%H:%M:%S')}")
            print("------------------------------------------")

        return False