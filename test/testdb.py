import sys
sys.path.append("src")
from compressor.compressorlogic import *
import compressor.compressorlogic as compressor

# Definición de excepciones personalizadas
class DuplicateEntryError(Exception):
    pass

class EntryNotFoundError(Exception):
    pass

class DataValidationError(Exception):
    pass

class UpdateNotFoundError(Exception):
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
        self.fecha_hora = None

    def is_equal(self, other):
        """Compara esta instancia con otra para asegurarse de que son iguales."""
        return (self.nombre == other.nombre and
                self.cedula == other.cedula and
                self.telefono == other.telefono and
                self.correo == other.correo and
                self.texto_original == other.texto_original and
                self.tipo_evento == other.tipo_evento)

    # Otras funciones...

    def validate(self):
        # Validar que todos los campos necesarios están presentes
        if not all([self.nombre, self.cedula, self.correo, self.telefono, self.texto_original, self.tipo_evento]):
            raise DataValidationError("Todos los campos son requeridos, excepto fecha_hora que se genera automáticamente.")

    @staticmethod
    def primary_key_exists(cedula, controller):
        # Verificar si ya existe un usuario con la misma cédula
        if controller.user_exists(cedula):
            raise DuplicateEntryError(f"Ya existe un usuario con la cédula {cedula}.")

# Clase para manejar la salida de usuario
class UserOutput:
    def __init__(self, nombre, cedula, telefono, correo, texto_procesado, fecha_hora, tipo_evento):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
        self.texto_procesado = texto_procesado
        self.fecha_hora = fecha_hora
        self.tipo_evento = tipo_evento

    def is_equal(self, other_user):
        # Comparar esta instancia con otra para asegurarse que son iguales
        return all([
            self.nombre == other_user.nombre,
            self.cedula == other_user.cedula,
            self.correo == other_user.correo,
            self.telefono == other_user.telefono,
            self.texto_procesado == other_user.texto_procesado,
            self.fecha_hora == other_user.fecha_hora,
            self.tipo_evento == other_user.tipo_evento
        ])

    @staticmethod
    def user_not_found(user):
        # Verificar si la instancia del usuario no es válida
        if user is None:
            raise EntryNotFoundError("Usuario no encontrado.")
