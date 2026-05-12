from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from confi_logger import registrar_error

def ejecutar_simulacion():
    print("====================================================")
    print("   SISTEMA DE GESTIÓN SOFTWARE FJ - SIMULACIÓN")
    print("====================================================\n")

    # 1. Creamos algunos clientes
    cliente_valido = Cliente(101, "Juan Perez", "juan.perez@email.com")
    cliente_anonimo = Cliente(404, "Desconocido", "anonimo@email.com")

    # 2. Creamos los servicios disponibles
    sala_reunion = ReservaSala(1, "Sala de Juntas A", 50000)
    laptop_pro = AlquilerEquipo(2, "MacBook Pro", 80000, 200000)
    asesoria = AsesoriaEspecializada(3, "Consultoría Java", 120000)

    # 3. Lista de operaciones a simular (10 casos)
    # Formato: (Cliente, Servicio, Cantidad, Nota)
    operaciones = [
        (cliente_valido, sala_reunion, 3, "Reserva exitosa"),
        (cliente_valido, laptop_pro, 2, "Alquiler exitoso"),
        (cliente_valido, asesoria, 1, "Asesoría normal"),
        (cliente_valido, sala_reunion, -5, "ERROR: Horas negativas"),
        (cliente_anonimo, asesoria, 2, "Asesoría para otro cliente"),
        (cliente_valido, laptop_pro, 0, "ERROR: Cantidad cero"),
        (cliente_valido, sala_reunion, 10, "Reserva larga"),
        (cliente_anonimo, laptop_pro, 5, "Alquiler largo"),
        (cliente_valido, asesoria, 4, "Asesoría extensa"),
        (cliente_anonimo, sala_reunion, 1, "Última operación exitosa")
    ]

    # 4. Ejecución de las 10 operaciones
    contador = 1
    for c, s, cant, nota in operaciones:
        print(f"Operación #{contador}: [{nota}]")
        reserva = Reserva(c, s, cant)
        reserva.procesar_reserva()
        contador += 1

    print("\n====================================================")
    print("   SIMULACIÓN FINALIZADA - REVISE registro_eventos.log")
    print("====================================================")

if __name__ == "__main__":
    try:
        ejecutar_simulacion()
    except Exception as e:
        registrar_error(f"Error fatal en el sistema: {e}")
        print("El sistema sufrió un error inesperado, pero se registró en el log.")