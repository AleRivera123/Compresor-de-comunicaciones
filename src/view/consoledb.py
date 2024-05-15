import sys
sys.path.append("src")
from controller.ControladorUsuarios import UserData
import compressor.compressorlogic as compresorlogic  # Imports the compressor logic module
from compressor.compressorlogic import *  # Imports all elements from the compressorlogic module

import pandas as pd

print("""Bienvenido al sistema de compresión de textos. A continuación se describen las funcionalidades disponibles:
      - Crear una tabla inicial para usuarios.
      - Insertar nuevos usuarios y sus textos.
      - Actualizar información de los usuarios.
      - Eliminar usuarios.
      - Hacer consultas sobre los usuarios.""")

def create_tables():
    UserData.create_table()
    print("Tabla de usuarios creada con éxito.")

def insert_user():
    compresor = compresorlogic.CompresorRLE()
    print("Ingresa la siguiente información del usuario:")
    cedula = int(input("Cédula del usuario: "))
    nombre = input("Nombre del usuario: ")
    telefono = int(input("Teléfono del usuario: "))
    correo = input("Correo electrónico del usuario: ")
    texto_original = input("Texto original: ")
    tipo_evento = input("(comprimir/descomprimir): ")

    if tipo_evento=="comprimir":
        texto_procesado = compresor.comprimir(texto_original)
    elif tipo_evento=="descomprimir":
        texto_procesado = compresor.descomprimir(texto_original)
    else:
        print("opcion incorreta")


    # Llama a la función con un solo diccionario como argumento
    UserData.insert_user(cedula,nombre,telefono,correo,tipo_evento,texto_original,texto_procesado)
    print("Usuario insertado correctamente.")


def update_user():
    cedula = int(input("Cédula del usuario a actualizar: "))
    campo = input("Campo a actualizar (nombre, telefono, correo, texto_original): ")
    nuevo_valor = input("Nuevo valor: ")
    UserData.update_user(cedula, campo, nuevo_valor)
    print("Usuario actualizado correctamente.")

def delete_user():
    cedula = int(input("Cédula del usuario a eliminar: "))
    UserData.delete_user(cedula)
    print("Usuario eliminado correctamente.")

def query_user():
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

create_tables()

while True:
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
