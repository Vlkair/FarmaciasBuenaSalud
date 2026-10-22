<div align="center">
  <strong>CADENA DE FARMACIAS BUENA SALUD E.I.R.L.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | CADENA DE FARMACIAS BUENA SALUD E.I.R.L. |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 8 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **Punto de venta y stock** | Producto del rubro farmacia, instalado local por local | Servidor por local, consolidación nocturna | Sí |
| **Consolidación central** | Proceso nocturno por archivos, desarrollo propio | Servidor central | No, lo mantiene el jefe de sistemas |
| **Programa de fidelización** | Módulo del proveedor del POS | Nube del proveedor | Sí |
| **Compras y distribución a locales** | Hojas de cálculo y correo | — | No |
| **Receta digital y control de estupefacientes** | Libro físico foliado, exigido por DIGEMID | Papel | — |
| **Hoja de cálculo · Compras y distribución a los locales, por correo** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Promociones, de marketing** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · El libro foliado de productos controlados, en papel** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Compras a laboratorios y droguerías | Compras y distribución a locales |
| Distribución a los 23 locales | Compras y distribución a locales |
| Venta y dispensación | Punto de venta y stock |
| Control de productos controlados | Receta digital y control de estupefacientes |
| Fidelización de clientes | Programa de fidelización |
| Cierre de caja y consolidación | Consolidación central |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Punto de venta de cada local | Consolidación central | Proceso nocturno por archivos, propio. Falla dos veces por semana |
| Punto de venta | Programa de fidelización | En línea con la nube del proveedor |
| Consolidación central | Compras | Manual, a un libro de cálculo |
| Libro de productos controlados | Punto de venta | Ninguna |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Stock por local | 23 puntos de venta · Consolidación central · Libro de compras | 4 100 productos por local · 94 300 · 4 100 | Cada punto de venta para su local; el central cuando no falla | Jefe de sistemas, de hecho | El stock central queda desactualizado dos días por semana | Interna | No |
| Cliente del programa | Programa de fidelización · Punto de venta · Libro de marketing | 61 000 · 61 000 · 61 000 | Programa de fidelización | Marketing | Medicamentos comprados exportados a un libro de cálculo | Restringida | Sí, de salud |
| Producto controlado | Libro foliado por local · Punto de venta | por local | El libro, por norma | Director técnico | 214 unidades de diferencia en cuatro locales | Restringida | No |
| Venta | Punto de venta · Consolidación · SUNAT | 1.9 millones de líneas al año | Punto de venta | Contabilidad | Días sin consolidar que SUNAT sí recibió | Confidencial | Sí |

## 6. Nodos, dispositivos y redes

**Nodos.** 23 servidores locales de punto de venta · un servidor central de consolidación · la nube del proveedor para la fidelización · dos PC por local y 15 estaciones centrales.

**Redes.** No hay red entre locales. Cada local tiene internet doméstico y transfiere archivos de noche.

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

