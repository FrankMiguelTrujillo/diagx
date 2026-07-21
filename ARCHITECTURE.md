# Diagx — Decisiones de Arquitectura

## SOLID
- Cada tipo de problema (ventas, tráfico, gestión, reputación) vive en su propia
  clase detectora (GetLowSales, GetLowTraffic, GetManagement, GetBadReputation),
  cada una con una sola responsabilidad (SRP).
- Todas las clases detectoras cumplen el contrato `IssueDetector` (Protocol),
  lo que permite agregar detectores nuevos sin modificar `DiagxSession` (Open/Closed)
  y sustituir cualquiera sin romper el resto (Liskov).
- `DiagxSession` depende de la abstracción `IssueDetector`, no de las clases
  concretas — Dependency Inversion.

## Patrón Factory
- `create_detectors()` centraliza la instanciación de los 4 detectores a partir
  de los datos crudos de una empresa, para que quien arma la sesión de diagnóstico
  no necesite conocer las clases concretas.

## Patrón Strategy
- Los 4 detectores son implementaciones intercambiables del mismo contrato
  (`detect_issues() -> list[str]`), combinadas dinámicamente en `DiagxSession.run_diagnosis()`.

## Decisiones consideradas y descartadas
- Se evaluó reemplazar las clases detectoras por un diccionario de reglas
  (condición + mensaje). Se descartó por ahora porque las clases son más legibles
  para lógica de negocio compleja, aunque el diccionario sería preferible si las
  reglas necesitaran cambiar sin re-desplegar la aplicación (a revisar en Fase 2
  si se conecta a una fuente de configuración externa).