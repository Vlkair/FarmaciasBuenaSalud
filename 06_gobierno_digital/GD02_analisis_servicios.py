"""Adaptado del programa del curso. No sustituye datos ausentes por cero."""
from pathlib import Path
import json
import textwrap
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

BASE=Path(__file__).resolve().parent
s=pd.read_csv(BASE/'GD01_catalogo_servicios.csv')
n=pd.to_numeric(s['Nivel actual (0–5)'],errors='coerce')
v=pd.to_numeric(s['Volumen anual'],errors='coerce')
obj=pd.to_numeric(s['Nivel objetivo'],errors='coerce')
assert len(s)>=7 and s.id.is_unique
assert n.dropna().between(0,5).all() and obj.between(0,5).all()
assert v.dropna().ge(0).all()
print('EMPRESA 10 — FARMACIAS BUENA SALUD | Grupo 10')
print(f'Servicios: {len(s)}; con volumen anual confirmado: {v.notna().sum()}')
print(f'Niveles propuestos con valor: {n.notna().sum()}; sin determinar: {n.isna().sum()}')
print('Los niveles son documentales o inferidos; falta validar recorridos.')
simple=float(n.mean()) if n.notna().all() else None
pond=float((n*v).sum()/v.sum()) if n.notna().all() and v.notna().all() and v.sum()>0 else None
print('Promedio simple completo:', f'{simple:.2f}' if simple is not None else 'NO CALCULABLE: faltan niveles')
print('Promedio ponderado completo:', f'{pond:.2f}' if pond is not None else 'NO CALCULABLE: faltan volúmenes o niveles')
print('No interpretar nivel/5 como porcentaje de transacciones digitales.')
print('PRINCIPIO DE UNA SOLA VEZ')
docs=pd.to_numeric(s['Documentos solicitados'],errors='coerce')
red=pd.to_numeric(s['De ellos, ya en poder de la organización'],errors='coerce')
if docs.notna().all() and red.notna().all():
    assert docs.ge(0).all() and red.ge(0).all() and red.le(docs).all()
    print(f'Solicitudes documentales por catálogo: {docs.sum():g}; redundantes: {red.sum():g}')
    print('Proporción:', f'{red.sum()/docs.sum():.1%}' if docs.sum()>0 else 'No aplica: denominador cero')
else:
    print('NO EVALUABLE: faltan requisitos concretos y contraste de documentos existentes.')
print('TOP 5 POR BRECHA × VOLUMEN')
if pond is None:
    print('PENDIENTE: no se publica ranking numérico con datos incompletos.')
else:
    out=s[['id','Servicio']].copy();out['impacto']=(obj-n)*v
    print(out.nlargest(5,'impacto').to_string(index=False))
outdir=BASE.parent/'graficos';outdir.mkdir(exist_ok=True)
fig,ax=plt.subplots(figsize=(8,6))
y=list(range(len(s)))
ax.barh(y,obj,color='#DDE6EF',label='Objetivo propuesto')
known=n.notna()
ax.barh([i for i in y if known.iloc[i]],n[known],color='#216869',label='Nivel preliminar')
for i in y:
    ax.text(0.08,i, 'N/D' if not known.iloc[i] else str(int(n.iloc[i])),va='center',fontsize=12)
ax.set_yticks(y, [textwrap.fill(f'{row.id} {row.Servicio}',28) for row in s.itertuples()],fontsize=11)
ax.set_xlim(0,5);ax.invert_yaxis()
ax.set_xlabel('Nivel 0 a 5 — niveles actuales sujetos a validación')
ax.set_title('Farmacias Buena Salud — catálogo preliminar')
ax.legend(loc='lower right');fig.tight_layout()
fig.savefig(outdir/'GD_servicios.png',dpi=150);plt.close(fig)
(BASE/'GD02_resumen.json').write_text(json.dumps({'servicios':len(s),'volumenes_confirmados':int(v.notna().sum()),'media_simple_completa':simple,'media_ponderada_completa':pond,'estado':'Preliminar; faltan entrevista y recorridos'},ensure_ascii=False,indent=2),encoding='utf-8')
