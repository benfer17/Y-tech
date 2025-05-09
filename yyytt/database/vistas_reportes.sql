CREATE VIEW vista_ultimas_mediciones AS
SELECT 
    sensores.nombre AS nombre_sensor,
    mediciones_real.valor,
    mediciones_real.fecha_hora
FROM mediciones_real
JOIN sensores ON sensores.id_sensor = mediciones_real.id_sensor
ORDER BY fecha_hora DESC;

CREATE VIEW v_alarmas
