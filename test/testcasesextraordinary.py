import unittest
import zlib

import sys
sys.path.append("compresor_de_comunicaciones/")
sys.path.append("./")

from src.compressor.compressorlogic import *
import src.compressor.compressorlogic as lc

class TestCompresorRLEExtraordinarios(unittest.TestCase):
    def setUp(self):
        self.compresor = lc.CompresorRLE()

    # Casos extraordinarios para comprimir
    def test_comprimir_texto_largo(self):
        texto_largo = "a" * 10000  # Genera un texto de 10,000 'a'
        self.assertIsInstance(self.compresor.comprimir(texto_largo), bytes)

    def test_comprimir_texto_multilingue(self):
        texto_multilingue = "Hello, こんにちは, 안녕하세요, 你好"
        self.assertIsInstance(self.compresor.comprimir(texto_multilingue), bytes)

    def test_comprimir_con_emojis(self):
        texto_con_emojis = "Python is fun 🐍😊"
        self.assertIsInstance(self.compresor.comprimir(texto_con_emojis), bytes)

    # Casos extraordinarios para descomprimir
    def test_descomprimir_no_hexadecimal(self):
        self.assertIsNone(self.compresor.descomprimir("Esto no es hexadecimal"))

    def test_descomprimir_hexadecimal_invalido(self):
        texto_hex_invalido = "zz"  # No es un valor hexadecimal válido
        self.assertIsNone(self.compresor.descomprimir(texto_hex_invalido))

    def test_descomprimir_corrupto(self):
        texto_comprimido_corrupto = zlib.compress(b"Hola").hex()[:-1]  # Se elimina el último carácter para corromperlo
        self.assertIsNone(self.compresor.descomprimir(texto_comprimido_corrupto))

# La siguiente línea se descomenta para ejecutar los tests si se ejecuta este script directamente.
if __name__ == '__main__':
    unittest.main()
