# Anexo — Caso simulado de respaldo · **DISTRIBUIDORA ANDINA DEL SUR S.A.C.**

> **Cuándo se usa.** Sustituye a la organización real cuando el equipo no consigue acceso, o cuando el acceso se pierde durante el semestre. Permite construir el PETI completo (Sección 0 a Sección 10) sin perder continuidad.
> **Advertencia.** La organización es **ficticia**. Cualquier coincidencia con una empresa existente es casual. **No debe presentarse como un caso real ante terceros.**
> Este caso es el mismo que usa el curso SI-084 Auditoría de Sistemas, lo que permite a un estudiante que curse ambos ver la misma organización desde las dos perspectivas.

---

## 1. Ficha de la organización

| Campo | Valor |
|---|---|
| Razón social | Distribuidora Andina del Sur S.A.C. |
| RUC (ficticio) | 20###### (asignado por el docente) |
| Naturaleza | **Empresa privada no supervisada** |
| Sector | Comercio al por mayor de productos de consumo masivo |
| Ámbito | Tacna, Moquegua y Arequipa |
| Antigüedad | Más de diez años de operación |
| Personal | 64 trabajadores (8 administración · 22 almacén y despacho · 26 fuerza de ventas · 5 TI · 3 gerencia) |
| Ventas anuales | S/ 38 millones · margen bruto 18 % (promedio del sector: 24 %) |
| Clientes | 8 400 bodegas y minoristas registrados |
| Proveedores | 47 activos; 6 concentran el 78 % del volumen |
| **Marco normativo aplicable** | Ley 29733 y D. S. 016-2024-JUS · D. Leg. 822 · Ley 30096 · Ley 27269 · normativa de SUNAT sobre comprobantes y libros electrónicos. **No** le aplican el D. Leg. 1412, la Res. SBS 504-2021 ni la normativa de la Contraloría |

## 2. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado |
|---|---|---|---|
| Plan Estratégico Institucional vigente | **Sí** | Vigente | Aprobado en acta de directorio; no se evalúa |
| Presupuesto anual | Sí | Ejercicio en curso | Aprobado |
| Plan de TI o PETI previo | **No** | — | Nunca ha existido |
| Plan de continuidad | **No** | — | — |

**Extracto del Plan Estratégico Institucional vigente** (entregado por el docente):

| Objetivo estratégico | Meta declarada |
|---|---|
| **OE-1** Ampliar la cobertura de puntos de venta atendidos en la macrorregión sur | Del 41 % al 60 % de los puntos de venta al cierre del horizonte |
| **OE-2** Digitalizar el canal de venta al detalle | Sin meta cuantificada |
| **OE-3** Mejorar el margen bruto | De 18 % a 22 % al cierre del horizonte |
| **OE-4** Consolidar la relación de largo plazo con el pequeño comerciante | Sin meta cuantificada |

> **Hallazgo para la sección 1.2.** Dos de los cuatro objetivos institucionales no tienen meta cuantificada. El PETI debe articularse a los que sí la tienen y proponer la métrica de los otros dos.

## 3. Gobierno y cultura

- **No existe comité de TI.** Las decisiones tecnológicas las toma el Gerente de Administración con el Jefe de TI.
- El **Jefe de TI reporta a la Gerencia de Administración**; su presupuesto compite con gasto corriente.
- El directorio **no ha tratado tecnología** en ninguna de las 11 actas de los últimos 24 meses.
- **No existe declaración de apetito de riesgo.**
- Perfil cultural medido con el Competing Values Framework (N = 38 respondientes):

| Tipo | Hoy | Deseado | Brecha |
|---|---|---|---|
| **Jerarquía** | **42** | 30 | −12 |
| Clan | 26 | 24 | −2 |
| Mercado | 20 | 20 | 0 |
| Adhocracia | 12 | **26** | **+14** |

- **Supuestos básicos detectados.** «Las decisiones las toma una sola persona» · «reportar un error trae consecuencias» · «la información es fuente de poder del área» · «si funciona, no se toca».
- Solo el **28 %** del personal reconoce la misión declarada.

## 4. Cadena de valor y sistemas

| Actividad | Volumen mensual | % del costo operativo | Sistema que la soporta | Nivel de soporte |
|---|---|---|---|---|
| Logística interna | 340 recepciones | 12 % | ERP Inventarios + papel | Parcial |
| Operaciones (preparación) | 6 200 pedidos | 18 % | WMS + escáner | Bueno |
| **Logística externa (ruteo y despacho)** | 6 200 despachos | **22 %** | **Hoja de cálculo** | **Deficiente** |
| **Marketing y ventas (toma de pedido)** | 6 200 pedidos | 15 % | Teléfono + papel + portal (4 %) | **Deficiente** |
| Servicio posventa | 180 casos | 4 % | Correo | **Deficiente** |
| Desarrollo tecnológico | — | 6 % | — | Dependencia de una persona |
| Abastecimiento | 47 proveedores | 8 % | ERP Compras | Bueno |
| RR. HH. | 64 personas | 9 % | Sistema de planilla externo | Parcial |
| Infraestructura | — | 6 % | ERP Contabilidad + hojas de cálculo | Parcial |

| Sistema | Proveedor / origen | Ubicación | Observación |
|---|---|---|---|
| **ERP Comercial** (Compras, Ventas, Inventarios, Contabilidad) | Producto empaquetado local, en uso desde hace más de una década | Servidor físico en Tacna | 87 usuarios · **contrato de soporte vencido** · sistema operativo fuera de soporte |
| Sistema de Planilla | Proveedor externo | Nube, región no verificada | Contiene **datos sensibles** de salud ocupacional |
| **Portal de pedidos B2B** | desarrollo propio | VPS contratado en el extranjero | **Adopción del 4 %** · expuesto a internet · **un solo desarrollador lo conoce** |
| Correo y ofimática | Suite en la nube | **Servidores en el extranjero** | **Flujo transfronterizo** sin garantías verificadas |
| **Hojas de cálculo de Gerencia Comercial** | Elaboración propia | Carpeta compartida en la nube | Márgenes por cliente, presupuesto y comisiones · **una sola analista** · sin control de versiones |
| WMS de almacén | Módulo del ERP | Servidor local | Integración con el ERP por **archivo plano nocturno** |

## 5. Entidades de información

| Entidad | Sistemas donde reside | Registros por sistema | Fuente autoritativa | Dueño del dato | ¿Datos personales? |
|---|---|---|---|---|---|
| **Cliente** | ERP · Portal · Hoja comercial | 8 400 / 340 / 8 900 | **Ninguna** | **Ninguno** | Sí |
| Producto | ERP · WMS · Hoja de precios | 2 140 / 2 140 / 2 310 | ERP (de hecho) | Ninguno | No |
| Pedido | ERP · Portal · WMS | — | ERP | Ninguno | Sí (contacto) |
| **Trabajador** | Planilla · ERP · Hoja de RR. HH. | 64 / 71 / 64 | Ninguna | Ninguno | **Sí, sensibles** |
| Proveedor | ERP | 47 | ERP | Ninguno | Sí (personas naturales) |
| Ruta de despacho | Hoja de cálculo | — | Hoja de cálculo | Ninguno | No |

## 6. Catálogo de servicios

| Servicio | Destinatario | Volumen anual | Nivel actual (0–5) | Canales | Documentos solicitados / ya en poder |
|---|---|---|---|---|---|
| Registro de pedido | Cliente | 74 400 | **1** | Teléfono, vendedor, portal (4 %) | 0 / 0 |
| Consulta de estado de pedido | Cliente | 22 000 | **0** | Teléfono al vendedor | 0 / 0 |
| Solicitud de línea de crédito | Cliente | 320 | **2** | Formulario en papel | 4 / **2** |
| Reclamo o devolución | Cliente | 180 | **1** | Teléfono, correo | 2 / 1 |
| Descarga de comprobante | Cliente | 74 400 | **2** | Correo bajo pedido | 0 / 0 |
| Solicitud de vacaciones | Trabajador | 130 | **0** | Papel | 1 / **1** |
| Consulta de boleta de pago | Trabajador | 768 | **2** | Impresa | 0 / 0 |

## 7. Presupuesto de TI

| Categoría | Año anterior (S/) | Año en curso (S/) | Tipo |
|---|---|---|---|
| Licencias y suscripciones | 180 000 | 210 000 | Operar |
| Infraestructura y nube | 120 000 | 145 000 | Operar |
| Soporte y personal operativo | 240 000 | 250 000 | Operar |
| Mantenimiento correctivo | 60 000 | 72 000 | Operar |
| Seguridad de la información | 25 000 | **18 000** | Operar |
| Nuevos módulos del ERP | 90 000 | 40 000 | Crecer |
| **Canal digital** | 45 000 | **20 000** | Crecer |
| **Analítica de datos** | 30 000 | **0** | Transformar |
| **Total** | **790 000** | **755 000** | |

> **Contraste para la sección 3.5 y la sección 7.1.6.** El plan estratégico declara la digitalización del canal como objetivo (OE-2) y el presupuesto del año en curso lo **reduce en 56 %** y elimina «Transformar». **Lo que se dice y lo que se financia no coinciden.**
>
> **Presupuesto disponible acordado para el PETI.** S/ 320 000 anuales durante tres años (Entrevista 3 con la gerencia).

## 8. Inversiones cerradas (para Val IT y la sección 7.1.5)

| Inversión | Año | Monto | Caso de negocio | Beneficio proyectado | Beneficio medido |
|---|---|---|---|---|---|
| Portal de pedidos B2B | Año -4 | S/ 180 000 | Sí, dos páginas | «Aumentar 20 % los pedidos del canal detalle» | **No se midió** |
| Renovación de servidores de almacén | Año -2 | S/ 95 000 | No | — | **No se midió** |
| Módulo de comisiones del ERP | Año -1 | S/ 40 000 | Correo del Gerente de Ventas | «Reducir el tiempo de cálculo» | **No se midió** |

## 9. Contexto e incidentes

**Datos del entorno** (para la sección 1.1 y la sección 3.3). Los equipos descargan las series reales de **INEI, BCRP y OSIPTEL** correspondientes a la región de Tacna y al sector de comercio al por mayor. **El contexto no se simula. Se toma de las fuentes oficiales.**

**Incidentes de los últimos 24 meses.**

1. Caída del ERP durante 9 horas por falla del disco del servidor (<mes/año>). Sin plan de contingencia; se recuperó reinstalando y restaurando el respaldo del día anterior.
2. Correo de un vendedor comprometido, usado para solicitar cambio de cuenta bancaria a tres clientes (<mes/año>). Dos clientes detectaron el intento; uno transfirió S/ 12 400.
3. Borrado accidental de la tabla de precios, recuperado desde respaldo en 6 horas (<mes/año>).

**Entrevistas simuladas.** El docente entrega la transcripción de tres entrevistas —Gerencia General, Jefatura de TI y Gerencia Comercial— con las preguntas de las semanas 4, 9 y 14 ya respondidas, para que el equipo procese el material como si lo hubiera recogido.

**Encuestas simuladas.** Se entregan los conjuntos de respuestas de la encuesta de percepción (N = 38) y del instrumento de cultura (N = 38), en CSV, con la estructura que consumen los scripts de las semanas 4 y 5.

## 10. Declaración obligatoria en el PETI

Todo equipo que use este caso incorpora en la Sección 0.2 del plan:

> *«El presente Plan Estratégico de Tecnologías de Información se elaboró sobre un caso de estudio simulado con fines académicos, denominado Distribuidora Andina del Sur S.A.C. La organización, sus datos, sistemas y documentos son ficticios y fueron construidos por el docente del curso SI-886 de la Escuela Profesional de Ingeniería de Sistemas de la Universidad Privada de Tacna. Los datos de contexto macroeconómico y sectorial provienen de fuentes oficiales reales. La metodología, los marcos y el nivel de exigencia aplicados son los mismos que se emplearían en un encargo real.»*
