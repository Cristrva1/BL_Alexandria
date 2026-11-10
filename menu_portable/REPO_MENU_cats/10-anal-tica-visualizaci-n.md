# 10. Analítica & Visualización — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-dataviz`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.
**Stack:** Markdown
**Repo:** https://github.com/hal9ai/awesome-dataviz

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-dataviz/). Si necesitas el código: git clone https://github.com/hal9ai/awesome-dataviz`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas opciones de visualización y aún no has elegido
**Evita si:** ya elegiste tu librería y solo necesitas usarla
**Combina con:** `echarts`, `awesome-bigdata`

## `chart-js`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Ocho tipos de gráfico listos, responsivos y animados con muy poco código. Ideal para dashboards web simples.
**Stack:** JavaScript, Canvas
**Repo:** https://github.com/chartjs/Chart.js

**Instalación** [~]: `npm install chart.js   (o: pnpm add chart.js)`
_Nombre npm puede diferir de 'Chart.js'; verifica en npmjs.com._

**Elige si:** quieres gráficos simples sin aprender una librería compleja
**Evita si:** necesitas visualizaciones a medida; mira `d3`
**Alternativas (elige una):** `echarts`, `recharts`

## `d3`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Da control total sobre cada elemento visual. Base de muchas librerías de gráficos y del periodismo de datos.
**Stack:** JavaScript, SVG
**Repo:** https://github.com/d3/d3

**Instalación** [~]: `npm install d3.js   (o: pnpm add d3.js)`
_Nombre npm puede diferir de 'D3.js'; verifica en npmjs.com._

**Elige si:** necesitas visualizaciones totalmente personalizadas
**Evita si:** quieres gráficos estándar rápido; mira `chart-js` o `recharts`
**Alternativas (elige una):** `echarts`

## `daily-stock-analysis`
role=app · exec=cloud · setup=medium · mcp=False · prov=['openai', 'google']

**Qué es:** Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Telegram, Slack, correo o WeChat. Puede correr gratis con GitHub Actions.
**Stack:** Python, GitHub Actions
**Repo:** https://github.com/ZhuLinsen/daily_stock_analysis

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres un análisis bursátil diario automatizado
**Evita si:** buscas asesoría financiera: esto no lo es
**Combina con:** `n8n`

## `dash`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Cubre el caso de dashboards productivos en Python sin salir del lenguaje.
**Stack:** Python, Plotly, Flask, web
**Repo:** https://github.com/plotly/dash

**Instalación** [~]: `pip install dash   (o: uv add dash)`
_Nombre PyPI puede diferir de 'dash'; verifica en pypi.org._

**Elige si:** quieres dashboards productivos en Python con control del frontend
**Evita si:** prefieres prototipos ultrarrápidos (streamlit)
**Combina con:** `streamlit`, `echarts`

## `echarts`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Cubre casi cualquier tipo de chart en el navegador.
**Stack:** JavaScript/TypeScript
**Repo:** https://github.com/apache/echarts

**Instalación** [~]: `npm install echarts   (o: pnpm add echarts)`
_Nombre npm puede diferir de 'echarts'; verifica en npmjs.com._

**Elige si:** necesitas gráficos ricos y variados embebidos
**Evita si:** solo series temporales simples y priorizas peso (uPlot)
**Combina con:** `metabase`, `heroui`
**Alternativas (elige una):** `d3`, `chart-js`, `recharts`

## `gradio`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Envuelve una función Python en una interfaz web con entradas y salidas de texto, imagen, audio o chat. Base de Hugging Face Spaces.
**Stack:** Python, Svelte
**Repo:** https://github.com/gradio-app/gradio

**Instalación** [~]: `pip install gradio   (o: uv add gradio)`
_Nombre PyPI puede diferir de 'Gradio'; verifica en pypi.org._

**Elige si:** quieres una demo web de tu modelo rápido
**Evita si:** construyes una app de datos con varias páginas; mira `streamlit`
**Combina con:** `transformers`
**Alternativas (elige una):** `streamlit`

## `grafana`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.
**Stack:** Go, TypeScript, Docker
**Repo:** https://github.com/grafana/grafana

**Instalación** [~]: `git clone https://github.com/grafana/grafana && cd grafana && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas monitoreo y alertas en tiempo real
**Evita si:** buscas BI de negocio; mira `superset` o `metabase`
**Combina con:** `langfuse`

## `matomo`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Analítica web completa con embudos, mapas de calor y comercio electrónico, auto-hospedada.
**Stack:** PHP, MySQL
**Repo:** https://github.com/matomo-org/matomo

**Instalación** [?]: `git clone https://github.com/matomo-org/matomo (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas analítica completa como Google Analytics pero propia
**Evita si:** quieres algo simple; mira `umami`
**Alternativas (elige una):** `umami`, `plausible`

## `metabase`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Apunta a perfiles no técnicos que necesitan reporting propio.
**Stack:** Java/Clojure, BD, web
**Repo:** https://github.com/metabase/metabase

**Instalación** [?]: `git clone https://github.com/metabase/metabase (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres BI accesible para perfiles no técnicos
**Evita si:** necesitas analítica de eventos por usuario (posthog)
**Combina con:** `posthog`, `echarts`
**Alternativas (elige una):** `superset`, `redash`

## `pandas-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=['openai', 'local']

**Qué es:** Haces preguntas en lenguaje natural y genera el código de análisis o gráficos. Útil para analistas y apps de datos.
**Stack:** Python, pandas
**Repo:** https://github.com/sinaptik-ai/pandas-ai

**Instalación** [~]: `pip install pandasai   (o: uv add pandasai)`
_Nombre PyPI puede diferir de 'PandasAI'; verifica en pypi.org._

**Elige si:** quieres preguntar a tus tablas en lenguaje natural
**Evita si:** necesitas text-to-SQL gobernado para la empresa; mira `wrenai`
**Combina con:** `duckdb`
**Alternativas (elige una):** `wrenai`

## `plausible`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos.
**Stack:** Elixir, ClickHouse, PostgreSQL
**Repo:** https://github.com/plausible/analytics

**Instalación** [?]: `git clone https://github.com/plausible/analytics (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres analítica minimalista y privada
**Evita si:** necesitas embudos y eventos complejos; mira `posthog`
**Alternativas (elige una):** `umami`, `matomo`

## `posthog`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** Cubre todo el ciclo de medición de producto sin integrar varias herramientas.
**Stack:** Python/Node, ClickHouse, self-host o cloud
**Repo:** https://github.com/PostHog/posthog

**Instalación** [~]: `git clone https://github.com/PostHog/posthog && cd posthog && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres entender el uso real y el comportamiento de usuarios
**Evita si:** solo necesitas BI sobre una BD estática (metabase)
**Combina con:** `metabase`

## `recharts`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Construye gráficos con componentes de React. Muy usada en dashboards de apps React y en shadcn/ui.
**Stack:** TypeScript, React, D3
**Repo:** https://github.com/recharts/recharts

**Instalación** [~]: `npm install recharts   (o: pnpm add recharts)`
_Nombre npm puede diferir de 'Recharts'; verifica en npmjs.com._

**Elige si:** tu app es React y quieres gráficos declarativos
**Evita si:** no usas React; mira `chart-js`
**Combina con:** `ui`
**Alternativas (elige una):** `chart-js`, `echarts`

## `redash`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Pensada para analistas que escriben SQL y quieren compartir resultados rápido con el equipo.
**Stack:** Python, TypeScript, PostgreSQL, Redis
**Repo:** https://github.com/getredash/redash

**Instalación** [~]: `git clone https://github.com/getredash/redash && cd redash && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu equipo trabaja con SQL y quiere compartir rápido
**Evita si:** necesitas BI con permisos finos; mira `superset`
**Alternativas (elige una):** `metabase`, `superset`

## `streamlit`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Convierte un script de datos en una app web interactiva casi al instante.
**Stack:** Python
**Repo:** https://github.com/streamlit/streamlit

**Instalación** [~]: `pip install streamlit   (o: uv add streamlit)`
_Nombre PyPI puede diferir de 'streamlit'; verifica en pypi.org._

**Elige si:** quieres una UI de datos al vuelo y prototipos rápidos
**Evita si:** necesitas una app productiva con control fino del frontend (dash)
**Combina con:** `dash`, `data-science-ipython-notebooks`
**Alternativas (elige una):** `gradio`

## `superset`
role=platform · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso.
**Stack:** Python, React, Docker
**Repo:** https://github.com/apache/superset

**Instalación** [~]: `git clone https://github.com/apache/superset && cd superset && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres BI empresarial abierto
**Evita si:** buscas algo muy fácil para no técnicos; mira `metabase`
**Combina con:** `duckdb`, `wrenai`
**Alternativas (elige una):** `metabase`, `redash`

## `umami`
role=platform · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Mide visitas, campañas, eventos, conversiones e ingresos en un panel simple, cumpliendo GDPR.
**Stack:** TypeScript, Next.js, PostgreSQL
**Repo:** https://github.com/umami-software/umami

**Instalación** [~]: `git clone https://github.com/umami-software/umami && cd umami && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres analítica web simple y privada
**Evita si:** necesitas analítica de producto avanzada; mira `posthog`
**Alternativas (elige una):** `plausible`, `matomo`

## `uplot`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.
**Stack:** JavaScript
**Repo:** https://github.com/leeoniya/uPlot

**Instalación** [~]: `npm install uplot   (o: pnpm add uplot)`
_Nombre npm puede diferir de 'uPlot'; verifica en npmjs.com._

**Elige si:** priorizas velocidad y peso del bundle
**Evita si:** necesitas tipos de gráfico variados (echarts)
**Combina con:** `swr`

## `wrenai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=['openai', 'local']

**Qué es:** Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.
**Stack:** Python, TypeScript, Rust
**Repo:** https://github.com/Canner/WrenAI

**Instalación** [~]: `git clone https://github.com/Canner/WrenAI && cd WrenAI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres text-to-SQL confiable para el negocio
**Evita si:** solo analizas un CSV; mira `pandas-ai`
**Combina con:** `superset`, `duckdb`
**Alternativas (elige una):** `pandas-ai`
