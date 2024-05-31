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