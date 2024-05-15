import unittest
import sys
sys.path.append("compresor_de_comunicaciones/")  # Incluye la ruta del directorio donde se encuentran los módulos del proyecto.
sys.path.append("./")  # Incluye el directorio actual para facilitar la importación de módulos.

# Importaciones de clases desde los módulos específicos del proyecto.
from src.model.Usuario import UserInput, DuplicateEntryError, EntryNotFoundError, DataValidationError
from src.controller.ControladorUsuarios import UserData

# Definición de la clase de prueba, que utiliza unittest.TestCase para aprovechar las funcionalidades de prueba unitaria.
class TestDatabaseOperations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """ Método de clase que se ejecuta antes de todas las pruebas de la clase.
        Se utiliza para preparativos que son comunes a todas las pruebas, como configurar la base de datos.
        """
        UserData.create_table()  # Crea la tabla de usuarios en la base de datos antes de ejecutar las pruebas.

    @classmethod
    def tearDownClass(cls):
        """ Método de clase que se ejecuta después de todas las pruebas de la clase.
        Se utiliza para limpiar recursos, como eliminar la tabla de usuarios de la base de datos.
        """
        UserData.drop_table()  # Elimina la tabla de usuarios para limpiar la base de datos después de las pruebas.

    def test_insert_user(self):
        """ Prueba la inserción de un usuario en la base de datos.
        Verifica que el usuario se inserte correctamente y que los datos insertados se puedan recuperar.
        """
        user = UserInput('Jorge', '123456789', '3001234567', 'jorge@example.com', 'Hola mundo', 'insert')
        user.validate()  # Valida los datos del usuario antes de intentar insertarlos en la base de datos.
        UserData.insert_user(user.cedula, user.nombre, user.telefono, user.correo, user.tipo_evento, user.texto_original, '')
        result = UserData.query_user(user.cedula)  # Consulta el usuario insertado por cédula.
        self.assertIsNotNone(result)  # Asegura que el resultado no sea None.
        self.assertEqual(result[1], user.nombre)  # Compara el nombre del resultado con el nombre del usuario insertado.

    def test_update_user(self):
        """ Prueba la actualización de la información de un usuario en la base de datos.
        Verifica que la actualización del campo especificado cambie correctamente en la base de datos.
        """
        user = UserInput('Ana', '987654321', '3007654321', 'ana@example.com', 'Texto para Ana', 'update')
        user.validate()
        UserData.insert_user(user.cedula, user.nombre, user.telefono, user.correo, user.tipo_evento, user.texto_original, '')
        UserData.update_user(user.cedula, 'Telefono', '3019876543')  # Actualiza el teléfono del usuario.
        updated_user = UserData.query_user(user.cedula)
        self.assertEqual(str(updated_user[2]), '3019876543')  # Comprueba que el teléfono actualizado sea el esperado.

    def test_delete_user(self):
        """ Prueba la eliminación de un usuario de la base de datos.
        Verifica que después de eliminar un usuario, una consulta por su cédula no devuelva resultados.
        """
        user = UserInput('Luis', '111222333', '3101234567', 'luis@example.com', 'Texto para eliminar', 'delete')
        user.validate()
        UserData.insert_user(user.cedula, user.nombre, user.telefono, user.correo, user.tipo_evento, user.texto_original, '')
        UserData.delete_user(user.cedula)
        with self.assertRaises(EntryNotFoundError):  # Espera que se levante una excepción al buscar un usuario eliminado.
            UserData.query_user(user.cedula)

    def test_entry_not_found_exception(self):
        """ Verifica que la función maneje correctamente cuando un usuario no se encuentra.
        Esto se prueba intentando consultar un usuario con una cédula que no existe.
        """
        with self.assertRaises(EntryNotFoundError):
            UserData.query_user('000000000')

    def test_invalid_data_entry_exception(self):
        """ Prueba la validación de datos al intentar insertar un usuario con información incompleta.
        Se espera que se levante una excepción DataValidationError debido a datos incompletos.
        """
        user = UserInput('', '', '', 'invalid@example.com', 'Prueba de validación', 'insert')
        with self.assertRaises(DataValidationError):
            user.validate()
            UserData.insert_user(user.cedula, user.nombre, user.telefono, user.correo, user.tipo_evento, user.texto_original, '')

if __name__ == '__main__':
    unittest.main()  # Ejecuta todas las pruebas definidas en la clase TestDatabaseOperations.
