# 04_normativa/MG04_analisis_capacidad.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
c = pd.read_csv("MG03_capacidad.csv")
c["brecha"] = c["Nivel objetivo"] - c["Nivel actual"]

print(f"Objetivos evaluados         : {len(c)}")
print(f"Nivel medio actual          : {c['Nivel actual'].mean():.2f}")
print(f"Nivel medio objetivo        : {c['Nivel objetivo'].mean():.2f}")
print(f"Brecha total                : {c.brecha.sum()} niveles")
print(f"Procesos en nivel 0         : {(c['Nivel actual']==0).sum()}  ← no existen")
print(f"Objetivos con brecha ≥ 2    : {(c.brecha>=2).sum()}")
print("\n=== PRIORIDAD: relevancia 5 con brecha ≥ 2 ===")
p = c[(c.Relevancia==5) & (c.brecha>=2)].sort_values("brecha", ascending=False)
print(p[["Objetivo","Nombre","Nivel actual","Nivel objetivo","brecha"]].to_string(index=False))

# Radar
ang = np.linspace(0, 2*np.pi, len(c), endpoint=False).tolist(); ang += ang[:1]
fig, ax = plt.subplots(figsize=(9,9), subplot_kw=dict(polar=True))
for col, lab, st, color in [("Nivel actual","Actual","-","#16285C"),
                            ("Nivel objetivo","Objetivo","--","#0EA5E9")]:
    v = c[col].tolist(); v += v[:1]
    ax.plot(ang, v, st, linewidth=2.5, label=lab, color=color); ax.fill(ang, v, alpha=.12, color=color)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(c.Objetivo, fontsize=9)
ax.set_yticks(range(6)); ax.set_ylim(0,5)
ax.set_title("Capacidad de los procesos de TI — COBIT 2019", pad=24)
ax.legend(loc="upper right", bbox_to_anchor=(1.28,1.1))
plt.tight_layout(); plt.savefig("../graficos/MG_capacidad_cobit.png", dpi=140)
