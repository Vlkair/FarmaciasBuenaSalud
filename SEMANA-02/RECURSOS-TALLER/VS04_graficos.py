# 01_marco/VS04_graficos.py
import pandas as pd, matplotlib.pyplot as plt

AZUL_UPT, AZUL_EPIS, CIAN = "#16285C", "#174380", "#0EA5E9"

bcrp = pd.read_csv("../evidencias/VS_series_bcrp.csv")
bm   = pd.read_csv("../evidencias/VS_series_banco_mundial.csv")

fig, ax = plt.subplots(1, 2, figsize=(14,5))

# Serie nacional: tipo de cambio
tc = bcrp[bcrp.codigo == "PN01207PM"]
ax[0].plot(range(len(tc)), tc.valor, color=AZUL_UPT, linewidth=2)
ax[0].set_title("Tipo de cambio bancario venta (S/ por US$)\nFuente: BCRP", fontsize=11)
ax[0].set_xticks(range(0, len(tc), max(1, len(tc)//8)))
ax[0].set_xticklabels(tc.periodo.iloc[::max(1, len(tc)//8)], rotation=45, ha="right", fontsize=8)
ax[0].grid(alpha=.3)

# Comparación regional: uso de internet
uso = bm[bm.codigo == "IT.NET.USER.ZS"]
for pais, g in uso.groupby("pais"):
    g = g.sort_values("año")
    ax[1].plot(g.año, g.valor, marker="o", markersize=3,
               linewidth=2.5 if pais == "Peru" else 1.2,
               color=AZUL_UPT if pais == "Peru" else "#9CA3AF", label=pais)
ax[1].set_title("Personas que usan internet (% de la población)\nFuente: Banco Mundial", fontsize=11)
ax[1].legend(fontsize=8); ax[1].grid(alpha=.3); ax[1].set_ylabel("%")

plt.tight_layout(); plt.savefig("../graficos/VS_contexto.png", dpi=140)
print("Gráfico generado: graficos/VS_contexto.png")
