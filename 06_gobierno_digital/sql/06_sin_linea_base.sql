SELECT eje, indicador, linea_base, proyecto_instrumentacion
FROM ejes_gd WHERE linea_base ILIKE '%No se mide%' ORDER BY eje;
