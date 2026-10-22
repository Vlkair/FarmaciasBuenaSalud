-- Barras horizontales: actual vs objetivo; nulos se muestran como sin determinar.
SELECT id, servicio, nivel_actual, nivel_objetivo, estado_nivel
FROM servicios ORDER BY id;
