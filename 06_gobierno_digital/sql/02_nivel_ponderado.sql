-- No publica un promedio parcial como si fuera el catálogo completo.
SELECT CASE WHEN COUNT(volumen_anual)=COUNT(*) AND COUNT(nivel_actual)=COUNT(*)
  AND SUM(volumen_anual)>0
  THEN SUM(nivel_actual * volumen_anual)/SUM(volumen_anual) ELSE NULL END AS nivel_ponderado
FROM servicios;
