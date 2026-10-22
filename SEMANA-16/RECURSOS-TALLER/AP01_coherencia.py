# 09_aprobacion/AP01_coherencia.py
import pandas as pd, re, sys

def csv(ruta, cols=None):
    try:
        return pd.read_csv(ruta)
    except FileNotFoundError:
        print(f"  ⚠ FALTA el archivo {ruta}")
        return pd.DataFrame(columns=cols or [])

obj  = csv("../06_gobierno_digital/OB02_objetivos.csv")
est  = csv("../03_diagnostico/PE03_foda_cruzado.csv")
proy = csv("../07_portafolio/PF01_portafolio_candidatos.csv")
hr   = csv("../07_portafolio/PR05_hoja_ruta.csv")
pres = csv("../07_portafolio/PR06_presupuesto.csv")
brec = csv("../05_arquitectura/AR03_brechas.csv")
ries = csv("../08_riesgos/RG04_tratamiento.csv")
vis  = open("../02_identidad/2.2_vision.md").read() if __import__("os").path.exists("../02_identidad/2.2_vision.md") else ""

errores, avisos = [], []
print("=" * 78)
print("VERIFICACIÓN DE COHERENCIA DEL PETI")
print("=" * 78)

# --- 1. Visión → objetivos ---
print("\n[1] VISIÓN → OBJETIVOS")
metricas = re.findall(r"(\d+[.,]?\d*)\s*%", vis)
print(f"    Métricas detectadas en la visión: {metricas or 'ninguna'}")
if metricas:
    texto_obj = " ".join(obj["Enunciado SMART"].astype(str)) if "Enunciado SMART" in obj else ""
    huerfanas = [m for m in metricas if m not in texto_obj]
    if huerfanas:
        errores.append(f"Métricas de la visión sin objetivo que las mida: {huerfanas}")
        print(f"    ✗ Sin objetivo asociado: {huerfanas}")
    else:
        print("    ✔ Todas las métricas de la visión tienen objetivo")
else:
    avisos.append("La visión no contiene métricas verificables")

# --- 2 y 3. Estrategias ↔ objetivos ---
print("\n[2-3] ESTRATEGIAS ↔ OBJETIVOS")
ids_est = set(est.id) if "id" in est else set()
en_obj = set()
if "Estrategias que lo sustentan" in obj:
    for x in obj["Estrategias que lo sustentan"].astype(str):
        en_obj |= {e.strip() for e in x.split(",") if e.strip()}
sin_obj = ids_est - en_obj
if sin_obj:
    avisos.append(f"Estrategias sin objetivo asociado: {sorted(sin_obj)}")
    print(f"    ~ Estrategias sin objetivo: {sorted(sin_obj)} — justificar o retirar")
inexistentes = en_obj - ids_est
if inexistentes:
    errores.append(f"Objetivos que citan estrategias inexistentes: {sorted(inexistentes)}")
    print(f"    ✗ Estrategias citadas que no existen: {sorted(inexistentes)}")
if not sin_obj and not inexistentes:
    print("    ✔ Correspondencia completa")

# --- 4. Objetivos → proyectos ---
print("\n[4] OBJETIVOS → PROYECTOS")
ids_obj = set(obj["Código"]) if "Código" in obj else set()
obj_en_proy = set()
if "objetivo" in proy:
    for x in proy.objetivo.astype(str):
        obj_en_proy |= {o.strip() for o in x.split(",") if o.strip()}
sin_proy = ids_obj - obj_en_proy
if sin_proy:
    errores.append(f"Objetivos sin ningún proyecto: {sorted(sin_proy)}")
    print(f"    ✗ Objetivos sin proyecto: {sorted(sin_proy)}")
else:
    print("    ✔ Todo objetivo tiene al menos un proyecto")

# --- 5. Proyectos → hoja de ruta → presupuesto ---
print("\n[5] PROYECTOS → HOJA DE RUTA → PRESUPUESTO")
ids_proy = set(proy.codigo) if "codigo" in proy else set()
en_hr = set(hr.Proyecto) if "Proyecto" in hr else set()
no_programados = ids_proy - en_hr
if no_programados:
    avisos.append(f"Proyectos del portafolio no programados: {sorted(no_programados)}")
    print(f"    ~ Sin programar: {sorted(no_programados)} — ¿son los descartados de sección 7.2.5?")
fantasma = en_hr - ids_proy
if fantasma:
    errores.append(f"Proyectos en la hoja de ruta que no están en el portafolio: {sorted(fantasma)}")
    print(f"    ✗ En la hoja de ruta sin ficha: {sorted(fantasma)}")
if not pres.empty:
    print(f"    ✔ Presupuesto elaborado para {len(pres)} años, total S/ {pres.total.sum():,.0f}")

# --- 6. Arquitectura → proyectos ---
print("\n[6] BRECHAS DE ARQUITECTURA → PROYECTOS")
if "actual" in brec:
    print(f"    Brechas identificadas: {len(brec)}")
    print("    → Verificar manualmente que cada brecha tenga paquete de trabajo y proyecto")

# --- 7. Riesgos → tratamiento → recursos ---
print("\n[7] RIESGOS → TRATAMIENTO")
if "Valor residual" in ries:
    sobre = ries[ries["Valor residual"] > 6]
    print(f"    Riesgos residuales sobre el criterio: {len(sobre)} → requieren firma en sección 9")
    sin_resp = ries[ries["Responsable (cargo)"].isna()] if "Responsable (cargo)" in ries else pd.DataFrame()
    if len(sin_resp):
        errores.append(f"Tratamientos sin responsable: {len(sin_resp)}")
        print(f"    ✗ Tratamientos sin responsable: {len(sin_resp)}")
    else:
        print("    ✔ Todos los tratamientos tienen responsable")

# --- Contraste con los Lineamientos del PGD ---
print("\n[PGD] COBERTURA DE LOS COMPONENTES EXIGIDOS")
doc = open("PETI_COMPLETO.md").read()
COMPONENTES = {
 "1 Introducción y marco normativo": ["marco normativo", "presentación"],
 "2 Situación actual": ["análisis interno", "análisis externo", "situación actual"],
 "3 Alineamiento estratégico": ["articula", "alineamiento", "objetivo superior"],
 "4 Objetivos de gobierno digital": ["objetivos", "indicador", "meta"],
 "5 Portafolio de proyectos": ["portafolio", "proyecto"],
 "6 Gestión de riesgos": ["riesgo", "tratamiento"],
 "7 Cronograma e implementación": ["hoja de ruta", "cronograma", "presupuesto"],
 "8 Supervisión y evaluación": ["supervisión", "seguimiento", "evaluación"],
}
for comp, claves in COMPONENTES.items():
    presente = any(k.lower() in doc.lower() for k in claves)
    print(f"    {'✔' if presente else '✗ FALTA'}  {comp}")
    if not presente:
        errores.append(f"Componente del PGD ausente: {comp}")

print("\n" + "=" * 78)
if avisos:
    print(f"AVISOS ({len(avisos)}):")
    for a in avisos: print(f"  ~ {a}")
if errores:
    print(f"\nNO CONFORMIDADES ({len(errores)}):")
    for e in errores: print(f"  ✗ {e}")
    print("\nEl PETI no puede someterse a aprobación hasta corregirlas.")
    sys.exit(1)
