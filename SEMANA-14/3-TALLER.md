[Semana 14](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 14

## Priorización multicriterio, hoja de ruta y presupuesto plurianual

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S14-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 14» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Diseñar el **modelo de priorización multicriterio** con pesos derivados del diagnóstico, **incluido el criterio de impacto social y ambiental**.
- **Separar los proyectos no negociables** del modelo y ubicarlos por su plazo.
- Calcular el **puntaje de cada proyecto** y construir la matriz esfuerzo-impacto.
- Determinar explícitamente los proyectos que **no se harán**.
- Construir la **hoja de ruta** en olas, respetando dependencias, plazos y capacidad simultánea.
- Elaborar el **presupuesto plurianual** con CAPEX, OPEX y la **curva de OPEX acumulado**.
- Redactar las secciones **Sección 7.2**, **Sección 7.3** y **Sección 7.4** del PETI (Plan Estratégico de Tecnologías de Información).

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **pandas** | Separa los no negociables, calcula el modelo multicriterio con pesos, el presupuesto plurianual y la curva de OPEX acumulado | `PR01`, `PR03`, `PR06`, `PR_presupuesto.png` |
| **networkx** | Calcula los niveles de dependencia para ordenar las olas sin romper precedencias | Salida de `PR04_hoja_ruta.py` |
| **GanttProject** u **OpenProject** (Docker) | Carga la hoja de ruta con dependencias fin-inicio, hitos de decisión y plazos normativos | Archivo `.gan` y captura |
| **matplotlib** | Grafica la matriz esfuerzo-impacto y la curva de gasto operativo | `PR_esfuerzo_impacto.png`, `PR_presupuesto.png` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Documentos del caso de su organización y programas de este taller, listos para copiar. El [README](RECURSOS-TALLER/README.md) de la carpeta explica cada archivo |
| Secciones Sección 2.4, Sección 4.1.5, Sección 6.2, Sección 7.1 del PETI | Insumos obligatorios |
| Notas de la **Entrevista 3 con la gerencia** | Criterios de priorización y presupuesto disponible. Con el banco de casos, la entrevista es simulada con el docente |
| **GanttProject** | https://www.ganttproject.biz/ |
| **OpenProject** (Docker, alternativa) | https://www.openproject.org/ |
| **Python 3.11+** con `pandas`, `matplotlib`, `networkx` | Priorización y visualización |
| **LibreOffice Calc** | Presupuesto |

### 1.3. Seguridad

1. El presupuesto es información **Confidencial** de la organización.
2. **El criterio «Impacto social y ambiental» es obligatorio en el modelo**, con un peso no menor al 10 %. Se fija antes de calcular, como los demás.
3. Los pesos del modelo se acuerdan con la gerencia **antes** de calcular. Un modelo cuyos pesos se ajustan después de ver el resultado no prioriza. Justifica una decisión ya tomada.
4. Los proyectos descartados y los riesgos asumidos se comunican **explícitamente** a la gerencia. Es la información más incómoda del plan y la que más protege a la organización.
5. Las cifras se presentan con su rango de incertidumbre, nunca como valores cerrados.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Su equipo usa la subcarpeta de su organización, `RECURSOS-TALLER/EMPRESA-<NN>-<nombre>/`. Trae `FICHA.md` (presupuesto de TI del periodo, sección B), `presupuesto_ti.csv`, `inversiones_cerradas.csv` y `expedientes-de-inversion.md`. Con eso se fija la capacidad real de gasto que el presupuesto plurianual del Paso D debe respetar. Los criterios de priorización y el presupuesto disponible que daría la «Entrevista 3 con la gerencia» se acuerdan en la entrevista simulada con el docente, y el acuerdo se registra en `PR02_pesos.md` **antes** de calcular.
>
> **Las tablas de ejemplo de esta guía**, y los datos que traen los programas, están resueltas sobre Distribuidora Andina del Sur S.A.C., el caso de respaldo del curso descrito en [`ANEXO-CASO-SIMULADO.md`](../ANEXO-CASO-SIMULADO.md). Muestran el formato y el nivel de detalle que se espera. Las cifras de su informe salen de su organización, no de estas tablas.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `07_portafolio/PR05_hoja_ruta.csv`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Separar los no negociables y fijar los pesos

**Programa [`PR01_no_negociables.py`](RECURSOS-TALLER/PR01_no_negociables.py).** Lee `PF01_portafolio_candidatos.csv`. Produce `PR01_portafolio_marcado.csv`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-14/RECURSOS-TALLER/PR01_no_negociables.py 07_portafolio/
cd 07_portafolio && python3 PR01_no_negociables.py
```

**Pesos acordados con la gerencia**, archivo `07_portafolio/PR02_pesos.md` del repositorio del equipo — cada peso con su justificación:

| Criterio | Peso | Justificación acordada con la gerencia |
|---|---|---|
| Contribución a los objetivos | 0.25 | La gerencia priorizó los objetivos OD-01 y OD-03 en la Entrevista 3 |
| Beneficio económico | 0.20 | El margen actual (18 %) está bajo el promedio del sector; el retorno pesa |
| Urgencia | 0.15 | Existe un plazo técnico del fabricante y obligaciones vigentes |
| Habilitación | 0.15 | El diagnóstico reveló dependencias fuertes entre proyectos |
| Riesgo de no hacerlo | 0.10 | |
| Facilidad de ejecución | 0.10 | **Equipo de 5 personas.** La capacidad es la restricción real |
| Aceptación organizacional | 0.05 | **Cultura de jerarquía.** El cambio se acepta si está normado |

### Paso B — Calcular la priorización

**Programa [`PR03_priorizacion.py`](RECURSOS-TALLER/PR03_priorizacion.py).** Lee `PF02_tco.csv`; los puntajes por criterio se escriben dentro del programa. Produce `PR03_priorizado.csv` y `graficos/PR_esfuerzo_impacto.png`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-14/RECURSOS-TALLER/PR03_priorizacion.py 07_portafolio/
cd 07_portafolio && python3 PR03_priorizacion.py
```

### Paso C — Construir la hoja de ruta

**Programa [`PR04_hoja_ruta.py`](RECURSOS-TALLER/PR04_hoja_ruta.py).** Lee `PR03_priorizado.csv`, `PR01_portafolio_marcado.csv` y `PF02_tco.csv`. Produce los niveles de dependencia y la propuesta de olas en pantalla; la hoja de ruta se registra a mano en `PR05_hoja_ruta.csv`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-14/RECURSOS-TALLER/PR04_hoja_ruta.py 07_portafolio/
cd 07_portafolio && python3 PR04_hoja_ruta.py
```

**Cronograma en GanttProject.** Se carga la hoja de ruta con un grupo por ola, una tarea por proyecto con su duración en meses, las **dependencias como enlaces fin-inicio**, hitos de decisión al cierre de cada ola y los plazos normativos como hitos rojos.

**Archivo que se crea en el repositorio:** `07_portafolio/PR05_hoja_ruta.csv`:

| Proyecto | Ola | Año | Semestre | Inicio | Fin | Duración (meses) | Depende de | Hito de decisión | Área usuaria afectada |
|---|---|---|---|---|---|---|---|---|---|

### Paso D — Presupuesto plurianual y curva de OPEX

**Programa [`PR06_presupuesto.py`](RECURSOS-TALLER/PR06_presupuesto.py).** Lee `PF02_tco.csv` y `PR05_hoja_ruta.csv`. Produce `PR06_presupuesto.csv` y `graficos/PR_presupuesto.png`. Se copia a `07_portafolio/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-14/RECURSOS-TALLER/PR06_presupuesto.py 07_portafolio/
cd 07_portafolio && python3 PR06_presupuesto.py
```

### Paso E — Declarar lo que no se hará y redactar

**Archivo que se crea en el repositorio:** `07_portafolio/PR07_no_se_hara.csv`:

| Proyecto | Puntaje | Cuadrante | **Objetivo que queda sin cumplir** | **Riesgo que la organización asume** | Responsable de aceptar el riesgo | Fecha de revisión |
|---|---|---|---|---|---|---|

```markdown
## 7.2 Priorización del portafolio
### 7.2.1 Proyectos no negociables y su plazo
### 7.2.2 Modelo multicriterio · criterios, pesos y su justificación acordada
### 7.2.3 Resultados de la priorización
### 7.2.4 Matriz esfuerzo-impacto
### 7.2.5 **Proyectos que NO se ejecutarán** y el riesgo que la organización asume

## 7.3 Hoja de ruta
### 7.3.1 Restricciones · dependencias, plazos, capacidad y absorción del cambio
### 7.3.2 Olas de implantación y su fundamento
### 7.3.3 Cronograma plurianual con hitos de decisión
### 7.3.4 Verificación · dependencias respetadas y capacidad no excedida

## 7.4 Presupuesto
### 7.4.1 Estructura · CAPEX, OPEX, gestión del cambio y contingencia
### 7.4.2 Presupuesto por año
### 7.4.3 **Curva de gasto operativo acumulado** y su interpretación
### 7.4.4 Supuestos y rangos de incertidumbre
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Comprobar que los pesos suman uno y que cada peso tiene su justificación en el diagnóstico.
2. Verificar que ningún proyecto está programado antes que aquel del que depende.
3. Comprobar que el presupuesto por año cuadra con la capacidad real de gasto de la organización.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S14: priorizacion, hoja de ruta y presupuesto — secciones 7.2 a 7.4"
git tag -a v0.14 -m "PETI v0.14 — plan ejecutable"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `07_portafolio/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S14/` | URL del archivo |
> | Salida de comandos | `evidencias/S14/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-14` sobre el commit entregado:
>
> ```bash
> git tag -a taller-14 -m "Taller 14 · SI886"
> git push origin taller-14
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-14`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v0.14`): `taller-14` marca el commit que se entrega a calificar y `v0.14` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El modelo de priorización** | Pesos derivados del diagnóstico, con los no negociables separados | Modelo multicriterio |
| **La hoja de ruta** | Por semestre, respetando las dependencias entre proyectos | Sección 7.3 |
| **El presupuesto plurianual** | Inversión y gasto operativo por año, cuadrados | Sección 7.4 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | **Proyectos no negociables separados** del modelo, con su norma y plazo | `PR01_portafolio_marcado.csv` |
| 2 | Pesos del modelo con **justificación acordada con la gerencia**, sumando 1 | `PR02_pesos.md` |
| 3 | Priorización calculada para todos los proyectos que compiten | `PR03_priorizado.csv` |
| 4 | Matriz esfuerzo-impacto con los cuatro cuadrantes poblados | `PR_esfuerzo_impacto.png` |
| 5 | **Proyectos del cuadrante ④ identificados** como candidatos a no ejecutar | Salida de `PR03_priorizacion.py` |
| 6 | Niveles de dependencia calculados; **cero dependencias rotas** en la hoja de ruta | Salida de `PR04_hoja_ruta.py` |
| 7 | Hoja de ruta en **tres olas** con su fundamento | `PR05_hoja_ruta.csv` |
| 8 | **Capacidad simultánea respetada** en todos los trimestres | Verificación del script |
| 9 | Cronograma en GanttProject con dependencias, hitos de decisión y plazos normativos | Archivo `.gan` y captura |
| 10 | Presupuesto plurianual con CAPEX, OPEX, gestión del cambio y contingencia | `PR06_presupuesto.csv` |
| 11 | **Curva de OPEX acumulado** graficada e interpretada | `PR_presupuesto.png` |
| 12 | Tabla de **lo que no se hará** con el riesgo asumido y su responsable de aceptación | `PR07_no_se_hara.csv` |
| 13 | Secciones Sección 7.2 a Sección 7.4 redactadas · etiqueta `v0.14` | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El modelo de priorización** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La hoja de ruta** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El presupuesto plurianual** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. Priorizar es decidir qué no se hará. Un plan que no declara explícitamente sus proyectos descartados y el riesgo que ello implica no ha priorizado, solo ha ordenado por preferencia.
2. La secuencia de la hoja de ruta la determinan las dependencias y la capacidad de absorción del cambio, no el puntaje; ejecutar los proyectos de mayor valor antes que sus habilitadores produce entregables que no funcionan.
3. El gasto operativo acumulado crece con cada proyecto entregado y nunca baja; mostrar esa curva es lo que permite a la gerencia aprobar el plan sabiendo qué compromiso asume, y no descubrirlo en el tercer año.

## 5. Referencias Bibliográficas

- Project Management Institute. *The Standard for Portfolio Management*. https://www.pmi.org/
- ISO 21500:2021. *Project, programme and portfolio management*. https://www.iso.org/standard/75704.html
- ISACA. (2018). *COBIT 2019*, **APO05 Managed Portfolio** y **APO06 Managed Budget and Costs**. https://www.isaca.org/resources/cobit
- ISACA. *Val IT Framework* — gestión del portafolio de inversiones de TI. https://www.isaca.org/resources/frameworks-standards-and-models
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — cronograma e implementación del PGD (Plan de Gobierno Digital). https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Rodríguez Bermúdez, J. R. (2015). *Planificación y dirección estratégica de sistemas de información*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875
- González Millán, J. (2020). *Manual práctico de planeación estratégica*. Ediciones Díaz de Santos. https://elibro.net/es/lc/bibliotecaupt/titulos/129291
- Kotter, J. P. (2012). *Leading Change*. Harvard Business Review Press. — capacidad de absorción del cambio.
- GanttProject. *User Guide*. https://www.ganttproject.biz/

## 6. Anexos

- `anexo_A_priorizacion.xlsx`
- `anexo_B_esfuerzo_impacto.png`
- `anexo_C_hoja_ruta.gan` y su exportación en PDF
- `anexo_D_presupuesto.xlsx`
- `anexo_E_curva_opex.png`
- `anexo_F_no_se_hara.pdf`

---

---

[Semana 14](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
