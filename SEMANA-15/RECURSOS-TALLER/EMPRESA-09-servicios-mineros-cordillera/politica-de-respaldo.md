<div align="center">
  <strong>SERVICIOS MINEROS CORDILLERA S.A.C.</strong><br>
  <em>Documento del caso</em>
</div>

---

# Política de respaldo y recuperación de la información

| | |
|---|---|
| **Organización** | SERVICIOS MINEROS CORDILLERA S.A.C. |
| **Documento** | Política de respaldo y recuperación de la información |
| **Entregado por** | Tecnologías de la Información |
| **Fecha de entrega** | 3 de julio de 2026 |
| **Clasificación** | Uso interno |

> Documento de una organización ficticia, elaborado para el curso. Cualquier parecido con una empresa real es coincidencia.

---

## Ficha del documento

| Campo | Contenido |
|---|---|
| Código | POL-TI-011 |
| Versión | 1.0 |
| Fecha de aprobación | 9 de abril de 2023 |
| Aprobado por | Gerencia de Administración y Finanzas |
| Próxima revisión programada | 17 de octubre de 2024 |
| ¿Se ha revisado? | **No** |
| ¿Se difundió al personal? | «Se envió por correo» |

## 1. Objetivo

Establecer los lineamientos para la generación, custodia y recuperación de las copias de seguridad de la información de la organización.

## 2. Alcance

Aplica a todos los sistemas de información de la organización.

## 3. Lineamientos

**3.1.** Se realizará una copia de seguridad **completa semanal** y copias **incrementales diarias** de todos los sistemas críticos.

**3.2.** Las copias se conservarán por un periodo mínimo de **doce meses**.

**3.3.** Se mantendrá **una copia fuera de las instalaciones** de la organización.

**3.4.** Se realizará una **prueba de restauración trimestral**, dejando constancia de su resultado.

**3.5.** El responsable de Tecnologías de la Información verificará **diariamente** la ejecución correcta de las copias.

**3.6.** Los medios de respaldo se **cifrarán** y su acceso se restringirá al personal autorizado.

**3.7.** Se mantendrá un **registro de las restauraciones** solicitadas y ejecutadas.

**3.8.** Los tiempos objetivo de recuperación se definirán en el **análisis de impacto al negocio**, que se actualizará anualmente.

## 4. Responsables

| Rol | Responsabilidad |
|---|---|
| Jefe de Tecnologías de la Información | Ejecución, verificación y custodia |
| Gerencia de Administración y Finanzas | Aprobación y provisión de recursos |
| Usuarios | Guardar la información en las unidades de red establecidas |

---

## 5. Análisis de impacto al negocio vigente

Elaborado por un practicante en abril de 2024. No fue revisado ni aprobado. Se entrega tal como está.

| ID | Proceso | Criticidad | RTO (h) | RPO (h) | Sistema de soporte | Responsable | Impacto a 24 h | Última prueba |
|---|---|---|---|---|---|---|---|---|
| BIA01 | Licitación y contratación con el cliente minero | Alta | 24 | 48 | ERP corporativo | Lucía Mamani Nina | Bajo | **Nunca** |
| BIA02 | Planificación y ejecución de servicios en operación | Alta | 72 | 48 | ERP corporativo | Miguel Apaza Medina | Alto | **Nunca** |
| BIA03 | Gestión de seguridad y salud ocupacional | Alta | 4 | 8 | Gestión de seguridad y salud ocupacional | Luis Colque Núñez | Alto | 2025-08-07 |
| BIA04 | Control de personal y campamento | Alta | 48 | 1 | Control de personal en campamento | Hugo Mamani Ancco | Alto | **Nunca** |
| BIA05 | Mantenimiento de equipos | Baja | 4 | 24 | Gestión de mantenimiento de equipos | Teresa Medina Torres | Medio | 2025-11-01 |
| BIA06 | Facturación y valorizaciones | Alta | 72 | 24 | ERP corporativo | Óscar Ilaquita Núñez | Bajo | 2025-01-02 |

> El archivo original está en [`bia.csv`](bia.csv).

## 6. Lo que la organización responde

| Pregunta | Respuesta |
|---|---|
| ¿Se cumple la prueba de restauración trimestral del punto 3.4? | «No se ha hecho. Se asume que el respaldo funciona porque termina sin error» |
| ¿Dónde está la copia fuera de las instalaciones del punto 3.3? | «El jefe de sistemas se lleva un disco los viernes» |
| ¿Los medios están cifrados, como pide el 3.6? | «El disco no. El respaldo en nube sí, según el proveedor» |
| ¿Existe el registro de restauraciones del punto 3.7? | «No se lleva» |
| ¿El BIA se actualiza anualmente, como pide el 3.8? | «Es el único que tenemos» |
| ¿Quién definió los RTO y RPO de la tabla? | «El practicante los propuso. Nadie los validó con las áreas» |
| ¿Existe un plan de continuidad del negocio? | «No» |

