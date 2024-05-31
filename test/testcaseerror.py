import unittest
import zlib

import sys
sys.path.append("compresor_de_comunicaciones/src")
sys.path.append("./src")

from src.compressor.compressorlogic import *

import src.compressor.compressorlogic as lc

class TestCompresorZlibErrores(unittest.TestCase):
    def setUp(self):
        self.compresor = lc.CompresorZlib()

    # Casos de error para comprimir
    def test_comprimir_entrada_no_string(self):
        with self.assertRaises(TypeError):
            self.compresor.comprimir(1234)

    def test_comprimir_string_codificacion_inmanejable(self):
        with self.assertRaises(UnicodeEncodeError):
            self.compresor.comprimir("😊".encode('ascii', 'ignore').decode('ascii'))

    def test_comprimir_none_como_entrada(self):
        with self.assertRaises(AttributeError):
            self.compresor.comprimir(None)

    def test_comprimir_objeto_clase_personalizada(self):
        class ObjetoPersonalizado:
            pass
        with self.assertRaises(AttributeError):
            self.compresor.comprimir(ObjetoPersonalizado())

    # Casos de error para descomprimir
    def test_descomprimir_entrada_no_string_hexadecimal(self):
        with self.assertRaises(TypeError):
            self.compresor.descomprimir(1234)

    def test_descomprimir_string_vacio_como_entrada_hexadecimal(self):
        with self.assertRaises(ValueError):
            self.compresor.descomprimir("")

    def test_descomprimir_none_como_entrada_hexadecimal(self):
        with self.assertRaises(TypeError):
            self.compresor.descomprimir(None)

    def test_descomprimir_objeto_clase_personalizada_como_entrada_hexadecimal(self):
        class ObjetoPersonalizado:
            pass
        with self.assertRaises(TypeError):
            self.compresor.descomprimir(ObjetoPersonalizado())

# La siguiente línea se descomenta para ejecutar los tests si se ejecuta este script directamente.
if __name__ == '__main__':
    unittest.main()
