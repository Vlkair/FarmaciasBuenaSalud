# 01_marco/VS02_extraccion_bcrp.py
import requests, pandas as pd, hashlib, json
from datetime import date

BASE = "https://estadisticas.bcrp.gob.pe/estadisticas/series/api"

# Rango relativo: siempre los últimos N años respecto de la fecha de ejecución.
# Así el script no envejece con el material.
HOY   = date.today()
DESDE = f"{HOY.year - 6}-1"
HASTA = f"{HOY.year}-{HOY.month}"

SERIES = {
    "PN01207PM": "Tipo de cambio interbancario (S/ por US$) — promedio del periodo",
    "PN01273PM": "IPC de Lima Metropolitana — variación % de los últimos 12 meses",
    "PN01770AM": "Producto bruto interno — índice 2007 = 100",
}

def serie_bcrp(codigo, desde=DESDE, hasta=HASTA):
    url = f"{BASE}/{codigo}/json/{desde}/{hasta}/esp"
    r = requests.get(url, timeout=30); r.raise_for_status()
    d = r.json()
    df = pd.DataFrame([{"periodo": p["name"], "valor": p["values"][0]} for p in d["periods"]])
    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")
    df["codigo"] = codigo
    df["url_origen"] = url
    df["fecha_descarga"] = date.today().isoformat()
    df["hash_respuesta"] = hashlib.sha256(r.content).hexdigest()[:16]
    return df

frames = []
for cod, nombre in SERIES.items():
    try:
        s = serie_bcrp(cod); s["indicador"] = nombre
        frames.append(s)
        print(f"✔ {cod}: {len(s)} observaciones — {nombre}")
    except Exception as e:
        print(f"✗ {cod}: {e}  → registrar como limitación en el papel de trabajo")

datos = pd.concat(frames, ignore_index=True)

# Transformación documentada. El BCRP publica el PBI como índice, no como tasa:
# la variación interanual se calcula aquí y se registra identificada como cálculo
# propio, nunca como si fuera el dato original de la fuente.
pbi = datos[datos.codigo == "PN01770AM"].copy()
pbi["valor"] = pbi["valor"].pct_change(12) * 100
pbi["codigo"] = "PN01770AM/var12"
pbi["indicador"] = "Producto bruto interno — variación % interanual (cálculo propio)"
datos = pd.concat([datos, pbi.dropna(subset=["valor"])], ignore_index=True)

datos.to_csv("../evidencias/VS_series_bcrp.csv", index=False)
print(datos.groupby("indicador").valor.agg(["count","min","max","last"]).to_string())
