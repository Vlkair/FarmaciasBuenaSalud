# 03_diagnostico/AI02_analisis_cadena.py
import pandas as pd, matplotlib.pyplot as plt

cv = pd.read_csv("AI01_cadena_valor.csv")
cv["pct_costo"] = cv["% del costo operativo"].str.rstrip(" %").astype(float)

print("=== CONCENTRACIÓN DEL COSTO ===")
print(cv.nlargest(5, "pct_costo")[["id","Actividad","pct_costo","Nivel de soporte"]].to_string(index=False))

print("\n=== BRECHA COSTO vs. SOPORTE TECNOLÓGICO ===")
PESO = {"Bueno": 3, "Parcial": 2, "Deficiente": 1}
cv["soporte_num"] = cv["Nivel de soporte"].map(PESO).fillna(1)
cv["brecha"] = cv.pct_costo / cv.soporte_num
print(cv.nlargest(5, "brecha")[["id","Actividad","pct_costo","Nivel de soporte","brecha"]].to_string(index=False))
print("\n→ Las actividades de mayor brecha concentran costo con soporte deficiente:")
print("  son las candidatas naturales del portafolio de proyectos (Sección 7).")

# Gráfico: costo vs. soporte
fig, ax = plt.subplots(figsize=(10,6))
COL = {"Bueno":"#16A34A", "Parcial":"#D97706", "Deficiente":"#B91C1C"}
ax.barh(cv.Actividad, cv.pct_costo,
        color=[COL.get(s, "#9CA3AF") for s in cv["Nivel de soporte"]])
ax.set_xlabel("% del costo operativo")
ax.set_title("Cadena de valor: concentración del costo y nivel de soporte tecnológico")
for s, c in COL.items(): ax.barh([], [], color=c, label=s)
ax.legend(title="Soporte de TI"); plt.tight_layout()
plt.savefig("../graficos/AI_cadena_valor.png", dpi=140)
