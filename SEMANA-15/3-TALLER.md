[Semana 15](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

# Semana 15

## Registro de riesgos del plan y matriz de comunicación

**SI-886 - Planeamiento Estratégico de TI** - Sesión 2 en laboratorio - **Taller grupal** · calificación **procedimental**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S15-TALLER-Grupo<N>.pdf` |
| **Modalidad** | **Taller grupal.** Un informe por equipo, con los códigos de todos los integrantes. El repositorio y el PETI son del equipo |
| **Plantilla obligatoria** | [SI886-PLANTILLA-TALLER.docx](../PLANTILLAS/SI886-PLANTILLA-TALLER.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT, el índice actualizado y las capturas numeradas |
| **Qué va dentro** | Las secciones de la plantilla. La sección **5. Resultados y evidencias** de la plantilla se llena con la lista de comprobación 3.2 de esta guía, una fila por resultado, y **cada resultado necesita la evidencia que lo demuestre**. No se copian de aquí los objetivos, la duración ni los resultados de aprendizaje |
| **Dónde se sube** | Aula virtual, tarea «Taller · Semana 15» |
| **Cuándo vence** | Según lo programado en el aula virtual |

> No se califica un informe entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con resultados declarados sin evidencia.

---

## 1. Información sobre el evento práctico

### 1.1. Objetivos

- Definir el **contexto y los criterios** de riesgo del plan, acordados con la gerencia.
- Identificar riesgos sobre **las nueve categorías**, sin omitir ninguna.
- Evaluar cada riesgo con escalas definidas **antes** de evaluar.
- Determinar el **tratamiento** de cada riesgo y su **riesgo residual**.
- Definir la **señal temprana** y el **umbral de alerta** de cada riesgo de valor > 6.
- Registrar los riesgos en **SimpleRisk** y producir el mapa de calor.
- Construir la **matriz de comunicación del riesgo**.
- Redactar la **Sección 8** del PETI (Plan Estratégico de Tecnologías de Información).

**Tecnología que aplica el estudiante en este taller**

| Tecnología | Qué hace con ella | Dónde queda la evidencia |
|---|---|---|
| **pandas** y **numpy** | Evalúa probabilidad × impacto, calcula el riesgo residual y detecta riesgos sin señal temprana | `RG03_evaluado.csv`, salida de `RG05_residual.py` |
| **matplotlib** | Genera el mapa de calor de riesgos | `RG_mapa_calor.png` |
| **Docker** (SimpleRisk + MariaDB) | Despliega una herramienta de gestión de riesgos, configura escalas y criterio de aceptación y carga los riesgos ≥ 12 | Capturas de SimpleRisk |
| **Git** como evidencia de fecha | Demuestra con el historial que los criterios se fijaron antes de evaluar | `git log` de `RG01_contexto.md` |

### 1.2. Recursos

| Recurso | Detalle |
|---|---|
| **[`RECURSOS-TALLER/`](RECURSOS-TALLER/)** | Documentos del caso de su organización y programas de este taller, listos para copiar. El [README](RECURSOS-TALLER/README.md) de la carpeta explica cada archivo |
| **ISO 31000:2018** | https://www.iso.org/standard/65694.html |
| **ISO/IEC 27005:2022** | Referencia metodológica complementaria |
| **SimpleRisk Community** (Docker) | https://www.simplerisk.com/ |
| **Python 3.11+** con `pandas`, `matplotlib` | Evaluación y mapa de calor |
| Secciones Sección 2.4, Sección 7.2, Sección 7.3 y Sección 7.4 del PETI | Insumos del análisis |
| Resultado del pre-mortem de la dinámica de aula | Insumo de identificación |

### 1.3. Seguridad

1. El registro de riesgos expone las **vulnerabilidades de ejecución** de la organización. Información **Confidencial**.
2. Los riesgos de categoría **patrocinio** y **personal clave** involucran a personas — se redactan por **cargo**, describiendo el riesgo estructural, nunca la conducta de un individuo.
3. Los criterios y escalas se acuerdan con la gerencia **antes** de evaluar. Un criterio ajustado después del resultado no evalúa. Justifica.
4. La aceptación de riesgo residual requiere **firma del dueño del riesgo**; el equipo formulador no puede aceptarlo en su nombre.

---

## 2. Procedimiento o Metodología

> **Recursos de este taller.** Están en [`RECURSOS-TALLER/`](RECURSOS-TALLER/) y su [README](RECURSOS-TALLER/README.md) explica cada archivo. Su equipo usa la subcarpeta de su organización, `RECURSOS-TALLER/EMPRESA-<NN>-<nombre>/`. Trae `politica-de-respaldo.md` (la política declarada, para contrastar con la práctica real), `bia.csv` (el análisis de impacto al negocio: criticidad, RTO, RPO y última prueba por proceso) y `universo-auditable-y-riesgos.md` (los riesgos que la organización ya conoce y no ha tratado). Son fuentes de identificación del Paso B, junto con el pre-mortem de la dinámica. Los documentos declaran lo que la organización dice hacer; el BIA trae incoherencias que no están señaladas.
>
> **Las tablas de ejemplo de esta guía**, y los datos que traen los programas, están resueltas sobre Distribuidora Andina del Sur S.A.C., el caso de respaldo del curso descrito en [`ANEXO-CASO-SIMULADO.md`](../ANEXO-CASO-SIMULADO.md). Muestran el formato y el nivel de detalle que se espera. Las cifras de su informe salen de su organización, no de estas tablas.

> **Cómo leer los pasos.** Cada paso nombra el archivo que el equipo crea, con su ruta dentro del repositorio del PETI, por ejemplo `08_riesgos/RG02_registro.csv`. La carpeta es la de la sección del plan, dentro de la estructura de carpetas del repositorio; el nombre es el que usan los programas y la lista de comprobación. La tabla o la plantilla que sigue a la ruta es **el contenido de ese archivo**. Ese mismo archivo, versionado en GitHub, es la evidencia que se enlaza en el informe.

### Paso A — Contexto y criterios

**Archivo que se crea en el repositorio:** `08_riesgos/RG01_contexto.md`:

| Campo | Contenido |
|---|---|
| **Alcance del análisis** | Riesgos que amenazan la **ejecución del PETI Año 1 – Año 3**. Excluye los riesgos operativos de TI (tratados en el proyecto de gestión de riesgo del portafolio) y los riesgos de negocio (del PEI (Plan Estratégico Institucional)) |
| Horizonte | 3 años |
| Escalas de probabilidad e impacto | Las de la sección 1.3, con su definición operativa |
| **Criterio de aceptación** | ≤ 6 aceptable con documentación · 7–14 requiere tratamiento con plazo · ≥ 15 requiere decisión de la gerencia general antes de aprobar el plan |
| Dueños de riesgo | Por cargo, según la categoría |
| Frecuencia de revisión | Trimestral, y ante cualquier hito de decisión de la hoja de ruta |
| Fecha de acuerdo de los criterios | Anterior a la evaluación — **verificable en el historial de Git** |

### Paso B — Identificar sobre las nueve categorías

**Archivo que se crea en el repositorio:** `08_riesgos/RG02_registro.csv`:

| id | Categoría | **Riesgo (evento + causa + consecuencia)** | Objetivos o proyectos afectados | Origen | P | I | **Valor** | Nivel |
|---|---|---|---|---|---|---|---|---|
| R-01 | Presupuestal | Que el presupuesto de TI se recorte más del 30 % en el segundo año por reasignación a otra prioridad, retrasando la ola 3 completa | OD-01, OD-03 · PR-04, PR-06, PR-07 | Pre-mortem · Sección 7.4 | 4 | 4 | **16** | Crítico |
| R-02 | Patrocinio | Que el gerente que patrocina el plan deje el cargo y su sucesor no lo asuma, dejando el plan sin autoridad | Todos | Pre-mortem | 3 | 5 | **15** | Crítico |
| R-03 | Personal clave | Que el único desarrollador que conoce el portal renuncie antes de completar la gestión del conocimiento (PR-10) | OD-01, OD-06 · PR-04 | Sección 3.1.3 VRIO · Sección 4.3 APO07 | 4 | 4 | **16** | Crítico |
| R-04 | Capacidad de ejecución | Que el área de TI, con 5 personas, no sostenga 3 proyectos simultáneos mientras mantiene la operación | Toda la hoja de ruta | Sección 7.3 | 4 | 3 | **12** | Alto |
| R-05 | Resistencia al cambio | Que la fuerza de ventas no adopte el canal digital porque percibe que reduce su intermediación con el cliente | OD-01 · PR-04 | Sección 2.4 · Sección 3.2.2 interesado I-03 | 4 | 4 | **16** | Crítico |
| R-06 | Resistencia al cambio | Que la analista comercial resista la integración del maestro de clientes por percibir pérdida de control de la información | OD-02 · PR-01 | Sección 3.2.2 interesado I-04 | 4 | 3 | **12** | Alto |
| R-07 | Proveedor | Que el proveedor del ERP no brinde soporte a la migración por estar vencido el contrato de soporte | OD-04 · PR-09 | Sección 3.1.1 · Sección 4.3 APO10 | 4 | 4 | **16** | Crítico |
| R-08 | Técnico | Que la capa de integración no logre exponer los datos del ERP por limitaciones no documentadas de la plataforma | OD-01, OD-02, OD-03 · PR-03 y dependientes | Sección 5.2.3 | 3 | 5 | **15** | Crítico |
| R-09 | Normativo | Que la autoridad de protección de datos emita normativa adicional que amplíe las obligaciones durante la ejecución | OD-05 · PR-02, PR-11 | Sección 4.1 · Sección 3.3 PE-07 | 3 | 3 | **9** | Medio |
| R-10 | De alcance | Que aparezcan pedidos de las áreas sin caso de negocio y consuman la capacidad prevista | Toda la hoja de ruta | Sección 7.1 regla de admisión | 4 | 3 | **12** | Alto |
| R-11 | Ejecución del plan | Que el plan se apruebe y no se ejecute por ausencia de responsable designado y de seguimiento | Todos | Riesgo característico | 4 | 5 | **20** | **Crítico** |
| R-12 | Presupuestal | Que el gasto operativo acumulado del año 3 supere la capacidad presupuestal y obligue a abandonar servicios ya entregados | OD-01, OD-04 | Sección 7.4 curva de OPEX | 3 | 4 | **12** | Alto |

> **Redacción del riesgo.** La estructura es **evento + causa + consecuencia**. «Riesgo de presupuesto» no es un riesgo. Es una categoría. «Que el presupuesto se recorte más del 30 % en el segundo año por reasignación a otra prioridad, retrasando la ola 3 completa» sí lo es.

**Programa [`RG03_evaluacion.py`](RECURSOS-TALLER/RG03_evaluacion.py).** Lee `RG02_registro.csv`, en la misma carpeta. Produce `RG03_evaluado.csv` y `graficos/RG_mapa_calor.png`. Se copia a `08_riesgos/` del repositorio del equipo y **se edita con los datos de su organización**: el programa hace el cálculo, las cifras y su justificación son del equipo.

```bash
# desde la raíz del repositorio del equipo; <curso> es la carpeta del material del curso
cp <curso>/SEMANA-15/RECURSOS-TALLER/RG03_evaluacion.py 08_riesgos/
cd 08_riesgos && python3 RG03_evaluacion.py
```

### Paso C — Tratamiento, señal temprana y riesgo residual

**Archivo que se crea en el repositorio:** `08_riesgos/RG04_tratamiento.csv`:

| id | Valor | **Decisión** | **Acciones concretas de tratamiento** | Responsable (cargo) | Plazo | Costo | P residual | I residual | **Valor residual** | **Señal temprana** | **Umbral de alerta** | ¿Quién acepta el residual? |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R-11 | 20 | **Mitigar** | Designar por resolución un responsable del plan; establecer el comité de TI (PR-13) como órgano de seguimiento; tablero de indicadores con reporte trimestral obligatorio a la gerencia | Gerencia General | Al aprobar el plan | Bajo | 2 | 4 | **8** | Comité sin sesionar | 1 trimestre sin acta | Gerencia General |
| R-01 | 16 | **Mitigar + Asumir con contingencia** | Aprobación plurianual formal del presupuesto por acta; hitos de decisión por ola; escenario reducido preparado que prioriza olas 1 y 2 | Gerencia General y de Administración | Al aprobar el plan | Bajo | 3 | 3 | **9** | Presupuesto de TI no aprobado en la fecha habitual | 30 días de retraso | Gerencia General |
| R-03 | 16 | **Mitigar** | Adelantar PR-10 (gestión del conocimiento) a la ola 1; documentar la arquitectura del portal; formar un segundo responsable; revisar condiciones de retención | Jefatura de TI y RR. HH. | 90 días | Medio | 2 | 4 | **8** | Una sola persona figura en todos los proyectos activos | Cualquier proyecto con factor bus = 1 | Gerencia General |
| R-05 | 16 | **Mitigar** | Incorporar a dos vendedores líderes como cocreadores del canal; rediseñar el esquema de comisiones para que el pedido digital también comisione; piloto con 20 clientes antes del despliegue | Gerencia Comercial | Antes de PR-04 | Medio | 2 | 4 | **8** | Participación en el piloto por debajo del 50 % | 2 semanas con adopción < 10 % | Gerencia Comercial |
| R-07 | 16 | **Transferir + Mitigar** | Renegociar y firmar el contrato de soporte con niveles de servicio y penalidad **antes** de iniciar PR-09; documentar el plan de salida de la plataforma | Gerencia de Administración | Antes de la ola 2 | Medio | 2 | 4 | **8** | Contrato sin firmar a 60 días del inicio de PR-09 | 60 días | Gerencia General |
| R-08 | 15 | **Mitigar** | Ejecutar una **prueba de concepto de integración** antes de comprometer el presupuesto de PR-03; si falla, activar la alternativa de integración por archivo con mayor frecuencia | Jefatura de TI | Antes de PR-03 | Bajo | 2 | 4 | **8** | Prueba de concepto pospuesta | 2 postergaciones | Gerencia General |
| R-02 | 15 | **Mitigar** | Radicar el patrocinio en el **comité de TI**, no en una persona; acta de aprobación firmada por la gerencia general; inducción del plan a todo el comité | Gerencia General | Al aprobar el plan | Bajo | 2 | 4 | **8** | Ausencia del patrocinador en el comité | 2 sesiones consecutivas | Gerencia General |
| R-10 | 12 | **Mitigar** | Aplicar la regla de admisión de sección 7.1. Todo pedido nuevo requiere caso de negocio y aprobación del comité; control de cambios del plan | Comité de TI | Continuo | Bajo | 2 | 3 | **6** | Proyectos activos sin caso de negocio | 1 caso | Comité de TI |
| R-09 | 9 | **Aceptar con vigilancia** | Vigilancia normativa trimestral del portal de la autoridad; margen de adaptación en el diseño de PR-02 y PR-11 | Jefatura de TI + Legal | Continuo | Bajo | 3 | 3 | **9** | Prepublicación de proyecto normativo | Publicación en consulta | Gerencia General |

**Análisis del residual.**

```python
# 08_riesgos/RG05_residual.py
import pandas as pd
t = pd.read_csv("RG04_tratamiento.csv")
t["reduccion"] = t.Valor - t["Valor residual"]
t["reduccion_pct"] = (t.reduccion / t.Valor * 100).round(0)

print(t[["id","Valor","Valor residual","reduccion","reduccion_pct","Decisión"]].to_string(index=False))
print(f"\nValor agregado del plan de tratamiento: {t.reduccion.sum()} puntos "
      f"({t.reduccion.sum()/t.Valor.sum():.0%} de reducción)")

sobre = t[t["Valor residual"] > 6]
print(f"\n=== RIESGOS RESIDUALES POR ENCIMA DEL CRITERIO ({len(sobre)}) ===")
print(sobre[["id","Valor residual","¿Quién acepta el residual?"]].to_string(index=False))
print("→ Cada uno requiere ACEPTACIÓN FORMAL FIRMADA antes de aprobar el plan.")
print("  Un riesgo residual sin firma no está aceptado: está ignorado.")

sin_senal = t[t["Señal temprana"].isna() | (t["Señal temprana"].astype(str).str.strip()=="")]
print(f"\nRiesgos sin señal temprana: {len(sin_senal)} → {list(sin_senal.id)}")
print("→ Sin señal observable no hay seguimiento posible: el riesgo se detecta cuando ya ocurrió.")
```

**Registro en SimpleRisk.**

```bash
docker run -d --name peti_srdb -e MARIADB_ROOT_PASSWORD=peti_sr \
  -e MARIADB_DATABASE=simplerisk mariadb:11
docker run -d --name peti_simplerisk --link peti_srdb:db \
  -p 127.0.0.1:8084:80 simplerisk/simplerisk:latest
```

Se configura la fórmula clásica (probabilidad × impacto), se cargan las escalas con su **definición operativa escrita**, el criterio de aceptación, los dueños de riesgo por cargo, y luego los riesgos de valor ≥ 12 con su plan de tratamiento.

### Paso D — Matriz de comunicación del riesgo

El sílabo lo pide expresamente. *«Comunicar las acciones para tratar el riesgo»*.

**Archivo que se crea en el repositorio:** `08_riesgos/RG06_comunicacion.csv`:

| id del riesgo | **Qué se comunica** | **A quién** (cargo) | **Cuándo / frecuencia** | **Canal** | **Quién comunica** | Formato | Qué decisión habilita |
|---|---|---|---|---|---|---|---|
| R-11 | Estado de ejecución del plan y avance de indicadores | Gerencia General y comité de TI | Trimestral | Sesión de comité | Responsable del plan | Tablero + acta | Continuar, ajustar o detener |
| R-01 | Ejecución presupuestal vs. planificado y proyección del año siguiente | Gerencia General y de Administración | Trimestral, y ante cualquier desviación > 10 % | Informe escrito | Jefatura de TI | Reporte de 1 página | Reasignación o escenario reducido |
| R-03 | Estado del factor bus por proyecto y avance de la gestión del conocimiento | Gerencia General y RR. HH. | Mensual mientras el residual sea > 6 | Correo con tablero | Jefatura de TI | Indicador | Priorizar contratación o formación |
| R-05 | Adopción del canal digital por vendedor y por cliente | Gerencia Comercial y fuerza de ventas | Semanal durante el piloto; mensual después | Reunión de equipo | Gerencia Comercial | Tablero visible | Ajustar incentivos o rediseñar |
| R-07 | Estado de la renegociación contractual | Gerencia General | Quincenal hasta la firma | Correo | Gerencia de Administración | Estado en una línea | Escalar o activar plan de salida |
| R-08 | Resultado de la prueba de concepto de integración | Comité de TI | Al concluir la prueba | Sesión de comité | Jefatura de TI | Informe técnico | Aprobar PR-03 o activar la alternativa |
| **Todos ≥ 15** | Riesgo, tratamiento, residual y responsable de la aceptación | Gerencia General | **Antes de aprobar el plan** | Sesión formal | Responsable del plan | Anexo del PETI con firmas | Aprobar el plan con conocimiento del riesgo |

> **La última fila es la más importante.** La gerencia debe aprobar el plan **conociendo y firmando** los riesgos críticos residuales. Un plan aprobado sin esa conversación transfiere al equipo formulador una responsabilidad que no le corresponde.

### Paso E — Redactar la Sección 8

```markdown
## 8. Gestión de riesgos del plan

### 8.1 Alcance, contexto y criterios
Qué riesgos gestiona esta sección y cuáles no. Escalas con definición operativa,
criterio de aceptación acordado y fecha del acuerdo.

### 8.2 Método
ISO 31000:2018. Fuentes de identificación: pre-mortem, diagnóstico, interesados,
lecciones de planes comparables.

### 8.3 Registro de riesgos
Tabla completa con las nueve categorías. **Categorías sin riesgo identificado y su
justificación.**

### 8.4 Evaluación y mapa de calor
Distribución por nivel. Riesgos ≥ 15 que requieren decisión de la gerencia general.

### 8.5 Tratamiento y riesgo residual
Decisión, acciones, responsable, plazo, costo y residual por riesgo.
Reducción total lograda por el plan de tratamiento.

### 8.6 Señales tempranas y umbrales de alerta
Tabla de señal y umbral por riesgo. **Sin señal observable no hay seguimiento.**

### 8.7 Matriz de comunicación del riesgo
Qué, a quién, cuándo, por qué canal y quién comunica.

### 8.8 Riesgos residuales que requieren aceptación formal
Tabla con el responsable de la aceptación. **Anexo de firmas de la sección 9.**

### 8.9 Seguimiento y revisión
Frecuencia, responsable y disparadores de revisión extraordinaria.
```

### Paso F — Validar y corregir

El resultado no vale por estar hecho, sino por resistir una comprobación. Se ejecutan estas tres y **se corrige lo que falle antes de cerrar la sesión**.

1. Comprobar que las nueve categorías tienen al menos un riesgo, o la declaración de por qué no aplica.
2. Verificar que probabilidad e impacto están justificados con un dato, no elegidos por intuición.
3. Comprobar que todo riesgo de valor alto tiene tratamiento y responsable por cargo.

> Lo que no se pueda corregir hoy se anota en la sección **Problemas y mejoras** de la evidencia, con lo que faltó y por qué. Un resultado parcial documentado con honestidad vale más que uno declarado sin prueba.

### Paso G — Registrar la evidencia y cerrar

Se versiona lo producido, se anota la URL de cada resultado y se responde en dos frases la pregunta de transferencia — **qué riesgo correría una organización real si esto se hiciera mal**.

```bash
git add . && git commit -m "S15: registro de riesgos del plan, tratamiento y comunicacion — seccion 8"
git tag -a v0.15 -m "PETI v0.15 — gestion de riesgos"
```

---

## 3. Resultados

> **Evidencia obligatoria en GitHub.** Todo resultado de este taller se versiona en el repositorio del equipo. El informe **no consigna capturas sueltas**. Consigna la **URL** del artefacto en GitHub. Una captura no permite verificar autoría, fecha ni contenido; un enlace sí.
>
> | Qué se entrega | Dónde vive | Qué se escribe en el informe |
> |---|---|---|
> | Programas y archivos CSV del taller | La carpeta de la sección del PETI que el taller indica (esta semana, `08_riesgos/`), en la rama del taller fusionada a `develop` vía Pull Request | URL del Pull Request |
> | Documentos y matrices | La misma carpeta de la sección, en formato de texto versionable | URL del archivo en la rama |
> | Capturas y videos que el taller exija | `evidencias/S15/` | URL del archivo |
> | Salida de comandos | `evidencias/S15/salidas/*.txt` | URL del archivo |
>
> **Etiqueta del taller.** Al cerrar el taller se crea la etiqueta `taller-15` sobre el commit entregado:
>
> ```bash
> git tag -a taller-15 -m "Taller 15 · SI886"
> git push origin taller-15
> ```
>
> La URL que se consigna en el informe apunta a esa etiqueta:
> `https://github.com/<organizacion>/<repositorio>/tree/taller-15`
>
> Esta etiqueta convive con la de versión del PETI que crea el último paso del procedimiento (`v0.15`): `taller-15` marca el commit que se entrega a calificar y `v0.15` marca el estado del documento. Pueden apuntar al mismo commit.
>
> **El informe es lo que se califica; el repositorio es lo que lo prueba.** Cada resultado de la sección 3 del informe lleva la URL con la que se verifica, y **un resultado sin su URL se califica como no logrado**, por bien redactado que esté. Lo que no se puede abrir no se puede dar por hecho.

### 3.1. Los tres resultados que se califican

Son los que la rúbrica evalúa. El resto de la lista tiene que existir, pero no se califica fila por fila.

| Resultado | Qué demuestra | Dónde está |
|---|---|---|
| **El registro completo** | Las nueve categorías cubiertas, con criterios acordados | Registro de riesgos |
| **La valoración fundamentada** | Probabilidad e impacto justificados con datos | Matriz de riesgo |
| **El tratamiento** | Cada riesgo alto con tratamiento, responsable y señal temprana | `RG04_tratamiento.csv` y sección 8.5 |

### 3.2. Lista de comprobación del taller

Todo esto debe existir al cerrar la sesión.

| # | Resultado esperado | Verificación |
|---|---|---|
| 1 | Contexto y criterios definidos, con **fecha de acuerdo anterior a la evaluación** | `RG01_contexto.md` + historial de Git |
| 2 | Escalas de probabilidad e impacto con **definición operativa escrita** | `RG01_contexto.md` |
| 3 | **Las nueve categorías** evaluadas; las omitidas, justificadas | Salida de `RG03_evaluacion.py` |
| 4 | Registro con **≥ 12 riesgos**, redactados como evento + causa + consecuencia | `RG02_registro.csv` |
| 5 | Cada riesgo trazado a los objetivos y proyectos que afecta | Misma tabla |
| 6 | Mapa de calor generado | `RG_mapa_calor.png` |
| 7 | Riesgos ≥ 15 identificados como **decisión de la gerencia general** | Salida del script |
| 8 | Tratamiento definido para **todos** los riesgos de valor > 6 | `RG04_tratamiento.csv` |
| 9 | **Riesgo residual calculado**, con la reducción lograda | Salida de `RG05_residual.py` |
| 10 | **Señal temprana y umbral de alerta** en cada riesgo > 6; cero riesgos sin señal | Salida del script |
| 11 | Riesgos residuales sobre el criterio, con **responsable de la aceptación identificado** | Salida del script |
| 12 | Registro cargado en SimpleRisk con escalas y criterio configurados | Capturas |
| 13 | Matriz de comunicación con las ocho columnas | `RG06_comunicacion.csv` |
| 14 | Sección 8 redactada · etiqueta `v0.15` | `git tag` |

## Rúbrica procedimental (20 puntos)

Se aplica sobre el informe entregado y la evidencia enlazada en el repositorio. **Cada criterio se califica de forma independiente.**

| Criterio | 4 — Logrado | 2 — En proceso | 0 — Insuficiente |
|---|---|---|---|
| **El criterio de éxito** | Se cumple tal como lo pide el reto de esta sesión | Se cumple con reservas que el equipo declara | No se cumple, o se afirma cumplido sin prueba |
| **El registro completo** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La valoración fundamentada** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **El tratamiento** | Completo y correcto, con la evidencia que lo respalda | Completo con errores menores, o correcto sin toda la evidencia | Incompleto o sin evidencia |
| **La validación** | Las tres comprobaciones ejecutadas, y lo que falló quedó corregido o documentado | Ejecutadas sin corregir lo que falló | No se validó nada |

## 4. Conclusiones

1. El pre-mortem produce riesgos concretos y específicos de la organización, mientras que la pregunta directa «¿qué puede salir mal?» produce categorías genéricas que ningún plan de tratamiento puede atacar.
2. Un riesgo sin señal temprana observable no se gestiona. Se detecta cuando ya ocurrió. La señal y su umbral son lo que convierte el registro en un instrumento de control y no en un inventario.
3. El riesgo residual aceptado sin firma del dueño del riesgo no está aceptado, está ignorado; la conversación de aprobación del plan es el momento en que la gerencia asume conscientemente el riesgo que queda.

## 5. Referencias Bibliográficas

- ISO 31000:2018. *Risk management — Guidelines*. https://www.iso.org/standard/65694.html
- ISO/IEC 27005:2022. *Guidance on managing information security risks*. https://www.iso.org/standard/80585.html
- IEC 31010:2019. *Risk management — Risk assessment techniques*. https://www.iso.org/standard/72140.html
- ISACA. (2018). *COBIT 2019*, **APO12 Managed Risk** y **EDM03 Ensured Risk Optimization**. https://www.isaca.org/resources/cobit
- Project Management Institute. *PMBOK Guide* — gestión de riesgos del proyecto. https://www.pmi.org/
- Klein, G. (2007). Performing a project premortem. *Harvard Business Review*, 85(9), 18–19.
- Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI, Anexo I — gestión de riesgos del PGD (Plan de Gobierno Digital). https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf
- SimpleRisk. *Documentation*. https://www.simplerisk.com/documentation
- Rodríguez Bermúdez, J. R. (2015). *Planificación y dirección estratégica de sistemas de información*. Editorial UOC. https://elibro.net/es/lc/bibliotecaupt/titulos/57875

## 6. Anexos

- `anexo_A_registro_riesgos.xlsx`
- `anexo_B_mapa_calor.png`
- `anexo_C_plan_tratamiento.xlsx`
- `anexo_D_matriz_comunicacion.xlsx`
- `anexo_E_premortem.pdf`
- `anexo_F_aceptacion_residual.pdf` — formato de firmas para la sección 9

---

---

[Semana 15](README.md) · [Teoría](1-TEORIA.md) · [Dinámica de aula](2-DINAMICA.md) · **Taller de laboratorio**

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
