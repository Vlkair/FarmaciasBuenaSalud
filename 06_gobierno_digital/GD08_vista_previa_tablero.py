# 06_gobierno_digital/GD08_vista_previa_tablero.py
# Ejecuta las 6 consultas de GD06 contra PostgreSQL y dibuja una vista previa del tablero.
# NO reemplaza las capturas de Metabase: sirve para verificar los datos antes de armarlo.
import re, psycopg, pandas as pd, matplotlib.pyplot as plt, textwrap
con = psycopg.connect("host=127.0.0.1 port=5433 dbname=peti user=peti password=peti_lab")
sql = open("GD06_preguntas_tablero.sql", encoding="utf-8").read()
Q = {}
for b in [b for b in sql.split(";") if "SELECT" in b]:
    k = re.search(r"-- (V\d) · ([^·\n]+)", b)
    cur = con.execute(b[b.index("SELECT"):])
    Q[k.group(1)] = (k.group(2).strip(), pd.DataFrame(cur.fetchall(), columns=[d.name for d in cur.description]))
AZ, CE, RO = "#16285C", "#0EA5E9", "#B91C1C"
fig, ax = plt.subplots(3, 2, figsize=(16, 17)); ax = ax.ravel()
t, d = Q["V1"]; d = d.iloc[::-1]
ax[0].barh(d.servicio.str.slice(0, 42), d.nivel_actual, color=AZ, label="Actual")
ax[0].barh(d.servicio.str.slice(0, 42), d.nivel_objetivo - d.nivel_actual, left=d.nivel_actual, color=CE, alpha=.5, label="Brecha")
ax[0].set_xlim(0, 5); ax[0].legend(loc="lower right"); ax[0].tick_params(axis="y", labelsize=8)
t, d = Q["V2"]; ax[1].axis("off")
ax[1].text(.5, .58, f"{float(d.nivel_ponderado[0]):.2f}", ha="center", fontsize=80, color=AZ, weight="bold")
ax[1].text(.5, .38, "nivel ponderado por volumen (0–5)", ha="center", fontsize=14)
ax[1].text(.5, .26, f"promedio simple: {float(d.nivel_simple[0]):.2f}", ha="center", fontsize=13, color=RO)
t3, d = Q["V3"]; ax[2].bar(d.eje.str.split(". ", n=1, regex=False).str[1], d.nivel.astype(float), color=AZ)
ax[2].set_ylim(0, 5); ax[2].tick_params(axis="x", rotation=30, labelsize=9)
t4, d = Q["V4"]; ax[3].pie(d.obligaciones, labels=[f"{e} ({n})" for e, n in zip(d.estado, d.obligaciones)],
                         colors=[RO, "#F59E0B", "#059669", "#9CA3AF"], wedgeprops=dict(width=.4), startangle=90)
t5, d = Q["V5"]; x = range(len(d))
ax[4].bar([i - .2 for i in x], d.nivel_actual, .4, color=AZ, label="Actual")
ax[4].bar([i + .2 for i in x], d.nivel_objetivo, .4, color=CE, label="Objetivo")
ax[4].set_xticks(list(x)); ax[4].set_xticklabels(d.objetivo, rotation=45, fontsize=9); ax[4].set_ylim(0, 5); ax[4].legend()
t6, d = Q["V6"]; ax[5].axis("off")
tb = ax[5].table(cellText=[[e, textwrap.fill(i, 30), textwrap.fill(p, 34)] for e, i, p in d.values],
                 colLabels=["Eje", "Indicador", "Proyecto"], loc="center", cellLoc="left", colWidths=[.22, .36, .42])
tb.auto_set_font_size(False); tb.set_fontsize(8); tb.scale(1, 3.2)
for a, (k, (tt, _)) in zip(ax, Q.items()): a.set_title(f"{k} · {tt}", fontsize=12, weight="bold", color=AZ)
fig.suptitle("Tablero de línea base · Cadena de Farmacias Buena Salud\n(vista previa desde PostgreSQL — no es captura de Metabase)", fontsize=15)
plt.tight_layout(); plt.savefig("../graficos/GD_tablero_vista_previa.png", dpi=110)
print("graficos/GD_tablero_vista_previa.png")
