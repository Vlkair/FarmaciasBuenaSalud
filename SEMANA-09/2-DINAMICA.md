[Semana 09](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

# Semana 09

## La feria de marcos

**SI-886 - Planeamiento Estratégico de TI** - Actividad en aula, **dentro de la sesión de teoría** · calificación **cognitiva**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S09-DINAMICA-Grupo<N>.pdf` |
| **Plantilla obligatoria** | [SI886-PLANTILLA-DINAMICA.docx](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT y los apellidos, nombres y códigos de todos los integrantes |
| **Qué va dentro** | Lo que el grupo resolvió en aula. Las tablas de la sección **Producto** van completas, con los textos redactados, y cada decisión va justificada |
| **Dónde se sube** | Aula virtual, tarea «Dinámica · Semana 09» |
| **Cuándo vence** | Según lo programado en el aula virtual. La tabla se resuelve en aula; el PDF se formatea y se sube después |
| **Exposición** | En la ronda de cierre de **esta misma sesión**. El grupo **lee y explica su resultado** ante el aula, con el documento a la vista. No se usan diapositivas |

> No se califica un trabajo entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con las tablas del producto vacías.

---

## Consigna

> **«La feria de marcos»**
> COBIT, ITIL, ISO 27001, TOGAF y CMMI se venden hoy en el aula. Su dirección tiene un presupuesto de esfuerzo limitado y no alcanza para todos.

| | |
|---|---|
| **Su papel** | Dos integrantes son **proveedores** del marco que les fue asignado y tienen que venderlo. El resto es **la dirección**, que compra |
| **Misión** | Adoptar solo lo que resuelve un problema que el diagnóstico ya encontró, y **descartar el resto por escrito** |
| **Restricción** | **Doce unidades de esfuerzo.** Una adopción completa cuesta 6, una selectiva 3, una práctica suelta 1. Adoptar todo es imposible |

De la teoría de hoy. Los tres criterios que deciden — ¿hay obligación? ¿qué problema diagnosticado resuelve? ¿es proporcional al tamaño de la organización?

## Producto

**La decisión de marcos.**

| Marco | ¿Se adopta? | ¿Hay obligación? | Problema diagnosticado que resuelve | ¿Proporcional? | Alcance | Unidades |
|---|---|---|---|---|---|---|
| COBIT 2019 | | | | | | |
| ITIL 4 | | | | | | |
| ISO/IEC 27001:2022 | | | | | | |
| TOGAF | | | | | | |
| CMMI | | | | | | |

Con el total **de doce unidades gastadas ___** y las **tres prácticas prioritarias** que se implantan primero, cada una con la brecha que cierra y su herramienta libre.

> **Dónde va.** Este producto se presenta en la **sección 2 de la [plantilla de dinámica](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx)**, «El producto». No se copia la consigna ni la teoría. Solo el resultado y lo que lo sostiene.

## Ejemplo resuelto

*El caso de este ejemplo es distinto del que le toca a tu grupo. Sirve para que veas el nivel de detalle que se espera, no para copiarlo.*

**La organización del ejemplo.** Empresa prestadora de saneamiento · 68 000 conexiones · TI 5 personas.

**La decisión de marcos, con doce unidades de esfuerzo.**

| Marco | ¿Se adopta? | ¿Obligación? | Problema diagnosticado que resuelve | ¿Proporcional? | Alcance | Unidades |
|---|---|---|---|---|---|---|
| COBIT 2019 | Sí | No | Sección 3.2 · nadie responde por las decisiones de TI | Solo por partes | Selectiva · APO01, APO12 y DSS04 | **3** |
| ITIL 4 | Sí | No | Sección 3.4 · los reclamos de sistemas se atienden por WhatsApp | Sí | Selectiva · gestión de incidencias y de solicitudes | **3** |
| ISO/IEC 27001:2022 | Sí | **Sí**, por la RSGD para entidades del Estado | Sección 3.1 · no hay inventario de activos | Solo el núcleo | Selectiva · cláusulas 4 a 10 sin certificar | **6** |
| TOGAF | No | No | — | No, para 5 personas de TI es inviable | — | 0 |
| CMMI | No | No | — | No, la organización no desarrolla software | — | 0 |

**Total, 12 de 12 unidades.**

**Las tres prácticas prioritarias.** APO12 gestión de riesgos, porque el plan lo exige · gestión de incidencias de ITIL, con GLPI, porque hoy no hay registro de nada · inventario de activos del A.5.9, porque sin él ninguna otra práctica de seguridad se sostiene.

**Por qué se descartó TOGAF.** El proveedor lo vendió bien y el problema de arquitectura existe. Pero TOGAF con cinco personas consume el año entero del equipo y deja la operación sin nadie. La proporcionalidad decidió, no la utilidad.

**La diferencia entre aprobar y no aprobar**

| Así no | Así sí |
|---|---|
| «Adoptaremos COBIT, ITIL e ISO 27001.» | «COBIT selectivo, tres objetivos. ITIL selectivo, dos prácticas. ISO, cláusulas 4 a 10 sin certificar. Doce unidades.» |
| «TOGAF no aplica.» | «TOGAF resolvería un problema real, pero con cinco personas consume el año del equipo. Se descarta por proporcionalidad.» |

## Reglas

- **Doce unidades y ni una más.** Un plan que adopta todo no priorizó nada.
- El problema que el marco resuelve tiene que estar **en el diagnóstico de la organización**, citado por su sección. Un problema hipotético no justifica una adopción.
- **Descartar también se califica.** Un descarte con fundamento vale igual que una adopción.
- Sesenta segundos de venta. Pasado ese tiempo se cierra la intervención.
- La exposición es la ronda de cierre de esta misma sesión. El grupo **lee y explica su resultado**. No se usan diapositivas.

## Rúbrica cognitiva (20 puntos)

| Criterio | 5 | 3 | 1 |
|---|---|---|---|
| **Los tres criterios** | Aplicados a los cinco marcos, con respuesta explícita en cada uno | Aplicados a tres o cuatro | Se decide sin aplicarlos |
| **El anclaje al diagnóstico** | Cada adopción cita el problema real y su sección de origen | Cita el problema sin la sección | Justifica con un problema hipotético |
| **El presupuesto** | Se respetan las doce unidades y el alcance declarado es coherente con lo pagado | Se respeta el total con algún alcance incoherente | Se excede, o se adopta todo |
| **El descarte** | Los marcos descartados con fundamento propio de esta organización | Descarte genérico | No se descarta nada |

## Anexo · Material de trabajo

Cada equipo recibe la ficha de su organización con **lo que el diagnóstico ya encontró** y **lo que la obliga**. La feria no se decide con la descripción del marco. Se decide con estos cinco problemas y estas obligaciones, contra las doce unidades de esfuerzo de la consigna.

**Reparto.** Una ficha por equipo, **la misma organización que le tocó en la Semana 03**. Son las diez de siempre, con los mismos tamaños, presupuestos, objetivos y proyectos.

**Lo que cuesta cada cosa.** Una adopción completa, 6 unidades. Una adopción selectiva, 3. Una práctica suelta, 1. Lo que ninguna norma exige y ningún problema pide, no se compra.

### Ficha 1 · Agroexportadora de aceituna y orégano · 142 trabajadores · TI 3 personas · S/ 486 000

> **Lo que el diagnóstico encontró.** El servidor de planta se cifró en marzo y la última copia legible era de 14 días antes · La trazabilidad del lote se arma a mano en hojas de cálculo y el comprador la exige certificada · El contacto con el cliente internacional pasó a una casilla compartida y nadie mide la respuesta · El único indicador del comité es el costo por tonelada. No hay indicador de TI · Tres personas de TI atienden planta, oficina y campaña sin registro de pedidos.
> **Lo que la obliga.** Ninguna norma le exige un marco. El comprador europeo exige trazabilidad certificada y, desde el próximo ciclo, un capítulo de seguridad y datos.

### Ficha 2 · Clínica privada de 60 camas · 310 trabajadores · TI 6 personas · S/ 1 240 000

> **Lo que el diagnóstico encontró.** Dos de seis integrantes de TI renunciaron en el año y el único que conoce la integración clínica lleva ocho meses · 17 usuarios administrativos consultaron una historia sin relación con su función y nadie lo detectó a tiempo · El proveedor del sistema clínico deja de actualizar la versión local en 20 meses · Los resultados de laboratorio viajan impresos de un piso a otro · Las citas en línea pasaron de 0 a 31 % y nadie mide la caída del portal.
> **Lo que la obliga.** La historia clínica electrónica tiene norma propia. La seguridad de la información no tiene marco exigible, pero el dato de salud es sensible por ley.

### Ficha 3 · Municipalidad distrital · 41 800 habitantes · TI 3 personas · S/ 520 000

> **Lo que el diagnóstico encontró.** No existe Comité ni Líder de Gobierno Digital, exigibles por norma · El trámite documentario cayó en abril y 1 340 expedientes quedaron sin estado recuperable · No hay UPS ni respaldo fuera de la sede · La partida de proyectos nuevos ejecutó el 38 % · Tres personas de TI con rotación de jefe tres veces en cuatro años.
> **Lo que la obliga.** Es entidad pública. La NTP-ISO/IEC 27001 es de uso obligatorio por resolución de la PCM, y el gobierno digital tiene ley y reglamento propios.

### Ficha 4 · Cooperativa de ahorro y crédito · 18 400 socios · TI 7 personas · S/ 980 000

> **Lo que el diagnóstico encontró.** No hay procedimiento de reporte de incidentes al supervisor, que lo exige · El contrato del core está en dólares, vence en 16 meses y la versión sale de soporte en diciembre · El centro de datos propio consume el 11 % de la energía de la sede · La unidad de Analítica de Socio opera modelos de puntaje sin gobierno del dato · Siete personas de TI y ninguna práctica de gestión de cambios escrita.
> **Lo que la obliga.** La Resolución SBS N.º 504-2021 exige un sistema de gestión de seguridad de la información. Esa obligación no se negocia en la feria.

### Ficha 5 · Empresa de transporte de carga · 96 trabajadores · TI 2 personas · S/ 320 000

> **Lo que el diagnóstico encontró.** El sistema de flota lo mantiene una sola persona sin documentación · La guía de remisión electrónica depende de un intermediario cuyo contrato vence en 7 meses · El 6 % de las entregas tiene incidencia y nadie sabe en qué etapa se originan · Dos personas de TI para 96 trabajadores y una flota en ruta · Las tarifas son de lista y el ejecutivo de cuenta se eliminó.
> **Lo que la obliga.** Ninguna norma le exige un marco. SUNAT exige la emisión electrónica y el cliente exige puntualidad.

### Ficha 6 · Distribuidora mayorista de consumo masivo · 157 trabajadores · TI 4 personas · S/ 742 000

> **Lo que el diagnóstico encontró.** El proveedor del ERP, de la app de ventas y de la facturación deja de dar soporte a la versión local en 15 meses · El módulo de almacén se dejó de usar y el inventario se lleva en hojas de cálculo · Se tratan datos de 8 400 bodegas sin inventario ni registro de tratamiento · El portal de pedidos lo usa el 4 % de las bodegas · Cuatro personas de TI atienden ventas en ruta, almacén y oficina.
> **Lo que la obliga.** Ninguna norma le exige un marco. La migración del ERP la impone el proveedor.

### Ficha 7 · Instituto de educación superior tecnológica · 2 100 estudiantes · TI 3 personas · S/ 410 000

> **Lo que el diagnóstico encontró.** El campus virtual es un repositorio de archivos y las evaluaciones van en papel · El docente que administra el campus dicta programación con carga completa · Las actas se corrigen fuera del sistema y el licenciamiento se renueva en 11 meses · No hay política sobre el uso de asistentes de inteligencia artificial · TI depende de Administración y no participa en el comité académico.
> **Lo que la obliga.** El licenciamiento exige gestión académica verificable. Ninguna norma le exige un marco de TI.

### Ficha 8 · Empresa prestadora de servicios de saneamiento · 68 000 conexiones · TI 5 personas · S/ 890 000

> **Lo que el diagnóstico encontró.** Un cambio directo en producción emitió 11 400 recibos erróneos, con S/ 61 000 de reemisión · Catastro y facturación se concilian a mano cada mes · No hay ambiente de pruebas · El regulador exige reporte mensual con trazabilidad al dato origen · Los servidores del sistema comercial tienen 7 años y salen de soporte en 24 meses.
> **Lo que la obliga.** Es empresa pública. La NTP-ISO/IEC 27001 es de uso obligatorio por resolución de la PCM, y el regulador exige trazabilidad.

### Ficha 9 · Servicios de ingeniería para minería · 88 trabajadores · TI 4 personas · S/ 640 000

> **Lo que el diagnóstico encontró.** El desarrollador de telemetría es uno solo y tiene acceso directo a producción · Los contratos de los clientes incorporan cláusulas de seguridad y la renovación del 34 % de la facturación es en 10 meses · El informe técnico tarda 12 días en llegar al cliente · La instrumentación se importa en dólares sin contrato marco · La plataforma de telemetría acumula dos años de lecturas sin gobierno del dato.
> **Lo que la obliga.** Ninguna norma le exige un marco. El cliente minero sí exige evidencia de controles, y eso vale tanto como una norma.

### Ficha 10 · Cadena regional de farmacias · 34 locales · TI 5 personas · S/ 560 000

> **Lo que el diagnóstico encontró.** La consolidación de los 34 locales depende de un proceso que falla y de una persona · El programa de cliente frecuente registra datos de salud y marketing los exporta a hoja de cálculo · No hay canal digital de pedido y el 73 % de los clientes tiene teléfono con datos · La receta electrónica avanza en el sector y la cadena no tiene plan · Cinco personas de TI atienden 34 locales por teléfono.
> **Lo que la obliga.** Ninguna norma le exige un marco. La protección de datos de salud y la receta electrónica son las dos obligaciones que empujan.

---

---

[Semana 09](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
