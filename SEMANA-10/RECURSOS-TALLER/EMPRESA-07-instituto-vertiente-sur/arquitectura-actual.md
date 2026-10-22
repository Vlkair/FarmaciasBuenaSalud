<div align="center">
  <strong>INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR</strong><br>
  <em>Documento del caso</em>
</div>

---

# Inventario de la arquitectura actual

| | |
|---|---|
| **Organización** | INSTITUTO SUPERIOR TECNOLÓGICO VERTIENTE SUR |
| **Documento** | Inventario de la arquitectura actual |
| **Entregado por** | Tecnologías de la Información, a pedido del equipo |
| **Fecha de entrega** | 16 de julio de 2026 |
| **Clasificación** | Restringido |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## 1. Qué es este documento

Es lo que el área de tecnologías de la información entrega cuando se le pide **cómo están armados sus sistemas**. No existía. Se armó a pedido del equipo con lo que el área sabe, y el propio jefe advierte que «faltan cosas que solo están en la cabeza de alguien».

## 2. Aplicaciones que operan

Los sistemas de la ficha, más **las hojas de cálculo que operan como sistema**. El área reconoce que sin ellas la organización no funciona.

| Aplicación | Qué es | Dónde corre | ¿Tiene soporte vigente? |
|---|---|---|---|
| **Sistema académico** | Producto para institutos, matrícula, notas y certificados | Servidor propio | Sí |
| **Aula virtual** | Moodle autoalojado | Servidor propio | Administrado por un docente |
| **Cobranzas y tesorería** | Módulo del sistema académico | Mismo servidor | Sí |
| **Correo y ofimática** | Suite en nube, licencias educativas | Nube | Proveedor |
| **Biblioteca** | Software libre, instalado en 2018 | PC de biblioteca | No |
| **Hoja de cálculo · Carga docente** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Seguimiento de deserción, de bienestar estudiantil** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |
| **Hoja de cálculo · Inventario de biblioteca** | Libro de cálculo que un área mantiene por su cuenta | PC del área o carpeta compartida | No |

## 3. Qué sistema soporta cada proceso

| Proceso de negocio | Sistema que lo soporta |
|---|---|
| Admisión y matrícula | Sistema académico |
| Programación académica y carga docente | Sistema académico |
| Registro de evaluaciones y actas | Sistema académico |
| Cobranza de pensiones | Cobranzas y tesorería |
| Titulación y certificación | Sistema académico |
| Bienestar y seguimiento estudiantil | Aula virtual |

## 4. Integraciones entre sistemas

| De | A | Cómo se integra hoy |
|---|---|---|
| Sistema académico | Aula virtual | Carga manual por lotes, por el docente administrador |
| Sistema académico | Cobranzas | Módulo del mismo producto |
| Sistema académico | Correo en nube | Ninguna. Las cuentas se crean a mano |
| Biblioteca | Nadie | Ninguna |

## 5. Entidades de datos y dónde viven

Lo que el área pudo reconstruir. Los conteos son los que cada sistema devuelve hoy; cuando no coinciden, el área no sabe cuál es el bueno.

| Entidad | Sistemas donde reside | Registros por sistema | ¿Fuente autoritativa declarada? | Dueño del dato, por cargo | Discrepancia que el área conoce | Clasificación | ¿Datos personales? |
|---|---|---|---|---|---|---|---|
| Estudiante | Sistema académico · Aula virtual · Cobranzas · Libro de bienestar | 3 240 · 3 600 usuarios · 3 240 · 180 casos | Sistema académico, declarada | Secretaría académica | 360 usuarios del aula virtual sin matrícula vigente | Restringida | Sí, con menores de edad |
| Nota y acta | Sistema académico · Calificaciones del aula virtual · Papel | por curso y ciclo | Sistema académico | Ninguno por cargo | 17 notas alteradas fuera del periodo de registro | Restringida | Sí |
| Docente | Planilla · Sistema académico · Aula virtual | 88 en planilla · 112 por horas · 130 usuarios | Planilla | Recursos Humanos | Docentes de licencia con cuenta activa | Confidencial | Sí |
| Sección | Sistema académico · Aula virtual · Libro de carga docente | 410 · 450 · 410 | Ninguna | Coordinador de carrera | Secciones duplicadas en el aula virtual | Interna | No |

## 6. Nodos, dispositivos y redes

**Nodos.** Servidor propio del sistema académico y de cobranzas · servidor propio del aula virtual, administrado por un docente · suite de correo en nube · PC de biblioteca · tres laboratorios de 25 equipos y 30 estaciones administrativas.

**Redes.** Una sola red compartida entre administración, laboratorios y estudiantes. Internet de un proveedor.

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

