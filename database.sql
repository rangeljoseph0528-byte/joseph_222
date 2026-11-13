-- SOLO PARA LOCAL: crea la base de datos y la tabla.
CREATE DATABASE institucion;

USE institucion;

CREATE TABLE aprendices (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  correo VARCHAR(100) NOT NULL
);

-- EN RAILWAY: NO ejecutes CREATE DATABASE ni USE.
-- Selecciona la base MYSQLDATABASE y ejecuta solo el CREATE TABLE.
