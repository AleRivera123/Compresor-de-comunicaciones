import sys
sys.path.append("src")

# Definición de excepciones personalizadas
class DuplicateEntryError(Exception):
    """Excepción para entradas duplicadas en la base de datos."""
    pass

class EntryNotFoundError(Exception):
    """Excepción para búsquedas de entradas que no existen en la base de datos."""
    pass

class DataValidationError(Exception):
    """Excepción para datos de entrada inválidos."""
    pass

class EventTypeError(Exception):
    """Excepción para tipos de eventos no soportados."""
    pass

# Clase para manejar la entrada de usuario
class UserInput:
    def __init__(self, nombre, cedula, telefono, correo, texto_original, tipo_evento):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.texto_original = texto_original
        self.tipo_evento = tipo_evento

    def validate(self):
        if not all([self.nombre, self.cedula, self.correo, self.telefono, self.texto_original, self.tipo_evento]):
            raise DataValidationError("Todos los campos son requeridos.")
        
        if self.tipo_evento not in ['comprimir', 'descomprimir']:
            raise EventTypeError("Tipo de evento inválido. Debe ser 'comprimir' o 'descomprimir'.")

        self.validate_email(self.correo)

    @staticmethod
    def validate_email(email):
        import re
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise DataValidationError("Correo electrónico inválido.")

    # Validación de existencia utilizando una función externa de verificación
    @staticmethod
    def check_primary_key(cedula, db_check_func):
        if db_check_func(cedula):
            raise DuplicateEntryError(f"Ya existe un usuario con la cédula {cedula}.")

# Clase para manejar la salida de usuario
class UserOutput:
    @staticmethod
    def validate_user_found(found, operation):
        if not found:
            raise EntryNotFoundError(f"Usuario no encontrado para la operación: {operation}.")
