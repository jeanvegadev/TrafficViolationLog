-- Create Persona table
CREATE TABLE IF NOT EXISTS persona (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(254) NOT NULL
);

-- Create Vehiculo table
CREATE TABLE IF NOT EXISTS vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa_patente VARCHAR(6) NOT NULL,
    marca VARCHAR(50) NOT NULL,
    color VARCHAR(50) NOT NULL,
    propietario_id INT NOT NULL,
    FOREIGN KEY (propietario_id) REFERENCES persona(id)
);

-- Create Oficial table
CREATE TABLE IF NOT EXISTS oficial (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    numero_identificatorio VARCHAR(50) NOT NULL UNIQUE
);

-- Create Infraccion table
CREATE TABLE IF NOT EXISTS infraccion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehiculo_id INT NOT NULL,
    oficial_id INT NOT NULL,
    timestamp DATETIME NOT NULL,
    motivo VARCHAR(1000) NOT NULL,
    FOREIGN KEY (vehiculo_id) REFERENCES vehiculo(id),
    FOREIGN KEY (oficial_id) REFERENCES oficial(id)
);

-- Create AccessToken table
CREATE TABLE IF NOT EXISTS access_token (
    id INT AUTO_INCREMENT PRIMARY KEY,
    oficial_id INT NOT NULL UNIQUE,
    token VARCHAR(255) NOT NULL,
    FOREIGN KEY (oficial_id) REFERENCES oficial(id)
);
