<div align="center">
  <img src="../../../Logos/logo_universidad.png" alt="Universidad Privada de Tacna" height="62">
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <img src="../../../Logos/logo_escuela_sistemas.jpeg" alt="Escuela Profesional de Ingeniería de Sistemas" height="62">
</div>

<p align="center">
  <strong>Universidad Privada de Tacna</strong><br>
  Facultad de Ingeniería · Escuela Profesional de Ingeniería de Sistemas
</p>

<h1 align="center">SERVICIOS MINEROS CORDILLERA S.A.C.</h1>

<p align="center">
  Banco de casos · <strong>Empresa 09</strong> · Servicios especializados a la gran minería<br>
  <em>Organización ficticia. Cualquier parecido con una empresa real es coincidencia.</em>
</p>

---

## A. Ficha de la organización

| Campo | Contenido |
|---|---|
| **Razón social** | SERVICIOS MINEROS CORDILLERA S.A.C. |
| **Sector** | Servicios especializados a la gran minería |
| **Domicilio fiscal** | Tacna, con campamento en Moquegua |
| **RUC** | 20603XXXXX *(enmascarado; es una organización ficticia)* |
| **Años de operación** | 12 |
| **Personal en planilla** | 421 |
| **Personal adicional** | Picos de 700 en paradas de planta |
| **Facturación / presupuesto anual** | S/ 96.8 millones |
| **Mercado o población atendida** | Dos operaciones mineras del sur |
| **Naturaleza** | Empresa privada. |
| **Entidades que la regulan o supervisan** | MINEM · OSINERGMIN · SUNAFIL · SUNAT · el propio cliente minero (auditorías de homologación) |

**Objetivo declarado para TI en el periodo.** Cerrar las observaciones de homologación del cliente y asegurar la continuidad del enlace.

## B. Estructura y gobierno

| | |
|---|---|
| **Personal de TI** | 5 personas |
| **Responsable de TI** | Superintendente de TI, reporta a Gerencia de Operaciones |
| **Comité de TI o de gobierno digital** | No existe. |
| **Política de seguridad de la información** | Existe desde 2022, sin difusión ni revisión posterior. |
| **Presupuesto de TI del periodo** | S/ 1 460 000 · 1.51 % de la facturación |

> **Sin marco de gobierno digital obligatorio.** Al ser privada, las exigencias provienen de su regulador sectorial, de la Ley 29733 de protección de datos personales y de sus compromisos contractuales.

## C. Sistemas de información

| Sistema | Descripción | Dónde corre | Desde | ¿Tiene soporte vigente? |
|---|---|---|---|---|
| **ERP corporativo** | Producto internacional, módulos de proyectos, compras y finanzas | Nube privada del proveedor | 2021 | Sí, con SLA |
| **Gestión de seguridad y salud ocupacional** | Producto especializado, obligatorio para el cliente | SaaS | 2020 | Sí |
| **Control de personal en campamento** | Biométrico más sistema del proveedor | Servidor en campamento | 2019 | Parcial |
| **Gestión de mantenimiento de equipos** | Módulo del ERP | Nube privada | 2021 | Sí |
| **Enlace de datos campamento–Tacna** | Radioenlace más respaldo satelital | Infraestructura propia | 2018 | Contrato con operador |

**El problema que la organización reconoce.** El cliente minero exige homologación anual con evidencia de controles de seguridad de la información. La última homologación se aprobó con nueve observaciones, ninguna cerrada.

## D. Procesos de negocio

| N.º | Proceso | ¿Qué sistema lo soporta? |
|---|---|---|
| 1 | Licitación y contratación con el cliente minero | ERP corporativo |
| 2 | Planificación y ejecución de servicios en operación | ERP corporativo |
| 3 | Gestión de seguridad y salud ocupacional | Gestión de seguridad y salud ocupacional |
| 4 | Control de personal y campamento | Control de personal en campamento |
| 5 | Mantenimiento de equipos | Gestión de mantenimiento de equipos |
| 6 | Facturación y valorizaciones | ERP corporativo |

## E. Instrumentos de planeamiento existentes

| Instrumento | ¿Existe? | Vigencia | Estado real |
|---|---|---|---|
| Plan estratégico o plan de negocio | Sí | 2023–2027 | Aprobado por resolución, se cumple parcialmente. |
| Plan operativo anual | Sí | 2025 | Se formula cada año para efectos presupuestales. |
| Plan Estratégico de Tecnologías de la Información (PETI) | **No** | — | **Nunca se ha formulado.** |
| Plan de transformación digital | No | — | No se ha formulado. |
| Política de seguridad de la información | Parcial | — | Existe desde 2022, sin difusión ni revisión posterior. |
| Plan de continuidad del negocio | No | — | No existe. El BIA de `datos/bia.csv` es un borrador incompleto elaborado por un practicante. |
| Catálogo de servicios de TI | No | — | Sin responsable asignado. |

## F. Situación de TI — hechos verificables para el diagnóstico

Son los hechos que la organización admite y que pueden darse por ciertos. Todo lo demás se pregunta en la entrevista.

| Aspecto | Situación verificada |
|---|---|
| **Registro de incidentes** | No se registra. Se resuelve y se olvida. |
| **Contratos con proveedores de TI** | Dos de los cinco contratos están vencidos y el servicio continúa. |
| **Inventario de activos de TI** | No existe. |
| **Respaldos** | Se ejecutan a un disco externo que permanece conectado al mismo servidor. |
| **Segundo factor de autenticación** | Solo en el correo corporativo. |
| **Capacitación en seguridad** | Nunca se ha hecho. |
| **Gestión de cambios** | Hay un formato de cambio que se llena después de aplicar el cambio. |
| **Contraseñas** | Las cuentas de administrador se comparten entre dos personas de TI. |

## G. El incidente del periodo

**Interrupción del enlace de campamento durante parada de planta**

El radioenlace principal falló durante una parada de planta programada. El respaldo satelital no estaba operativo porque su contrato había vencido nueve meses antes sin que nadie lo advirtiera. Se perdieron 14 horas de registro de avance, con penalidad contractual.

## H. Riesgos que la organización ya conoce y no ha tratado

| N.º | Riesgo conocido | ¿Tratado? |
|---|---|---|
| 1 | Observaciones de homologación del cliente sin cierre | No |
| 2 | Contratos de servicios críticos sin control de vencimiento | No |
| 3 | Enlace de comunicaciones sin redundancia efectiva | No |

## I. Datos entregados

Los siete archivos de `datos/` corresponden al periodo del 1 de enero al 31 de diciembre de 2025. Fueron generados con la semilla de esta empresa. **No coinciden con los de ningún otro equipo**.

| Archivo | Qué contiene | Registros |
|---|---|---|
| `pagos.csv` | Población de pagos del periodo — comprobante, fecha, proveedor, concepto, monto, quién registró y quién aprobó | 25 185 |
| `proveedores.csv` | Maestro de proveedores con su contacto y documento de identidad | 210 |
| `empleados.csv` | Planilla del periodo, con fechas de ingreso y cese | 420 |
| `usuarios_erp.csv` | Usuarios del ERP con su perfil, último acceso y estado | 267 |
| `bia.csv` | Análisis de impacto al negocio por proceso, con RTO, RPO y fecha de la última prueba | 6 |
| `presupuesto_ti.csv` | Presupuesto de TI del periodo por partida, planificado contra ejecutado | 7 |
| `inversiones_cerradas.csv` | Tres inversiones cerradas con su beneficio declarado y si se midió | 3 |

---

**Docente** · Dr. Oscar Juan Jimenez Flores
[oscarjimenezflores@upt.pe](mailto:oscarjimenezflores@upt.pe) · [LinkedIn](https://www.linkedin.com/in/oscar-jimenez-flores/) · [CTI Vitae — CONCYTEC](https://ctivitae.concytec.gob.pe/appDirectorioCTI/VerDatosInvestigador.do?id_investigador=33398)

Escuela Profesional de Ingeniería de Sistemas · Universidad Privada de Tacna · Tacna, Perú
