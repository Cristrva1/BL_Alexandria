[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 9. Diseño, UI & Frontend](09-dise-o-ui-frontend.md) · [11. Generación de Imagen & Visión ➡️](11-generaci-n-de-imagen-visi-n.md)

# 📊 10. Analítica & Visualización

> Analítica web y de producto, BI y dashboards, chat con tus datos, librerías de gráficos y apps de datos en Python.

**20 repos** · 5 subcategorías · ⭐ 883k estrellas en total · 🆕 11 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [Umami](../fichas/umami.md) | 40k | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | `docker compose up -d` |
| [Apache Superset](../fichas/superset.md) | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | `git clone https://github.com/apache/superset && cd superset && docker compose -f docker-compose-image-tag.yml up` |
| [WrenAI](../fichas/wrenai.md) | 18.1k | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | Descarga el lanzador de releases o usa Docker Compose del repo. |
| [Recharts](../fichas/recharts.md) | 27.7k | Librería de gráficos para React construida con D3, declarativa y componible. | `npm i recharts` |
| [Gradio](../fichas/gradio.md) | 44k | Librería Python para crear y compartir apps web de modelos de ML en minutos. | `pip install gradio` |
| [daily_stock_analysis](../fichas/daily-stock-analysis.md) | 69.5k | Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario. | Haz fork y configura los secretos para GitHub Actions, o ejecútalo con Docker siguiendo… |

## 🧭 Subcategorías

- [Analítica web y de producto](#analítica-web-y-de-producto) — 4 repos
- [BI, dashboards y chat con datos](#bi-dashboards-y-chat-con-datos) — 6 repos
- [Librerías de gráficos](#librerías-de-gráficos) — 5 repos
- [Apps de datos en Python](#apps-de-datos-en-python) — 3 repos
- [Recursos y casos de uso](#recursos-y-casos-de-uso) — 2 repos

## Analítica web y de producto

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Umami](../fichas/umami.md) 🆕 | 40k | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | quieres analítica web simple y privada | 🟢 |
| [posthog](../fichas/posthog.md) | 40.7k | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. | quieres entender el uso real y el comportamiento de usuarios | 🔴 |
| [Plausible Analytics](../fichas/plausible.md) 🆕 | 29.8k | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. | quieres analítica minimalista y privada | 🟡 |
| [Matomo](../fichas/matomo.md) 🆕 | 22k | Alternativa open source a Google Analytics con control total de los datos. | necesitas analítica completa como Google Analytics pero propia | 🟡 |

## BI, dashboards y chat con datos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Apache Superset](../fichas/superset.md) 🆕 | 75.5k | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | quieres BI empresarial abierto | 🟡 |
| ⭐ [WrenAI](../fichas/wrenai.md) 🆕 | 18.1k | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | quieres text-to-SQL confiable para el negocio | 🟡 |
| [Grafana](../fichas/grafana.md) 🆕 | 77.8k | Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. | necesitas monitoreo y alertas en tiempo real | 🟢 |
| [metabase](../fichas/metabase.md) | 50.3k | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | quieres BI accesible para perfiles no técnicos | 🟡 |
| [Redash](../fichas/redash.md) 🆕 | 28.9k | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. | tu equipo trabaja con SQL y quiere compartir rápido | 🟡 |
| [PandasAI](../fichas/pandas-ai.md) 🆕 | 23.9k | Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. | quieres preguntar a tus tablas en lenguaje natural | 🟢 |

## Librerías de gráficos

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Recharts](../fichas/recharts.md) 🆕 | 27.7k | Librería de gráficos para React construida con D3, declarativa y componible. | tu app es React y quieres gráficos declarativos | 🟢 |
| [D3.js](../fichas/d3.md) 🆕 | 114k | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. | necesitas visualizaciones totalmente personalizadas | 🟡 |
| [Chart.js](../fichas/chart-js.md) 🆕 | 67.8k | Librería JavaScript sencilla para gráficos HTML5 en canvas. | quieres gráficos simples sin aprender una librería compleja | 🟢 |
| [echarts](../fichas/echarts.md) | 67.7k | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | necesitas gráficos ricos y variados embebidos | 🟡 |
| [uPlot](../fichas/uplot.md) | 10.6k | Librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. | priorizas velocidad y peso del bundle | 🟢 |

## Apps de datos en Python

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Gradio](../fichas/gradio.md) | 44k | Librería Python para crear y compartir apps web de modelos de ML en minutos. | quieres una demo web de tu modelo rápido | 🟢 |
| [streamlit](../fichas/streamlit.md) | 46.3k | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | quieres una UI de datos al vuelo y prototipos rápidos | 🟢 |
| [dash](../fichas/dash.md) | 24.5k | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | quieres dashboards productivos en Python con control del frontend | 🟡 |

## Recursos y casos de uso

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [daily_stock_analysis](../fichas/daily-stock-analysis.md) | 69.5k | Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario. | quieres un análisis bursátil diario automatizado | 🟡 |
| [awesome-dataviz](../fichas/awesome-dataviz.md) | 4.5k | Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. | buscas opciones de visualización y aún no has elegido | 🟢 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### Umami, Plausible Analytics, Matomo

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Umami](../fichas/umami.md) | 40k | quieres analítica web simple y privada | necesitas analítica de producto avanzada; mira `posthog` |
| [Plausible Analytics](../fichas/plausible.md) | 29.8k | quieres analítica minimalista y privada | necesitas embudos y eventos complejos; mira `posthog` |
| [Matomo](../fichas/matomo.md) | 22k | necesitas analítica completa como Google Analytics pero propia | quieres algo simple; mira `umami` |

### Apache Superset, metabase, Redash

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Apache Superset](../fichas/superset.md) | 75.5k | quieres BI empresarial abierto | buscas algo muy fácil para no técnicos; mira `metabase` |
| [metabase](../fichas/metabase.md) | 50.3k | quieres BI accesible para perfiles no técnicos | necesitas analítica de eventos por usuario (posthog) |
| [Redash](../fichas/redash.md) | 28.9k | tu equipo trabaja con SQL y quiere compartir rápido | necesitas BI con permisos finos; mira `superset` |

### WrenAI, PandasAI

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [WrenAI](../fichas/wrenai.md) | 18.1k | quieres text-to-SQL confiable para el negocio | solo analizas un CSV; mira `pandas-ai` |
| [PandasAI](../fichas/pandas-ai.md) | 23.9k | quieres preguntar a tus tablas en lenguaje natural | necesitas text-to-SQL gobernado para la empresa; mira `wrenai` |

### Recharts, D3.js, Chart.js, echarts

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Recharts](../fichas/recharts.md) | 27.7k | tu app es React y quieres gráficos declarativos | no usas React; mira `chart-js` |
| [D3.js](../fichas/d3.md) | 114k | necesitas visualizaciones totalmente personalizadas | quieres gráficos estándar rápido; mira `chart-js` o `recharts` |
| [Chart.js](../fichas/chart-js.md) | 67.8k | quieres gráficos simples sin aprender una librería compleja | necesitas visualizaciones a medida; mira `d3` |
| [echarts](../fichas/echarts.md) | 67.7k | necesitas gráficos ricos y variados embebidos | solo series temporales simples y priorizas peso (uPlot) |

### Gradio, streamlit

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Gradio](../fichas/gradio.md) | 44k | quieres una demo web de tu modelo rápido | construyes una app de datos con varias páginas; mira `streamlit` |
| [streamlit](../fichas/streamlit.md) | 46.3k | quieres una UI de datos al vuelo y prototipos rápidos | necesitas una app productiva con control fino del frontend (dash) |

## 🧪 Recetas que usan esta categoría

- [📈 Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.
- [🌐 Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [📊 Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
