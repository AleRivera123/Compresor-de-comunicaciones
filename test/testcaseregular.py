
import unittest
import zlib
import sys
sys.path.append("compresor_de_comunicaciones/src")
sys.path.append("./src")

from compressor.compressorlogic import *
import compressor.compressorlogic as lc

class TestCompresorZlib(unittest.TestCase):
    def setUp(self):
        self.compresor = lc.CompresorZlib()

    # Casos de prueba para comprimir
    def test_comprimir_simple(self):
        self.assertEqual(self.compresor.comprimir("Hola mundo"), zlib.compress(b"Hola mundo"))

    def test_comprimir_vacio(self):
        self.assertEqual(self.compresor.comprimir(""), zlib.compress(b""))

    def test_comprimir_numeros(self):
        self.assertEqual(self.compresor.comprimir("12345"), zlib.compress(b"12345"))

    # Casos de prueba para descomprimir
    def test_descomprimir_simple(self):
        texto_comprimido = zlib.compress(b"Hola mundo").hex()
        self.assertEqual(self.compresor.descomprimir(texto_comprimido), "Hola mundo")

    def test_descomprimir_vacio(self):
        texto_comprimido = zlib.compress(b"").hex()
        self.assertEqual(self.compresor.descomprimir(texto_comprimido), "")

    def test_descomprimir_numeros(self):
        texto_comprimido = zlib.compress(b"12345").hex()
        self.assertEqual(self.compresor.descomprimir(texto_comprimido), "12345")

# La siguiente línea se descomenta para ejecutar los tests si se ejecuta este script directamente.
if __name__ == '__main__':
    unittest.main()
