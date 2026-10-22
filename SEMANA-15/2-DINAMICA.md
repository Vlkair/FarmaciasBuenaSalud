[Semana 15](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

# Semana 15

## Pre-mortem con incidente

**SI-886 - Planeamiento Estratégico de TI** - Actividad en aula, **dentro de la sesión de teoría** · calificación **cognitiva**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S15-DINAMICA-Grupo<N>.pdf` |
| **Plantilla obligatoria** | [SI886-PLANTILLA-DINAMICA.docx](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT y los apellidos, nombres y códigos de todos los integrantes |
| **Qué va dentro** | Lo que el grupo resolvió en aula. Las tablas de la sección **Producto** van completas, con los textos redactados, y cada decisión va justificada |
| **Dónde se sube** | Aula virtual, tarea «Dinámica · Semana 15» |
| **Cuándo vence** | Según lo programado en el aula virtual. La tabla se resuelve en aula; el PDF se formatea y se sube después |
| **Exposición** | En la ronda de cierre de **esta misma sesión**. El grupo **lee y explica su resultado** ante el aula, con el documento a la vista. No se usan diapositivas |

> No se califica un trabajo entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con las tablas del producto vacías.

---

## Consigna

> **«Pre-mortem con incidente»**
> Estamos al cierre del horizonte del plan. **El plan fracasó y se abandonó.** Su comité tiene que explicar por qué, y hacerlo ahora, cuando todavía se puede evitar.

| | |
|---|---|
| **Su papel** | **Comité de riesgos** que hace la autopsia del plan |
| **Misión** | Cinco razones del fracaso, escritas en pasado, convertidas en riesgos con su señal temprana |
| **Restricción** | **Prohibido «falta de presupuesto» como causa única.** Es la respuesta de quien no quiere mirar. A mitad de sesión entra un incidente que el comité no había previsto |

El pre-mortem invierte la pregunta. En lugar de «¿qué podría salir mal?», que produce listas genéricas, pregunta **«ya salió mal, ¿qué pasó?»**, que produce nombres, fechas y responsables.

## Producto

**El informe de la autopsia.** > «Estamos en el cierre del horizonte. El Plan Estratégico de TI se abandonó en el año ___. Estas son las cinco razones.»

| # | Qué pasó, en pasado y como hecho | ¿Cuándo empezó a fallar? | La primera señal que nadie atendió |
|---|---|---|---|

**Y los riesgos que se derivan.**

| # | Riesgo, redactado en presente | P | I | Valor | Tratamiento | Responsable | Señal temprana que lo detectaría |
|---|---|---|---|---|---|---|---|

**Y el incidente** — si el comité lo habría detectado con sus señales, y qué señal faltaba.

> **Dónde va.** Este producto se presenta en la **sección 2 de la [plantilla de dinámica](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx)**, «El producto». No se copia la consigna ni la teoría. Solo el resultado y lo que lo sostiene.

## Ejemplo resuelto

*El caso de este ejemplo es distinto del que le toca a tu grupo. Sirve para que veas el nivel de detalle que se espera, no para copiarlo.*

**La organización del ejemplo.** Cooperativa de ahorro y crédito, plan a tres años.

**La autopsia.** «El PETI se abandonó en el año 2.»

| # | Qué pasó | ¿Cuándo empezó a fallar? | La primera señal que nadie atendió |
|---|---|---|---|
| 1 | El gerente que patrocinaba el plan salió y el que entró no lo hizo suyo | Mes 8 | El nuevo gerente no pidió el plan en su primera semana |
| 2 | El comité de TI dejó de reunirse | Mes 5 | Se pasó de mensual a «cuando haya tema» |
| 3 | El único que sabía del core se fue a la competencia | Mes 11 | Pidió licencia sin goce dos veces en el mismo trimestre |
| 4 | Los proyectos siguieron ejecutándose sin medir beneficio | Mes 3 | El primer cierre de proyecto no tuvo acta de beneficio |
| 5 | El presupuesto del año 2 se aprobó sin mirar el plan | Mes 14 | El área de finanzas no convocó a TI a la formulación |

**Dos de los riesgos derivados.**

| # | Riesgo, en presente | P | I | Valor | Tratamiento | Responsable | Señal temprana |
|---|---|---|---|---|---|---|---|
| R-01 | El patrocinio del plan depende de una sola persona | 4 | 5 | 20 | Mitigar · acta de compromiso del Consejo, no del gerente | Presidencia del Consejo | Un cambio de gerencia sin traspaso formal del plan |
| R-03 | El conocimiento del core reside en una persona | 4 | 5 | 20 | Mitigar · documentación y un segundo técnico formado | Jefatura de TI | Una licencia sin goce o una ausencia larga sin reemplazo |

**El incidente que entró a mitad de sesión.** «En el mes 6, la SBS observó a la cooperativa por no tener registro de accesos privilegiados.»

**¿Lo habrían detectado?** **No.** Ninguna de las cinco razones apuntaba al cumplimiento regulatorio. La señal que faltaba era **la fecha de la próxima visita de la SBS en el calendario del comité**. Se agregó como R-06.

**Lo que enseña.** Las cinco razones del equipo eran de personas y de gobierno, que es lo habitual. El riesgo regulatorio no apareció porque no había fallado todavía.

## Reglas

- Las razones se escriben **en pasado**. «Podría faltar compromiso» no es una razón; «la gerencia dejó de asistir al comité en el mes cuatro» sí.
- **«Falta de presupuesto» no puede ser la causa única.** Puede acompañar, no explicar.
- Toda razón necesita **una señal temprana observable**, algo que alguien habría podido ver.
- El responsable se nombra **por cargo**.
- Si el comité reconoce que **no habría detectado** el incidente, eso suma. Fingir que sí, baja la nota.
- La exposición es la ronda de cierre de esta misma sesión. El grupo **lee y explica su resultado**. No se usan diapositivas.

## Rúbrica cognitiva (20 puntos)

| Criterio | 5 | 3 | 1 |
|---|---|---|---|
| **La autopsia** | Cinco razones en pasado, concretas y verosímiles para esta organización | Tres o cuatro concretas | Riesgos genéricos en futuro condicional |
| **La señal temprana** | Cada razón con una señal observable y el momento en que se pudo ver | Señales en la mayoría | Señales que solo se ven cuando ya ocurrió el daño |
| **La conversión a riesgo** | Los cinco con probabilidad, impacto, tratamiento y responsable por cargo | Cuatro completos | Riesgos sin tratamiento o sin responsable |
| **El incidente** | Se evalúa con honestidad si lo habrían detectado y se identifica la señal que faltaba | Se evalúa sin identificar la señal | Se afirma que lo habrían detectado sin sustento |

## Anexo · Material de trabajo

Cada equipo recibe **el plan de su organización en una página**. Los objetivos, la cartera que quedó después de la negociación de la Semana 14, lo que el plan da por sentado y las personas de las que depende. Con eso se hace la autopsia.

**Reparto.** Una ficha por equipo, **la misma organización que le tocó en la Semana 03**. Son las diez de siempre, con los mismos tamaños, presupuestos, objetivos y proyectos.

**A mitad de sesión entra un incidente.** No está en esta ficha. Cuando llegue, el comité responde si sus señales lo habrían detectado y qué señal faltaba.

### Ficha 1 · Agroexportadora de aceituna y orégano · 142 trabajadores · TI 3 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 160 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir 12 % el costo por tonelada procesada · **OE-02** certificar la trazabilidad del lote que exige el comprador europeo.
> **Los cuatro proyectos de mayor puntaje.** Digitalización de la trazabilidad de planta · Reemplazo del servidor de planta y respaldo fuera de la sede · Portal del cliente internacional con seguimiento del pedido · Tablero de costo por tonelada en tiempo real.
> **Lo que el plan da por sentado.** El plan descansa en que el jefe de planta adopte la captura digital, en que el proveedor del ERP integre la balanza y en que la campaña de mayo a agosto no se toque.
> **Las personas y los plazos de los que depende.** El Jefe de Sistemas lleva 6 años y no tiene reemplazo. El proveedor del ERP es una empresa de 12 personas. El comprador europeo revisa cada 12 meses.

### Ficha 2 · Clínica privada de 60 camas · 310 trabajadores · TI 6 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 335 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir 30 % el tiempo de espera en consulta externa · **OE-02** que el 60 % de los actos de atención no exijan papel al paciente.
> **Los cuatro proyectos de mayor puntaje.** Integración de historia clínica y laboratorio · Renovación de los servidores del centro de datos · Revisión de accesos a la historia clínica y bitácora · Aplicación del paciente con resultados y citas.
> **Lo que el plan da por sentado.** El plan descansa en que el proveedor del sistema clínico entregue la interfaz de integración, en que los médicos usen el visor en vez del papel y en que el centro de datos aguante hasta la renovación.
> **Las personas y los plazos de los que depende.** Dos de seis integrantes de TI renunciaron en el año. El único que conoce la integración lleva ocho meses. La versión local del sistema clínico deja de actualizarse en 20 meses.

### Ficha 3 · Municipalidad distrital · 41 800 habitantes · TI 3 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 214 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir de 12 a 5 días el plazo de atención del trámite más demandado · **OE-02** elevar 15 % la recaudación del impuesto predial.
> **Los cuatro proyectos de mayor puntaje.** Pago en línea del impuesto predial · UPS y respaldo fuera de la sede para el trámite documentario · Comité de Gobierno Digital y formulación del PGD · Expediente electrónico de la licencia de funcionamiento.
> **Lo que el plan da por sentado.** El plan descansa en que el Concejo apruebe el Comité de Gobierno Digital, en que la pasarela de pagos del Estado se integre al sistema de rentas y en que el jefe de TI dure más que los tres anteriores.
> **Las personas y los plazos de los que depende.** La partida de proyectos ejecutó el 38 %. El jefe de TI rotó tres veces en cuatro años. Hay elecciones municipales en el segundo año del plan.

### Ficha 4 · Cooperativa de ahorro y crédito · 18 400 socios · TI 7 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 470 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** incrementar 18 % la colocación por socio activo · **OE-02** que el 50 % de las operaciones del socio se hagan por la aplicación móvil.
> **Los cuatro proyectos de mayor puntaje.** Migración del core · Apertura de productos desde la aplicación móvil · Procedimiento y herramienta de reporte de incidentes a la SBS · Modelo de puntaje para crédito de campaña.
> **Lo que el plan da por sentado.** El plan descansa en que la migración del core termine antes de que la versión salga de soporte, en que el Consejo apruebe el gasto en dólares y en que los socios adopten la apertura digital.
> **Las personas y los plazos de los que depende.** El contrato del core está en dólares y vence en 16 meses. Siete personas de TI y ninguna práctica de cambios escrita. La SBS inspecciona en 5 meses.

### Ficha 5 · Empresa de transporte de carga · 96 trabajadores · TI 2 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 141 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir 8 % el costo por tonelada-kilómetro · **OE-02** bajar de 6 % a 2 % las entregas con incidencia.
> **Los cuatro proyectos de mayor puntaje.** Integración de flota con facturación · Aplicación de registro de entrega con firma · Segundo proveedor de guía electrónica y contingencia · Documentación y respaldo del sistema de flota.
> **Lo que el plan da por sentado.** El plan descansa en que la única persona que conoce el sistema de flota se quede, en que el intermediario de guía electrónica siga operando y en que la integración con facturación no rompa la emisión.
> **Las personas y los plazos de los que depende.** Dos personas de TI. El sueldo del perfil subió 18 % en dos años. El contrato del intermediario vence en 7 meses.

### Ficha 6 · Distribuidora mayorista de consumo masivo · 157 trabajadores · TI 4 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 286 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir el quiebre de stock de 5.8 % a 2 % · **OE-02** elevar de 4 % a 30 % el pedido autoatendido por la bodega.
> **Los cuatro proyectos de mayor puntaje.** Reactivación del módulo de almacén · Migración del ERP a la versión en nube · Rediseño del portal de pedidos de la bodega · Ruteo optimizado de la distribución.
> **Lo que el plan da por sentado.** El plan descansa en que el almacén vuelva a usar el módulo del ERP, en que la migración a la nube no cambie los procesos a mitad de camino y en que las bodegas adopten el portal.
> **Las personas y los plazos de los que depende.** El proveedor del ERP deja de dar soporte a la versión local en 15 meses. El portal lo usa el 4 %. El módulo de almacén ya se abandonó una vez.

### Ficha 7 · Instituto de educación superior tecnológica · 2 100 estudiantes · TI 3 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 272 500 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir la deserción del primer ciclo de 31 % a 20 % · **OE-02** que el 100 % de las carreras entregue y califique trabajos por el campus virtual.
> **Los cuatro proyectos de mayor puntaje.** Alerta temprana de deserción · Bitácora de modificaciones de notas y actas · Módulo de entrega y calificación en el campus virtual · Campus virtual utilizable desde el teléfono.
> **Lo que el plan da por sentado.** El plan descansa en que el docente que administra el campus ceda la administración, en que las carreras adopten la entrega digital y en que bienestar actúe sobre la alerta.
> **Las personas y los plazos de los que depende.** TI no participa en el comité académico. El docente administrador tiene carga completa. La visita de renovación del licenciamiento es en 11 meses.

### Ficha 8 · Empresa prestadora de servicios de saneamiento · 68 000 conexiones · TI 5 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 399 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** reducir el plazo de atención de reclamos de 9 a 5 días hábiles · **OE-02** bajar del 12 % al 5 % la facturación observada por error de catastro.
> **Los cuatro proyectos de mayor puntaje.** Integración del catastro comercial con facturación · Ambiente de pruebas y control de cambios · Telemetría de presión en cinco zonas · Portal del usuario con recibo y reclamo.
> **Lo que el plan da por sentado.** El plan descansa en que catastro y facturación acepten una sola base, en que el ambiente de pruebas exista antes de la integración y en que los servidores aguanten 24 meses.
> **Las personas y los plazos de los que depende.** No hay ambiente de pruebas. Un cambio directo en producción ya costó S/ 61 000. El regulador exige trazabilidad mensual.

### Ficha 9 · Servicios de ingeniería para minería · 88 trabajadores · TI 4 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 396 500 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** desarrollar dos servicios nuevos por año · **OE-02** bajar de 12 a 4 días la entrega del informe técnico al cliente.
> **Los cuatro proyectos de mayor puntaje.** Automatización del informe técnico · Marco de gestión de incidentes exigido por los contratos · Segundo desarrollador y control de cambios de la telemetría · Migración del ERP administrativo.
> **Lo que el plan da por sentado.** El plan descansa en que el desarrollador de telemetría se quede y documente, en que el cliente renueve el contrato del 34 % de la facturación y en que la migración del ERP no coincida con una campaña.
> **Las personas y los plazos de los que depende.** Un solo desarrollador con acceso a producción. El puesto se cotiza por encima de lo que la empresa paga. La renovación es en 10 meses.

### Ficha 10 · Cadena regional de farmacias · 34 locales · TI 5 personas

> **Horizonte.** 2027 a 2029, tres años. **Presupuesto del horizonte** S/ 258 000 de inversión, la mitad de lo que las áreas pidieron.
> **Objetivos.** **OE-01** bajar la rotura de stock de 3.1 % a 1.5 % · **OE-02** reducir 10 % el capital inmovilizado en inventario.
> **Los cuatro proyectos de mayor puntaje.** Reposición predictiva por local · Reemplazo de la consolidación nocturna por sincronización en línea · Tablero de inventario y antigüedad por local · Base legal y consentimiento del programa de cliente frecuente.
> **Lo que el plan da por sentado.** El plan descansa en que la consolidación nocturna se reemplace sin parar los 34 locales, en que marketing deje de exportar la base de clientes y en que la reposición predictiva funcione con el histórico que existe.
> **Las personas y los plazos de los que depende.** La consolidación falla dos veces por semana y una sola persona la reprocesa. Marketing exporta datos de salud a hoja de cálculo. La receta electrónica llega sin fecha cierta.

---

---

[Semana 15](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
