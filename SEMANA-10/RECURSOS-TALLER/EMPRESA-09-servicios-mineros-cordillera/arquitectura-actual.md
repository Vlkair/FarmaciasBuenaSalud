<div align="center">
  <strong>SERVICIOS MINEROS CORDILLERA S.A.C.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | SERVICIOS MINEROS CORDILLERA S.A.C. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 25 de junio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **ERP corporativo** | Producto internacional, módulos de proyectos, compras y finanzas | Nube privada del proveedor | Sí, con SLA |
| **Gestión de seguridad y salud ocupacional** | Producto especializado, obligatorio para el cliente | SaaS | Sí |
| **Control de personal en campamento** | Biométrico más sistema del proveedor | Servidor en campamento | Parcial |
| **Gestión de mantenimiento de equipos** | Módulo del ERP | Nube privada | Sí |
| **Enlace de datos campamento–Tacna** | Radioenlace más respaldo satelital | Infraestructura propia | Contrato con operador |
| **Hoja de cálculo · Programación de servicios, de operaciones** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Control de vencimiento de contratos** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Reportes de asistencia para el cliente, salida de la integración** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Licitación y contratación con el cliente minero | ERP corporativo |
| Planificación y ejecución de servicios en operación | ERP corporativo |
| Gestión de seguridad y salud ocupacional | Gestión de seguridad y salud ocupacional |
| Control de personal y campamento | Control de personal en campamento |
| Mantenimiento de equipos | Gestión de mantenimiento de equipos |
| Facturación y valorizaciones | ERP corporativo |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Control de personal en campamento | Sistema del proveedor | Integración propia, mantenida por correo con un exempleado |
| Sistema de personal | ERP | Archivo mensual |
| Seguridad y salud ocupacional | ERP | Ninguna |
| Enlace campamento–Tacna | Todo | Radioenlace con respaldo satelital vencido |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Personal en campamento | ERP · Biométrico · Seguridad y salud ocupacional · Planilla | 420 · hasta 700 en paradas · 480 · 420 | Ninguna | Operaciones, de hecho | El reporte al cliente difiere del biométrico | Restringida | Sí, sensibles |
| Equipo | Mantenimiento del ERP · Libro de operaciones · Registro del cliente | 310 · 310 · 290 | ERP | Superintendente de mantenimiento | Horas de equipo distintas entre ERP y libro | Interna | No |
| Contrato | Compras del ERP · Libro de contratos · Archivo legal en papel | 140 · 140 · 140 | Ninguna | Ninguno | El contrato satelital venció sin aviso | Confidencial | No |
| Servicio | Proyectos del ERP · Libro de operaciones · Informe al cliente | 36 al año | ERP | Gerente de operaciones | Horas facturables distintas en el informe y en el ERP | Confidencial | No |

## 6. Nodos, dispositivos y redes

**Nodos.** El ERP en la nube privada del proveedor · el SaaS de seguridad y salud ocupacional · un servidor en campamento para el biométrico · el radioenlace campamento–Tacna con respaldo satelital inoperativo · 90 estaciones en Tacna y 40 en campamento.

**Redes.** Dos redes, Tacna y campamento, unidas por el enlace. Sin redundancia efectiva.

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

