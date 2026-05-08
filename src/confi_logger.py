import logging

# Archivo de errores
logging.basicConfig(
    filename='registro_eventos.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_error(mensaje):
    logging.error(mensaje)
    print(f"Error registrado: {mensaje}")