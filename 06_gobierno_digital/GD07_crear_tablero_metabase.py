# 06_gobierno_digital/GD07_crear_tablero_metabase.py
# Crea en Metabase las 6 preguntas de GD06_preguntas_tablero.sql y el tablero
# "Línea base de gobierno digital · Buena Salud" usando la API REST de Metabase.
#
# Requisitos: contenedores peti_db y peti_metabase arriba, GD05_carga_tablero.py ejecutado
# y la cuenta de administrador creada en http://127.0.0.1:3001 (asistente inicial).
# Uso:  pip install requests
#       MB_USER=correo@upt.pe MB_PASS=su_clave python3 GD07_crear_tablero_metabase.py
import os, re, sys, requests

MB = os.environ.get("MB_URL", "http://127.0.0.1:3001")
USER, PASS = os.environ.get("MB_USER"), os.environ.get("MB_PASS")
if not USER or not PASS:
    sys.exit("Defina MB_USER y MB_PASS con la cuenta de administrador de Metabase.")

s = requests.Session()
tok = s.post(f"{MB}/api/session", json={"username": USER, "password": PASS}).json()["id"]
s.headers["X-Metabase-Session"] = tok

def lista(r):                       # /api/database devuelve lista o {"data": [...]} según versión
    j = r.json();  return j["data"] if isinstance(j, dict) and "data" in j else j

# 1. Fuente de datos "peti" (la crea si no existe)
dbs = [d for d in lista(s.get(f"{MB}/api/database")) if d["name"] == "peti"]
if dbs:
    db_id = dbs[0]["id"]
else:
    db_id = s.post(f"{MB}/api/database", json={
        "engine": "postgres", "name": "peti",
        "details": {"host": "host.docker.internal", "port": 5433, "dbname": "peti",
                    "user": "peti", "password": "peti_lab", "ssl": False}}).json()["id"]
print(f"Base de datos 'peti' en Metabase: id {db_id}")

# 2. Preguntas: se leen del archivo SQL (un bloque por visualización)
VIS = {"V1": "row", "V2": "scalar", "V3": "bar", "V4": "pie", "V5": "bar", "V6": "table"}
sql = open("GD06_preguntas_tablero.sql", encoding="utf-8").read()
cards = []
for bloque in [b for b in sql.split(";") if "SELECT" in b]:
    m = re.search(r"-- (V\d) · ([^·\n]+)", bloque)
    clave, nombre = m.group(1), m.group(2).strip()
    consulta = bloque[bloque.index("SELECT"):].strip()
    card = s.post(f"{MB}/api/card", json={
        "name": f"{clave} · {nombre}", "display": VIS[clave],
        "dataset_query": {"type": "native", "database": db_id, "native": {"query": consulta}},
        "visualization_settings": {}}).json()
    cards.append(card["id"]);  print(f"Pregunta creada: {clave} · {nombre} (id {card['id']})")

# 3. Tablero con las seis tarjetas en una rejilla de 2 columnas
dash = s.post(f"{MB}/api/dashboard", json={
    "name": "Línea base de gobierno digital · Buena Salud",
    "description": "PETI · Sección 6.1 · Taller S11"}).json()
pos = [(0, 0), (0, 12), (8, 0), (8, 12), (16, 0), (16, 12)]
dashcards = [{"id": -(i + 1), "card_id": c, "row": r, "col": col, "size_x": 12, "size_y": 8,
              "parameter_mappings": [], "series": [], "visualization_settings": {}}
             for i, (c, (r, col)) in enumerate(zip(cards, pos))]
r = s.put(f"{MB}/api/dashboard/{dash['id']}", json={"dashcards": dashcards})
if r.status_code >= 400:            # versiones anteriores a la 0.47
    for d in dashcards:
        s.post(f"{MB}/api/dashboard/{dash['id']}/cards",
               json={k: d[k] for k in ("card_id", "row", "col", "size_x", "size_y")} | {"cardId": d["card_id"]})
print(f"Tablero listo: {MB}/dashboard/{dash['id']}")
