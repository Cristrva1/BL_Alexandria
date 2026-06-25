# uplot vs echarts

Generado: 2026-06-25T03:39:27.698706+00:00

| Criterio | uPlot | echarts |
|---|---|---|
| Uso real | librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. | Apache ECharts is a free, powerful charting and visualization library offering easy ways to add intuitive, interactive, and highly customizable charts to your commercial products. It is written in pure JavaScript and based on zrender , which is a whole new lightweight canvas library. |
| Elegir si | priorizas velocidad/peso | quieres apache echarts |
| Evitar si | necesitas tipos de gráfico variados ([echarts](#-echarts)). | ya tienes una herramienta equivalente o no encaja con tu stack actual |
| Instalacion | reference_only | reference_only |

## Regla practica

Elige `uplot` si su caso de uso encaja mejor ahora. Deja `echarts` como alternativa, salvo que el proyecto necesite explicitamente ambos.
