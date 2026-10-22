# 03_diagnostico/AI06_capacidades.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt
c = pd.read_csv("AI05_capacidades_ti.csv")
c["brecha"] = c["Nivel requerido por la visión"] - c["Nivel actual (1–5)"]
print(c.sort_values("brecha", ascending=False)[["Capacidad de TI","Nivel actual (1–5)",
      "Nivel requerido por la visión","brecha","Criticidad"]].to_string(index=False))
print(f"\nNivel medio actual: {c['Nivel actual (1–5)'].mean():.2f} | "
      f"requerido: {c['Nivel requerido por la visión'].mean():.2f}")
print(f"Brecha total: {c.brecha.sum()} niveles | Capacidades críticas con brecha ≥ 2: "
      f"{len(c[(c.Criticidad=='Crítica') & (c.brecha>=2)])}")

ang = np.linspace(0, 2*np.pi, len(c), endpoint=False).tolist(); ang += ang[:1]
fig, ax = plt.subplots(figsize=(9,9), subplot_kw=dict(polar=True))
for col, lab, st, color in [("Nivel actual (1–5)","Actual","-","#16285C"),
                            ("Nivel requerido por la visión","Requerido","--","#0EA5E9")]:
    v = c[col].tolist(); v += v[:1]
    ax.plot(ang, v, st, linewidth=2.5, label=lab, color=color); ax.fill(ang, v, alpha=.12, color=color)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(c["Capacidad de TI"], fontsize=8)
ax.set_yticks(range(6)); ax.set_ylim(0,5)
ax.set_title("Capacidades de TI: nivel actual vs. requerido por la visión", pad=24)
ax.legend(loc="upper right", bbox_to_anchor=(1.3,1.1))
plt.tight_layout(); plt.savefig("../graficos/AI_capacidades_ti.png", dpi=140)
