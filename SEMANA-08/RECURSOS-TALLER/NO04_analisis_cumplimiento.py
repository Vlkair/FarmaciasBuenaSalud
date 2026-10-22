# 04_normativa/NO04_analisis_cumplimiento.py
import pandas as pd
m = pd.read_csv("NO03_matriz_cumplimiento.csv")

print("=== ESTADO DE CUMPLIMIENTO ===")
print(m.Estado.value_counts().to_string())
print(f"\nObligaciones evaluadas: {len(m)}")
print(f"Cumple totalmente     : {(m.Estado=='Cumple').sum()} ({(m.Estado=='Cumple').mean():.0%})")
print(f"Cumple parcialmente   : {(m.Estado=='Parcial').sum()}")
print(f"NO CUMPLE             : {(m.Estado=='No cumple').sum()}")

print("\n=== OBLIGACIONES SIN RESPONSABLE ASIGNADO ===")
sin = m[m['Área responsable'].isna() | (m['Área responsable'].astype(str).str.strip()=="")]
print(f"{len(sin)} obligaciones sin responsable: {list(sin.id)}")
print("→ Una obligación sin responsable no se gestiona: se descubre cuando llega la sanción.")

print("\n=== PROYECTOS NO NEGOCIABLES (derivados de incumplimiento con plazo) ===")
nn = m[(m.Estado != "Cumple") & m.Plazo.notna()]
proy = nn.groupby("Proyecto que la cierra").agg(
    obligaciones=("id","count"),
    normas=("Norma", lambda s: ", ".join(sorted(set(s)))),
    plazo_mas_exigente=("Plazo","min")).sort_values("obligaciones", ascending=False)
print(proy.to_string())
print("\n→ Estos proyectos NO compiten en la matriz de priorización (Sección 7.2):")
print("  entran al portafolio con la fecha que impone la norma.")

print("\n=== CONCENTRACIÓN DEL INCUMPLIMIENTO POR NORMA ===")
print(m[m.Estado != "Cumple"].Norma.value_counts().to_string())
