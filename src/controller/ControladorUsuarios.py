import sys
sys.path.append("src")
import psycopg2
import compressor.compressorlogic as compressor
from model.Usuario import DuplicateEntryError
from model.Usuario import EntryNotFoundError
# Configuración desde el módulo de ajustes de seguridad.
import controller.SecretConfig as st

class UserData:
    """ Clase para operaciones de base de datos relacionadas con los usuarios. """

    @staticmethod
    def get_connection():
        """ 
        Establece y retorna una conexión a la base de datos utilizando los ajustes especificados en la configuración de seguridad.
        """
        return psycopg2.connect(database=st.PGDATABASE, user=st.PGUSER, password=st.PGPASSWORD, host=st.PGHOST, port=st.PGPORT)

    @staticmethod
    def create_table():
        """
        Crea la tabla de usuarios en la base de datos si no existe.
        Define la estructura de la tabla con columnas para cédula, nombre, teléfono, correo electrónico, tipo de evento,
        texto original y procesado, y una marca de tiempo por defecto.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Usuarios (
                        Cedula BIGINT PRIMARY KEY,
                        Nombre VARCHAR(100) NOT NULL,
                        Telefono BIGINT,
                        CorreoElectronico VARCHAR(100),
                        tipoEvento VARCHAR(10),
                        TextoOriginal TEXT,
                        TextoProcesado TEXT,
                        FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                conn.commit()  # Confirma la operación en la base de datos.

    @staticmethod
    def drop_table():
        """
        Elimina la tabla de usuarios de la base de datos.
        Este método es útil para limpiar durante pruebas o cuando se necesita reconstruir la tabla.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Usuarios;")
                conn.commit()

    @staticmethod
    def insert_user(cedula, nombre, telefono, correo, tipo_evento, texto_original, texto_procesado):
        """
        Inserta un nuevo usuario en la base de datos. Si se produce un error de integridad (por ejemplo, duplicado de cédula),
        se revierte la transacción y se lanza una excepción personalizada.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("""
                        INSERT INTO Usuarios (Cedula, Nombre, Telefono, CorreoElectronico, tipoEvento, TextoOriginal, TextoProcesado)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);
                    """, (cedula, nombre, telefono, correo, tipo_evento, texto_original, texto_procesado))
                    conn.commit()
                except psycopg2.IntegrityError:
                    conn.rollback()  # Revoca la transacción en caso de error.
                    raise DuplicateEntryError(f"Ya existe un usuario con la cédula {cedula}.")

    @staticmethod
    def delete_user(cedula):
        """
        Elimina un usuario de la base de datos basado en la cédula proporcionada.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Usuarios WHERE Cedula = %s;", (cedula,))
                conn.commit()

    @staticmethod
    def update_user(cedula, key, value):
        """
        Actualiza la información de un usuario en la base de datos. Si no se encuentra un usuario con la cédula proporcionada,
        se lanza una excepción de EntryNotFoundError.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE Usuarios SET {key} = %s WHERE Cedula = %s;", (value, cedula))
                if cursor.rowcount == 0:  # Verifica si alguna fila fue actualizada.
                    conn.rollback()  # Revoca si no hay filas actualizadas.
                    raise EntryNotFoundError(f"No se encontró un usuario con cédula {cedula} para actualizar.")
                conn.commit()

    @staticmethod
    def query_user(cedula):
        """
        Consulta la información de un usuario por su cédula y retorna los datos si están disponibles.
        Si no se encuentra el usuario, se lanza una excepción de EntryNotFoundError.
        """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Usuarios WHERE Cedula = %s;", (cedula,))
                result = cursor.fetchone()
                if not result:
                    raise EntryNotFoundError("Usuario no encontrado.")
                return result

