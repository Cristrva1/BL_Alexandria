[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Dashboards, analítica y mapas

Analítica web, BI, gráficos y herramientas geoespaciales. Medir visitas, consultar un negocio y procesar fotografías para crear mapas requieren piezas diferentes.

22 repos · 6 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [Umami](../fichas/umami.md) | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | Sin clave propia de API de IA en la ruta básica |
| [Apache Superset](../fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | Sin clave propia de API de IA en la ruta básica |
| [WrenAI](../fichas/wrenai.md) | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | Depende de la ruta elegida |
| [Recharts](../fichas/recharts.md) | Librería de gráficos para React construida con D3, declarativa y componible. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Analítica web y de producto](#analítica-web-y-de-producto) — 4 repos
- [BI, dashboards y chat con datos](#bi-dashboards-y-chat-con-datos) — 6 repos
- [Librerías de gráficos](#librerías-de-gráficos) — 5 repos
- [Recursos y casos de uso](#recursos-y-casos-de-uso) — 2 repos
- [Inteligencia de fuentes abiertas y mapas](#inteligencia-de-fuentes-abiertas-y-mapas) — 3 repos
- [Fotogrametría y mapas desde imágenes](#fotogrametría-y-mapas-desde-imágenes) — 2 repos

## Analítica web y de producto

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Umami](../fichas/umami.md) | Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. | Tu objetivo encaja con estos ejemplos: Medir visitas de una web; Comparar campañas mediante eventos propios | Sin clave propia de API de IA en la ruta básica |
| [posthog](../fichas/posthog.md) | Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. | Tu objetivo encaja con estos ejemplos: Entender abandono en un flujo de registro; Revisar errores y sesiones de una app | API de IA opcional |
| [Plausible Analytics](../fichas/plausible.md) | Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. | Tu objetivo encaja con estos ejemplos: Medir una web de contenido; Comparar conversiones de una landing | Sin clave propia de API de IA en la ruta básica |
| [Matomo](../fichas/matomo.md) | Alternativa open source a Google Analytics con control total de los datos. | Tu objetivo encaja con estos ejemplos: Gestionar analítica en servidor propio; Crear informes de comportamiento de una web | Sin clave propia de API de IA en la ruta básica |

## BI, dashboards y chat con datos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Apache Superset](../fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | Tu objetivo encaja con estos ejemplos: Explorar métricas de una base SQL; Compartir un dashboard interno | Sin clave propia de API de IA en la ruta básica |
| [WrenAI](../fichas/wrenai.md) | BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. | Tu objetivo encaja con estos ejemplos: Definir ingresos de forma consistente; Crear dashboards desde preguntas de negocio | Depende de la ruta elegida |
| [Grafana](../fichas/grafana.md) | Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. | Tu objetivo encaja con estos ejemplos: Observar consumo de un servicio; Compartir métricas de una operación | Sin clave propia de API de IA en la ruta básica |
| [metabase](../fichas/metabase.md) | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | Tu objetivo encaja con estos ejemplos: Explorar ventas sin escribir cada consulta SQL; Compartir un informe operativo | Sin clave propia de API de IA en la ruta básica |
| [Redash](../fichas/redash.md) | Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. | Tu objetivo encaja con estos ejemplos: Compartir consultas de negocio; Crear dashboards a partir de fuentes SQL | Sin clave propia de API de IA en la ruta básica |
| [PandasAI](../fichas/pandas-ai.md) | Librería para conversar con tus datos (SQL, CSV, Parquet) usando LLM. | Tu objetivo encaja con estos ejemplos: Explorar una tabla con lenguaje natural; Generar un gráfico desde una pregunta | Depende de la ruta elegida |

## Librerías de gráficos

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Recharts](../fichas/recharts.md) | Librería de gráficos para React construida con D3, declarativa y componible. | Tu objetivo encaja con estos ejemplos: Visualizar una serie de ventas; Comparar categorías en un dashboard React | Sin clave propia de API de IA en la ruta básica |
| [D3.js](../fichas/d3.md) | Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. | Tu objetivo encaja con estos ejemplos: Diseñar una visualización a medida; Explorar relaciones entre datos con interacción | Sin clave propia de API de IA en la ruta básica |
| [Chart.js](../fichas/chart-js.md) | Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. | Tu objetivo encaja con estos ejemplos: Añadir gráficos a una página sencilla; Comparar resultados por periodo | Sin clave propia de API de IA en la ruta básica |
| [echarts](../fichas/echarts.md) | Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. | Tu objetivo encaja con estos ejemplos: Construir un dashboard interactivo; Combinar mapa y estadísticas en una web | Sin clave propia de API de IA en la ruta básica |
| [uPlot](../fichas/uplot.md) | Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a renderizar datos con Canvas y controles programables. | Tu objetivo encaja con estos ejemplos: Mostrar métricas temporales de un sensor; Comparar rendimiento de gráficas con tus propios datos | Sin clave propia de API de IA en la ruta básica |

## Recursos y casos de uso

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [awesome-dataviz](../fichas/awesome-dataviz.md) | Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. | Tu objetivo encaja con estos ejemplos: Encontrar una biblioteca de mapas; Comparar gráficos para React y JavaScript | Sin clave propia de API de IA en la ruta básica |
| [data-analyst-roadmap](../fichas/data-analyst-roadmap.md) | Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. | Tu objetivo encaja con estos ejemplos: Organizar un plan inicial de estudio; Identificar conocimientos para un primer proyecto | Sin clave propia de API de IA en la ruta básica |

## Inteligencia de fuentes abiertas y mapas

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [gods-eye-view](../fichas/gods-eye-view.md) | Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el navegador. | Tu objetivo encaja con estos ejemplos: Explorar información geoespacial pública; Consultar el globo desde un agente MCP | API de IA opcional |
| [osiris](../fichas/osiris.md) | Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. | Tu objetivo encaja con estos ejemplos: Explorar noticias por ubicación; Comparar eventos públicos en un globo | API de IA opcional |
| [Pythia](../fichas/pythia.md) | Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. | Tu objetivo encaja con estos ejemplos: Resumir fuentes públicas con un LLM local; Comparar escenarios sobre un conjunto de eventos | Sin clave propia de API de IA en la ruta básica |

## Fotogrametría y mapas desde imágenes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [ODM](../fichas/odm.md) | Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación. | Tu objetivo encaja con estos ejemplos: Crear un mapa a partir de fotos de dron; Producir una nube de puntos para inspección | Sin clave propia de API de IA en la ruta básica |
| [WebODM](../fichas/webodm.md) | Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap. | Tu objetivo encaja con estos ejemplos: Procesar imágenes de dron desde una interfaz; Comparar resultados de dos vuelos de práctica | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Marketing de agencia](../playbooks/marketing-de-agencia.md) — Operar campañas, contenido y email a escala con agentes y herramientas propias.
- [Web app moderna con IA](../playbooks/web-app-moderna-con-ia.md) — Construir un frontend pulido con chat o funciones de IA integradas.
- [Analítica de producto con IA](../playbooks/analitica-con-ia.md) — Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
