# Jerarquía de errores
class ErrorSoftwareFJ(Exception):
    """Clase base para todos los errores de nuestra empresa"""
    pass

class ErrorValidacion(ErrorSoftwareFJ):
    """Se lanzará cuando un dato (nombre o ID) sea inválido"""
    pass

class ErrorServicio(ErrorSoftwareFJ):
    """Se lanzará cuando algo falle específicamente con una reserva o servicio"""
    pass