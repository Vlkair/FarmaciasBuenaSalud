# 08_riesgos/RG03_evaluacion.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt

r = pd.read_csv("RG02_registro.csv")
r["valor"] = r.P * r.I
r["nivel"] = pd.cut(r.valor, [0,6,11,14,25],
                    labels=["Bajo","Medio","Alto","Crítico"])
r = r.sort_values("valor", ascending=False)
r.to_csv("RG03_evaluado.csv", index=False)

print("=== REGISTRO DE RIESGOS DEL PLAN ===")
print(r[["id","Categoría","P","I","valor","nivel"]].to_string(index=False))
print(f"\nRiesgos evaluados : {len(r)}")
print(r.nivel.value_counts().reindex(["Crítico","Alto","Medio","Bajo"]).fillna(0).astype(int).to_string())

CATS = ["Presupuestal","Patrocinio","Capacidad de ejecución","Personal clave",
        "Resistencia al cambio","Proveedor","Técnico","Normativo","De alcance"]
faltan = [c for c in CATS if c not in set(r["Categoría"])]
print(f"\nCategorías SIN riesgo identificado: {faltan or 'ninguna ✔'}")
if faltan:
    print("→ Cada categoría omitida debe justificarse explícitamente en sección 8.")

criticos = r[r.valor >= 15]
print(f"\n=== RIESGOS ≥ 15 — requieren decisión de la gerencia general ===")
print(criticos[["id","Categoría","valor"]].to_string(index=False))

# Mapa de calor
m = np.zeros((5,5))
for _, x in r.iterrows(): m[5-x.I, x.P-1] += 1
fig, ax = plt.subplots(figsize=(8,7))
im = ax.imshow(m, cmap="RdYlGn_r", vmin=0, vmax=max(m.max(),1))
for i in range(5):
    for j in range(5):
        v = int(m[i,j])
        if v: ax.text(j, i, v, ha="center", va="center", fontsize=13, fontweight="bold")
ax.set_xticks(range(5)); ax.set_xticklabels(["1 Muy baja","2 Baja","3 Media","4 Alta","5 Muy alta"], fontsize=8)
ax.set_yticks(range(5)); ax.set_yticklabels(["5 Catastrófico","4 Mayor","3 Moderado","2 Menor","1 Insignif."], fontsize=8)
ax.set_xlabel("Probabilidad"); ax.set_ylabel("Impacto")
ax.set_title("Mapa de calor — riesgos de ejecución del PETI")
plt.colorbar(im, label="N.º de riesgos"); plt.tight_layout()
plt.savefig("../graficos/RG_mapa_calor.png", dpi=140)
