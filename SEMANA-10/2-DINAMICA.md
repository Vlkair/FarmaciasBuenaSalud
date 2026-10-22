[Semana 10](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

# Semana 10

## Rastreo del dato

**SI-886 - Planeamiento Estratégico de TI** - Actividad en aula, **dentro de la sesión de teoría** · calificación **cognitiva**

> ¿Un término no le resulta claro? Está definido en el [glosario técnico del curso](../GLOSARIO.md).

---

## Qué entregas

| | |
|---|---|
| **Archivo** | `SI886-S10-DINAMICA-Grupo<N>.pdf` |
| **Plantilla obligatoria** | [SI886-PLANTILLA-DINAMICA.docx](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx) |
| **Formato** | PDF exportado desde la plantilla en Word, con la carátula de la UPT y los apellidos, nombres y códigos de todos los integrantes |
| **Qué va dentro** | Lo que el grupo resolvió en aula. Las tablas de la sección **Producto** van completas, con los textos redactados, y cada decisión va justificada |
| **Dónde se sube** | Aula virtual, tarea «Dinámica · Semana 10» |
| **Cuándo vence** | Según lo programado en el aula virtual. La tabla se resuelve en aula; el PDF se formatea y se sube después |
| **Exposición** | En la ronda de cierre de **esta misma sesión**. El grupo **lee y explica su resultado** ante el aula, con el documento a la vista. No se usan diapositivas |

> No se califica un trabajo entregado en `.docx`, sin carátula, sin los códigos de los integrantes o con las tablas del producto vacías.

---

## Consigna

> **«Rastreo del dato»**
> El mismo dato aparece con tres valores distintos en tres sistemas. Gerencia pregunta cuál es el bueno y nadie sabe responder.

| | |
|---|---|
| **Su papel** | **Arquitecto de datos** citado por gerencia para dar una respuesta hoy |
| **Misión** | Encontrar la fuente autoritativa del dato, o demostrar que **no existe**, y decir qué se rompe por eso |
| **Restricción** | **No vale responder «hay que integrar».** Hay que nombrar quién es el dueño del dato, por cargo |

Un dato que vive en cuatro sistemas y no tiene dueño no es un problema técnico. Es un problema **de la capa de negocio**, y por eso el análisis de brechas del ADM lo encuentra antes que cualquier herramienta.

## Producto

**El informe del arquitecto.**

| Dónde vive el dato | Registros | Campos | Quién lo actualiza | ¿Es la fuente autoritativa? |
|---|---|---|---|---|

**Y el veredicto, en cuatro líneas.**

| | Contenido |
|---|---|
| **La fuente autoritativa** | Cuál es, o **«hoy no existe»** si es el caso |
| **El dueño** | El cargo que responde por el dato. Si nadie responde, ese es el hallazgo |
| **El daño concreto** | Un caso real o verosímil donde la organización ya perdió tiempo, dinero o credibilidad por esto |
| **La capa donde está la brecha** | La capa de ArchiMate donde de verdad está — negocio, datos, aplicaciones o tecnología. Casi nunca es la que parece |
| **Qué exige arreglarlo** | La decisión de gobierno, no solo la integración técnica |

> **Dónde va.** Este producto se presenta en la **sección 2 de la [plantilla de dinámica](../PLANTILLAS/SI886-PLANTILLA-DINAMICA.docx)**, «El producto». No se copia la consigna ni la teoría. Solo el resultado y lo que lo sostiene.

## Ejemplo resuelto

*El caso de este ejemplo es distinto del que le toca a tu grupo. Sirve para que veas el nivel de detalle que se espera, no para copiarlo.*

**La entidad rastreada.** «Cliente», en una distribuidora mayorista.

| Dónde vive el dato | Registros | Campos | Quién lo actualiza | ¿Fuente autoritativa? |
|---|---|---|---|---|
| ERP, módulo Ventas | 8 400 | 14 | Facturación, al emitir | Se asume que sí |
| Portal B2B | 340 | 6 | El propio cliente | No |
| Hoja de cálculo comercial | 8 900 | 22 | Un analista, a mano | No, pero es la que se usa para decidir |
| Correo del vendedor | variable | — | Nadie | No |

**El veredicto.**

| | Contenido |
|---|---|
| **La fuente autoritativa** | **Hoy no existe.** El ERP tiene el dato fiscal, pero la hoja de cálculo tiene 500 clientes más y 8 campos más, y es la que la gerencia mira |
| **El dueño** | Nadie. Ningún cargo responde por el maestro de clientes. **Ese es el hallazgo principal** |
| **El daño concreto** | En la campaña de marzo se envió la promoción a 8 400 clientes del ERP. Las 500 bodegas que solo estaban en la hoja de cálculo no la recibieron, y son las de mayor rotación. Se perdió la campaña con el mejor segmento |
| **Qué exige arreglarlo** | Designar al **Jefe Comercial** como dueño del maestro de clientes, con facultad para aprobar altas y bajas. La integración viene después, y sin el dueño no sirve de nada |

**La diferencia entre aprobar y no aprobar**

| Así no | Así sí |
|---|---|
| «El ERP es la fuente principal.» | «Hoy no existe fuente autoritativa: la hoja de cálculo tiene 500 clientes más y es la que se usa para decidir.» |
| «Hay que integrar los sistemas.» | «Designar al Jefe Comercial como dueño del maestro. La integración viene después.» |
| «Existe riesgo de inconsistencia.» | «En marzo, 500 bodegas de alta rotación no recibieron la promoción.» |

## Reglas

- El dueño se nombra **por cargo**, nunca por persona.
- «Hay que integrar los sistemas» **no es una respuesta**. La integración es la consecuencia, no la decisión.
- El daño se cuenta como **un caso**, con su fecha o su situación. Una lista de riesgos genéricos no se califica.
- Declarar que no hay fuente autoritativa **es un hallazgo válido** y suele ser el correcto.
- La exposición es la ronda de cierre de esta misma sesión. El grupo **lee y explica su resultado**. No se usan diapositivas.

## Rúbrica cognitiva (20 puntos)

| Criterio | 5 | 3 | 1 |
|---|---|---|---|
| **El mapa** | Todos los lugares donde vive el dato, con volumen y responsable de actualización | Falta un lugar o un responsable | Solo los sistemas formales, sin las hojas de cálculo ni el correo |
| **La fuente autoritativa** | Determinada con criterio, o declarada inexistente con fundamento | Determinada sin fundamentar | Se elige la más grande sin criterio |
| **La capa y el dueño** | La brecha situada en su capa de la arquitectura, y el dueño nombrado por cargo. Si no existe, se dice con todas las letras | Nombrado de forma difusa | Ausente |
| **El daño** | Un caso concreto que la organización reconocería | Un caso verosímil pero genérico | Una lista de riesgos |

## Anexo · Material de trabajo

Cada equipo recibe **un dato** de su organización y **lo que cada área respondió** cuando gerencia preguntó por él. Son declaraciones, no un inventario. El equipo arma con ellas la tabla del informe del arquitecto, decide cuál es la fuente autoritativa, quién es el dueño por cargo y en qué capa está la brecha.

**Reparto.** Una ficha por equipo, **la misma organización que le tocó en la Semana 03**. Son las diez de siempre, con los mismos tamaños, presupuestos, objetivos y proyectos.

### Ficha 1 · Agroexportadora de aceituna y orégano · 142 trabajadores · TI 3 personas

> **El dato.** El stock de aceituna del lote 2025-114.
> **Lo que preguntó gerencia.** Gerencia quiere saber cuántas toneladas del lote quedan para embarcar y recibió tres cifras.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Jefe de planta.** «Lo tenemos en hoja de cálculo de trazabilidad de planta. Son 1 lote por fila, 2 300 filas, con los campos lote, kilos, calibre, fecha. Lo actualiza el jefe de planta, al cierre del turno. Para lo que pregunta gerencia, hoy figura **38.2 t**.»
> **Almacenero.** «Lo tenemos en ERP, módulo de almacén. Son 1 ítem por calibre, 410 ítems, con los campos ítem, kilos, almacén. Lo actualiza el almacenero, cuando despacha. Para lo que pregunta gerencia, hoy figura **36.9 t**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en software de la balanza. Son 1 pesada por fila, 9 800 pesadas, con los campos fecha, kilos, placa. Nadie. La balanza registra sola. Para lo que pregunta gerencia, hoy figura **39.1 t ingresadas**.»
> **Asistente de exportación.** «Lo tenemos en hoja del área de exportación. Son 1 embarque por fila, con los campos contenedor, lote, kilos. Lo actualiza el asistente de exportación, al armar el embarque. Para lo que pregunta gerencia, hoy figura **37.0 t**.»

### Ficha 2 · Clínica privada de 60 camas · 310 trabajadores · TI 6 personas

> **El dato.** El número de aseguradora y el plan del paciente.
> **Lo que preguntó gerencia.** Facturación devolvió 140 atenciones del mes porque la aseguradora rechazó el plan registrado.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Admisionista.** «Lo tenemos en sistema clínico, admisión. Son 48 000 pacientes, con los campos documento, aseguradora, plan, vigencia. Lo actualiza el admisionista, al filiar. Para lo que pregunta gerencia, hoy figura **Plan A, vigente**.»
> **Facturador.** «Lo tenemos en sistema clínico, facturación. Son Mismo paciente, otra tabla, con los campos aseguradora, plan, tarifario. Lo actualiza el facturador, al cerrar la atención. Para lo que pregunta gerencia, hoy figura **Plan B**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en portal de citas en línea. Son 31 % de las citas, con los campos documento, aseguradora declarada. El propio paciente. Para lo que pregunta gerencia, hoy figura **Plan A**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en archivo que envía la aseguradora cada mes. Son Hoja de cálculo, con los campos documento, plan, estado. Nadie lo carga. Se consulta a mano. Para lo que pregunta gerencia, hoy figura **Plan C, suspendido**.»

### Ficha 3 · Municipalidad distrital · 41 800 habitantes · TI 3 personas

> **El dato.** La deuda del contribuyente por impuesto predial.
> **Lo que preguntó gerencia.** Un vecino mostró tres montos distintos de su deuda y el alcalde pidió explicación.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Rentas.** «Lo tenemos en sistema de rentas. Son 22 600 predios, con los campos código de predio, deuda, periodo. Lo actualiza el rentas, al cierre mensual. Para lo que pregunta gerencia, hoy figura **S/ 1 840**.»
> **Cajero.** «Lo tenemos en caja, módulo de cobranza. Son Pagos del día, con los campos recibo, monto, periodo pagado. Lo actualiza el cajero, al cobrar. Para lo que pregunta gerencia, hoy figura **S/ 1 420 pendiente**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en mesa de partes virtual. Son Solicitudes de fraccionamiento, con los campos expediente, monto declarado. El propio contribuyente. Para lo que pregunta gerencia, hoy figura **S/ 2 100**.»
> **Fiscalizador.** «Lo tenemos en hoja del área de fiscalización. Son Predios fiscalizados, con los campos predio, área nueva, deuda recalculada. Lo actualiza el fiscalizador, por campaña. Para lo que pregunta gerencia, hoy figura **S/ 2 310**.»

### Ficha 4 · Cooperativa de ahorro y crédito · 18 400 socios · TI 7 personas

> **El dato.** El socio activo.
> **Lo que preguntó gerencia.** El Consejo preguntó cuántos socios activos hay y recibió tres respuestas en la misma sesión.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Plataforma.** «Lo tenemos en core financiero. Son 18 400 socios, con los campos código, estado, último movimiento. Lo actualiza la plataforma, al atender. Para lo que pregunta gerencia, hoy figura **14 900 activos**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en aplicación móvil. Son Usuarios registrados, con los campos usuario, último acceso. El propio socio. Para lo que pregunta gerencia, hoy figura **7 540 activos en el mes**.»
> **Analista.** «Lo tenemos en unidad de Analítica de Socio. Son Extracción mensual, con los campos código, perfil, actividad calculada. Lo actualiza el analista, cada mes. Para lo que pregunta gerencia, hoy figura **12 100 activos**.»
> **Oficial de cumplimiento.** «Lo tenemos en sistema de prevención de lavado de activos. Son Socios con operaciones, con los campos código, operaciones, alertas. Lo actualiza el oficial de cumplimiento. Para lo que pregunta gerencia, hoy figura **15 800 con operación en el año**.»

### Ficha 5 · Empresa de transporte de carga · 96 trabajadores · TI 2 personas

> **El dato.** El estado de la entrega del cliente.
> **Lo que preguntó gerencia.** Un cliente reclamó por una entrega que el sistema daba por hecha y que nunca llegó.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en sistema de flota con GPS. Son Viajes del día, con los campos viaje, placa, posición, hora. El GPS, solo. Para lo que pregunta gerencia, hoy figura **Entregado 14:20**.»
> **Operador.** «Lo tenemos en central telefónica, hoja de seguimiento. Son Llamadas de clientes, con los campos cliente, guía, estado anotado. Lo actualiza el operador, cuando el cliente llama. Para lo que pregunta gerencia, hoy figura **En ruta**.»
> **Facturador.** «Lo tenemos en facturación. Son Guías emitidas, con los campos guía, cliente, fecha de entrega. Lo actualiza el facturador, al emitir. Para lo que pregunta gerencia, hoy figura **Pendiente de conformidad**.»
> **Supervisor.** «Lo tenemos en hoja del supervisor de ruta. Son Entregas de la semana, con los campos guía, incidencia, observación. Lo actualiza el supervisor, al cierre de la semana. Para lo que pregunta gerencia, hoy figura **Rechazada por el receptor**.»

### Ficha 6 · Distribuidora mayorista de consumo masivo · 157 trabajadores · TI 4 personas

> **El dato.** El stock disponible de un producto de alta rotación.
> **Lo que preguntó gerencia.** El vendedor en ruta vendió 120 cajas que el almacén no tenía.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en ERP, módulo de almacén. Son 6 200 ítems, con los campos ítem, stock, ubicación. Nadie desde 2024. Se dejó de usar. Para lo que pregunta gerencia, hoy figura **340 cajas**.»
> **Jefe de almacén.** «Lo tenemos en hoja de cálculo del almacén. Son Ítems en uso, con los campos ítem, stock físico, fecha de conteo. Lo actualiza el jefe de almacén, al contar. Para lo que pregunta gerencia, hoy figura **215 cajas**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en aplicación de fuerza de ventas. Son Catálogo sincronizado, con los campos ítem, disponible, precio. Se sincroniza desde el ERP cada noche. Para lo que pregunta gerencia, hoy figura **340 cajas**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en portal de pedidos de la bodega. Son Catálogo publicado, con los campos ítem, disponible. Se actualiza a mano por marketing. Para lo que pregunta gerencia, hoy figura **Disponible**.»

### Ficha 7 · Instituto de educación superior tecnológica · 2 100 estudiantes · TI 3 personas

> **El dato.** El estudiante matriculado en el ciclo.
> **Lo que preguntó gerencia.** Cobranza persigue a estudiantes que ya se retiraron y el campus virtual tiene alumnos que no existen en matrícula.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Secretaría académica.** «Lo tenemos en sistema académico, matrícula. Son 2 100 estudiantes, con los campos código, carrera, ciclo, estado. Lo actualiza la secretaría académica, al matricular. Para lo que pregunta gerencia, hoy figura **2 100 matriculados**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en campus virtual. Son Usuarios en cursos, con los campos usuario, cursos, último acceso. El docente administrador, por lotes. Para lo que pregunta gerencia, hoy figura **2 340 usuarios activos**.»
> **Tesorería.** «Lo tenemos en cobranza, módulo del sistema académico. Son Cuentas por cobrar, con los campos código, pensión, estado de deuda. Lo actualiza la tesorería, al cobrar. Para lo que pregunta gerencia, hoy figura **2 215 con pensión vigente**.»
> **Coordinadora de bienestar.** «Lo tenemos en hoja de bienestar estudiantil. Son Casos de seguimiento, con los campos código, situación, retiro. Lo actualiza la coordinadora de bienestar. Para lo que pregunta gerencia, hoy figura **180 retirados no registrados**.»

### Ficha 8 · Empresa prestadora de servicios de saneamiento · 68 000 conexiones · TI 5 personas

> **El dato.** La conexión activa y su categoría tarifaria.
> **Lo que preguntó gerencia.** El regulador observó 3 100 recibos con categoría distinta a la del catastro.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Catastro.** «Lo tenemos en catastro comercial. Son 68 000 conexiones, con los campos código, dirección, categoría, estado. Lo actualiza el catastro, por inspección. Para lo que pregunta gerencia, hoy figura **Doméstica**.»
> **Facturación.** «Lo tenemos en facturación. Son Conexiones facturadas, con los campos código, categoría, consumo, monto. Lo actualiza la facturación, al cierre del ciclo. Para lo que pregunta gerencia, hoy figura **Comercial**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en aplicación de lectura móvil. Son Rutas de lectura, con los campos código, lectura, observación. Lo actualiza el lecturista, en campo. Para lo que pregunta gerencia, hoy figura **Cortada**.»
> **Atención al usuario.** «Lo tenemos en registro único de reclamos. Son Reclamos del año, con los campos código, motivo, estado. Lo actualiza la atención al usuario. Para lo que pregunta gerencia, hoy figura **Reclamo por categoría, abierto**.»

### Ficha 9 · Servicios de ingeniería para minería · 88 trabajadores · TI 4 personas

> **El dato.** Las horas de instrumentación instaladas en el proyecto del cliente.
> **Lo que preguntó gerencia.** El cliente discute la factura porque el informe técnico y el estado de cuenta no coinciden.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en plataforma de telemetría propia. Son Lecturas por sensor, con los campos sensor, proyecto, horas activas. El sensor, solo. Para lo que pregunta gerencia, hoy figura **1 240 horas**.»
> **Administración.** «Lo tenemos en ERP administrativo, módulo de proyectos. Son Partidas del contrato, con los campos proyecto, partida, horas facturables. Lo actualiza la administración, al facturar. Para lo que pregunta gerencia, hoy figura **1 100 horas**.»
> **Jefe de proyecto.** «Lo tenemos en hoja del jefe de proyecto. Son Avance semanal, con los campos semana, equipo instalado, horas. Lo actualiza el jefe de proyecto, cada viernes. Para lo que pregunta gerencia, hoy figura **1 310 horas**.»
> **Ingeniero de campo.** «Lo tenemos en informe técnico al cliente. Son Un informe por campaña, con los campos equipo, periodo, horas, resultado. Lo actualiza el ingeniero de campo, al redactar. Para lo que pregunta gerencia, hoy figura **1 180 horas**.»

### Ficha 10 · Cadena regional de farmacias · 34 locales · TI 5 personas

> **El dato.** El stock de un medicamento en un local.
> **Lo que preguntó gerencia.** Un local vendió un producto que la central daba por agotado, y otro rechazó una venta de un producto que sí tenía.
>
> **Lo que respondió cada área, en el orden en que gerencia preguntó.**
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en punto de venta del local. Son Ítems del local, con los campos ítem, stock, lote, vencimiento. El vendedor, al vender. Para lo que pregunta gerencia, hoy figura **12 unidades**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en consolidación central nocturna. Son Stock de los 34 locales, con los campos local, ítem, stock al cierre. Proceso nocturno, si no falla. Para lo que pregunta gerencia, hoy figura **0 unidades**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en reposición automática. Son Sugerencias de compra, con los campos ítem, stock calculado, pedido. Se calcula desde la central. Para lo que pregunta gerencia, hoy figura **Pedido emitido por 24**.»
> **Tecnologías de la Información, por lo que consta en el sistema.** «Lo tenemos en programa de cliente frecuente. Son Compras registradas, con los campos cliente, ítem, fecha. El punto de venta, al vender. Para lo que pregunta gerencia, hoy figura **3 vendidas hoy**.»

---

---

[Semana 10](README.md) · [Teoría](1-TEORIA.md) · **Dinámica de aula** · [Taller de laboratorio](3-TALLER.md)

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
