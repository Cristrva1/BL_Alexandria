[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Analizar datos, crear dashboards y mapas

Herramientas para explorar datos, crear gráficos, medir productos y visualizar fuentes abiertas. El chat con datos sí puede añadir un modelo; un gráfico convencional no lo necesita.

23 repos · 6 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Umami](../fichas/umami.md) | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | Sin API de IA en la ruta básica |
| [Apache Superset](../fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | Sin API de IA en la ruta básica |
| [WrenAI](../fichas/wrenai.md) | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | Depende de la ruta elegida |
| [Recharts](../fichas/recharts.md) | Librería de gráficos para React construida con D3, declarativa y componible. | Sin API de IA en la ruta básica |
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | Sin API de IA en la ruta básica |

## Secciones

- [Analítica web y de producto](#analítica-web-y-de-producto) — 4 repos
- [BI, dashboards y chat con datos](#bi-dashboards-y-chat-con-datos) — 6 repos
- [Librerías de gráficos](#librerías-de-gráficos) — 5 repos
- [Apps de datos en Python](#apps-de-datos-en-python) — 3 repos
- [Recursos y casos de uso](#recursos-y-casos-de-uso) — 3 repos
- [Inteligencia de fuentes abiertas y mapas](#inteligencia-de-fuentes-abiertas-y-mapas) — 2 repos

## Analítica web y de producto

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Umami](../fichas/umami.md) | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | quieres analítica web simple y privada | Sin API de IA en la ruta básica |
| [posthog](../fichas/posthog.md) | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. | quieres entender el uso real y el comportamiento de usuarios | Sin API de IA en la ruta básica |
| [Plausible Analytics](../fichas/plausible.md) | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. | quieres analítica minimalista y privada | Sin API de IA en la ruta básica |
| [Matomo](../fichas/matomo.md) | Alternativa open source a Google Analytics con control total de los datos. | necesitas analítica completa como Google Analytics pero propia | Sin API de IA en la ruta básica |

## BI, dashboards y chat con datos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Apache Superset](../fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | quieres BI empresarial abierto | Sin API de IA en la ruta básica |
| [WrenAI](../fichas/wrenai.md) | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | quieres text-to-SQL confiable para el negocio | Depende de la ruta elegida |
| [Grafana](../fichas/grafana.md) | Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. | necesitas monitoreo y alertas en tiempo real | Sin API de IA en la ruta básica |
| [metabase](../fichas/metabase.md) | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | quieres BI accesible para perfiles no técnicos | Sin API de IA en la ruta básica |
| [Redash](../fichas/redash.md) | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. | tu equipo trabaja con SQL y quiere compartir rápido | Sin API de IA en la ruta básica |
| [PandasAI](../fichas/pandas-ai.md) | Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. | quieres preguntar a tus tablas en lenguaje natural | Depende de la ruta elegida |

## Librerías de gráficos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Recharts](../fichas/recharts.md) | Librería de gráficos para React construida con D3, declarativa y componible. | tu app es React y quieres gráficos declarativos | Sin API de IA en la ruta básica |
| [D3.js](../fichas/d3.md) | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. | necesitas visualizaciones totalmente personalizadas | Sin API de IA en la ruta básica |
| [Chart.js](../fichas/chart-js.md) | Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. | quieres gráficos simples sin aprender una librería compleja | Sin API de IA en la ruta básica |
| [echarts](../fichas/echarts.md) | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | necesitas gráficos ricos y variados embebidos | Sin API de IA en la ruta básica |
| [uPlot](../fichas/uplot.md) | Librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. | priorizas velocidad y peso del bundle | Sin API de IA en la ruta básica |

## Apps de datos en Python

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Gradio](../fichas/gradio.md) | Librería Python para crear y compartir apps web de modelos de ML en minutos. | quieres una demo web de tu modelo rápido | Sin API de IA en la ruta básica |
| [streamlit](../fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | quieres una UI de datos al vuelo y prototipos rápidos | Sin API de IA en la ruta básica |
| [dash](../fichas/dash.md) | Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. | quieres dashboards productivos en Python con control del frontend | Sin API de IA en la ruta básica |

## Recursos y casos de uso

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [awesome-dataviz](../fichas/awesome-dataviz.md) | Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. | buscas opciones de visualización y aún no has elegido | Sin API de IA en la ruta básica |
| [data-analyst-roadmap](../fichas/data-analyst-roadmap.md) | Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. | quieres ordenar un plan de aprendizaje para análisis de datos | Sin API de IA en la ruta básica |
| [DataAnalystPortfolioProjects](../fichas/dataanalystportfolioprojects.md) | Portafolio de ejemplos de análisis de datos con SQL, Python, Tableau, Excel y Hive. | quieres consultar ejemplos para construir tu propio portafolio de análisis | Sin API de IA en la ruta básica |

## Inteligencia de fuentes abiertas y mapas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [osiris](../fichas/osiris.md) | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. | quieres visualizar varias fuentes de actualidad en un mapa | Sin API de IA en la ruta básica |
| [Pythia](../fichas/pythia.md) | Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. | quieres explorar fuentes OSINT y escenarios desde un panel local | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.
- [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
