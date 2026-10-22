"""Carga datos disponibles. No crea matrices de otras semanas ni borra tablas previas."""
from pathlib import Path
import os
import pandas as pd
from sqlalchemy import create_engine
BASE=Path(__file__).resolve().parent
eng=create_engine(os.environ.get('PETI_DATABASE_URL','postgresql+psycopg2://peti:peti_lab@127.0.0.1:5433/peti'))
files=[(BASE/'GD01_catalogo_servicios.csv','servicios'),(BASE/'GD03_ejes.csv','ejes_gd'),(BASE.parent/'04_normativa/NO03_matriz_cumplimiento.csv','cumplimiento'),(BASE.parent/'04_normativa/MG03_capacidad.csv','capacidad')]
for path,table in files:
    if not path.exists():
        print(f'PENDIENTE: {path.name}; no se inventa la tabla {table}.');continue
    df=pd.read_csv(path)
    if table=='servicios':
        rename={'Servicio':'servicio','Volumen anual':'volumen_anual','Nivel actual (0–5)':'nivel_actual','Nivel objetivo':'nivel_objetivo','Estado del nivel':'estado_nivel'}
    elif table=='ejes_gd':
        rename={'Eje':'eje','Indicador':'indicador','Línea base':'linea_base','Nivel del eje (1–5)':'nivel_eje','Proyecto de instrumentación':'proyecto_instrumentacion'}
    else:
        rename={}
    df.rename(columns=rename).to_sql(table,eng,if_exists='replace',index=False)
    print(f'{table}: {len(df)} filas cargadas.')
print('Fuente de datos de Metabase: host postgres, puerto interno 5432, base peti.')
