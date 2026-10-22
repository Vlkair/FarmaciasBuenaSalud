[Semana 17](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 17

## Matriz de comunicaciones, reportes de avance y tablero de supervisión

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S17-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 17» |
| **Cuándo vence** | Según lo programado en el aula virtual. El plazo se cuenta desde la sesión de laboratorio de la semana, se desarrolle el taller dentro de ella o fuera de ella |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Definir la **gobernanza de la ejecución**. Responsable del plan, órgano de seguimiento y su periodicidad.
- Construir la **matriz de comunicaciones** del plan, diferenciada por audiencia.
- Diseñar el **formato de reporte de avance** trimestral y su procedimiento de solicitud.
- Construir el **tablero de supervisión** en Metabase sobre los indicadores de la sección 6.2.
- Definir el **procedimiento de evaluación anual** y de actualización del plan.
- Diseñar el **plan de gestión del cambio** derivado del diagnóstico de cultura.
- Redactar la **Sección 10** y cerrar el PETI (Plan Estratégico de Tecnologías de Información) en su versión definitiva.

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **pandas** + **SQLAlchemy** | Interpola la trayectoria anual de cada indicador y carga el modelo del tablero en PostgreSQL | Salida de `IM05_tablero.py` |
| **Metabase** (Docker) | Construye los siete tableros de supervisión del plan | Capturas de los tableros |
| **Pandoc** y **SHA-256** | Genera el PETI final en PDF y registra su hash | `PETI_FINAL.pdf`, `HASH_PETI_FINAL.txt` |
| **CSV** en LibreOffice Calc | Estructura la matriz RACI, la de comunicaciones y el plan de gestión del cambio | `IM02`, `IM03`, `IM06` |
| **Git** con etiquetas | Cierra el repositorio con `v1.1` y `entrega-final` | `git tag` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Esta semana no trae documentos del caso ni programas: todo el código está en esta guía. El [README](RECURSOS-TALLER/README.md) lo explica |
| PETI v1.0 completo | Secciones Sección 0 a Sección 9 |
| **Metabase** y **PostgreSQL** (Docker) | Tablero de supervisión |
| **Python 3.11+** con `pandas`, `sqlalchemy` | Carga de indicadores |
| **RSGD 005-2018-PCM/SEGDI**, Anexo I | Supervisión y evaluación del PGD |
| Secciones Sección 2.4 y Sección 8 del PETI | Cultura y riesgos, para el plan de cambio |
| **LibreOffice Calc** | Matrices y formatos |

### 1.3. Seguridad

1. El tablero de supervisión contiene indicadores de desempeño de la organización. **Confidencial**. Se despliega en local y con datos agregados.
2. El tablero **no debe contener datos personales**; los indicadores de uso se agregan por área, nunca por persona.
3. La matriz de comunicaciones define quién recibe qué. La información sobre riesgos y sobre proyectos descartados tiene destinatarios acotados.
4. Al entregar el tablero a la organización se documentan las credenciales de acceso y se le transfiere su administración.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Esta semana no se usan documentos del caso ni programas externos: todo el código está en esta guía y el insumo es el PETI v1.0 del equipo.
>
> **Las tablas de ejemplo de esta guía**, y los datos que traen los programas, están resueltas sobre Distribuidora Andina del Sur S.A.C., el caso de respaldo del curso descrito en [`ANEXO-CASO-SIMULADO.md`](../ANEXO-CASO-SIMULADO.md). Muestran el formato y el nivel de detalle que se espera. Las cifras de su informe salen de su organización, no de estas tablas.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `10_implementacion/IM01_gobernanza.md`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Gobernanza de la ejecución

**Archivo que se crea en el repositorio:** `10_implementacion/IM01_gobernanza.md`:

| Elemento | Definición |
|---|---|
| **Responsable del plan** | Cargo designado por el acto de aprobación, con autoridad para convocar y solicitar información |
| **Órgano de seguimiento** | Comité de TI o de Gobierno Digital — composición, periodicidad (mínimo trimestral), quórum y facultades |
| **Responsables por objetivo** | Un cargo por cada objetivo de la sección 6.2 |
| **Responsables por proyecto** | Un cargo por cada proyecto de la sección 7.1 |
| **Hitos de decisión** | Al cierre de cada ola continuar, ajustar o detener |
| **Facultad de replanificación** | Quién puede modificar la hoja de ruta y con qué formalidad |
| **Regla de admisión de nuevos proyectos** | La de la sección 7.1. Cinco fuentes admisibles, caso de negocio y aprobación del comité |

**Matriz RACI de la ejecución**, archivo `10_implementacion/IM02_raci.csv` del repositorio del equipo:

| Actividad | Gerencia General | Comité de TI | Responsable del plan | Jefatura de TI | Áreas usuarias |
|---|---|---|---|---|---|
| Aprobar el plan y su presupuesto | **A** | C | R | C | I |
| Ejecutar los proyectos | I | I | **A** | R | R |
| Reportar el avance trimestral | I | **A** | R | C | C |
| Decidir en los hitos de ola | **A** | R | C | C | I |
| Admitir nuevos proyectos | I | **A** | R | C | R |
| Aceptar riesgos residuales | **A** | C | R | C | I |
| Evaluar el plan anualmente | **A** | R | R | C | C |
| Actualizar el plan | C | **A** | R | C | C |

> **Un solo A por fila.** Si dos actores figuran como responsables de aprobar la misma actividad, nadie responde.

### Paso B — Matriz de comunicaciones

El sílabo la pide expresamente. Se construye diferenciada por audiencia:

**Archivo que se crea en el repositorio:** `10_implementacion/IM03_comunicaciones.csv`:

| id | **Qué se comunica** | **A quién** (cargo) | **Para qué** (decisión que habilita) | **Cuándo** | **Canal** | **Formato** | **Quién comunica** | Confidencialidad |
|---|---|---|---|---|---|---|---|---|
| C-01 | Aprobación del plan, sus objetivos y lo que implica para cada área | Todo el personal | Conocimiento y alineamiento | Al aprobar | Reunión general + intranet | Presentación de 10 min | Gerencia General | Interna |
| C-02 | Avance de objetivos e indicadores frente a la meta | Gerencia General y comité | Continuar, ajustar o detener | Trimestral | Sesión de comité | Tablero + reporte de 2 páginas | Responsable del plan | Confidencial |
| C-03 | **Avance de proyectos.** Hitos, desviaciones y bloqueos | Comité de TI | Desbloquear o replanificar | Mensual | Sesión de comité | Tablero de proyectos | Jefatura de TI | Confidencial |
| C-04 | Qué cambia para su área y cuándo | Gerencia del área afectada | Preparar a su equipo | 60 días antes del proyecto | Reunión bilateral | Ficha de una página | Responsable del plan | Interna |
| C-05 | Qué cambia en su trabajo cotidiano | Usuarios del área afectada | Adoptar el cambio | 30 días antes y al desplegar | Taller presencial | Guía práctica y demostración | Jefatura de TI + área usuaria | Interna |
| C-06 | Ejecución presupuestal y proyección | Gerencia de Administración | Autorizar o reasignar | Trimestral | Informe escrito | Reporte de 1 página | Responsable del plan | Confidencial |
| C-07 | Estado de los riesgos ≥ criterio y de sus señales tempranas | Gerencia General | Activar tratamientos o contingencias | Trimestral, e inmediato al superarse un umbral | Sesión o correo urgente | Tabla de riesgos activos | Responsable del plan | **Restringido** |
| C-08 | Estado del cumplimiento normativo | Gerencia General y asesoría legal | Priorizar la remediación | Trimestral | Informe escrito | Matriz de la sección 4.1 actualizada | Jefatura de TI + Legal | **Restringido** |
| C-09 | Resultados alcanzados y beneficios realizados | Todo el personal y clientes, si aplica | Reconocimiento y sostenimiento del cambio | Al cierre de cada ola | Comunicado + reunión | Antes y después con cifras | Gerencia General | Pública o interna |
| C-10 | Evaluación anual del plan y propuesta de actualización | Órgano de gobierno | Aprobar la actualización | Anual | Sesión formal | Informe de evaluación | Responsable del plan | Confidencial |

> **La fila C-09 es la que más se omite y la que sostiene la ejecución en el año 2.** Comunicar los resultados alcanzados —con cifras del antes y el después— es lo que mantiene el respaldo de la organización cuando el entusiasmo inicial se agota.

### Paso C — Reporte de avance y tablero

**C.1 — Formato del reporte trimestral**, archivo `10_implementacion/IM04_reporte_avance.md` del repositorio del equipo, **máximo dos páginas**:

```markdown
# Reporte de avance del PETI — <Trimestre> <Año>
Responsable del plan: <cargo> · Fecha: <fecha> · Confidencial

## 1. Semáforo general
| Dimensión | Estado | Comentario en una línea |
|---|---|---|
| Objetivos | En plazo / En riesgo / Retrasado | |
| Proyectos | En plazo / En riesgo / Retrasado | |
| Presupuesto | En plazo / En riesgo / Retrasado | |
| Riesgos | Bajo control / En vigilancia / Materializado | |

## 2. Avance de los objetivos frente a la trayectoria prevista
| Objetivo | Indicador | Línea base | Meta del año | Valor actual | % de avance | Estado | ¿Supera el umbral de alerta? |
|---|---|---|---|---|---|---|---|

## 3. Proyectos del trimestre
| Proyecto | Ola | Estado | % avance | Presupuesto ejecutado | Desviación | Bloqueo | Acción solicitada al comité |
|---|---|---|---|---|---|---|---|

## 4. Presupuesto
Ejecutado del trimestre · acumulado del año · proyección de cierre · **OPEX comprometido**.

## 5. Riesgos activos
| id | Riesgo | Valor actual | ¿Señal temprana disparada? | Tratamiento en curso | Acción requerida |
|---|---|---|---|---|---|

## 6. Decisiones que se solicitan al comité
Numeradas, cada una en una oración, con la opción recomendada.

## 7. Cambios al plan desde el último reporte
Proyectos admitidos, postergados o retirados, con su acta de aprobación.
```

> **Regla del reporte.** **Dos páginas.** Un reporte de avance de quince páginas no se lee, y un comité que no lee el reporte decide sin información.

**C.2 — Tablero de supervisión en Metabase.**

```python
# 10_implementacion/IM05_tablero.py
import pandas as pd
from sqlalchemy import create_engine

eng = create_engine("postgresql://peti:peti_lab@127.0.0.1:5433/peti")

# Indicadores con su trayectoria prevista · la base contra la que se mide el avance
ind = pd.read_csv("../06_gobierno_digital/OB03_indicadores.csv")
tray = []
for _, r in ind.iterrows():
    try:
        lb = float(str(r.linea_base).replace("%","").replace("S/","").strip())
        mf = float(str(r.meta_final).replace("%","").replace("S/","").strip())
    except (ValueError, TypeError):
        continue
    for i, año in enumerate(["Año 1", "Año 2", "Año 3"], start=1):
        tray.append({"indicador": r.id, "objetivo": r.get("objetivo"), "año": año,
                     "meta_anual": round(lb + (mf-lb) * i/3, 2),
                     "linea_base": lb, "meta_final": mf,
                     "umbral_alerta": r.get("umbral_alerta")})
pd.DataFrame(tray).to_sql("trayectoria_indicadores", eng, if_exists="replace", index=False)

# Resto del modelo del tablero
pd.read_csv("../07_portafolio/PR05_hoja_ruta.csv").to_sql("hoja_ruta", eng, if_exists="replace", index=False)
pd.read_csv("../07_portafolio/PR06_presupuesto.csv").to_sql("presupuesto", eng, if_exists="replace", index=False)
pd.read_csv("../08_riesgos/RG04_tratamiento.csv").to_sql("riesgos", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/NO03_matriz_cumplimiento.csv").to_sql("cumplimiento", eng, if_exists="replace", index=False)
pd.read_csv("../04_normativa/NO05_calendario.csv").to_sql("calendario_obligaciones", eng, if_exists="replace", index=False)
print("Modelo del tablero cargado. Metabase: http://127.0.0.1:3001")
```

**Los siete tableros mínimos.**

| # | Tablero | Visualización | Pregunta que responde |
|---|---|---|---|
| 1 | Semáforo general | Cuatro números grandes con color | ¿Cómo va el plan hoy? |
| 2 | Avance de objetivos | Barras: actual vs. trayectoria prevista | ¿Qué objetivo está atrasado? |
| 3 | Estado de proyectos | Gantt o barras de progreso | ¿Qué proyecto está bloqueado? |
| 4 | Ejecución presupuestal | Barras acumuladas + línea de OPEX | ¿Estamos dentro del presupuesto? |
| 5 | Riesgos activos | Mapa de calor + tabla de señales disparadas | ¿Qué riesgo se está materializando? |
| 6 | Cumplimiento normativo | Anillo por estado | ¿Cerramos la exposición legal? |
| 7 | **Calendario de obligaciones** | Tabla de próximos vencimientos | ¿Qué vence este trimestre? |

### Paso D — Gestión del cambio y evaluación anual

**D.1 — Plan de gestión del cambio**, derivado del diagnóstico de cultura (Sección 2.4):

**Archivo que se crea en el repositorio:** `10_implementacion/IM06_gestion_cambio.csv`:

| Proyecto | Área afectada | **Quién pierde algo y qué pierde** | Resistencia esperada | Estrategia según el perfil cultural (Sección 2.4) | Actividad concreta | Responsable | Cuándo |
|---|---|---|---|---|---|---|---|
| PR-04 Canal digital | Fuerza de ventas | Pierde la intermediación exclusiva con el cliente | Alta | Cultura de jerarquía + interesado I-03. Formalizar por directiva **y** cocrear con vendedores líderes | Rediseño de comisiones + piloto con 2 vendedores y 20 clientes | Gerencia Comercial | 60 días antes |
| PR-01 Gobierno del dato | Gerencia Comercial | La analista pierde el control exclusivo de la información | Alta | **Redefinir su rol.** Designarla **dueña del dato**, no desplazarla | Nombramiento formal + capacitación en el nuevo rol | Gerencia General | Al iniciar |
| PR-08 Mesa de servicio | Todo el personal | Pierde el acceso directo e informal al técnico | Media | **Cultura de jerarquía.** Directiva de uso obligatorio + demostración de la ventaja | Directiva + taller de 1 hora por área | Jefatura de TI | Al desplegar |
| PR-09 Renovación del ERP | Todas las áreas usuarias | Pierde la familiaridad con la interfaz conocida | Alta | Formación anticipada + acompañamiento en sitio las 2 primeras semanas | Plan de formación por rol + soporte reforzado | Jefatura de TI | 30 días antes |

> **La pregunta que anticipa la resistencia** no es «¿qué gana la organización?» sino **«¿quién pierde algo con este proyecto y qué pierde?»**. Un proyecto sin perdedores identificados suele ser un proyecto mal analizado.

**D.2 — Procedimiento de evaluación anual**, archivo `10_implementacion/IM07_evaluacion_anual.md` del repositorio del equipo — obligación normativa en entidades públicas:

| Paso | Actividad | Responsable | Producto |
|---|---|---|---|
| 1 | Medir todos los indicadores de la sección 6.2 a la fecha de corte | Responsable de cada indicador | Valores del año |
| 2 | Contrastar con la meta anual y explicar cada desviación | Responsable del plan | Análisis de desviación |
| 3 | Evaluar el estado de cada proyecto y su beneficio realizado | Jefatura de TI | Estado del portafolio |
| 4 | **Verificar el beneficio realizado** de los proyectos cerrados frente a su caso de negocio | Responsable del plan | Informe Val IT |
| 5 | **Actualizar el diagnóstico.** Contexto, normativa y madurez | Equipo del plan | Diagnóstico actualizado |
| 6 | Revisar el registro de riesgos y sus señales | Responsable del plan | Registro actualizado |
| 7 | Proponer la actualización del plan. Objetivos, portafolio y presupuesto | Responsable del plan | Propuesta de actualización |
| 8 | **Aprobar la actualización** por el órgano de gobierno | Titular o directorio | Acta o resolución |
| 9 | Comunicar la actualización | Responsable del plan | Comunicado |

**El disparador de revisión extraordinaria.** Cambio del titular o del patrocinador, recorte presupuestal superior al 25 %, cambio normativo que altere las obligaciones, incidente grave, o materialización de un riesgo de valor ≥ 15.

### Paso E — Redactar Sección 10 y cerrar el PETI

```markdown
## 10. Implementación, comunicación y supervisión

### 10.1 Gobernanza de la ejecución
Responsable del plan, órgano de seguimiento, periodicidad, hitos de decisión y
facultad de replanificación. Matriz RACI de la ejecución.

### 10.2 Matriz de comunicaciones
Qué, a quién, para qué, cuándo, por qué canal, en qué formato y quién comunica.
Nivel de confidencialidad por comunicación.

### 10.3 Reporte de avance
Formato de dos páginas, procedimiento de solicitud y calendario de reportes.

### 10.4 Tablero de supervisión
Los siete tableros, su fuente de datos y su responsable de actualización.

### 10.5 Plan de gestión del cambio
Por proyecto: quién pierde qué, resistencia esperada y estrategia derivada del
perfil cultural de la sección 2.4.

### 10.6 Evaluación anual y actualización del plan
Procedimiento de nueve pasos, calendario y disparadores de revisión extraordinaria.

### 10.7 Condiciones de éxito
Las cinco condiciones sin las cuales este plan no se ejecutará, declaradas
explícitamente para que el órgano de gobierno las conozca al aprobarlo.
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Comprobar que el órgano de seguimiento tiene periodicidad fijada y quién lo convoca.
2. Verificar que cada audiencia de la matriz recibe algo distinto y con la frecuencia que le sirve.
3. Comprobar que cada indicador del tablero tiene fuente del dato y responsable de reportarlo.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S17: implementacion, comunicaciones y supervision — seccion 10"
git tag -a v1.1 -m "PETI v1.1 — plan completo, 10 secciones"
pandoc 09_aprobacion/PETI_COMPLETO.md 10_implementacion/10_implementacion.md \
  -o 09_aprobacion/PETI_FINAL.pdf --toc --toc-depth=3 --number-sections \
  -V geometry:margin=2.5cm -V documentclass=report
sha256sum 09_aprobacion/PETI_FINAL.pdf | tee evidencias/HASH_PETI_FINAL.txt
git add . && git commit -m "PETI FINAL: documento completo entregable a la organizacion"
git tag -a entrega-final -m "SI-886  — PETI entregado"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `10_implementacion/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S17/` | URL del archivo |
> | Salida de comandos | `evidencias/S17/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-17` sobre el commit entregado:
>
> ```bash
> git tag -a taller-17 -m "Taller 17 · SI886"
> git push origin taller-17
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-17`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v1.1`): `taller-17` marca el commit que se entrega a calificar y `v1.1` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **La gobernanza** | Responsable del plan, órgano de seguimiento y periodicidad | Sección 10.1 |
| **La matriz de comunicaciones** | Diferenciada por audiencia, con contenido y frecuencia | Matriz |
| **El tablero de supervisión** | Cada indicador con fuente, responsable y umbral de alerta | Tablero |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | **Gobernanza definida.** Responsable, órgano, periodicidad y hitos de decisión | `IM01_gobernanza.md` |
| 2 | Matriz RACI de la ejecución con **un solo A por actividad** | `IM02_raci.csv` |
| 3 | Matriz de comunicaciones con **≥ 10 comunicaciones**, todas con las ocho columnas | `IM03_comunicaciones.csv` |
| 4 | Comunicación de **resultados alcanzados** presente en la matriz | Fila C-09 |
| 5 | Nivel de confidencialidad asignado a cada comunicación | Misma tabla |
| 6 | Formato de reporte de avance de **dos páginas** con sus siete secciones | `IM04_reporte_avance.md` |
| 7 | Tabla de **trayectoria de indicadores** cargada, con la meta anual interpolada | Salida de `IM05_tablero.py` |
| 8 | **Los siete tableros** construidos en Metabase | Capturas |
| 9 | Tablero sin datos personales; indicadores agregados por área | Revisión del modelo |
| 10 | Plan de gestión del cambio con **«quién pierde qué»** por proyecto | `IM06_gestion_cambio.csv` |
| 11 | Estrategia de cambio **derivada del perfil cultural de la sección 2.4** en cada proyecto | Misma tabla |
| 12 | Procedimiento de evaluación anual de nueve pasos, con disparadores extraordinarios | `IM07_evaluacion_anual.md` |
| 13 | Sección 10.7 con las **cinco condiciones de éxito** declaradas | Sección 10.7 |
| 14 | **PETI FINAL** generado en PDF, con su hash, y etiquetas `v1.1` y `entrega-final` | `git tag`, `HASH_PETI_FINAL.txt` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **La gobernanza** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La matriz de comunicaciones** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El tablero de supervisión** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. Un plan aprobado sin gobernanza de la ejecución —responsable con autoridad, órgano de seguimiento y periodicidad— tiene una probabilidad muy alta de no ejecutarse, y ese es el riesgo de mayor valor de casi todos los pre-mortem.
2. La comunicación de resultados alcanzados, con cifras del antes y el después, es lo que sostiene el respaldo organizacional cuando el entusiasmo inicial del año 1 se agota.
3. La pregunta «quién pierde algo con este proyecto» anticipa la resistencia con más precisión que cualquier análisis de beneficios; un proyecto sin perdedores identificados suele estar mal analizado.

## 5. Referencias Bibliográficas

- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — supervisión y evaluación del Plan de Gobierno Digital. https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- Decreto Legislativo 1412 y Decreto Supremo 029-2021-PCM. https://www.gob.pe/13326-reglamento-de-la-ley-de-gobierno-digital
- Decreto Supremo 085-2023-PCM, Política Nacional de Transformación Digital al 2030. https://busquedas.elperuano.pe/dispositivo/NL/2200457-5
- CEPLAN. *Guía para el Planeamiento Institucional* — seguimiento y evaluación. https://www.gob.pe/ceplan
- ISACA. (2018). *COBIT 2019*, **MEA01 Managed Performance and Conformance Monitoring** y **BAI05 Managed Organizational Change**. https://www.isaca.org/resources/cobit
- ISACA. *Val IT Framework* — verificación del beneficio realizado. https://www.isaca.org/resources/frameworks-standards-and-models
- Kotter, J. P. (2012). *Leading Change*. Harvard Business Review Press.
- Kaplan, R. S. y Norton, D. P. (1996). *The Balanced Scorecard*. Harvard Business School Press.
- Project Management Institute. *The Standard for Portfolio Management*. https://www.pmi.org/
- Metabase. *Documentation*. https://www.metabase.com/docs/latest/

## 6. Anexos

- `anexo_A_gobernanza_y_raci.pdf`
- `anexo_B_matriz_comunicaciones.xlsx`
- `anexo_C_formato_reporte_avance.pdf`
- `anexo_D_tablero_supervision.pdf` — capturas de los siete tableros
- `anexo_E_gestion_cambio.xlsx`
- `anexo_F_evaluacion_anual.pdf`
- `anexo_G_PETI_FINAL.pdf` — documento completo entregable

---

---

[Semana 17](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
