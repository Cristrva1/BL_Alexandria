# 10. Analítica & Visualización — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `awesome-dataviz`
role=directory · exec=cloud · setup=easy · mcp=False · prov=—

**Qué es:** directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad.
**Stack:** Markdown
**Repo:** https://github.com/javierluraschi/awesome-dataviz

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-dataviz/). Si necesitas el código: git clone https://github.com/javierluraschi/awesome-dataviz`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas opciones de visualización
**Evita si:** ya elegiste tu librería.
**Combina con:** `echarts`, `awesome-bigdata`

## `dash`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos.
**Stack:** Python, Plotly, web
**Repo:** https://github.com/plotly/dash

**Instalación** [~]: `pip install dash   (o: uv add dash)`
_Nombre PyPI puede diferir de 'dash'; verifica en pypi.org._

**Elige si:** quieres dashboards en Python
**Evita si:** prefieres prototipos ultrarrápidos ([streamlit](#-streamlit)).
**Combina con:** `streamlit`, `echarts`
**Alternativas (elige una):** `streamlit`

## `echarts`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos.
**Stack:** JavaScript/TypeScript
**Repo:** https://github.com/apache/echarts

**Instalación** [~]: `npm install echarts   (o: pnpm add echarts)`
_Nombre npm puede diferir de 'echarts'; verifica en npmjs.com._

**Elige si:** necesitas gráficos ricos
**Evita si:** solo series temporales simples ([uPlot](#-uplot)).
**Combina con:** `metabase`, `heroui`
**Alternativas (elige una):** `uplot`

## `metabase`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=—

**Qué es:** herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL.
**Stack:** Java/Clojure, BD, web
**Repo:** https://github.com/metabase/metabase

**Instalación** [?]: `git clone https://github.com/metabase/metabase (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres BI accesible
**Evita si:** necesitas analítica de eventos ([posthog](#-posthog)).
**Combina con:** `posthog`, `echarts`
**Alternativas (elige una):** `posthog`

## `posthog`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=—

**Qué es:** plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite.
**Stack:** Python/Node, self-host o cloud
**Repo:** https://github.com/PostHog/posthog

**Instalación** [~]: `git clone https://github.com/PostHog/posthog && cd posthog && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres entender el uso real
**Evita si:** solo necesitas BI sobre una BD ([metabase](#-metabase)).
**Combina con:** `metabase`
**Alternativas (elige una):** `metabase`

## `streamlit`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS.
**Stack:** Python
**Repo:** https://github.com/streamlit/streamlit

**Instalación** [~]: `pip install streamlit   (o: uv add streamlit)`
_Nombre PyPI puede diferir de 'streamlit'; verifica en pypi.org._

**Elige si:** quieres una UI de datos al vuelo
**Evita si:** necesitas una app productiva ([dash](#-dash)).
**Combina con:** `dash`, `data-science-ipython-notebooks`
**Alternativas (elige una):** `dash`

## `uplot`
role=library · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento.
**Stack:** JavaScript
**Repo:** https://github.com/leeoniya/uPlot

**Instalación** [~]: `npm install uplot   (o: pnpm add uplot)`
_Nombre npm puede diferir de 'uPlot'; verifica en npmjs.com._

**Elige si:** priorizas velocidad/peso
**Evita si:** necesitas tipos de gráfico variados ([echarts](#-echarts)).
**Combina con:** `swr`
**Alternativas (elige una):** `echarts`
