<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">CADENA DE FARMACIAS BUENA SALUD E.I.R.L.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 10</strong> · Retail farmacéutico · 23 locales<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | CADENA DE FARMACIAS BUENA SALUD E.I.R.L. |
| **Sector** | Retail farmacéutico · 23 locales |
| **Domicilio fiscal** | Tacna, Moquegua e Ilo |
| **RUC** | 20577XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 15 |
| **Personal en planilla** | 196 |
| **Personal adicional** | 28 químicos farmacéuticos por turnos |
| **Facturación / presupuesto anual** | S/ 42.3 millones |
| **Mercado o población atendida** | Tacna, Moquegua e Ilo |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | DIGEMID · DIRESA · SUNAT · INDECOPI · ANPD |

**Objetivo declarado para TI en el periodo.** Eliminar la dependencia de una sola persona y cumplir la trazabilidad exigida por DIGEMID.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 3 personas |
| **Responsable de TI** | Jefe de Sistemas, reporta a Gerencia General. Es el único con conocimiento del sistema de puntos de venta |
| **Comité de TI o de gobierno digital** | Existe en el papel; no se ha reunido en el último año. |
| **Política de seguridad de la información** | En borrador desde hace dos años; nunca se aprobó. |
| **Presupuesto de TI del periodo** | S/ 468 000 · 1.11 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **Punto de venta y stock** | Producto del rubro farmacia, instalado local por local | Servidor por local, consolidación nocturna | 2016 | Sí |
| **Consolidación central** | Proceso nocturno por archivos, desarrollo propio | Servidor central | 2016 | No, lo mantiene el jefe de sistemas |
| **Programa de fidelización** | Módulo del proveedor del POS | Nube del proveedor | 2021 | Sí |
| **Compras y distribución a locales** | Hojas de cálculo y correo | — | — | No |
| **Receta digital y control de estupefacientes** | Libro físico foliado, exigido por DIGEMID | Papel | — | — |

**El problema que la organización reconoce.** La consolidación nocturna falla en promedio dos veces por semana y nadie más que el jefe de sistemas sabe reprocesarla. Cuando falla, el stock central queda desactualizado y se compra de más.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Compras a laboratorios y droguerías | Compras y distribución a locales |
| 2 | Distribución a los 23 locales | Compras y distribución a locales |
| 3 | Venta y dispensación | Punto de venta y stock |
| 4 | Control de productos controlados | Receta digital y control de estupefacientes |
| 5 | Fidelización de clientes | Programa de fidelización |
| 6 | Cierre de caja y consolidación | Consolidación central |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado, pero no se ha revisado desde su aprobación. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | Parcial | — | En borrador desde hace dos años; nunca se aprobó. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Segundo factor de autenticación** | Solo en el correo corporativo. |
| **Inventario de activos de TI** | Existe una hoja de cálculo actualizada por última vez hace dos años. |
| **Respaldos** | Existen respaldos programados, pero tres de los sistemas quedaron fuera del alcance sin que nadie lo advirtiera. |
| **Contratos con proveedores de TI** | No hay control de vencimientos; se detectan cuando el proveedor deja de responder. |
| **Gestión de cambios** | Hay un formato de cambio que se llena después de aplicar el cambio. |
| **Contraseñas** | Hay política escrita desde hace cuatro años, pero el sistema principal no la puede exigir técnicamente. |
| **Capacitación en seguridad** | Se hizo una charla de una hora en la inducción, hace tres años. |
| **Registro de incidentes** | No se registra. Se resuelve y se olvida. |

## G. El incidente del periodo

**Diferencia de inventario en productos controlados**

Un cruce entre el libro físico de estupefacientes y el sistema arrojó una diferencia de 214 unidades en cuatro locales durante 2025. DIGEMID puede sancionar. No hay forma de reconstruir el movimiento porque el POS no conserva el detalle más allá de 90 días.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Dependencia crítica de una sola persona | No |
| 2 | Retención de datos insuficiente frente a la exigencia regulatoria | No |
| 3 | Datos de salud de clientes en el programa de fidelización sin base legal declarada | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 11 014 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 98 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 196 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 132 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| [`presupuesto_ti.csv`](presupuesto_ti.csv) | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| [`inversiones_cerradas.csv`](inversiones_cerradas.csv) | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
