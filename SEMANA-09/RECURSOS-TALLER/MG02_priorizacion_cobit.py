# 04_normativa/MG02_priorizacion_cobit.py
import pandas as pd

# Los 40 objetivos con su relevancia estimada según los factores de diseño de ESTA organización.
# La relevancia se justifica en la columna 'fundamento', trazada al diagnóstico.
OBJ = pd.DataFrame([
 # dominio, código, nombre, relevancia 1-5, fundamento
 ("EDM","EDM01","Marco de gobierno establecido y mantenido",        5,"F4: no existe comité de TI; decisiones informales"),
 ("EDM","EDM02","Entrega de beneficios asegurada",                  4,"F4: inversiones sin medición de beneficio"),
 ("EDM","EDM03","Optimización del riesgo asegurada",                5,"F3: perfil de riesgo alto; sin apetito declarado"),
 ("EDM","EDM04","Optimización de recursos asegurada",               3,"F11: organización pequeña, presupuesto acotado"),
 ("EDM","EDM05","Compromiso con las partes interesadas",            3,"F1: enfoque de servicio al cliente"),
 ("APO","APO01","Marco de gestión de I&T",                          5,"F4: sin procedimientos ni roles definidos"),
 ("APO","APO02","Estrategia gestionada",                            5,"F1, F2: este PETI es el producto"),
 ("APO","APO03","Arquitectura empresarial gestionada",              4,"F4: sin documentación de arquitectura"),
 ("APO","APO05","Portafolio gestionado",                            4,"F4: sin priorización formal de la demanda"),
 ("APO","APO06","Presupuesto y costos gestionados",                 3,"F11: presupuesto asignado por Administración"),
 ("APO","APO07","Recursos humanos gestionados",                     5,"F4: dependencia crítica de una persona"),
 ("APO","APO08","Relaciones gestionadas",                           4,"F1: TI desconectada de las áreas usuarias"),
 ("APO","APO09","Acuerdos de servicio gestionados",                 4,"F4: sin catálogo ni niveles de servicio"),
 ("APO","APO10","Proveedores gestionados",                          5,"F8: contrato del ERP vencido; modelo híbrido"),
 ("APO","APO12","Riesgo gestionado",                                5,"F3: perfil de riesgo alto"),
 ("APO","APO13","Seguridad gestionada",                             5,"F6: requisitos de cumplimiento altos"),
 ("APO","APO14","Datos gestionados",                                5,"F4: sin gobierno del dato; ventaja no capturada"),
 ("BAI","BAI03","Identificación y construcción de soluciones",      3,"F9: desarrollo interno puntual"),
 ("BAI","BAI06","Cambios de TI gestionados",                        4,"F4: cambios sin control formal"),
 ("BAI","BAI07","Aceptación y transición del cambio",               4,"F4: despliegues sin aceptación del usuario"),
 ("BAI","BAI09","Activos gestionados",                              4,"F4: inventario desactualizado"),
 ("BAI","BAI10","Configuración gestionada",                         4,"F4: sin línea base de configuración"),
 ("BAI","BAI11","Proyectos gestionados",                            3,"F11: pocos proyectos simultáneos"),
 ("DSS","DSS01","Operaciones gestionadas",                          4,"F7: rol de fábrica; la operación depende de TI"),
 ("DSS","DSS02","Solicitudes e incidentes gestionados",             5,"F4: sin mesa de servicio ni registro"),
 ("DSS","DSS03","Problemas gestionados",                            3,"Incidentes recurrentes sin análisis de causa"),
 ("DSS","DSS04","Continuidad gestionada",                           5,"F3: sin BCP; servidor único; sin prueba de restauración"),
 ("DSS","DSS05","Servicios de seguridad gestionados",               5,"F6: cumplimiento alto"),
 ("DSS","DSS06","Controles de procesos de negocio gestionados",     3,"F1: enfoque de servicio"),
 ("MEA","MEA01","Desempeño y conformidad gestionados",              4,"F4: TI no reporta indicadores a la dirección"),
 ("MEA","MEA02","Sistema de control interno gestionado",            3,"F11: organización pequeña"),
 ("MEA","MEA03","Cumplimiento de requisitos externos gestionado",   5,"F6: requisitos altos; matriz Sección 4.1"),
 ("MEA","MEA04","Aseguramiento gestionado",                         2,"F11: sin auditoría interna"),
], columns=["dominio","codigo","nombre","relevancia","fundamento"])

OBJ = OBJ.sort_values("relevancia", ascending=False)
OBJ.to_csv("MG02_objetivos_priorizados.csv", index=False)

print("=== OBJETIVOS COBIT PRIORIZADOS (relevancia 5 = crítica) ===")
print(OBJ[OBJ.relevancia >= 5][["codigo","nombre","fundamento"]].to_string(index=False))
print(f"\nCon relevancia 5: {(OBJ.relevancia==5).sum()} objetivos")
print(f"Con relevancia 4: {(OBJ.relevancia==4).sum()} objetivos")
print(f"Alcance recomendado del PETI: los {(OBJ.relevancia>=4).sum()} objetivos con relevancia ≥ 4")
print(f"\nDistribución por dominio:\n{OBJ[OBJ.relevancia>=4].dominio.value_counts().to_string()}")
