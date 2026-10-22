<div align="center">
  <strong>COOPAC FRONTERA SUR</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | COOPAC FRONTERA SUR |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 23 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **Core financiero** | Producto especializado en cooperativas, licenciado | Servidor propio con réplica | Sí, contrato con SLA |
| **Banca por internet para socios** | Módulo web del mismo proveedor | Nube del proveedor | Sí |
| **Prevención de lavado de activos** | Sistema de alertas del proveedor | Servidor propio | Sí |
| **Central de riesgos** | Consulta a bureau externo por servicio web | SaaS | Sí |
| **Gestión documental de expedientes de crédito** | Carpetas compartidas en red | Servidor de archivos | No |
| **Hoja de cálculo · Reportes a la SBS, consultas y macros sobre el core** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Seguimiento de recuperaciones, un libro por agencia** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Captación de ahorros | Core financiero |
| Evaluación y otorgamiento de créditos | Central de riesgos |
| Recuperaciones y cobranza | Core financiero |
| Prevención de lavado de activos | Prevención de lavado de activos |
| Atención al socio en agencias | Banca por internet para socios |
| Cierre contable y reportes a la SBS | Core financiero |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Core financiero | Banca por internet | En línea, del mismo proveedor |
| Core financiero | Prevención de lavado de activos | Archivo diario automático |
| Core financiero | Central de riesgos | Servicio web en línea |
| Core financiero | Gestión documental de expedientes | Ninguna. El expediente es papel escaneado en carpetas |
| Core financiero | Planilla del proveedor | Ninguna |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Socio | Core · Banca por internet · Prevención de lavado · Carpetas de expedientes | 21 400 · 8 900 registrados · 21 400 · 14 200 | Core | Jefe de plataforma, de hecho | Socios activos. 16 100 según el core, 15 400 según prevención de lavado | Confidencial | Sí |
| Expediente de crédito | Carpetas compartidas · Core · Papel | 14 200 · 14 200 · 14 200 | El papel | Jefe de créditos | 1 900 descargados sin que quede registro | Restringida | Sí, sensibles |
| Trabajador | Planilla del proveedor · Usuarios del core · Biométrico | 96 · 75 · 96 | Planilla | Recursos Humanos | Cesados con usuario habilitado | Restringida | Sí |
| Operación | Core · Banca por internet · Reportes a la SBS | 1.1 millones al año | Core | Contabilidad | El reporte a la SBS se rehace a mano cuando cambia el formato | Confidencial | Sí |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor del core con réplica en la sede · servidor de prevención de lavado · servidor de archivos de expedientes · la nube del proveedor para la banca por internet · dos agencias conectadas por el enlace de un operador · 60 estaciones.

**Redes.** La sede tiene una red separada para cajas. Las agencias de Tarata y Locumba operan en red plana contra la sede.

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

