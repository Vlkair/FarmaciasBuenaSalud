# 06_gobierno_digital/OB05_trazabilidad.py
import pandas as pd

tz  = pd.read_csv("../03_diagnostico/PE05_trazabilidad.csv")
obj = pd.read_csv("OB02_objetivos.csv")
pt  = pd.read_csv("../05_arquitectura/AR03_brechas.csv")

print("=== CADENA COMPLETA: EVIDENCIA → FACTOR → ESTRATEGIA → OBJETIVO → PROYECTO ===")
for _, o in obj.iterrows():
    ests = [x.strip() for x in str(o["Estrategias que lo sustentan"]).split(",")]
    fila = tz[tz.Estrategia.astype(str).str.contains("|".join(ests), na=False)]
    print(f"\n{o.Código} — {o['Enunciado SMART'][:80]}...")
    print(f"   Articula a       : {o['Objetivo superior al que se articula']}")
    print(f"   Estrategias      : {', '.join(ests)}")
    print(f"   Evidencias base  : {len(fila)} registradas en la matriz de trazabilidad")
    print(f"   Paquetes         : {o['Paquetes de trabajo']}")
    print(f"   Responsable      : {o['Responsable (cargo)']}")
    if len(fila) == 0:
        print("   ⚠ OBJETIVO SIN EVIDENCIA TRAZABLE — revisar o retirar")

print("\n=== CONTROL DE COBERTURA ===")
print(f"Objetivos formulados: {len(obj)}  (rango recomendado: 5 a 8)")
comp = obj["Componente de gobierno digital"].str.split(" · ").explode().value_counts()
print(f"\nComponentes de gobierno digital cubiertos:\n{comp.to_string()}")
TODOS = {"Identidad digital","Servicios digitales","Arquitectura digital",
         "Interoperabilidad","Seguridad digital","Datos","Talento y cultura digital"}
print(f"\nComponentes SIN objetivo asociado: {sorted(TODOS - set(comp.index))}")
print("→ Verificar si la ausencia es una decisión deliberada de alcance o un vacío.")

print("\n=== PAQUETES DE TRABAJO SIN OBJETIVO ASOCIADO ===")
en_obj = set()
for x in obj["Paquetes de trabajo"].astype(str):
    en_obj |= {p.strip() for p in x.split(",")}
print("→ Todo paquete sin objetivo debe justificarse o retirarse del plan.")
