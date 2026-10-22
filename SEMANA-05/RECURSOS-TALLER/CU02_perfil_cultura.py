# 02_identidad/CU02_perfil_cultura.py
import pandas as pd, numpy as np, matplotlib.pyplot as plt

r = pd.read_csv("../evidencias/encuesta_cultura.csv")
DIM = ["caracteristicas","liderazgo","personal","cohesion","enfasis","exito"]
TIPOS = {"A":"Clan", "B":"Adhocracia", "C":"Mercado", "D":"Jerarquía"}

# --- Control de calidad: cada dimensión debe sumar 100 ---
malos = []
for d in DIM:
    for m in ["hoy","futuro"]:
        s = r[[f"{d}_{k}_{m}" for k in TIPOS]].sum(axis=1)
        malos += list(r.index[(s < 98) | (s > 102)])
if malos:
    print(f"⚠ {len(set(malos))} respuestas con sumas fuera de 100 — se excluyen")
    r = r.drop(index=set(malos))
print(f"Respuestas válidas: {len(r)}")

# --- Perfil promedio ---
perfil = {}
for m in ["hoy","futuro"]:
    perfil[m] = {TIPOS[k]: np.mean([r[f"{d}_{k}_{m}"].mean() for d in DIM]) for k in TIPOS}
p = pd.DataFrame(perfil).round(1)
p["brecha"] = (p.futuro - p.hoy).round(1)
p.to_csv("CU02_perfil_cultura.csv")
print("\n=== PERFIL CULTURAL ===")
print(p.to_string())
print(f"\nCultura DOMINANTE actual : {p.hoy.idxmax()} ({p.hoy.max():.1f} puntos)")
print(f"Cultura DESEADA          : {p.futuro.idxmax()} ({p.futuro.max():.1f} puntos)")
print(f"Mayor brecha             : {p.brecha.abs().idxmax()} ({p.loc[p.brecha.abs().idxmax(),'brecha']:+.1f})")

# --- Congruencia: ¿todas las dimensiones apuntan al mismo tipo? ---
print("\n=== CONGRUENCIA POR DIMENSIÓN (actual) ===")
for d in DIM:
    v = {TIPOS[k]: r[f"{d}_{k}_hoy"].mean() for k in TIPOS}
    dom = max(v, key=v.get)
    print(f"  {d:18s} → {dom:12s} ({v[dom]:.1f})")
print("→ Si las dimensiones apuntan a tipos distintos, la cultura es INCONGRUENTE:")
print("  la organización dice una cosa en el liderazgo y otra en el criterio de éxito.")

# --- Diferencias por área (dónde el cambio será más difícil) ---
if "area" in r.columns:
    print("\n=== PERFIL POR ÁREA (solo áreas con ≥5 respondientes) ===")
    for area, g in r.groupby("area"):
        if len(g) < 5: continue
        v = {TIPOS[k]: np.mean([g[f"{d}_{k}_hoy"].mean() for d in DIM]) for k in TIPOS}
        print(f"  {area:18s} → dominante: {max(v, key=v.get):12s} "
              f"({', '.join(f'{k[:4]} {x:.0f}' for k,x in v.items())})")

# --- Gráfico de radar ---
et = list(TIPOS.values()); ang = np.linspace(0, 2*np.pi, 4, endpoint=False).tolist(); ang += ang[:1]
fig, ax = plt.subplots(figsize=(7,7), subplot_kw=dict(polar=True))
for m, color, estilo in [("hoy","#16285C","-"), ("futuro","#0EA5E9","--")]:
    v = [perfil[m][t] for t in et]; v += v[:1]
    ax.plot(ang, v, estilo, linewidth=2.5, label=m.capitalize(), color=color)
    ax.fill(ang, v, alpha=.12, color=color)
ax.set_xticks(ang[:-1]); ax.set_xticklabels(et, fontsize=11)
ax.set_title("Perfil de cultura organizacional\nCompeting Values Framework", pad=24)
ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1))
plt.tight_layout(); plt.savefig("../graficos/CU_perfil_cultura.png", dpi=140)
