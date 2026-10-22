# FarmaciasBuenaSalud

PETI · Cadena de Farmacias Buena Salud E.I.R.L.

SI-886 Planeamiento Estratégico de TI · Universidad Privada de Tacna · Empresa 10

## Taller S11 · Diagnóstico de gobierno digital y tablero de línea base

| Archivo | Qué es |
|---|---|
| `06_gobierno_digital/GD01_catalogo_servicios.csv` | Catálogo de 11 servicios con volumen, nivel actual y objetivo |
| `06_gobierno_digital/GD02_analisis_servicios.py` | Nivel simple y ponderado, una sola vez, brecha × volumen |
| `06_gobierno_digital/GD03_ejes.csv` | 8 ejes, 27 indicadores con línea base |
| `06_gobierno_digital/GD04_madurez.py` | Madurez por eje y radar (con la corrección del split) |
| `06_gobierno_digital/GD05_carga_tablero.py` | Carga las 4 tablas en PostgreSQL |
| `06_gobierno_digital/GD06_preguntas_tablero.sql` | Las 6 preguntas SQL del tablero |
| `06_gobierno_digital/GD07_crear_tablero_metabase.py` | Crea las preguntas y el tablero en Metabase por API |
| `06_gobierno_digital/GD08_vista_previa_tablero.py` | Vista previa del tablero desde PostgreSQL |
| `06_gobierno_digital/6.1_situacion_actual.md` | Sección 6.1 del PETI |
| `graficos/` | GD_servicios.png, GD_madurez.png, GD_tablero_vista_previa.png |
| `04_normativa/NO03_matriz_cumplimiento.csv` | Matriz de cumplimiento (22 obligaciones), insumo del tablero |
| `04_normativa/MG03_capacidad.csv` | Capacidad COBIT actual vs. objetivo (13 objetivos), insumo del tablero |
| `evidencias/S11/salidas/` | Salidas de GD02, GD04, GD05 y GD06 |
| `evidencias/S11/validacion_paso_E.md` | Validación y problemas y mejoras (Paso E) |
| `evidencias/S11/anexo_*` | Anexos A, B, C, E y F del informe |
| `evidencias/S11/capturas/` | Capturas del tablero en Metabase (Anexo D) |

## Cómo reproducir

```bash
git clone https://github.com/Vlkair/FarmaciasBuenaSalud.git
cd FarmaciasBuenaSalud
```

```bash
docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab \
  -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16
docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 \
  --add-host=host.docker.internal:host-gateway \
  -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 \
  -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal \
  metabase/metabase
pip install pandas matplotlib sqlalchemy "psycopg[binary]" requests
cd 06_gobierno_digital
python3 GD02_analisis_servicios.py
python3 GD04_madurez.py
python3 GD05_carga_tablero.py
# Crear el administrador en http://127.0.0.1:3001 y luego:
MB_USER=correo MB_PASS=clave python3 GD07_crear_tablero_metabase.py
```

### En Windows (PowerShell)

```powershell
docker run -d --name peti_db -e POSTGRES_USER=peti -e POSTGRES_PASSWORD=peti_lab -e POSTGRES_DB=peti -p 127.0.0.1:5433:5432 postgres:16
docker run -d --name peti_metabase -p 127.0.0.1:3001:3000 --add-host=host.docker.internal:host-gateway -e MB_DB_TYPE=postgres -e MB_DB_DBNAME=peti -e MB_DB_PORT=5433 -e MB_DB_USER=peti -e MB_DB_PASS=peti_lab -e MB_DB_HOST=host.docker.internal metabase/metabase
pip install pandas matplotlib sqlalchemy "psycopg[binary]" requests
cd 06_gobierno_digital
python GD02_analisis_servicios.py
python GD04_madurez.py
python GD05_carga_tablero.py
$env:MB_USER="correo@upt.pe"; $env:MB_PASS="clave"; python GD07_crear_tablero_metabase.py
```
