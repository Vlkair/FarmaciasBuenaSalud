# Paso E — Validación del diagnóstico (Taller S11)

## Comprobación 1 · Recorrido de dos servicios de principio a fin

Recorrido de gabinete, hecho con los documentos del caso (FICHA, mesa de servicio). No se observó a un usuario real.

| Servicio | Recorrido del usuario, etapa por etapa | ¿Debe acudir o llamar? | Nivel comprobado |
|---|---|---|:---:|
| S-02 Consulta de disponibilidad | 1) El cliente busca el producto en internet: la cadena no tiene web ni app (FICHA §C). 2) Llama al local. 3) El vendedor revisa el POS **del local**; no ve el stock de otros locales porque el central está desactualizado cuando falla la consolidación. 4) Le sugiere ir a otro local o llamar. | Sí, siempre | **0** |
| S-06 Copia de comprobante | 1) El cliente escribe un correo o llama. 2) Administración busca el comprobante en el POS. 3) Lo reenvía en PDF por correo (24 h). | No acude, pero depende de que alguien lo atienda a mano; no hay autoservicio | **2** |

Resultado: los dos niveles coinciden con los de `GD01`. S-06 no llega a 3 ni a 4 aunque el cliente no acuda, porque no hay autoservicio: el envío depende de una persona.

## Comprobación 2 · Cada eje con su evidencia

Se revisó cada fila de `GD03_ejes.csv`: las 27 tienen fuente y fecha. 21 citan un documento del caso (FICHA, mesa de servicio, usuarios_erp.csv, registro de datos) y 6 declaran «No se mide» con el motivo. El indicador «Incidentes registrados» se dejó en «No se mide» y no en 0, porque la ficha dice que no se registran: cero registros no es cero incidentes.

## Comprobación 3 · Una sola vez sobre documentos concretos

Los 15 documentos están nombrados en la columna «Detalle documentos» de GD01. Los 6 redundantes también están nombrados: DNI del afiliado, comprobante, reporte de stock, datos de planilla, orden de compra y el comprobante de S-06.

## Problemas y mejoras

| Problema | Qué se hizo | Pendiente |
|---|---|---|
| `GD04_madurez.py` cortaba mal los nombres de eje («Identida», «Segurida»): `str.split(". ")` toma el punto como expresión regular | Se corrigió con `split(". ", n=1, regex=False)` | — |
| 10 de 11 volúmenes son estimaciones | Cada uno lleva su supuesto en la columna «Fuente del volumen» | Validarlos en la entrevista con el docente |
| La matriz NO03 contaba 73 instalaciones sin licencia | Se recontó: la suite ofimática y el software contable son Libre/MIT y no requieren licencia. Quedan 68 (lector PDF 54, editor 6, diseño 5, cliente BD 3) | — |
| SQLAlchemy 2.1 usa `psycopg` (v3) por defecto | Se instaló `psycopg[binary]` | — |
| NO03 y MG03 se reconstruyeron con los documentos del caso para alimentar el tablero | Quedan en `04_normativa/` | Reemplazarlos por las versiones de las semanas 8 y 9 del equipo, si difieren |
| Las capturas del tablero se toman en Metabase | `GD07_crear_tablero_metabase.py` crea las 6 preguntas y el tablero por API | Tomar las capturas en el laboratorio |
