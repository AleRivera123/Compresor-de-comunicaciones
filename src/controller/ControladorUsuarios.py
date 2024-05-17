import psycopg2
import sys
sys.path.append("src")
from model.Usuario import UserInput, UserOutput, DuplicateEntryError, EntryNotFoundError, DataValidationError
import controller.SecretConfig as st

class UserData:
    """ Clase para operaciones de base de datos relacionadas con los usuarios. """

    @staticmethod
    def get_connection():
        return psycopg2.connect(database=st.PGDATABASE, user=st.PGUSER, password=st.PGPASSWORD, host=st.PGHOST, port=st.PGPORT)

    @staticmethod
    def create_table():
        """ Crea la tabla de usuarios en la base de datos si no existe. """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS Usuarios (
                        Cedula BIGINT PRIMARY KEY,
                        Nombre VARCHAR(100) NOT NULL,
                        Telefono BIGINT,
                        CorreoElectronico VARCHAR(100),
                        TipoEvento VARCHAR(10),
                        TextoOriginal TEXT,
                        TextoProcesado TEXT,
                        FechaHora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                conn.commit()

    @staticmethod
    def drop_table():
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Usuarios;")
                conn.commit()
                

    @staticmethod
    def insert_user(cedula, nombre, telefono, correo, tipo_evento, texto_original, texto_procesado):
        """ Inserta un nuevo usuario en la base de datos tras validar la entrada. """
        user = UserInput(nombre, cedula, telefono, correo, texto_original, tipo_evento)
        user.validate()
        UserInput.check_primary_key(cedula, UserData.user_exists)
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Usuarios (Cedula, Nombre, Telefono, CorreoElectronico, TipoEvento, TextoOriginal, TextoProcesado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, (cedula, nombre, telefono, correo, tipo_evento, texto_original, texto_procesado))
                conn.commit()

    @staticmethod
    def delete_user(cedula):
        """ Elimina un usuario de la base de datos basado en la cédula proporcionada. """
        if not isinstance(cedula, int):
            raise DataValidationError("ID inválido.")
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Usuarios WHERE Cedula = %s;", (cedula,))
                affected_rows = cursor.rowcount
                conn.commit()
        UserOutput.validate_user_found(affected_rows != 0, "eliminar")

    @staticmethod
    def update_user(cedula, key, value):
        """ Actualiza la información de un usuario en la base de datos. """
        if not isinstance(cedula, int):
            raise DataValidationError("ID inválido.")
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE Usuarios SET {key} = %s WHERE Cedula = %s;", (value, cedula))
                affected_rows = cursor.rowcount
                conn.commit()
        UserOutput.validate_user_found(affected_rows != 0, "actualizar")

    @staticmethod
    def query_user(cedula):
        """ Consulta la información de un usuario por su cédula. """
        if not isinstance(cedula, int):
            raise DataValidationError("ID inválido.")
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Usuarios WHERE Cedula = %s;", (cedula,))
                result = cursor.fetchone()
                UserOutput.validate_user_found(result, "consulta")
                return result

    @staticmethod
    def user_exists(cedula):
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT EXISTS(SELECT 1 FROM Usuarios WHERE Cedula = %s)", (cedula,))
                return cursor.fetchone()[0]
