#!/usr/bin/env python3
"""Regenera encuesta_cultura.csv en la carpeta de cada organización (Semana 05 · SI-886).

Respuestas simuladas al instrumento del Competing Values Framework. Solo Python estándar.
Las semillas son fijas por organización: cada ejecución produce exactamente los mismos datos.
Tres respuestas por organización no suman 100 a propósito, para que el control de calidad
de CU02_perfil_cultura.py tenga algo que detectar.

    python3 generar_encuesta_cultura.py        # las diez organizaciones
    python3 generar_encuesta_cultura.py 06     # solo la 06
"""
import math, random, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PERSONAL = {'01': 142, '02': 214, '03': 178, '04': 96, '05': 268, '06': 157, '07': 88, '08': 312, '09': 421, '10': 196}
AREAS = {'01': {'Contabilidad': 12, 'Tecnologías de la Información': 11, 'Recursos Humanos': 18, 'Logística': 7, 'Comercial': 14, 'Tesorería': 12, 'Almacén': 16, 'Administración y Finanzas': 10, 'Operaciones': 15, 'Legal': 12, 'Compras': 9, 'Gerencia': 6}, '02': {'Compras': 21, 'Gerencia': 18, 'Almacén': 22, 'Tesorería': 18, 'Logística': 17, 'Operaciones': 27, 'Legal': 12, 'Tecnologías de la Información': 15, 'Contabilidad': 18, 'Administración y Finanzas': 17, 'Recursos Humanos': 16, 'Comercial': 13}, '03': {'Operaciones': 13, 'Administración y Finanzas': 10, 'Gerencia': 15, 'Contabilidad': 13, 'Recursos Humanos': 17, 'Logística': 16, 'Almacén': 18, 'Tesorería': 12, 'Legal': 15, 'Comercial': 18, 'Tecnologías de la Información': 16, 'Compras': 15}, '04': {'Logística': 2, 'Tecnologías de la Información': 15, 'Gerencia': 8, 'Operaciones': 5, 'Administración y Finanzas': 10, 'Recursos Humanos': 7, 'Contabilidad': 13, 'Almacén': 7, 'Tesorería': 4, 'Comercial': 10, 'Legal': 10, 'Compras': 5}, '05': {'Legal': 19, 'Recursos Humanos': 21, 'Administración y Finanzas': 30, 'Tesorería': 20, 'Contabilidad': 21, 'Logística': 16, 'Operaciones': 22, 'Compras': 21, 'Comercial': 24, 'Tecnologías de la Información': 30, 'Almacén': 21, 'Gerencia': 23}, '06': {'Legal': 17, 'Logística': 5, 'Almacén': 10, 'Tesorería': 14, 'Compras': 19, 'Tecnologías de la Información': 13, 'Administración y Finanzas': 16, 'Contabilidad': 11, 'Comercial': 15, 'Operaciones': 18, 'Gerencia': 9, 'Recursos Humanos': 10}, '07': {'Contabilidad': 7, 'Comercial': 11, 'Compras': 8, 'Administración y Finanzas': 10, 'Operaciones': 6, 'Tecnologías de la Información': 4, 'Logística': 7, 'Almacén': 5, 'Tesorería': 13, 'Legal': 7, 'Gerencia': 2, 'Recursos Humanos': 8}, '08': {'Administración y Finanzas': 27, 'Operaciones': 23, 'Tecnologías de la Información': 27, 'Recursos Humanos': 27, 'Almacén': 24, 'Logística': 22, 'Contabilidad': 42, 'Comercial': 28, 'Gerencia': 30, 'Legal': 17, 'Compras': 23, 'Tesorería': 22}, '09': {'Recursos Humanos': 42, 'Logística': 31, 'Almacén': 44, 'Comercial': 25, 'Tecnologías de la Información': 36, 'Administración y Finanzas': 46, 'Contabilidad': 28, 'Tesorería': 42, 'Legal': 38, 'Operaciones': 35, 'Compras': 31, 'Gerencia': 22}, '10': {'Gerencia': 21, 'Tecnologías de la Información': 13, 'Almacén': 16, 'Comercial': 20, 'Administración y Finanzas': 16, 'Legal': 14, 'Compras': 17, 'Logística': 17, 'Recursos Humanos': 21, 'Contabilidad': 10, 'Operaciones': 18, 'Tesorería': 13}}
PERFIL = {'01': ((22, 14, 30, 34), (24, 24, 32, 20)), '02': ((28, 12, 20, 40), (30, 24, 20, 26)), '03': ((24, 8, 20, 48), (28, 22, 18, 32)), '04': ((30, 10, 18, 42), (30, 20, 26, 24)), '05': ((20, 10, 36, 34), (22, 26, 30, 22)), '06': ((26, 12, 20, 42), (24, 26, 20, 30)), '07': ((38, 14, 18, 30), (30, 30, 18, 22)), '08': ((22, 8, 20, 50), (26, 18, 22, 34)), '09': ((16, 10, 38, 36), (20, 24, 32, 24)), '10': ((20, 10, 40, 30), (26, 24, 30, 20))}
AJUSTE_AREA = {'Tecnologías de la Información': (0, 8, 0, -8), 'Gerencia': (-4, 2, 8, -6), 'Comercial': (-2, 2, 8, -8), 'Contabilidad': (-2, -4, -2, 8), 'Legal': (-2, -4, -2, 8), 'Tesorería': (0, -4, 0, 4), 'Recursos Humanos': (6, 0, -4, -2), 'Operaciones': (0, 0, 2, -2)}
DIM = ['caracteristicas', 'liderazgo', 'personal', 'cohesion', 'enfasis', 'exito']
TIPOS = ['A', 'B', 'C', 'D']

def reparto_100(valores):
    """Convierte cuatro valores positivos en enteros que suman exactamente 100."""
    total = sum(valores)
    crudos = [v * 100 / total for v in valores]
    enteros = [int(math.floor(c)) for c in crudos]
    resto = 100 - sum(enteros)
    orden = sorted(range(4), key=lambda i: crudos[i] - enteros[i], reverse=True)
    for i in orden[:resto]:
        enteros[i] += 1
    return enteros


def generar_encuesta(nn, destino):
    rnd = random.Random(int(nn) * 1000 + 5)
    n = math.ceil(PERSONAL[nn] * 0.33)
    areas = list(AREAS[nn].items())
    poblacion = [a for a, c in areas for _ in range(c)]
    hoy_base, fut_base = PERFIL[nn]
    cab = ["id", "area"] + [f"{d}_{t}_{m}" for d in DIM for t in TIPOS for m in ("hoy", "futuro")]
    filas = []
    invalidas = set(rnd.sample(range(n), 3))  # tres respuestas con suma distinta de 100, a propósito
    for i in range(n):
        area = rnd.choice(poblacion)
        aj = AJUSTE_AREA.get(area, (0, 0, 0, 0))
        fila = [f"R{i + 1:03d}", area]
        for d in DIM:
            for m, base in (("hoy", hoy_base), ("futuro", fut_base)):
                vals = [max(2.0, b + a + rnd.gauss(0, 6)) for b, a in zip(base, aj)]
                rep = reparto_100(vals)
                if i in invalidas:
                    rep[rnd.randrange(4)] += rnd.choice([-12, 15])
                fila += rep
        # las columnas van ordenadas dim -> tipo -> momento; reordenar
        filas.append(fila)
    # reordenar cada fila al orden de la cabecera (dim, tipo, momento)
    salida = []
    for fila in filas:
        base = fila[:2]
        vals = fila[2:]
        # vals está en orden dim -> momento -> tipo; cabecera es dim -> tipo -> momento
        reord = []
        for di in range(len(DIM)):
            bloque = vals[di * 8:(di + 1) * 8]  # hoy[4], futuro[4]
            hoy, fut = bloque[:4], bloque[4:]
            for ti in range(4):
                reord += [hoy[ti], fut[ti]]
        salida.append(base + reord)
    with open(destino, "w", encoding="utf-8", newline="") as f:
        f.write(",".join(cab) + "\n")
        for fila in salida:
            f.write(",".join(str(x) for x in fila) + "\n")
    return n


if __name__ == "__main__":
    pedidas = sys.argv[1:] or sorted(PERSONAL)
    for carpeta in sorted(AQUI.glob("EMPRESA-*")):
        num = carpeta.name.split("-")[1]
        if num in pedidas:
            n = generar_encuesta(num, carpeta / "encuesta_cultura.csv")
            print(f"{carpeta.name}: {n} respuestas")
