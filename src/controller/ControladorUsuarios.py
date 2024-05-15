import sys
sys.path.append("src")
import psycopg2
import compressor.compressorlogic as compressor

# Configuration from your security settings module
import SecretConfig as st

class UserData:

    @staticmethod
    def get_connection():
        """ Establece conexión a la base de datos y retorna la conexión """
        return psycopg2.connect(database=st.PGDATABASE, user=st.PGUSER, password=st.PGPASSWORD, host=st.PGHOST, port=st.PGPORT)

    @staticmethod
    def create_table():
        """ Crea la tabla de usuarios en la base de datos """
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
                conn.commit()

    @staticmethod
    def drop_table():
        """ Elimina la tabla de usuarios de la base de datos """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS Usuarios;")
                conn.commit()

    @staticmethod
    def insert_user(cedula, nombre, telefono, correo, tipo_evento, texto_original,texto_procesado):
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Usuarios (Cedula, Nombre, Telefono, CorreoElectronico, tipoEvento, TextoOriginal, TextoProcesado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (Cedula) DO NOTHING;
                """, (cedula, nombre, telefono, correo, tipo_evento, texto_original,texto_procesado))
                conn.commit()

    @staticmethod
    def delete_user(cedula):
        """ Elimina un usuario basado en la cédula """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM Usuarios WHERE Cedula = %s;", (cedula,))
                conn.commit()

    @staticmethod
    def update_user(cedula, key, value):
        """ Actualiza la información del usuario """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(f"UPDATE Usuarios SET {key} = %s WHERE Cedula = %s;", (value, cedula))
                conn.commit()

    @staticmethod
    def query_user(cedula):
        """ Consulta la información de un usuario por cédula """
        with UserData.get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM Usuarios WHERE Cedula = %s;", (cedula,))
                return cursor.fetchone()

# Clases auxiliares pueden ser definidas aquí si son necesarias para manejar la lógica de negocio específica

# Asegúrate de adaptar este código según tus necesidades específicas, especialmente en la gestión de conexiones y manejo de excepciones
