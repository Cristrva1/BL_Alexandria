# echarts vs uplot

Generado: 2026-06-23T16:56:54.761958+00:00

| Criterio | echarts | uPlot |
|---|---|---|
| Uso real | librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. |
| Elegir si | necesitas gráficos ricos | priorizas velocidad/peso |
| Evitar si | solo series temporales simples ([uPlot](#-uplot)). | necesitas tipos de gráfico variados ([echarts](#-echarts)). |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `echarts` si su caso de uso encaja mejor ahora. Deja `uplot` como alternativa, salvo que el proyecto necesite explicitamente ambos.
