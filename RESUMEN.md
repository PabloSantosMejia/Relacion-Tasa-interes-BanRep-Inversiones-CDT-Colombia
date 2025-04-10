# Resumen Ejecutivo: Análisis de CDT y Tasas de Interés en Colombia

## Presentación del Proyecto

Este proyecto analiza la relación entre las tasas de interés del Banco de la República y las inversiones en Certificados de Depósito a Término (CDT) en Colombia durante el período 2017-2025. Utilizando técnicas de análisis estadístico y visualización de datos, el estudio examina patrones históricos, cuantifica relaciones y proyecta escenarios futuros para este importante instrumento del mercado financiero colombiano.

## Objetivo Principal

Determinar y cuantificar la influencia de las decisiones de política monetaria, expresadas a través de las tasas de interés de referencia, sobre el comportamiento de las inversiones en CDT en Colombia, con el fin de comprender la dinámica de este mercado y proyectar su evolución futura bajo diferentes escenarios.

## Metodología

El análisis emplea:
- Regresión lineal para modelar la relación entre tasas e inversiones
- Análisis de series temporales para identificar tendencias y ciclos
- Técnicas de visualización avanzada para representar patrones complejos
- Proyecciones basadas en modelos estadísticos para escenarios 2025-2026

El proyecto utiliza datos de la Superintendencia Financiera, informes bancarios, DANE y el Banco de la República, analizados mediante Python con bibliotecas especializadas como pandas, matplotlib y scipy.

## Principales Hallazgos

1. **Correlación positiva significativa**: Los datos confirman una fuerte correlación (r = 0.764) entre tasas de interés e inversiones en CDT.

2. **Cuantificación precisa**: Por cada punto porcentual de cambio en la tasa de interés, se observa un impacto de aproximadamente 6.12 billones de pesos en inversiones en CDT.

3. **Ciclo completo observado**: El análisis captura desde tasas históricamente bajas (1.88% en 2021) hasta máximos recientes (12.63% en 2023), permitiendo observar la respuesta del mercado en diferentes contextos.

4. **Efectos rezagados identificados**: Los máximos en inversiones en CDT se alcanzaron aproximadamente 6-9 meses después del pico en tasas de interés.

5. **Contracción acelerada reciente**: El primer trimestre de 2025 muestra una caída significativa (-9.23%) en CDT, coincidiendo con reducciones agresivas en tasas.

## Proyecciones y Escenarios

Bajo el escenario base (tasa del 5.00% para finales de 2026), se proyecta una contracción total del 26.0% en inversiones en CDT desde su máximo histórico, llegando a aproximadamente 175.2 billones de pesos.

Escenarios alternativos:
- **Reducción acelerada de tasas**: Contracción del 31.2%
- **Reducción pausada de tasas**: Contracción del 20.9%

## Implicaciones Prácticas

- **Para entidades financieras**: Necesidad de diversificar fuentes de fondeo ante la contracción proyectada en CDT.
- **Para inversionistas**: Oportunidad actual para asegurar rendimientos con CDT a plazos medios, antes de que continúe el ciclo de reducción de tasas.
- **Para reguladores**: Importancia de monitorear la estabilidad del sistema financiero durante esta fase de transición.

## Enlaces y Recursos

### Repositorio

- **Repositorio GitHub**: [Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia](https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia)

### Visualizaciones Principales

#### Evolución Histórica: CDT vs Tasas de Interés (2017-2025)

<img src="https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia/blob/main/imagenes/serie_temporal_combinada.png" alt="Evolución de CDT y Tasas de Interés" width="600"/>

*La gráfica muestra la clara correlación entre el ciclo de tasas de interés y las inversiones en CDT, incluyendo el impacto de la pandemia en 2020, el período de tasas bajas en 2021, y el posterior ciclo de aumento y reducción de tasas.*

#### Análisis de Correlación y Modelo de Regresión

<img src="https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia/blob/main/imagenes/correlacion_cdt_tasas.png" alt="Correlación entre CDT y Tasas" width="600"/>

*El diagrama de dispersión evidencia la correlación positiva significativa (r = 0.764) entre tasas e inversiones. La línea de regresión representa el modelo CDT = 6.12 × Tasa + 144.58, que explica el 58.4% de la variabilidad observada.*

#### Análisis del Período Reciente (2023-2025)

<img src="https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia/blob/main/imagenes/analisis_reciente.png" alt="Análisis del Período Reciente" width="600"/>

*Esta visualización muestra en detalle la variación mensual reciente de CDT y su relación con los cambios en tasas de interés, destacando la aceleración de la contracción en el primer trimestre de 2025.*

#### Proyección de CDT y Tasas (2025-2026)

<img src="https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia/blob/main/imagenes/proyeccion_2026.png" alt="Proyección 2025-2026" width="600"/>

*La proyección muestra la trayectoria esperada de CDT y tasas hasta finales de 2026, con una reducción gradual de tasas hasta 5.00% y la consiguiente contracción en inversiones.*

#### Escenarios Alternativos para 2026

<img src="https://github.com/PabloSantosMejia/Relacion-Tasa-interes-BanRep-Inversiones-CDT-Colombia/blob/main/imagenes/escenarios_alternativos.png" alt="Escenarios Alternativos" width="600"/>

*Comparación de diferentes escenarios para 2026 basados en distintas trayectorias de reducción de tasas, mostrando la contracción proyectada en cada caso.*

### Fuentes de Datos

- [Banco de la República - Tasas de Interés](https://www.banrep.gov.co/es/estadisticas/tasas-de-interes)
- [Superintendencia Financiera de Colombia - Estadísticas](https://www.superfinanciera.gov.co/inicio/informes-y-cifras/cifras/establecimientos-de-credito/informacion-periodica/mensual/evolucion-cdt-61326)
- [DANE - Información Estadística](https://www.dane.gov.co/index.php/estadisticas-por-tema/cuentas-nacionales)


---

*Nota: Este proyecto demuestra el uso de técnicas avanzadas de análisis de datos para comprender la dinámica del mercado financiero colombiano, específicamente la relación entre política monetaria e inversiones en CDT.*
