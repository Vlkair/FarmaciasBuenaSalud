# 06_gobierno_digital/GD05_carga_tablero.py
# Carga el catálogo, los ejes, la matriz de cumplimiento y la capacidad en PostgreSQL
# para construir el tablero de línea base en Metabase.
import pandas as pd
from sqlalchemy import create_engine, text

eng = create_engine("postgresql://peti:peti_lab@127.0.0.1:5433/peti")
tablas = {
    "servicios":    "GD01_catalogo_servicios.csv",
    "ejes_gd":      "GD03_ejes.csv",
    "cumplimiento": "../04_normativa/NO03_matriz_cumplimiento.csv",
    "capacidad":    "../04_normativa/MG03_capacidad.csv",
}
for tabla, archivo in tablas.items():
    df = pd.read_csv(archivo)
    df.to_sql(tabla, eng, if_exists="replace", index=False)
    print(f"{tabla:<13} ← {archivo:<45} {len(df):>3} filas")

with eng.connect() as c:
    for t in tablas:
        n = c.execute(text(f'select count(*) from "{t}"')).scalar()
        print(f"Verificación en PostgreSQL · {t}: {n} filas")
print("Datos cargados. Metabase: http://127.0.0.1:3001")
