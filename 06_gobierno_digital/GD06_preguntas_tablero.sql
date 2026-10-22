-- 06_gobierno_digital/GD06_preguntas_tablero.sql
-- Las seis preguntas del tablero de línea base (SQL nativo para Metabase).
-- Cada bloque es una "pregunta" de Metabase: New → SQL query → base "peti".

-- V1 · Nivel de digitalización por servicio · Barras horizontales (Row)
--      ¿Qué servicios están más atrasados?
SELECT "id" || ' ' || "Servicio" AS servicio,
       "Nivel actual (0–5)"     AS nivel_actual,
       "Nivel objetivo"         AS nivel_objetivo
FROM servicios
ORDER BY nivel_actual, "Volumen anual" DESC;

-- V2 · Nivel ponderado por volumen · Número grande (Number)
--      ¿Qué proporción de las atenciones es realmente digital?
SELECT ROUND(SUM("Nivel actual (0–5)" * "Volumen anual")::numeric
             / SUM("Volumen anual"), 2) AS nivel_ponderado,
       ROUND(AVG("Nivel actual (0–5)")::numeric, 2) AS nivel_simple
FROM servicios;

-- V3 · Madurez por eje · Barras
--      ¿Dónde está la mayor brecha de gobierno digital?
SELECT "Eje" AS eje,
       ROUND(AVG("Nivel del eje (1–5)")::numeric, 2) AS nivel
FROM ejes_gd
GROUP BY "Eje"
ORDER BY "Eje";

-- V4 · Estado de cumplimiento normativo · Anillo (Pie)
--      ¿Cuántas obligaciones se incumplen?
SELECT "Estado" AS estado, COUNT(*) AS obligaciones
FROM cumplimiento
GROUP BY "Estado"
ORDER BY obligaciones DESC;

-- V5 · Capacidad de procesos actual vs. objetivo · Barras agrupadas
--      ¿Qué procesos exigen mayor esfuerzo?
SELECT "Objetivo" AS objetivo,
       "Nivel actual"   AS nivel_actual,
       "Nivel objetivo" AS nivel_objetivo
FROM capacidad
ORDER BY "Brecha" DESC, "Objetivo";

-- V6 · Indicadores sin línea base · Tabla
--      ¿Qué necesitamos empezar a medir?
SELECT "Eje" AS eje, "Indicador" AS indicador,
       "Proyecto de instrumentación" AS proyecto
FROM ejes_gd
WHERE "Línea base" ILIKE '%no se mide%'
ORDER BY "Eje";
