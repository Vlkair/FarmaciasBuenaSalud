-- Una sola observación por eje. Puntajes documentales preliminares.
SELECT eje, MAX(nivel_eje) AS nivel_preliminar FROM ejes_gd GROUP BY eje ORDER BY eje;
