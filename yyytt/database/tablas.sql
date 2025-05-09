

-- Creamos la tabla de alarmas
CREATE TABLE alarmas (
  id_alarma INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  descripcion TEXT NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_alta DATE NOT NULL
);

-- Creamos la tabla de relaciones entre sensores y alarmas
CREATE TABLE sensores_alarmas (
  id_sensor INTEGER NOT NULL,
  id_alarma INTEGER NOT NULL,
  PRIMARY KEY (id_sensor, id_alarma),
  FOREIGN KEY (id_sensor) REFERENCES sensores(id_sensor),
  FOREIGN KEY (id_alarma) REFERENCES alarmas(id_alarma)
);

-- Tabla de descripciones de mediciones
CREATE TABLE mediciones (
  id_medicion INTEGER PRIMARY KEY,
  descripcion TEXT NOT NULL
);

-- Tabla mediciones_real (lecturas reales del sensor)
CREATE TABLE mediciones_real (
  id_med_real INTEGER PRIMARY KEY,
  id_sensor INTEGER NOT NULL,
  id_medicion INTEGER NOT NULL,
  valor FLOAT NOT NULL,
  fecha_hora DATETIME NOT NULL,
  FOREIGN KEY (id_sensor) REFERENCES sensores(id_sensor),
  FOREIGN KEY (id_medicion) REFERENCES mediciones(id_medicion)
);

-- Tabla de eventos
CREATE TABLE eventos (
  id_evento INTEGER PRIMARY KEY,
  id_sensor INTEGER NOT NULL,
  id_alarma INTEGER NOT NULL,
  fecha_hora DATETIME NOT NULL,
  observacion TEXT,
  FOREIGN KEY (id_sensor) REFERENCES sensores(id_sensor),
  FOREIGN KEY (id_alarma) REFERENCES alarmas(id_alarma)
);

-- Tabla de usuarios
CREATE TABLE usuarios (
  id_usuario INTEGER PRIMARY KEY,
  nombre TEXT NOT NULL,
  apellido TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  fecha_creacion DATE NOT NULL,
  fecha_alta DATE NOT NULL
);
