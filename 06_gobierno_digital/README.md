# Taller 11 de la empresa 10

Grupo 10. Diagnóstico documental de Farmacias Buena Salud. Estado: avance con
pendientes explícitos; no es una entrega final calificada como completa.

## Ejecución desde la raíz del repositorio

```powershell
python -m pip install -r 06_gobierno_digital/requirements.txt
python 06_gobierno_digital/GD02_analisis_servicios.py
python 06_gobierno_digital/GD04_madurez.py
docker compose -f 06_gobierno_digital/compose.yaml up -d
python 06_gobierno_digital/GD05_carga_tablero.py
```

Metabase abre en http://127.0.0.1:3001. Crear usuario administrador local y agregar
PostgreSQL: servidor `postgres`, puerto `5432`, base `peti`, usuario `peti`, contraseña
`peti_lab` del laboratorio. Desde Windows, PostgreSQL se publica solo en 127.0.0.1:5433.
La contraseña del ejemplo es exclusiva del entorno local del taller.

Crear las cuatro consultas SQL disponibles y configurar barras, número y tabla.
El número ponderado se mostrará sin valor hasta completar los datos; no convertirlo
en cero. Agregar cumplimiento (anillo) y capacidad (barras agrupadas) con las matrices
del equipo. Obtener capturas reales y numeradas en `evidencias/S11/`; no hay capturas
de Metabase fabricadas ni seis visualizaciones declaradas sin prueba.

Para detener el laboratorio conservando datos:
`docker compose -f 06_gobierno_digital/compose.yaml stop`.

## Qué falta para cerrar

- Volúmenes anuales y requisitos documentales confirmados por el docente.
- Recorridos de venta y distribución y validación de los puntajes.
- Matrices normativas y de capacidad de semanas previas.
- Seis visualizaciones de Metabase con capturas verificables.
- Validación del informe, índice y decisión sobre identificación de integrantes.
- Etiquetas `taller-11` y `v0.11` únicamente al cerrar la entrega, no durante el borrador.

La guía pide códigos de integrantes en la entrega evaluada. Se omiten aquí por
instrucción del usuario. El PDF se identifica como borrador del Grupo 10.

Referencias de instalación: [Metabase en Docker](https://www.metabase.com/docs/latest/installation-and-operation/running-metabase-on-docker)
y [orden de arranque de Compose](https://docs.docker.com/compose/how-tos/startup-order/).
