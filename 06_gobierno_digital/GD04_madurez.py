"""Valoración documental; no certifica madurez ni convierte falta de datos en cero."""
from pathlib import Path
import json
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
BASE=Path(__file__).resolve().parent
e=pd.read_csv(BASE/'GD03_ejes.csv')
level='Nivel del eje (1–5)'
assert e.Eje.nunique()==8 and e.groupby('Eje').size().ge(2).all()
assert e[level].between(1,5).all() and e.Evidencia.notna().all()
assert e.groupby('Eje')[level].nunique().eq(1).all(), 'Puntaje único por eje'
nm=e.groupby('Eje',sort=True)[level].first()
mean=float(nm.mean())
print('NIVELES PRELIMINARES POR EJE\n'+nm.to_string())
print(f'Índice documental con igual peso por eje: {mean:.2f} de 5')
print('Posicionamiento preliminar: nivel 1, Inicial/reactivo; gobernanza sin comité operativo ni PETI.')
print('No redondear este índice para declarar una certificación. Puntajes requieren validación del equipo.')
sin=e[e['Línea base'].str.contains('No se mide',case=False,na=False)]
print(f'Indicadores sin línea base utilizable: {len(sin)} de {len(e)}')
print(sin[['Eje','Indicador','Proyecto de instrumentación']].to_string(index=False))
ang=np.linspace(0,2*np.pi,len(nm),endpoint=False).tolist();ang+=ang[:1]
vals=nm.tolist();vals+=vals[:1]
fig,ax=plt.subplots(figsize=(9,8),subplot_kw={'polar':True})
ax.plot(ang,vals,color='#216869',linewidth=2);ax.fill(ang,vals,color='#216869',alpha=.2)
ax.set_xticks(ang[:-1],nm.index.str.split('. ',n=1,regex=False).str[1]);ax.set_ylim(0,5);ax.set_yticks([1,2,3,4,5])
ax.set_title('Farmacias Buena Salud\nMadurez documental preliminar — pendiente de validación',pad=35)
fig.tight_layout();fig.savefig(BASE.parent/'graficos/GD_madurez.png',dpi=150);plt.close(fig)
sin.to_csv(BASE/'GD06_indicadores_sin_linea_base.csv',index=False,encoding='utf-8-sig')
(BASE/'GD04_resumen.json').write_text(json.dumps({'indice_preliminar':mean,'indicadores':len(e),'sin_linea_base':len(sin),'nivel_modelo_preliminar':1},ensure_ascii=False,indent=2),encoding='utf-8')
