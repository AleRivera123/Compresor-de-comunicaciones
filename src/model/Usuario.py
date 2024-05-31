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
        # Verifica que todos los campos requeridos estén presentes
        if not self.nombre or not self.cedula or not self.telefono or not self.correo or not self.texto_original or not self.tipo_evento:
            print("Falta un campo requerido")
            return False
        # Verifica que la cédula y el teléfono sean números
        if not self.cedula.isdigit() or not self.telefono.isdigit():
            print("Cédula o teléfono no son números")
            return False
        # Verifica que el correo tenga un formato válido
        if "@" not in self.correo:
            print("Correo no tiene formato válido")
            return False
        # Verifica que tipo_evento sea "Comprimir" o "Descomprimir"
        if self.tipo_evento not in ["Comprimir", "Descomprimir"]:
            print("Tipo de evento no es válido")
            return False
        return True

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
