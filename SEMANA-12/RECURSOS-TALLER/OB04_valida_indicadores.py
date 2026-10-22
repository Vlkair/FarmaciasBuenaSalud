# 06_gobierno_digital/OB04_valida_indicadores.py
import pandas as pd
i = pd.read_csv("OB03_indicadores.csv")   # versión tabular de las fichas

print("=== VALIDACIÓN DE FICHAS ===")
CAMPOS = ["formula","fuente_dato","frecuencia","responsable_medicion",
          "linea_base","meta_final","umbral_alerta","supuestos","limitaciones"]
for c in CAMPOS:
    faltan = i[i[c].isna() | (i[c].astype(str).str.strip()=="")]
    print(f"  {'✔' if len(faltan)==0 else '✗'} {c:22s} — faltan en: {list(faltan.id) or 'ninguno'}")

print("\n=== LÍNEAS BASE ===")
sin_lb = i[i.linea_base.astype(str).str.contains("no se mide|N/D|—", case=False, na=True)]
print(f"Indicadores sin línea base verificada: {len(sin_lb)} → {list(sin_lb.id)}")
print("→ Cada uno requiere un proyecto de instrumentación ANTES de poder evaluarse.")

print("\n=== PROPORCIÓN POR TIPO ===")
p = i.tipo.value_counts(normalize=True).round(3)
print(p.to_string())
print(f"Resultado: {p.get('Resultado',0):.0%} (objetivo ≥ 60 %) | "
      f"Producto: {p.get('Producto',0):.0%} (máx. 30 %) | "
      f"Impacto: {p.get('Impacto',0):.0%} (≥ 1 por objetivo estratégico)")
if p.get('Resultado',0) < .6:
    print("⚠ Predominan indicadores de producto: el plan podrá cumplirse sin demostrar valor.")

print("\n=== ALCANZABILIDAD DE LAS METAS ===")
for _, r in i.iterrows():
    try:
        lb, mf = float(str(r.linea_base).replace("%","")), float(str(r.meta_final).replace("%",""))
        if lb > 0:
            print(f"  {r.id}: {lb} → {mf}  (×{mf/lb:.1f} en {r.get('años',3)} años)"
                  + ("   ⚠ verificar supuestos" if mf/lb > 5 else ""))
    except (ValueError, TypeError):
        print(f"  {r.id}: línea base o meta no numérica — verificar")
