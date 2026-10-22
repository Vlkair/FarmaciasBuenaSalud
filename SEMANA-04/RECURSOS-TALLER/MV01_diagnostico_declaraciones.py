# 02_identidad/MV01_diagnostico_declaraciones.py
"""Diagnóstico técnico de la misión y la visión publicadas por una empresa.

Aplica los instrumentos de la teoría de la Semana 04 — los cinco componentes,
los siete defectos, las tres pruebas de calidad y los cinco atributos de la
visión— y emite el veredicto. El programa detecta lo que se puede leer en el
texto; el juicio que exige evidencia lo pone el equipo, y lo sustenta.
"""
import re
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# LO QUE EL EQUIPO EDITA. Todo lo de abajo son los datos de una empresa de
# ejemplo, inventada para el programa. Se reemplazan por los de la empresa real
# que el equipo eligió en el Paso A.
# ---------------------------------------------------------------------------
EMPRESA = "Nexa Cloud Perú S.A.C."
COMPETIDORES = ["Andes Software S.A.C.",
                "Datacenter del Sur S.A.",
                "Kuntur Systems S.A.C."]

MISION = ("Brindar soluciones tecnológicas innovadoras y de calidad que satisfagan "
          "las necesidades de nuestros clientes, con un equipo comprometido y en "
          "constante mejora continua.")

VISION = ("Ser la empresa líder e innovadora en transformación digital, reconocida "
          "por su excelencia y su compromiso con el cliente.")

FUENTE = {
    "Dirección de la página": "https://www.nexacloud.example.pe/nosotros",
    "Fecha de consulta": "10 de septiembre de 2026",
    "¿Publica visión?": "Sí, en la misma página",
    "Prueba de la decisión": "No comprobable desde fuera de la empresa. Se declara así",
}

# Los cinco componentes. Se escribe el fragmento LITERAL de la declaración que
# porta cada uno, o None si no está. La cita es lo que hace verificable el
# diagnóstico — sin ella es una opinión.
COMPONENTES = {
    "Qué hacemos":        "Brindar soluciones tecnológicas",
    "Para quién":         None,
    "Cómo nos distingue": None,
    "Para qué":           None,
    "Con qué compromiso": "con un equipo comprometido",
}

# Los tres defectos que no se leen en el texto. Cada uno con la evidencia.
JUICIO_MISION = {
    "Intercambiable":
        (True, "Sobrevive a los tres competidores de la prueba de sustitución"),
    "Contradice la práctica":
        (False, "No hay evidencia pública que la contradiga"),
    "Escrita por una sola persona":
        (False, "No se puede comprobar desde fuera de la empresa"),
}

# Los tres atributos de la visión que exigen juicio del equipo.
JUICIO_VISION = {
    "Ambiciosa pero alcanzable":
        (False, "No declara ninguna meta, de modo que no hay nada que contrastar con su tamaño"),
    "Específica del negocio":
        (False, "«transformación digital» describe a cualquier empresa del rubro"),
    "Movilizadora":
        (False, "Nadie puede saber qué hacer distinto mañana a partir de esta frase"),
}

# ---------------------------------------------------------------------------
# LO QUE EL PROGRAMA DETECTA EN EL TEXTO
# ---------------------------------------------------------------------------
ASPIRACIONAL = re.compile(r"\b(ser|seremos|convertirnos|liderar|líder\w*|"
                          r"número uno|primera opción|la mejor)\b", re.I)
VALORES = re.compile(r"\b(honestidad|respeto|integridad|excelencia|compromis\w+|"
                     r"innovación|calidad total|trabajo en equipo|mejora continua|"
                     r"transparencia|responsabilidad)\b", re.I)
HORIZONTE = re.compile(r"(al\s+(año\s+)?20\d{2}|en\s+20\d{2}|"
                       r"al cierre del horizonte|a\s+\w+\s+años)", re.I)
METRICA = re.compile(r"\d+([.,]\d+)?\s*(%|por ciento|puntos|horas|días|millones|mil)", re.I)

pal_mision = len(MISION.split())
pal_vision = len(VISION.split())
presentes = {k: v for k, v in COMPONENTES.items() if v}

print("=" * 74)
print(f"DIAGNÓSTICO DE LAS DECLARACIONES PUBLICADAS · {EMPRESA}")
print("=" * 74)
for k, v in FUENTE.items():
    print(f"  {k:32s} {v}")

# --- Los cinco componentes de la misión ---
print(f"\n=== MISIÓN · {pal_mision} palabras ===")
print(f"«{MISION}»\n")
print("Los cinco componentes")
for comp, cita in COMPONENTES.items():
    marca = "SÍ" if cita else "NO"
    print(f"  [{marca}] {comp:20s} {cita or '— ausente'}")
print(f"  → {len(presentes)} de 5 componentes")

# --- Los siete defectos ---
detectados = {
    "Intercambiable": JUICIO_MISION["Intercambiable"],
    "Confunde misión con visión": (
        bool(ASPIRACIONAL.search(MISION)),
        "Lenguaje de aspiración en el texto — " + ", ".join(sorted(
            {m.group(0).lower() for m in ASPIRACIONAL.finditer(MISION)}))),
    "Enumera valores": (
        len({m.group(0).lower() for m in VALORES.finditer(MISION)}) >= 3,
        "Tres o más términos de valor en el texto"),
    "Omite al destinatario": (
        COMPONENTES["Para quién"] is None,
        "El componente «Para quién» no está en la declaración"),
    "Extensión desmedida": (
        pal_mision > 50, f"{pal_mision} palabras, el límite práctico es 50"),
    "Contradice la práctica": JUICIO_MISION["Contradice la práctica"],
    "Escrita por una sola persona": JUICIO_MISION["Escrita por una sola persona"],
}
print("\nLos siete defectos")
for defecto, (hay, razon) in detectados.items():
    print(f"  [{'X' if hay else ' '}] {defecto:30s} {razon if hay else ''}")
n_defectos = sum(1 for hay, _ in detectados.values() if hay)
print(f"  → {n_defectos} de 7 defectos")

# --- Las tres pruebas de calidad ---
print("\nPrueba de sustitución — se lee cada línea en voz alta")
for comp in COMPETIDORES:
    print(f"  · {comp} — «{MISION[:64]}…»")
sobrevive = JUICIO_MISION["Intercambiable"][0]
print(f"  → {'FALLA' if sobrevive else 'PASA'} la prueba de sustitución")
print(f"Prueba de la decisión  → {FUENTE['Prueba de la decisión']}")
print("Prueba del reconocimiento → se responde si el equipo tiene acceso; si no, se declara no comprobable")

# --- Los cinco atributos de la visión ---
print(f"\n=== VISIÓN · {pal_vision} palabras ===")
print(f"«{VISION}»\n")
hay_horizonte, hay_metrica = bool(HORIZONTE.search(VISION)), bool(METRICA.search(VISION))
atributos = {
    "Temporalmente acotada": (
        hay_horizonte, "Declara el horizonte" if hay_horizonte
        else "Sin horizonte. No se puede medir avance ni saber si se alcanzó"),
    "Verificable": (
        hay_metrica, "Trae una cifra comprobable" if hay_metrica
        else "Sin cifra. No orienta ninguna decisión de inversión"),
    "Ambiciosa pero alcanzable": JUICIO_VISION["Ambiciosa pero alcanzable"],
    "Específica del negocio": JUICIO_VISION["Específica del negocio"],
    "Movilizadora": JUICIO_VISION["Movilizadora"],
}
print("Los cinco atributos")
for atr, (cumple, razon) in atributos.items():
    print(f"  [{'SÍ' if cumple else 'NO'}] {atr:26s} {razon}")
n_atributos = sum(1 for c, _ in atributos.values() if c)
print(f"  → {n_atributos} de 5 atributos")
metricas = [m.group(0) for m in METRICA.finditer(VISION)]
print(f"Métricas implícitas en la visión → {metricas or 'ninguna. No hay avance que medir'}")


# --- Veredicto, con las reglas de la teoría ---
def veredicto_mision():
    if sobrevive:
        return ("SE REFORMULA",
                "Falla la prueba de sustitución. Una misión que sirve para un "
                "competidor no dice nada")
    if len(presentes) <= 3:
        return "SE REFORMULA", f"Solo porta {len(presentes)} de los cinco componentes"
    if len(presentes) == 4 or n_defectos:
        return "SE AJUSTA", "Le falta un componente o arrastra un defecto señalable"
    return "SE CONSERVA", "Cinco componentes y las tres pruebas superadas"


def veredicto_vision():
    if n_atributos <= 2:
        return "SE REFORMULA", f"Solo cumple {n_atributos} de los cinco atributos"
    if n_atributos <= 4:
        return "SE AJUSTA", "Le faltan atributos que sí se pueden completar"
    return "SE CONSERVA", "Cumple los cinco atributos"


print("\n" + "=" * 74)
for etiqueta, (v, razon) in [("MISIÓN", veredicto_mision()),
                             ("VISIÓN", veredicto_vision())]:
    print(f"  VEREDICTO DE LA {etiqueta} · {v}")
    print(f"     {razon}")
print("=" * 74)
print("  El equipo evalúa y propone. Cambiar la declaración es decisión de la")
print("  alta dirección de la empresa.")

# --- Gráfico del diagnóstico ---
fig, ejes = plt.subplots(1, 2, figsize=(11, 4))
for eje, datos, titulo in [
        (ejes[0], {k: bool(v) for k, v in COMPONENTES.items()},
         "Misión · los cinco componentes"),
        (ejes[1], {k: c for k, (c, _) in atributos.items()},
         "Visión · los cinco atributos")]:
    etiquetas = list(datos)[::-1]
    valores = [1 if datos[e] else 0 for e in etiquetas]
    eje.barh(etiquetas, valores,
             color=["#0F766E" if v else "#B45309" for v in valores])
    eje.set_xlim(0, 1)
    eje.set_xticks([0, 1])
    eje.set_xticklabels(["Ausente", "Presente"])
    eje.set_title(titulo, fontsize=10)
    eje.tick_params(labelsize=8)
fig.suptitle(f"Diagnóstico de las declaraciones vigentes · {EMPRESA}", fontsize=11)
plt.tight_layout()
plt.savefig("../graficos/MV_diagnostico_declaraciones.png", dpi=140)
