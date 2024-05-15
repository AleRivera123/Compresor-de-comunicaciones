import unittest

import sys
sys.path.append("compresor_de_comunicaciones/")
sys.path.append("./")

from src.controller.ControladorUsuarios import UserData

#from src.model.usuarios import UserData  # Asegúrate de que este sea el módulo correcto donde está la lógica de la DB


class DatabaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configura la base de datos antes de todas las pruebas."""
        UserData.create_table()

    @classmethod
    def tearDownClass(cls):
        """Limpia la base de datos después de todas las pruebas."""
        UserData.drop_table()

    def test_insert_user(self):
        """Prueba la inserción de un usuario."""
        UserData.insert_user(123456, 'Carlos', 9876543210, 'carlos@example.com', 'insert', 'some text', '')
        result = UserData.query_user(123456)
        self.assertIsNotNone(result)
        self.assertEqual(result[1], 'Carlos')

    def test_update_user(self):
        """Prueba la actualización de información de un usuario."""
        UserData.insert_user(654321, 'Ana', 1234567890, 'ana@example.com', 'update', 'some text', '')
        UserData.update_user(654321, 'telefono', 1122334455)
        result = UserData.query_user(654321)
        self.assertEqual(result[2], 1122334455)

    def test_delete_user(self):
        """Prueba la eliminación de un usuario."""
        UserData.insert_user(111222, 'Luis', 3334445556, 'luis@example.com', 'delete', 'text here', '')
        UserData.delete_user(111222)
        result = UserData.query_user(111222)
        self.assertIsNone(result)

    def test_query_nonexistent_user(self):
        """Prueba la consulta de un usuario que no existe."""
        result = UserData.query_user(999999)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
