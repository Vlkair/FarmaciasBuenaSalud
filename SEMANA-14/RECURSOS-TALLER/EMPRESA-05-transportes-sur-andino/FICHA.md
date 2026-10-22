<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">TRANSPORTES SUR ANDINO S.A.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 05</strong> · Transporte terrestre de pasajeros interprovincial<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | TRANSPORTES SUR ANDINO S.A. |
| **Sector** | Transporte terrestre de pasajeros interprovincial |
| **Domicilio fiscal** | Tacna, con terminales en Moquegua, Arequipa y Puno |
| **RUC** | 20232XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 27 |
| **Personal en planilla** | 268 |
| **Personal adicional** | Conductores en régimen mixto |
| **Facturación / presupuesto anual** | S/ 52.6 millones |
| **Mercado o población atendida** | Corredor sur: Tacna–Arequipa–Puno–Cusco |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | MTC · SUTRAN · SUNAT · ANPD · SUNAFIL |

**Objetivo declarado para TI en el periodo.** Recuperar el control del canal en línea e integrar la operación de venta, embarque y flota.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 4 personas |
| **Responsable de TI** | Jefe de Sistemas, reporta a Gerencia de Operaciones, no a Gerencia General |
| **Comité de TI o de gobierno digital** | Se reúne, pero no deja actas. |
| **Política de seguridad de la información** | No existe. |
| **Presupuesto de TI del periodo** | S/ 598 000 · 1.14 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **Venta de pasajes y manifiesto** | Producto del rubro, terminales en counter | Servidor central en Tacna | 2016 | Sí |
| **Venta en línea y app de pasajeros** | Desarrollo tercerizado en 2021 | Nube pública | 2021 | Contrato vencido |
| **GPS y control de flota** | Servicio del proveedor de rastreo | SaaS | 2019 | Sí |
| **Mantenimiento de unidades** | Hojas de cálculo compartidas | Drive corporativo | 2018 | No |
| **Planillas y control de descanso de conductores** | Sistema local | PC de RR. HH. | 2017 | No |

**El problema que la organización reconoce.** El control de horas de conducción y descanso —exigible por SUTRAN— se lleva en Excel y no cruza con el GPS. Una fiscalización de 2025 detectó inconsistencias en 23 manifiestos.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Programación de flota y rutas | GPS y control de flota |
| 2 | Venta de pasajes en counter y en línea | Venta de pasajes y manifiesto |
| 3 | Embarque y manifiesto de pasajeros | Venta de pasajes y manifiesto |
| 4 | Mantenimiento de unidades | Mantenimiento de unidades |
| 5 | Control de conductores y descansos | Planillas y control de descanso de conductores |
| 6 | Encomiendas y carga | Venta de pasajes y manifiesto |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado por resolución, se cumple parcialmente. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | No | — | No existe. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Registro de incidentes** | Existe un cuaderno físico en TI. |
| **Gestión de cambios** | Los cambios en producción se aplican directamente, sin registro ni aprobación. |
| **Segundo factor de autenticación** | No está habilitado en ningún sistema. |
| **Contraseñas** | Hay política escrita desde hace cuatro años, pero el sistema principal no la puede exigir técnicamente. |
| **Respaldos** | Existen respaldos programados, pero tres de los sistemas quedaron fuera del alcance sin que nadie lo advirtiera. |
| **Inventario de activos de TI** | Existe para equipos, no para sistemas ni para servicios contratados en nube. |
| **Contratos con proveedores de TI** | No hay control de vencimientos; se detectan cuando el proveedor deja de responder. |
| **Capacitación en seguridad** | Se envían correos de concientización que nadie confirma haber leído. |

## G. El incidente del periodo

**Venta duplicada de asientos en feriado largo**

El sistema de venta en línea y el de counter no comparten bloqueo de asiento. En el feriado de julio de 2025 se vendieron 78 asientos duplicados. Se resolvió con reembolsos y una crisis en terminal. El proveedor del sistema en línea no responde desde marzo.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Sistema en línea sin proveedor ni código fuente en poder de la empresa | No |
| 2 | Datos personales de pasajeros en un servicio sin contrato vigente | No |
| 3 | Sin control automatizado de jornada de conductores | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 13 694 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 134 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 268 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 183 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| [`presupuesto_ti.csv`](presupuesto_ti.csv) | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| [`inversiones_cerradas.csv`](inversiones_cerradas.csv) | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
