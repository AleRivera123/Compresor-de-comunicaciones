import sys
sys.path.append("src")  # Adds the 'src' directory to the Python module search path

import compressor.compressorlogic as compresorlogic  # Imports the compressor logic module
from compressor.compressorlogic import *  # Imports all elements from the compressorlogic module

class Aplicacion:
    def __init__(self):
        self.compresor = compresorlogic.CompresorRLE()  # Creates an instance of the CompresorRLE class

    def ejecutar(self):
        running = True
        print("Bienvenido a la aplicación de compresión/descompresión de texto.")
        
        while running:
            texto_usuario = input("Por favor, ingrese el texto: ")  # Requests the user to enter the text
            accion = input("¿Desea comprimir o descomprimir el texto? (comprimir/descomprimir): ")  # Asks whether to compress or decompress the text

            if accion.lower() == "comprimir":  # Processes the compression action
                resultado = self.compresor.comprimir(texto_usuario)  # Compresses the entered text

                print(f"Texto comprimido (en bytes): {resultado}")  # Displays the compressed text in hexadecimal format
            elif accion.lower() == "descomprimir":  # Processes the decompression action

                resultado = self.compresor.descomprimir(texto_usuario)  # Decompress the string
                print(f"Texto descomprimido: {resultado}")  # Displays the decompressed text
    
            continuar = input("¿Desea continuar udasn? (sí/no): ")
            if continuar.lower() != 'si':
                running = False


if __name__ == "__main__":
    app = Aplicacion()  # Creates an instance of Aplicacion
    app.ejecutar()  # Executes the ejecutar method of the instance
