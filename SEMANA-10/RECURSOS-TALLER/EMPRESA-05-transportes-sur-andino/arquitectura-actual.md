<div align="center">
  <strong>TRANSPORTES SUR ANDINO S.A.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | TRANSPORTES SUR ANDINO S.A. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 13 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **Venta de pasajes y manifiesto** | Producto del rubro, terminales en counter | Servidor central en Tacna | Sí |
| **Venta en línea y app de pasajeros** | Desarrollo tercerizado en 2021 | Nube pública | Contrato vencido |
| **GPS y control de flota** | Servicio del proveedor de rastreo | SaaS | Sí |
| **Mantenimiento de unidades** | Hojas de cálculo compartidas | Drive corporativo | No |
| **Planillas y control de descanso de conductores** | Sistema local | PC de RR. HH. | No |
| **Hoja de cálculo · Mantenimiento de unidades, en el Drive corporativo** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Control de horas de conducción y descanso, con macros** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Conciliación de la venta en línea** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Programación de flota y rutas | GPS y control de flota |
| Venta de pasajes en counter y en línea | Venta de pasajes y manifiesto |
| Embarque y manifiesto de pasajeros | Venta de pasajes y manifiesto |
| Mantenimiento de unidades | Mantenimiento de unidades |
| Control de conductores y descansos | Planillas y control de descanso de conductores |
| Encomiendas y carga | Venta de pasajes y manifiesto |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Venta de pasajes en counter | Venta en línea | Ninguna. No comparten el bloqueo de asiento |
| Venta en counter | Manifiesto | Módulo del mismo producto |
| GPS y control de flota | Nadie | Ninguna. Se consulta en la consola del proveedor |
| Planillas | Control de descansos | Ninguna. El libro se alimenta de los manifiestos impresos |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Pasajero | Counter · Venta en línea · Manifiesto impreso | 310 000 boletos al año · 96 000 · 310 000 | Ninguna | Ninguno | 78 asientos vendidos dos veces en un feriado | Confidencial | Sí |
| Conductor | Planillas · Libro de descansos · Manifiesto | 140 · 140 · por viaje | Ninguna | Jefe de operaciones | 23 manifiestos inconsistentes con el libro | Restringida | Sí |
| Unidad | GPS · Drive de mantenimiento · Habilitación del MTC · Programación | 48 · 48 · 48 · 48 | El MTC | Jefe de mantenimiento | El kilometraje difiere entre el GPS y el Drive | Interna | No |
| Viaje | Programación en libro de cálculo · Counter · GPS | 9 600 al año | Ninguna | Jefe de operaciones | Salidas programadas que el GPS no registra | Interna | No |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor central de venta en Tacna · la nube pública del canal en línea, con un proveedor sin contrato · el SaaS del GPS · PC de RR. HH. con planillas · counters en cuatro terminales de tres regiones · 44 estaciones.

**Redes.** Red plana en Tacna. Los terminales se conectan por internet doméstico. Sin enlace privado entre sedes.

## 7. Lo que la organización responde

| Pregunta del equipo | Respuesta |
|---|---|
| ¿Existe un diagrama de arquitectura? | «Hay uno de red en una pizarra. Nunca se dibujaron los sistemas» |
| ¿Quién aprueba que un área cree una hoja de cálculo para operar? | «Nadie. Aparecen y después hay que alimentarlas» |
| ¿Quién es el dueño de cada dato? | «El sistema que lo tiene. Si está en dos, los dos» |
| ¿Qué pasa cuando dos sistemas dicen cifras distintas? | «Se pregunta al que lo lleva y se usa esa» |
| ¿Hay principios de arquitectura escritos? | «No» |

## 8. Marco de referencia

| Marco | Qué aporta |
|---|---|
| **TOGAF, 10.ª edición · ADM** | Fases B, C y D para la arquitectura de negocio, de sistemas de información y de tecnología, y el análisis de brechas |
| **ArchiMate 3.2** | El lenguaje con el que se modelan las capas y sus relaciones |
| **COBIT 2019 · APO03** | Gestión de la arquitectura empresarial |

