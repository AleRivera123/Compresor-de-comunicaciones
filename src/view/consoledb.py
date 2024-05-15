import sys
sys.path.append("src")
from controller.ControladorUsuarios import UserData
import compressor.compressorlogic as compresorlogic  # Importa el módulo de lógica del compresor
from compressor.compressorlogic import *  # Importa todos los elementos del módulo compressorlogic

import pandas as pd

# Presenta las funcionalidades disponibles en la aplicación.
print("""Bienvenido al sistema de compresión de textos. A continuación se describen las funcionalidades disponibles:
      - Crear una tabla inicial para usuarios.
      - Insertar nuevos usuarios y sus textos.
      - Actualizar información de los usuarios.
      - Eliminar usuarios.
      - Hacer consultas sobre los usuarios.""")

def create_tables():
    # Crea la tabla de usuarios en la base de datos y notifica al usuario.
    UserData.create_table()
    print("Tabla de usuarios creada con éxito.")

def insert_user():
    # Instancia el compresor, recoge datos del usuario desde la consola, y procesa textos según se requiera comprimir o descomprimir.
    compresor = compresorlogic.CompresorRLE()
    print("Ingresa la siguiente información del usuario:")
    cedula = int(input("Cédula del usuario: "))
    nombre = input("Nombre del usuario: ")
    telefono = int(input("Teléfono del usuario: "))
    correo = input("Correo electrónico del usuario: ")
    texto_original = input("Texto original: ")
    tipo_evento = input("(comprimir/descomprimir): ")

    if tipo_evento == "comprimir":
        texto_procesado = compresor.comprimir(texto_original)
    elif tipo_evento == "descomprimir":
        texto_procesado = compresor.descomprimir(texto_original)
    else:
        print("Opción incorrecta")

    # Inserta el usuario en la base de datos.
    UserData.insert_user(cedula, nombre, telefono, correo, tipo_evento, texto_original, texto_procesado)
    print("Usuario insertado correctamente.")

def update_user():
    # Permite al usuario actualizar información específica de un usuario existente.
    cedula = int(input("Cédula del usuario a actualizar: "))
    campo = input("Campo a actualizar (nombre, telefono, correo, texto_original): ")
    nuevo_valor = input("Nuevo valor: ")
    UserData.update_user(cedula, campo, nuevo_valor)
    print("Usuario actualizado correctamente.")

def delete_user():
    # Elimina un usuario especificado por su cédula.
    cedula = int(input("Cédula del usuario a eliminar: "))
    UserData.delete_user(cedula)
    print("Usuario eliminado correctamente.")

def query_user():
    # Consulta y muestra información de un usuario por su cédula.
    cedula = int(input("Cédula del usuario a consultar: "))
    usuario = UserData.query_user(cedula)
    if usuario:
        data_series = pd.Series({
            "Cédula": usuario[0],
            "Nombre": usuario[1],
            "Teléfono": usuario[2],
            "Correo Electrónico": usuario[3],
            "Tipo de Evento": usuario[4],
            "Texto Original": usuario[5],
            "Texto Procesado": usuario[6],
            "FechaHora": usuario[7]
        })
        print(data_series)
    else:
        print("No se encontró ningún usuario con esa cédula.")

create_tables()  # Crea las tablas necesarias al iniciar el programa.

while True:
    # Menú de opciones para que el usuario elija qué acción realizar.
    print("""¿Qué acción deseas realizar?:
      - insertar_usuario
      - actualizar_usuario
      - eliminar_usuario
      - consultar_usuario
      - salir""")
    accion = input("Elige una opción: ").lower()
    
    if accion == 'insertar_usuario':
        insert_user()
    elif accion == 'actualizar_usuario':
        update_user()
    elif accion == 'eliminar_usuario':
        delete_user()
    elif accion == 'consultar_usuario':
        query_user()
    elif accion == 'salir':
        print("Saliendo del sistema.")
        break
    else:
        print("Opción no válida, intenta de nuevo.")
