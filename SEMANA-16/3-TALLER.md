[Semana 16](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 16

## Integración, control de calidad y expediente de aprobación del PETI

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S16-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 16» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

> **Este taller es evidencia de acreditación.** Sobre el informe y el PETI v1.0 que el grupo sube al aula virtual se mide el atributo **AG-I01 · El Profesional y el Mundo**, criterios **CD1 y CD2**, con la rúbrica institucional de 1 a 4 que está al final de esta página. **No afecta la nota del curso.**

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- **Integrar** las secciones Sección 0 a Sección 8 en un documento único con índice y numeración.
- Redactar la sección **«Impacto de la cartera en el desarrollo sostenible»**, que consolida el análisis de las Semanas 13 y 14.
- Ejecutar la **verificación automatizada de los siete puntos de coherencia**.
- Contrastar la estructura contra los **componentes exigidos por los Lineamientos del PGD**.
- Redactar el **resumen ejecutivo** de tres páginas.
- Elaborar el **expediente de aprobación** con sus seis componentes.
- Redactar la **Sección 9** del PETI.

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **Pandoc** con LaTeX | Integra las secciones en un documento único con índice, numeración y enlaces, y lo exporta a PDF | `PETI.pdf` |
| **Python** (pandas + expresiones regulares) | Ejecuta el verificador automatizado de los siete puntos de coherencia sobre los CSV y el Markdown del plan | Salida de `AP01_coherencia.py` |
| **Git** con etiqueta | Fija la versión final `v1.0` para aprobación | `git tag` |
| **Markdown** estructurado | Redacta el resumen ejecutivo, el proyecto de resolución, el anexo de riesgos y el acta de revisión | `09_aprobacion/` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Solo el programa de verificación de coherencia. Esta semana no hay documentos del caso; el [README](RECURSOS-TALLER/README.md) lo explica |
| Secciones Sección 0 a Sección 8 del PETI | Todo el trabajo del semestre |
| **RSGD 005-2018-PCM/SEGDI**, Anexo I | Estructura exigida del PGD |
| **Pandoc** | Generación del documento único: https://pandoc.org/ |
| **Python 3.11+** con `pandas` | Verificador de coherencia |
| **Git** | Versionado y etiqueta de la versión final |
| Acceso de lectura al repositorio del equipo revisado | Otorgado por el docente |

### 1.3. Seguridad

1. El documento integrado contiene el diagnóstico completo, la matriz de cumplimiento y el registro de riesgos — **Confidencial**, y las secciones Sección 4.1 y Sección 5 en particular, **Restringidas**.
2. La versión que se entrega a la organización se genera con los anexos técnicos separados, para permitir una distribución diferenciada.
3. Al finalizar la sesión se revoca el acceso cruzado.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Esta semana no se usan documentos del caso: el insumo es el PETI que el equipo construyó en las semanas anteriores. La carpeta trae solo el programa de verificación de coherencia.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `09_aprobacion/RESUMEN_EJECUTIVO.md`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Integrar el documento

```bash
cd peti-<organizacion>
cat 00_gestion/00_presentacion.md \
    01_marco/1.1_contexto_tendencias.md 01_marco/1.2_marco_planeamiento.md \
    02_identidad/2.1_mision.md 02_identidad/2.2_vision.md \
    02_identidad/2.3_valores.md 02_identidad/2.4_cultura.md \
    03_diagnostico/3.1_analisis_interno.md 03_diagnostico/3.2_analisis_externo.md \
    03_diagnostico/3.3_pestel.md 03_diagnostico/3.4_foda.md 03_diagnostico/3.5_estrategias.md \
    04_normativa/4.1_marco_normativo.md 04_normativa/4.2_marcos_gestion.md \
    04_normativa/4.3_madurez_procesos.md \
    05_arquitectura/5_arquitectura.md \
    06_gobierno_digital/6.1_situacion_actual.md 06_gobierno_digital/6.2_objetivos.md \
    07_portafolio/7.1_portafolio.md 07_portafolio/7.2_priorizacion.md \
    07_portafolio/7.3_hoja_ruta.md 07_portafolio/7.4_presupuesto.md \
    08_riesgos/8_riesgos.md \
    > 09_aprobacion/PETI_COMPLETO.md

pandoc 09_aprobacion/PETI_COMPLETO.md -o 09_aprobacion/PETI.pdf \
  --toc --toc-depth=3 --number-sections \
  -V geometry:margin=2.5cm -V fontsize=11pt -V documentclass=report \
  -V colorlinks=true -V linkcolor=NavyBlue \
  --metadata title="Plan Estratégico de Tecnologías de Información Año 1 – Año 3" \
  --metadata author="<Organización> · Equipo formulador SI-886 · UPT"
```

### Paso B — Verificar los siete puntos de coherencia

**Programa [`AP01_coherencia.py`](RECURSOS-TALLER/AP01_coherencia.py).** Lee `PETI_COMPLETO.md` y los CSV de las secciones 2, 3, 5, 6, 7 y 8. Produce el informe de los siete puntos de coherencia en pantalla. Se copia a `09_aprobacion/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-16/RECURSOS-TALLER/AP01_coherencia.py 09_aprobacion/
cd 09_aprobacion && python3 AP01_coherencia.py
```

### Paso C — Impacto de la cartera en el desarrollo sostenible

Consolida en **dos a tres páginas** lo que cada proyecto declaró en la Semana 13 y el peso que el impacto tuvo en la priorización de la Semana 14. Va como sección del PETI, antes del resumen ejecutivo.

| Dimensión | Proyectos de la cartera que la afectan | Efecto agregado, con su cifra | Norma o derecho aplicable | ¿Cambió el orden de la cartera? |
|---|---|---|---|---|
| **Sociedad** | | | | |
| **Economía** | | | | |
| **Salud y seguridad** | | | | |
| **Marco legal** | | | | |
| **Medio ambiente** | | | | |

**Y dos párrafos de cierre.**

1. **El alcance del plan.** A cuántas personas llega la cartera dentro de la organización y **cuántas fuera de ella**, incluidas las que no son clientes ni trabajadores. Con cifras.
2. **Lo que el impacto cambió.** Qué proyecto subió o bajó en la priorización por su impacto social o ambiental. **Si no cambió nada, se dice**, y se explica por qué el criterio no movió el orden.

> **Una dimensión que no aplica se declara y se explica.** Dejarla vacía cuenta como no analizada.

### Paso D — Expediente de aprobación

**D.1 — Resumen ejecutivo**, archivo `09_aprobacion/RESUMEN_EJECUTIVO.md` del repositorio del equipo, tres páginas con los siete bloques.

**D.2 — Presentación de aprobación**, 12 diapositivas para 20 minutos, con la carátula de la UPT y los créditos del equipo, pensada para el órgano de gobierno de la organización, no para el aula.

**D.3 — Proyecto de acta o resolución de aprobación**, archivo `09_aprobacion/PROYECTO_APROBACION.md` del repositorio del equipo:

```markdown
# Proyecto de <Resolución del titular / Acta de directorio> de aprobación

**Visto** el Plan Estratégico de Tecnologías de Información Año 1 – Año 3 de <organización>,
formulado por <equipo> con la participación de <áreas>, y la opinión favorable del
<Comité de Gobierno Digital / Comité de TI>;

**Considerando:**
1. Que el marco normativo aplicable obliga a <fundamento de la sección 4.1>;
2. Que el diagnóstico institucional determinó un nivel de madurez de gobierno digital
   de <nivel> y N brechas críticas descritas en la sección 6.1;
3. Que el plan se articula al <objetivo institucional o de negocio> del <instrumento>;
4. Que el plan comprende N objetivos, N proyectos y una inversión de S/ ___ en tres años,
   con un gasto operativo acumulado de S/ ___ al año 3;
5. Que existen N riesgos residuales por encima del criterio de aceptación, cuya asunción
   se documenta en el Anexo I;

**Se resuelve / acuerda:**
- **Artículo 1.** Aprobar el Plan Estratégico de Tecnologías de Información Año 1 – Año 3.
- **Artículo 2.** Designar a <cargo> como responsable de su ejecución, con autoridad para
  convocar al comité y solicitar información a las áreas.
- **Artículo 3.** Encargar al <Comité de TI / de Gobierno Digital> el seguimiento
  trimestral y la **evaluación anual** del plan.
- **Artículo 4.** Aprobar el presupuesto plurianual del Anexo II, sujeto a los hitos de
  decisión de cada ola.
- **Artículo 5.** Dejar constancia de la aceptación de los riesgos residuales del Anexo I.
- **Artículo 6.** Disponer la difusión del plan a todas las áreas y su publicación en
  <portal institucional>.
```

**D.4 — Anexo de aceptación de riesgos residuales**, archivo `09_aprobacion/ANEXO_I_riesgos.md` del repositorio del equipo:

| id | Riesgo | Valor residual | Consecuencia si se materializa | Dueño del riesgo (cargo) | **Firma** | Fecha |
|---|---|---|---|---|---|---|

**D.5 — Acta de la revisión con la organización**, archivo `09_aprobacion/ACTA_REVISION.md` del repositorio del equipo:

| # | Observación | Formulada por (cargo) | Sección | ¿Se acepta? | Justificación si se rechaza | Cambio realizado | Versión |
|---|---|---|---|---|---|---|---|

### Paso E — Redactar Sección 9 y versionar

```markdown
## 9. Aprobación y articulación

### 9.1 Proceso de formulación
Metodología, participantes, fuentes de evidencia y cronograma del proceso.

### 9.2 Verificación de coherencia interna
Resultado de los siete puntos de verificación y de las correcciones realizadas.

### 9.3 Cobertura de los componentes exigidos por los Lineamientos del PGD
Tabla de correspondencia y componentes adicionales de este plan.

### 9.4 Revisión con la organización
Acta de revisión, observaciones aceptadas y rechazadas con su justificación.

### 9.5 Articulación con el instrumento superior
Objetivo institucional o de negocio al que se articula, citado textualmente.

### 9.6 Aceptación de riesgos residuales
Anexo I con los riesgos que la organización asume, y sus firmas.

### 9.7 Acto de aprobación
Proyecto de resolución o acta. Responsable de la ejecución designado.
Vigencia, obligación de actualización y evaluación anual.
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Ejecutar la verificación automatizada y comprobar que los siete puntos salen en verde.
2. Verificar que ningún objetivo del plan queda sin proyecto y ningún proyecto sin objetivo.
3. Comprobar que las cifras del resumen ejecutivo coinciden con las de las secciones que resume.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S16: PETI integrado, coherencia verificada y expediente de aprobacion — seccion 9"
git tag -a v1.0 -m "PETI v1.0 — version final para aprobacion"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `09_aprobacion/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S16/` | URL del archivo |
> | Salida de comandos | `evidencias/S16/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-16` sobre el commit entregado:
>
> ```bash
> git tag -a taller-16 -m "Taller 16 · SI886"
> git push origin taller-16
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-16`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v1.0`): `taller-16` marca el commit que se entrega a calificar y `v1.0` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El documento integrado** | Único, con índice, numeración y las secciones enlazadas | PETI completo |
| **Los siete puntos de coherencia** | Todos verificados, sin excepciones abiertas | Salida de la verificación |
| **El expediente de aprobación** | Con el resumen ejecutivo y el acta de presentación | Expediente |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | Documento único con las secciones Sección 0 a Sección 9, índice y numeración | `PETI.pdf` |
| 2 | Verificador de coherencia ejecutado con **cero no conformidades** | Salida de `AP01_coherencia.py` |
| 3 | **Cero métricas de la visión sin objetivo** que las mida | Punto [1] |
| 4 | **Cero objetivos sin proyecto** asociado | Punto [4] |
| 5 | **Cero proyectos en la hoja de ruta sin ficha** en el portafolio | Punto [5] |
| 6 | **Los 8 componentes** exigidos por los Lineamientos del PGD cubiertos | Punto [PGD] |
| 7 | Resumen ejecutivo de **tres páginas exactas** con los siete bloques | `RESUMEN_EJECUTIVO.md` |
| 8 | Acta de revisión con observaciones **aceptadas y rechazadas con justificación** | `ACTA_REVISION.md` |
| 9 | Proyecto de resolución o acta de aprobación redactado, con los 6 artículos | `PROYECTO_APROBACION.md` |
| 10 | Anexo I de aceptación de riesgos residuales, con espacios de firma | `ANEXO_I_riesgos.md` |
| 11 | Presentación de aprobación de 12 diapositivas | Archivo `.pptx` |
| 12 | Sección 9 redactada · etiqueta **`v1.0`** en Git | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El documento integrado** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **Los siete puntos de coherencia** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El expediente de aprobación** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

### Rúbrica institucional AG-I01 · escala 1 a 4

Se aplica sobre el informe y el PETI v1.0 que el grupo sube al aula virtual, **sin trabajo adicional**. No afecta la nota del curso.

| Criterio | 1 · Inicio | 2 · En proceso | 3 · Logrado | 4 · Destacado |
|---|---|---|---|---|
| **CD1** · Alcance local y global de las TIC en la sociedad y las organizaciones | No identifica el alcance | Lo identifica de forma parcial o imprecisa | **Explica el alcance dentro y fuera de la organización con cifras, incluidas las personas que no son clientes ni trabajadores** | Además lo relaciona con el marco legal aplicable y con las decisiones de la cartera |
| **CD2** · Impacto de las soluciones en el desarrollo sostenible | No analiza el impacto | Analiza solo una o dos dimensiones, casi siempre la económica | **Cubre las cinco dimensiones con cifras, declara y explica la que no aplica, y nombra la norma con su artículo** | Además el impacto **cambió el orden de la cartera**, y se puede señalar qué proyecto subió o bajó por él |

> **Nivel de logro esperado.** Que al menos el **65 % de los estudiantes** alcance nivel 3 o superior.

## 4. Conclusiones

1. Las secciones de un plan construido durante meses pueden ser correctas por separado y contradictorias entre sí; la verificación automatizada de coherencia detecta en segundos lo que una lectura completa tarda horas en encontrar.
2. El resumen ejecutivo de tres páginas es el único componente que el órgano de gobierno leerá completo. Su lenguaje y su extensión determinan si el plan produce decisiones o queda archivado.
3. La aprobación no es un trámite. Es el acto que designa responsable, asigna recursos y deja constancia de los riesgos que la organización asume conscientemente. Un plan sin ese acto no obliga a nadie.

## 5. Referencias Bibliográficas

- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — Lineamientos para la formulación del Plan de Gobierno Digital. https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Resolución Ministerial 119-2018-PCM — Comité de Gobierno Digital y Líder de Gobierno Digital.
- Decreto Legislativo 1412 y Decreto Supremo 029-2021-PCM. https://www.gob.pe/13326-reglamento-de-la-ley-de-gobierno-digital
- CEPLAN. *Guía para el Planeamiento Institucional*. https://www.gob.pe/ceplan
- ISACA. (2018). *COBIT 2019*, **APO02 Managed Strategy** y **EDM01 Ensured Governance Framework Setting and Maintenance**. https://www.isaca.org/resources/cobit
- ISO/IEC 38500:2024. *Governance of IT for the organization*. https://www.iso.org/standard/81684.html
- Rodríguez Bermúdez, J. R. (2015). *Planificación y dirección estratégica de sistemas de información*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875
- González Millán, J. (2020). *Manual práctico de planeación estratégica*. Ediciones Díaz de Santos. https://elibro.net/es/lc/bibliotecaupt/titulos/129291
- MINTIC Colombia. *Guía para la construcción del PETI*. https://www.mintic.gov.co/arquitecturati/630/w3-propertyvalue-8114.html

## 6. Anexos

- `anexo_A_PETI_v1.0.pdf` — documento completo
- `anexo_B_resumen_ejecutivo.pdf`
- `anexo_C_verificacion_coherencia.pdf`
- `anexo_D_acta_revision.pdf`
- `anexo_E_proyecto_aprobacion.pdf` y `anexo_F_anexo_I_riesgos.pdf`

---

---

[Semana 16](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
