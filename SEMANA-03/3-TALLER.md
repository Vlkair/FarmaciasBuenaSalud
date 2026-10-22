[Semana 03](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 03

## Análisis comparado del PEI y del Plan de Gobierno Digital de una entidad real

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S03-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 03» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Localizar y descargar el **PEI** y el **PGD** vigentes de una entidad pública peruana, ambos documentos públicos.
- Verificar la **articulación** entre ambos. Rastrear cada objetivo del PGD hasta un objetivo del PEI.
- Evaluar el PGD contra la **estructura exigida por los Lineamientos** de la RSGD 005-2018-PCM/SEGDI.
- Construir el **mapa de instrumentos de planeamiento** aplicable a la organización objeto de estudio.
- Determinar el **objetivo superior de articulación** del PETI (Plan Estratégico de Tecnologías de Información) que se está construyendo.
- Redactar la **Sección 1.2** del PETI. Marco de planeamiento y articulación.

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **pdfplumber** y **expresiones regulares** en Python | Extrae la estructura y los objetivos de un PEI y un PGD en PDF, y verifica a mano el resultado | `MP02_estructura_*.csv`, `MP03_objetivos_*.csv` |
| **pandas** | Calcula el porcentaje de objetivos con articulación verificable, indicador, línea base y meta | Salida de `MP05_calidad.py` |
| **draw.io** | Dibuja el mapa de instrumentos de planeamiento de la organización | `mapa_instrumentos.png` |
| **CSV** en LibreOffice Calc | Registra la matriz de articulación y la evaluación contra los Lineamientos | `MP04_articulacion.csv`, `MP06_estructura_lineamientos.csv` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Documentos del caso de su organización y programas de este taller, listos para copiar. El [README](RECURSOS-TALLER/README.md) de la carpeta explica cada archivo |
| **Portal del Estado Peruano** | https://www.gob.pe — sección de transparencia de cada entidad |
| **CEPLAN** | https://www.gob.pe/ceplan — *Guía para el Planeamiento Institucional* |
| **Lineamientos del PGD** | https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf |
| **Normativa de gobierno digital** | https://www.gob.pe/institucion/pcm/colecciones/147-normativa-sobre-gobierno-digital |
| **Python 3.11+** con `pdfplumber`, `pandas` | Extracción de texto de los PDF |
| **draw.io** | Mapa de instrumentos |
| **LibreOffice Calc** | Matriz de articulación |

### 1.3. Seguridad

1. Los PEI y PGD son **documentos públicos**; se descargan de los portales institucionales de transparencia. Se registra la URL y la fecha de descarga.
2. El análisis se realiza sobre el documento **vigente**; si existe más de una versión, se trabaja con la aprobada por resolución y se cita esa resolución.
3. El análisis es **académico y metodológico**. Se evalúa la estructura y la articulación del documento, no se emiten juicios sobre la gestión de la entidad ni sobre personas.
4. La documentación de la organización objeto de estudio se mantiene bajo el acuerdo de confidencialidad.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Su equipo usa la subcarpeta de su organización, `RECURSOS-TALLER/EMPRESA-<NN>-<nombre>/`. Trae `FICHA.md` y `plan-institucional-extracto.md`. **Los Pasos A a C se hacen sobre una entidad pública real**, elegida por el equipo. **Los Pasos D y E se hacen sobre su organización**: el extracto trae el plan vigente, sus objetivos con indicador, línea base y meta, y las actas pertinentes a tecnología. De ahí salen la tabla de instrumentos `MP07`, el mapa de instrumentos y el objetivo superior de articulación de la sección 1.2.3. La sección E de la ficha confirma qué instrumentos existen y en qué estado.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `01_marco/MP04_articulacion.csv`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Localizar los documentos

Se selecciona una entidad pública peruana con ambos documentos publicados (ministerio, gobierno regional, municipalidad provincial, universidad pública, organismo público).

**Este paso no es de trámite. Produce el primer hallazgo del informe.** Cada columna existe porque su respuesta puede descalificar al documento como plan. Se registra en `01_marco/MP01_documentos.csv`:

| Documento | Entidad y periodo que cubre | Resolución que lo aprueba, con su fecha | ¿Se aprobó antes de iniciar el periodo? | ¿Sigue vigente hoy? | ¿Propone proyectos con presupuesto? |
|---|---|---|---|---|---|
| PEI | | | | | |
| PGD | | | | | |
| POI (opcional) | | | | | |

**Qué hallazgo produce cada columna**

| Columna | El hallazgo que puede producir |
|---|---|
| **Resolución que lo aprueba** | Un plan sin resolución **no es exigible a nadie**. Es un borrador. La teoría de esta semana lo dice del PGD — lo aprueba el titular de la entidad. Verifique además que quien firma tenga competencia para hacerlo |
| **¿Se aprobó antes de iniciar el periodo?** | Un plan 2023-2027 aprobado en noviembre de 2024 **no orientó los dos primeros años**. Es de los hallazgos más frecuentes y de los más difíciles de rebatir |
| **¿Sigue vigente hoy?** | El PGD se aprueba por un **mínimo de tres años** y se **actualiza y evalúa cada año**. Un plan vencido, o vigente pero sin ninguna evaluación anual publicada, es incumplimiento de la norma, no un descuido |
| **¿Propone proyectos con presupuesto?** | Es la prueba de que el documento es un **plan** y no una declaración de intenciones. Un documento que no llega a proyectos con costo no permite presupuestar y por eso no se ejecuta |

> **La URL y la fecha en que se consultó cada documento** van en la sección **6. Referencias** del informe, no en esta tabla. Un documento publicado puede cambiar o desaparecer, y la fecha de consulta fija la versión sobre la que usted concluyó.

> Si la entidad elegida no publica su PGD, es en sí un hallazgo relevante. La obligación de contar con el plan y de mantenerlo actualizado deriva del marco de gobierno digital. Se documenta y se elige otra entidad para el análisis comparado.

### Paso B — Extraer la estructura de los documentos

```python
# 01_marco/MP02_extraccion.py
import pdfplumber, re, pandas as pd

def estructura(ruta, patron_titulo=r"^\s*(\d+(?:\.\d+)*)\s+([A-ZÁÉÍÓÚÑ][^\n]{4,90})$"):
    """Extrae el índice real del documento a partir de sus encabezados numerados."""
    filas = []
    with pdfplumber.open(ruta) as pdf:
        for n, pagina in enumerate(pdf.pages, 1):
            texto = pagina.extract_text() or ""
            for linea in texto.split("\n"):
                m = re.match(patron_titulo, linea.strip())
                if m:
                    filas.append({"pagina": n, "numeral": m.group(1),
                                  "titulo": m.group(2).strip(),
                                  "nivel": m.group(1).count(".") + 1})
    return pd.DataFrame(filas).drop_duplicates(subset=["numeral","titulo"])

pei = estructura("../evidencias/PEI.pdf")
pgd = estructura("../evidencias/PGD.pdf")
pei.to_csv("MP02_estructura_pei.csv", index=False)
pgd.to_csv("MP02_estructura_pgd.csv", index=False)
print("=== ESTRUCTURA DEL PEI ===\n", pei[pei.nivel <= 2].to_string(index=False))
print("\n=== ESTRUCTURA DEL PGD ===\n", pgd[pgd.nivel <= 2].to_string(index=False))
```

```python
# 01_marco/MP03_objetivos.py — localizar los objetivos declarados
import pdfplumber, re, pandas as pd

def objetivos(ruta, patrones):
    encontrados = []
    with pdfplumber.open(ruta) as pdf:
        for n, p in enumerate(pdf.pages, 1):
            t = p.extract_text() or ""
            for pat in patrones:
                for m in re.finditer(pat, t):
                    encontrados.append({"pagina": n, "codigo": m.group(1).strip(),
                                        "texto": m.group(2).strip()[:180]})
    return pd.DataFrame(encontrados).drop_duplicates(subset=["codigo"])

PAT_PEI = [r"(OEI\s*\.?\s*\d+)\s*[:.\-]?\s*(.{20,200})",
           r"(AEI\s*\.?\s*[\d.]+)\s*[:.\-]?\s*(.{20,200})"]
PAT_PGD = [r"(O\.?\s?G\.?D\.?\s*\d+|OGD\s*\d+|Objetivo\s+\d+)\s*[:.\-]?\s*(.{20,200})"]

obj_pei = objetivos("../evidencias/PEI.pdf", PAT_PEI)
obj_pgd = objetivos("../evidencias/PGD.pdf", PAT_PGD)
obj_pei.to_csv("MP03_objetivos_pei.csv", index=False)
obj_pgd.to_csv("MP03_objetivos_pgd.csv", index=False)
print(f"Objetivos identificados — PEI: {len(obj_pei)} | PGD: {len(obj_pgd)}")
print(obj_pei.to_string(index=False)); print(obj_pgd.to_string(index=False))
```

> Los patrones deben ajustarse a la nomenclatura de la entidad. La **verificación manual del resultado es obligatoria**. La extracción automática es un acelerador, no una fuente.

### Paso C — Verificar la articulación

**Archivo que se crea en el repositorio:** `01_marco/MP04_articulacion.csv` — la matriz que responde la pregunta central del laboratorio:

| Objetivo del PGD | ¿Declara articulación con el PEI? | Objetivo del PEI al que se articula | ¿La articulación es **verificable** en el texto? | ¿Tiene indicador? | ¿Tiene línea base? | ¿Tiene meta anual? | Proyectos asociados |
|---|---|---|---|---|---|---|---|
| OGD 1 | Sí / No | OEI 03 | Sí / No / Declarada sin sustento | | | | |

**Análisis de calidad de la articulación.**

```python
# 01_marco/MP05_calidad.py
import pandas as pd
a = pd.read_csv("MP04_articulacion.csv")

n = len(a)
print(f"Objetivos del PGD analizados            : {n}")
print(f"Declaran articulación con el PEI        : {(a.iloc[:,1]=='Sí').sum()} ({(a.iloc[:,1]=='Sí').mean():.0%})")
print(f"Articulación VERIFICABLE en el texto    : {(a.iloc[:,3]=='Sí').sum()} ({(a.iloc[:,3]=='Sí').mean():.0%})")
print(f"Con indicador                           : {(a.iloc[:,4]=='Sí').sum()}")
print(f"Con línea base                          : {(a.iloc[:,5]=='Sí').sum()}")
print(f"Con meta anual                          : {(a.iloc[:,6]=='Sí').sum()}")
print(f"Con proyectos asociados                 : {a.iloc[:,7].notna().sum()}")

completos = a[(a.iloc[:,3]=='Sí') & (a.iloc[:,4]=='Sí') & (a.iloc[:,5]=='Sí') & (a.iloc[:,6]=='Sí')]
print(f"\nObjetivos COMPLETOS (articulados, con indicador, línea base y meta): "
      f"{len(completos)} de {n} ({len(completos)/n:.0%})")
print("\nInterpretación: el porcentaje de objetivos completos es el mejor predictor")
print("de que el plan pueda evaluarse al final del periodo.")
```

**Evaluación contra la estructura de los Lineamientos**, archivo `01_marco/MP06_estructura_lineamientos.csv` del repositorio del equipo:

| Componente exigido por los Lineamientos | ¿Presente en el PGD analizado? | Sección y página | Calidad (completo / parcial / declarativo) | Observación |
|---|---|---|---|---|
| 1. Introducción y marco normativo | | | | |
| 2. Situación actual: análisis interno y externo | | | | |
| 3. Alineamiento estratégico con el PEI y las políticas nacionales | | | | |
| 4. Objetivos de gobierno digital | | | | |
| 5. Portafolio de proyectos | | | | |
| 6. Gestión de riesgos | | | | |
| 7. Cronograma e implementación | | | | |
| 8. Supervisión y evaluación | | | | |
| 9. Anexos | | | | |
| **Adicional:** ¿se identifica al Líder de Gobierno Digital? | | | | |
| **Adicional:** ¿se evidencia el Comité de Gobierno Digital? | | | | |
| **Adicional:** ¿el periodo cubre al menos 3 años? | | | | |
| **Adicional:** ¿hay evidencia de actualización anual? | | | | |

### Paso D — Mapa de instrumentos de la organización propia

Se construye en draw.io el mapa aplicable a **la organización objeto de estudio**, distinguiendo si es pública o privada:

**Si es pública.**

```
Política Nacional de Transformación Digital al 2030 (D.S. 085-2023-PCM)
                     │
            PESEM del sector / PDC regional
                     │
        Plan Estratégico Institucional (PEI) ── vigente hasta ____
                     │
        Plan Operativo Institucional (POI) ──── año ____
                     │
  ╔═════════════════════════════════════════════════╗
  ║  PETI / Plan de Gobierno Digital Año 1 – Año 3      ║  ← este trabajo
  ║  Se articula al OEI ___ y a la AEI ___          ║
  ╚═════════════════════════════════════════════════╝
```

**Si es privada.**

```
        Visión y estrategia de negocio ──── documento: ____
                     │
        Plan de negocio / plan comercial ── vigente hasta ____
                     │
        Presupuesto anual ───────────────── año ____
                     │
  ╔═════════════════════════════════════════════════╗
  ║  PETI Año 1 – Año 3                                 ║  ← este trabajo
  ║  Se articula al objetivo de negocio: ____       ║
  ╚═════════════════════════════════════════════════╝
```

**Tabla de instrumentos de la organización**, archivo `01_marco/MP07_instrumentos_organizacion.csv` del repositorio del equipo:

| Instrumento | ¿Existe? | Vigencia | ¿Está aprobado formalmente? | ¿Se evalúa periódicamente? | Objetivo relevante para el PETI | Observación |
|---|---|---|---|---|---|---|

> **Si la organización no tiene ningún instrumento de planeamiento vigente**, ese es el primer hallazgo del diagnóstico y condiciona el PETI. El plan deberá **derivar los objetivos de negocio de las entrevistas con la gerencia** y documentar explícitamente esa limitación metodológica.

### Paso E — Redactar la Sección 1.2 del PETI

**Archivo que se crea en el repositorio:** `01_marco/1.2_marco_planeamiento.md`:

```markdown
## 1.2 Marco de planeamiento y articulación de instrumentos

### 1.2.1 Instrumentos de planeamiento de la organización
Tabla de instrumentos existentes, su vigencia y su estado de aprobación.

### 1.2.2 Mapa de articulación
Diagrama del mapa de instrumentos, con la posición de este PETI.

### 1.2.3 Objetivo superior de articulación
Objetivo institucional o de negocio al que se articula este plan, citado textualmente
con su fuente, y justificación de la elección.

### 1.2.4 Enfoque estratégico de la organización
Declaración de enfoque estratégico, sustentada en el contraste «dice, hace, financia»
de la dinámica de aula, incluida la cláusula de lo que este plan NO abordará.

### 1.2.5 Marco normativo de planeamiento aplicable
Para entidades públicas: D. Leg. 1412, D. S. 029-2021-PCM, RSGD 005-2018-PCM/SEGDI,
RM 119-2018-PCM, D. S. 085-2023-PCM y la guía del CEPLAN.
Para organizaciones privadas: marcos de referencia adoptados voluntariamente.

### 1.2.6 Referencia metodológica · análisis comparado
Síntesis de lo aprendido del análisis del PEI y PGD de <entidad analizada>: qué se
replica en este plan y qué defecto observado se evita deliberadamente.
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Tomar tres objetivos del PGD al azar y rehacer el rastreo a mano, para comprobar que la matriz no inventó enlaces.
2. Verificar que todo objetivo marcado como completo tiene de verdad indicador, línea base y meta.
3. Comprobar que la sección 1.2 cita el objetivo superior de articulación con su código y su texto literal.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S03: marco de planeamiento, articulacion de instrumentos y seccion 1.2 del PETI"
git tag -a v0.3 -m "PETI v0.3 — marco de planeamiento"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `01_marco/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S03/` | URL del archivo |
> | Salida de comandos | `evidencias/S03/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-03` sobre el commit entregado:
>
> ```bash
> git tag -a taller-03 -m "Taller 03 · SI886"
> git push origin taller-03
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-03`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v0.3`): `taller-03` marca el commit que se entrega a calificar y `v0.3` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **La articulación verificada** | Se distingue lo declarado de lo verificable, con el porcentaje calculado | Matriz de articulación |
| **El objetivo superior de articulación** | Identificado y citado textualmente, con su código | Sección 1.2.3 |
| **La declaración de enfoque** | Con la cláusula de lo que el plan no abordará | Sección 1.2.4 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | PEI y PGD localizados, con su resolución de aprobación y el veredicto de vigencia y de suficiencia | `MP01_documentos.csv` |
| 2 | Estructura de ambos documentos extraída y **verificada manualmente** | `MP02_estructura_*.csv` |
| 3 | Objetivos del PEI y del PGD identificados con su código y texto | `MP03_objetivos_*.csv` |
| 4 | Matriz de articulación completa, con la distinción entre articulación **declarada** y **verificable** | `MP04_articulacion.csv` |
| 5 | Porcentaje de **objetivos completos** (articulados, con indicador, línea base y meta) calculado | Salida de `MP05_calidad.py` |
| 6 | Evaluación del PGD contra los 9 componentes de los Lineamientos más los 4 adicionales | `MP06_estructura_lineamientos.csv` |
| 7 | Mapa de instrumentos de la organización propia, en diagrama | `graficos/mapa_instrumentos.png` |
| 8 | Tabla de instrumentos de la organización, con su estado de aprobación y evaluación | `MP07_instrumentos_organizacion.csv` |
| 9 | **Objetivo superior de articulación identificado y citado textualmente** | Sección 1.2.3 |
| 10 | Declaración de enfoque estratégico con la cláusula de exclusión | Sección 1.2.4 |
| 11 | Sección 1.2 redactada, incluida la lección del análisis comparado | `1.2_marco_planeamiento.md` |
| 12 | Etiqueta `v0.3` en Git | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **La articulación verificada** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El objetivo superior de articulación** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La declaración de enfoque** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. La articulación entre planes se declara con frecuencia y se verifica pocas veces; medir el porcentaje de objetivos con articulación verificable, indicador, línea base y meta expone la calidad real de un plan mucho mejor que su extensión.
2. Un objetivo de TI sin ancla en un objetivo institucional o de negocio compite por presupuesto sin argumento, y es el primero que se recorta cuando los recursos escasean.
3. El enfoque estratégico real de una organización se revela en lo que financia, no en lo que declara; construir el PETI sobre el enfoque declarado cuando el financiado es otro produce un plan que la organización no ejecutará.

## 5. Referencias Bibliográficas

- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI — *Lineamientos para la formulación del Plan de Gobierno Digital*, Anexo I. https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Resolución Ministerial 119-2018-PCM — Comité de Gobierno Digital y Líder de Gobierno Digital.
- Decreto Legislativo 1412, Ley de Gobierno Digital. https://www.gob.pe/institucion/pcm/colecciones/147-normativa-sobre-gobierno-digital
- Decreto Supremo 029-2021-PCM, Reglamento de la Ley de Gobierno Digital. https://www.gob.pe/13326-reglamento-de-la-ley-de-gobierno-digital
- Decreto Supremo 085-2023-PCM, Política Nacional de Transformación Digital al 2030. https://busquedas.elperuano.pe/dispositivo/NL/2200457-5
- CEPLAN. *Guía para el Planeamiento Institucional*. https://www.gob.pe/ceplan
- Rodríguez Bermúdez, J. R. (2015). *Planificación y dirección estratégica de sistemas de información*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875
- González Millán, J. (2020). *Manual práctico de planeación estratégica*. Ediciones Díaz de Santos. https://elibro.net/es/lc/bibliotecaupt/titulos/129291
- Treacy, M. y Wiersema, F. (1995). *The Discipline of Market Leaders*. Addison-Wesley.
- MINTIC Colombia. *Guía para la construcción del PETI*. https://www.mintic.gov.co/arquitecturati/630/w3-propertyvalue-8114.html

## 6. Anexos

- `anexo_A_matriz_articulacion.xlsx`
- `anexo_B_evaluacion_lineamientos.xlsx`
- `anexo_C_mapa_instrumentos.png`
- `anexo_D_seccion_1_2.pdf`
- `anexo_E_documentos_analizados.txt` — URL, resolución y fecha de descarga

---

---

[Semana 03](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
