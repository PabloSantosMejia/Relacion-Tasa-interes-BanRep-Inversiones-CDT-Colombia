# Análisis de la Relación entre Tasas de Interés y CDT en Colombia

Este repositorio contiene un análisis detallado sobre la relación entre las tasas de interés del Banco de la República de Colombia y las inversiones en Certificados de Depósito a Término (CDT) durante el período 2017-2025 Marzo.

## Descripción del Proyecto

Este proyecto realiza un análisis cuantitativo sobre el impacto de la política monetaria en el mercado de CDT en Colombia. El análisis examina datos históricos de los últimos 8 años, identificando patrones, relaciones estadísticas y puntos de inflexión significativos. El estudio no solo caracteriza la relación entre tasas de interés e inversiones en CDT, sino que también desarrolla un modelo predictivo para proyectar escenarios futuros.

La investigación identifica cuatro fases distintivas en la evolución del mercado de CDT y analiza con especial detalle el período más reciente (2023-2025), durante el cual se observaron tanto el máximo histórico de inversiones como el inicio de una fase de contracción significativa.

## Objetivo

**¿Cuál es la relación entre la tasa de interés del Banco de la República y las inversiones en CDT?**

El objetivo principal de este análisis es determinar la existencia, magnitud y características de la relación entre las tasas de interés establecidas por el Banco de la República y los montos de inversión en CDT en Colombia. Específicamente, se busca:

1. Cuantificar la correlación entre ambas variables
2. Desarrollar un modelo que permita estimar el impacto de cambios en tasas sobre las inversiones en CDT
3. Identificar patrones temporales y efectos rezagados
4. Proyectar la evolución futura del mercado bajo diferentes escenarios de política monetaria

## Conclusiones

1. **Correlación positiva significativa**: Los datos confirman una fuerte correlación positiva (r = 0.764) entre las tasas de interés y las inversiones en CDT, con un coeficiente de determinación (R²) de 0.584.

2. **Relación cuantificable**: Por cada punto porcentual de cambio en la tasa de interés del BanRep, se observa un impacto de aproximadamente 6.12 billones de pesos en el monto total de inversiones en CDT.

3. **Ciclo completo observado**: El análisis captura un ciclo completo de política monetaria, desde tasas históricamente bajas (1.88% en 2021) hasta máximos recientes (12.63% en 2023), permitiendo observar la respuesta del mercado en diferentes contextos.

4. **Efectos rezagados**: Los máximos en inversiones en CDT (236.9 billones COP en junio 2024) se alcanzaron aproximadamente 6-9 meses después del pico en tasas de interés, evidenciando un efecto rezagado.

5. **Contracción acelerada reciente**: El primer trimestre de 2025 muestra una contracción significativa (-9.23%) en CDT, coincidiendo con reducciones agresivas en tasas (125 puntos básicos en tres meses).

6. **Proyecciones**: Bajo el escenario base (tasa del 5.00% para finales de 2026), se proyecta una contracción total del 26.0% en inversiones en CDT desde su máximo histórico.

## Herramientas y Habilidades Utilizadas

### Lenguaje y Bibliotecas
- **Python**: Lenguaje principal de programación
- **pandas**: Manipulación y análisis de datos
- **numpy**: Operaciones numéricas y matrices
- **matplotlib** y **seaborn**: Visualización avanzada de datos
- **scipy**: Análisis estadístico y regresión lineal

### Técnicas Aplicadas
- **Análisis de Series Temporales**: Identificación de tendencias, estacionalidad y puntos de inflexión
- **Regresión Lineal**: Modelamiento de relaciones estadísticas
- **Visualización de Datos**: Creación de gráficos informativos y representaciones claras
- **Análisis Predictivo**: Proyección de escenarios futuros basado en modelos estadísticos
- **Análisis de Correlación**: Evaluación cuantitativa de relaciones entre variables
- **Interpretación Económica**: Contextualización de resultados en el marco de la política monetaria

## Estructura del Repositorio

- `RESEUME.md`: Resumen ejecutivo del proyecto.
- `cdt_colombia_data.csv`: Dataset con información histórica de CDT y tasas de interés.
- `analisis_cdt_colombia.py`: Script de Python para el análisis y generación de visualizaciones.
- `analisis_completo_CDT_tasa_BanRep.pdf`: Informe PDF con el analsis integral y los hallazgos.
- `imagenes/`: Carpeta que contiene las visualizaciones generadas una vez se corre el Script
- `README.md`: Este archivo, con la documentación del proyecto.

## Requisitos e Instalación

Para ejecutar el análisis se requieren las siguientes librerías de Python:

```
pandas
numpy
matplotlib
seaborn
scipy
```

Puede instalar todas las dependencias con:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar el análisis completo:

```bash
python analisis_cdt_colombia.py
```

El script generará todas las visualizaciones en la carpeta `imagenes/` y mostrará los resultados principales en la consola.

## Fuentes de Datos

- Superintendencia Financiera de Colombia
- Informes Bancarios Agregados
- DANE/Informes Económicos
- Banco de la República de Colombia

## Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.

## Contacto

Para cualquier consulta o sugerencia relacionada con este análisis, por favor abra un issue en este repositorio.

---

*Nota: Los datos utilizados incluyen información real hasta marzo 2025 y proyecciones basadas en modelos econométricos. Las condiciones futuras del mercado podrían variar en función de factores macroeconómicos y decisiones de política monetaria.*
