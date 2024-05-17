import psycopg2
import unittest
import sys
sys.path.append("compresor_de_comunicaciones/")  # Incluye la ruta del directorio donde se encuentran los módulos del proyecto.
sys.path.append("./")  # Incluye el directorio actual para facilitar la importación de módulos.

# Importaciones de clases desde los módulos específicos del proyecto.
from src.model.Usuario import UserInput, DuplicateEntryError, EntryNotFoundError, DataValidationError
from src.controller.ControladorUsuarios import UserData


class TestUserData(unittest.TestCase):

    def setUp(self):
        UserData.create_table()

    def tearDown(self):
        UserData.drop_table()

    # Pruebas para insert_user
    def test_insert_user_valid(self):
        """Prueba de inserción de un usuario con datos válidos."""
        try:
            UserData.insert_user(123, 'John Doe', 5551234, 'john@example.com', 'comprimir', 'texto original', 'texto procesado')
        except Exception as e:
            self.fail(f'Insert valid user raised an exception {e}')

    def test_insert_user_duplicate(self):
        """Prueba de inserción de un usuario duplicado para verificar que la excepción DuplicateEntryError es manejada."""
        UserData.insert_user(123, 'John Doe', 5551234, 'john@example.com', 'comprimir', 'texto original', 'texto procesado')
        with self.assertRaises(DuplicateEntryError):
            UserData.insert_user(123, 'John Doe', 5551234, 'john@example.com', 'comprimir', 'texto original', 'texto procesado')

    def test_insert_user_invalid_email(self):
        """Prueba de inserción de un usuario con correo electrónico inválido para verificar que la excepción DataValidationError es manejada."""
        with self.assertRaises(DataValidationError):
            UserData.insert_user(124, 'Jane Doe', 5555678, 'invalid-email', 'comprimir', 'texto original', 'texto procesado')

    # Pruebas para delete_user
    def test_delete_user_valid(self):
        """Prueba de eliminación de un usuario existente."""
        UserData.insert_user(127, 'John Smith', 5551234, 'john.smith@example.com', 'comprimir', 'texto original', 'texto procesado')
        try:
            UserData.delete_user(127)
        except Exception as e:
            self.fail(f'Delete valid user raised an exception {e}')

    def test_delete_user_nonexistent(self):
        """Prueba de eliminación de un usuario que no existe para verificar que la excepción EntryNotFoundError es manejada."""
        with self.assertRaises(EntryNotFoundError):
            UserData.delete_user(999)

    def test_delete_user_invalid_id(self):
        """Prueba de eliminación de un usuario con ID inválido para verificar que la excepción DataValidationError es manejada."""
        with self.assertRaises(DataValidationError):
            UserData.delete_user('invalid-id')

    # Pruebas para update_user
    def test_update_user_valid(self):
        """Prueba de actualización válida de un usuario."""
        UserData.insert_user(128, 'Jane Smith', 5559876, 'jane@example.com', 'comprimir', 'texto original', 'texto procesado')
        try:
            UserData.update_user(128, 'Nombre', 'Jane Doe')
        except Exception as e:
            self.fail(f'Valid update user raised an exception {e}')

    def test_update_user_nonexistent(self):
        """Prueba de actualización de un usuario que no existe para verificar que la excepción EntryNotFoundError es manejada."""
        with self.assertRaises(EntryNotFoundError):
            UserData.update_user(999, 'Nombre', 'New Name')

    def test_update_user_invalid_field(self):
        """Prueba de actualización de un campo que no existe en la base de datos para verificar que la excepción es manejada."""
        UserData.insert_user(129, 'John Update', 5559876, 'john.update@example.com', 'comprimir', 'texto original', 'texto procesado')
        with self.assertRaises(Exception):  # Aquí puedes usar una excepción más específica si es necesario
            UserData.update_user(129, 'CampoInexistente', 'valor')

    # Pruebas para query_user
    def test_query_user_valid(self):
        """Prueba de consulta de un usuario existente para verificar que no hay errores."""
        UserData.insert_user(131, 'John Query', 5551111, 'johnq@example.com', 'comprimir', 'texto original', 'texto procesado')
        result = UserData.query_user(131)
        self.assertIsNotNone(result)
        self.assertEqual(result[0], 131)

    def test_query_user_nonexistent(self):
        """Prueba de consulta de un usuario que no existe para verificar que la excepción EntryNotFoundError es manejada."""
        with self.assertRaises(EntryNotFoundError):
            UserData.query_user(999)

    def test_query_user_invalid_id(self):
        """Prueba de consulta de un usuario con ID inválido para verificar que la excepción DataValidationError es manejada."""
        with self.assertRaises(DataValidationError):
            UserData.query_user('invalid-id')

if __name__ == '__main__':
    unittest.main()
