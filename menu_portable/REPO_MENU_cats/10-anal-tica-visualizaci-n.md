# 10. Analítica & Visualización — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `autohedge`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=— · tags=finanzas,ai,blackrock,finance,goldmansachs,hedgefund,jpmorgan,ml

**Qué es:** Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. Distribuye análisis y decisiones entre agentes con funciones especializadas y herramientas de mercado.
**Stack:** Python, pyproject.toml
**Repo:** https://github.com/The-Swarm-Corporation/AutoHedge

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres estudiar una arquitectura de agentes para investigación de trading
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `awesome-dataviz`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=automation,dataviz,javascript

**Qué es:** Punto de partida para descubrir opciones de dataviz sin búsquedas dispersas.
**Stack:** Markdown
**Repo:** https://github.com/hal9ai/awesome-dataviz

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/awesome-dataviz/). Si necesitas el código: git clone https://github.com/hal9ai/awesome-dataviz`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** buscas opciones de visualización y aún no has elegido
**Evita si:** ya elegiste tu librería y solo necesitas usarla
**Combina con:** `echarts`, `awesome-bigdata`

## `binance-trader`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,arbitrage,binance,bitcoin,btc,cryptocurrency,trade,python

**Qué es:** Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. Consulta precios y procesa reglas de estrategia mediante scripts de prueba y ejecución.
**Stack:** Python, Docker
**Repo:** https://github.com/yasinkuyu/binance-trader

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres estudiar cómo se estructura un bot experimental conectado a Binance
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `chart-js`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=dataviz,javascript

**Qué es:** Ocho tipos de gráfico listos, responsivos y animados con muy poco código. Ideal para dashboards web simples.
**Stack:** JavaScript, Canvas
**Repo:** https://github.com/chartjs/Chart.js

**Instalación** [~]: `npm install chart.js   (o: pnpm add chart.js)`
_Nombre npm puede diferir de 'Chart.js'; verifica en npmjs.com._

**Elige si:** quieres gráficos simples sin aprender una librería compleja
**Evita si:** necesitas visualizaciones a medida; mira `d3`
**Alternativas (elige una):** `echarts`, `recharts`

## `chartanalyst`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=finanzas,python

**Qué es:** Experimento de aprendizaje profundo que usa redes convolucionales para reconocer patrones en gráficos bursátiles. Convierte ventanas de precios en representaciones que una CNN usa para clasificar patrones.
**Stack:** Python
**Repo:** https://github.com/huima58/chartAnalyst

**Instalación** [~]: `pip install chartanalyst   (o: uv add chartanalyst)`
_Nombre PyPI puede diferir de 'chartAnalyst'; verifica en pypi.org._

**Elige si:** quieres estudiar aprendizaje sobre imágenes de series financieras
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `crypto-trader`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,algorithm,bitcoin,bot,coinbase,exchange-api,gemini,market

**Qué es:** Biblioteca de Python con bindings de la API de Gemini y un ejemplo de estrategia de criptomonedas. Expone operaciones de la API del exchange y tipos para construir solicitudes y órdenes.
**Stack:** Python
**Repo:** https://github.com/pirate/crypto-trader

**Instalación** [~]: `pip install crypto-trader   (o: uv add crypto-trader)`
_Nombre PyPI puede diferir de 'crypto-trader'; verifica en pypi.org._

**Elige si:** quieres consultar una implementación sencilla de integración con Gemini
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `d3`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=dataviz,javascript

**Qué es:** Da control total sobre cada elemento visual. Base de muchas librerías de gráficos y del periodismo de datos.
**Stack:** JavaScript, SVG
**Repo:** https://github.com/d3/d3

**Instalación** [~]: `npm install d3.js   (o: pnpm add d3.js)`
_Nombre npm puede diferir de 'D3.js'; verifica en npmjs.com._

**Elige si:** necesitas visualizaciones totalmente personalizadas
**Evita si:** quieres gráficos estándar rápido; mira `chart-js` o `recharts`
**Alternativas (elige una):** `echarts`

## `daily-stock-analysis`
role=app · exec=cloud · setup=medium · mcp=False · prov=openai,google · tags=analytics,agents,python

**Qué es:** Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Telegram, Slack, correo o WeChat. Puede correr gratis con GitHub Actions.
**Stack:** Python, GitHub Actions
**Repo:** https://github.com/ZhuLinsen/daily_stock_analysis

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres un análisis bursátil diario automatizado
**Evita si:** buscas asesoría financiera: esto no lo es
**Combina con:** `n8n`

## `dash`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=automation,ui,python

**Qué es:** Cubre el caso de dashboards productivos en Python sin salir del lenguaje.
**Stack:** Python, Plotly, Flask, web
**Repo:** https://github.com/plotly/dash

**Instalación** [~]: `pip install dash   (o: uv add dash)`
_Nombre PyPI puede diferir de 'dash'; verifica en pypi.org._

**Elige si:** quieres dashboards productivos en Python con control del frontend
**Evita si:** prefieres prototipos ultrarrápidos (streamlit)
**Combina con:** `streamlit`, `echarts`

## `data-analyst-roadmap`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=recursos,blogs,businessintelligence,courses,data,dataanalysis,dataanalyst,excel

**Qué es:** Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. Organiza conocimientos y recursos desde bases de datos y programación hasta visualización y comunicación.
**Stack:** Recursos y documentación
**Repo:** https://github.com/mtahiraslan/data-analyst-roadmap

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/data-analyst-roadmap/). Si necesitas el código: git clone https://github.com/mtahiraslan/data-analyst-roadmap`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres ordenar un plan de aprendizaje para análisis de datos
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `dataanalystportfolioprojects`
role=directory · exec=local · setup=medium · mcp=False · prov=— · tags=recursos,analytics,dashboard,data-visualization,excel,hadoop,hiveq,portfolio

**Qué es:** Portafolio de ejemplos de análisis de datos con SQL, Python, Tableau, Excel y Hive. Presenta ejercicios de limpieza, exploración y construcción de dashboards sobre conjuntos de datos.
**Stack:** Jupyter Notebook
**Repo:** https://github.com/PriyankaJhaTheDeveloper/DataAnalystPortfolioProjects

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/DataAnalystPortfolioProjects/). Si necesitas el código: git clone https://github.com/PriyankaJhaTheDeveloper/DataAnalystPortfolioProjects`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres consultar ejemplos para construir tu propio portafolio de análisis
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `dexter`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,typescript

**Qué es:** Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. Ejecuta tareas de investigación con herramientas y modelos y organiza la evidencia obtenida.
**Stack:** TypeScript, Node.js
**Repo:** https://github.com/virattt/dexter

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres experimentar con investigación financiera asistida por un agente
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `echarts`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=dataviz,typescript

**Qué es:** Cubre casi cualquier tipo de chart en el navegador.
**Stack:** JavaScript/TypeScript
**Repo:** https://github.com/apache/echarts

**Instalación** [~]: `npm install echarts   (o: pnpm add echarts)`
_Nombre npm puede diferir de 'echarts'; verifica en npmjs.com._

**Elige si:** necesitas gráficos ricos y variados embebidos
**Evita si:** solo series temporales simples y priorizas peso (uPlot)
**Combina con:** `metabase`, `heroui`
**Alternativas (elige una):** `d3`, `chart-js`, `recharts`

## `finceptterminal`
role=app · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,ai-agents,algorithmic-trading,bloomberg-terminal,cpp,finance,financial-markets,fintech

**Qué es:** Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. Combina módulos de mercado y análisis en una aplicación de escritorio con integraciones de datos.
**Stack:** C++, Docker
**Repo:** https://github.com/Fincept-Corporation/FinceptTerminal

**Instalación** [~]: `git clone https://github.com/Fincept-Corporation/FinceptTerminal && cd FinceptTerminal && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres explorar una terminal abierta de investigación y datos financieros
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `gradio`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,python

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
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=observability,dataviz,typescript,docker

**Qué es:** Crea dashboards y alertas sobre Prometheus, Loki, bases SQL y decenas de fuentes. Estándar en monitoreo.
**Stack:** Go, TypeScript, Docker
**Repo:** https://github.com/grafana/grafana

**Instalación** [~]: `git clone https://github.com/grafana/grafana && cd grafana && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas monitoreo y alertas en tiempo real
**Evita si:** buscas BI de negocio; mira `superset` o `metabase`
**Combina con:** `langfuse`

## `intellitrader`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,binance,bitcoin,bot,crypto,cryptocurrencies,cryptocurrency,trading-bot

**Qué es:** Bot configurable de criptomonedas con componentes de simulación, señales y conexión a exchanges. Aplica una configuración de estrategias y proveedores para observar o ejecutar operaciones.
**Stack:** C#
**Repo:** https://github.com/jazzonaut/IntelliTrader

**Instalación** [?]: `git clone https://github.com/jazzonaut/IntelliTrader (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres estudiar la arquitectura de un bot con modo de trading virtual
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `machine-learning-for-trading`
role=directory · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,artificial-intelligence,backtesting,data-science,deep-learning,finance,investment

**Qué es:** Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. Recorre un flujo de investigación desde la obtención de datos hasta pruebas y despliegue de modelos.
**Stack:** Jupyter Notebook, Docker, pyproject.toml
**Repo:** https://github.com/stefan-jansen/machine-learning-for-trading

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/machine-learning-for-trading/). Si necesitas el código: git clone https://github.com/stefan-jansen/machine-learning-for-trading`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres aprender un proceso de investigación de trading basado en datos
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `matomo`
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=analytics,php

**Qué es:** Analítica web completa con embudos, mapas de calor y comercio electrónico, auto-hospedada.
**Stack:** PHP, MySQL
**Repo:** https://github.com/matomo-org/matomo

**Instalación** [?]: `git clone https://github.com/matomo-org/matomo (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** necesitas analítica completa como Google Analytics pero propia
**Evita si:** quieres algo simple; mira `umami`
**Alternativas (elige una):** `umami`, `plausible`

## `metabase`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=analytics,dataviz,docker

**Qué es:** Apunta a perfiles no técnicos que necesitan reporting propio.
**Stack:** Java/Clojure, BD, web
**Repo:** https://github.com/metabase/metabase

**Instalación** [?]: `git clone https://github.com/metabase/metabase (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres BI accesible para perfiles no técnicos
**Evita si:** necesitas analítica de eventos por usuario (posthog)
**Combina con:** `posthog`, `echarts`
**Alternativas (elige una):** `superset`, `redash`

## `open-sol-bot`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,blockchain,solana,telegram-bot,trader,transaction,python

**Qué es:** Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. Conecta servicios de la cadena y componentes de aplicación para seguir eventos y procesar operaciones.
**Stack:** Python, Docker, pyproject.toml
**Repo:** https://github.com/ChainBuff/open-sol-bot

**Instalación** [~]: `git clone https://github.com/ChainBuff/open-sol-bot && cd open-sol-bot && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres estudiar automatización y seguimiento de transacciones en Solana
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `osiris`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=osint,typescript

**Qué es:** Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. Agrega feeds y los representa en una interfaz geográfica con distintas capas de información.
**Stack:** TypeScript, Docker, Node.js
**Repo:** https://github.com/simplifaisoul/osiris

**Instalación** [~]: `git clone https://github.com/simplifaisoul/osiris && cd osiris && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres visualizar varias fuentes de actualidad en un mapa
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `pandas-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,local · tags=analytics,data,python

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
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=analytics,docker

**Qué es:** Un panel de una sola página con lo esencial: visitas, fuentes, páginas y objetivos.
**Stack:** Elixir, ClickHouse, PostgreSQL
**Repo:** https://github.com/plausible/analytics

**Instalación** [?]: `git clone https://github.com/plausible/analytics (verificar README para build/run)`
_Stack no claro; revisa el README tras clonar._

**Elige si:** quieres analítica minimalista y privada
**Evita si:** necesitas embudos y eventos complejos; mira `posthog`
**Alternativas (elige una):** `umami`, `matomo`

## `posthog`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=analytics,python,docker

**Qué es:** Cubre todo el ciclo de medición de producto sin integrar varias herramientas.
**Stack:** Python/Node, ClickHouse, self-host o cloud
**Repo:** https://github.com/PostHog/posthog

**Instalación** [~]: `git clone https://github.com/PostHog/posthog && cd posthog && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres entender el uso real y el comportamiento de usuarios
**Evita si:** solo necesitas BI sobre una BD estática (metabase)
**Combina con:** `metabase`

## `pythia`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=osint,typescript

**Qué es:** Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. Combina un panel de eventos con MiroFish y modelos locales para consultar información agregada.
**Stack:** TypeScript, pyproject.toml
**Repo:** https://github.com/jangles-byte/Pythia

**Instalación** [~]: `git clone https://github.com/jangles-byte/Pythia && cd Pythia && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres explorar fuentes OSINT y escenarios desde un panel local
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `qlib`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,auto-quant,deep-learning,finance,fintech,investment,machine-learning

**Qué es:** Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. Organiza preparación de datos, entrenamiento, predicción y backtesting en pipelines de investigación.
**Stack:** Python, Docker, pyproject.toml, Node.js
**Repo:** https://github.com/microsoft/qlib

**Instalación** [~]: `git clone https://github.com/microsoft/qlib && cd qlib && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** necesitas experimentar con modelos y evaluaciones cuantitativas reproducibles
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `quantharness`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agentic-ai,large-language-models,html

**Qué es:** Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading. Coordina agentes con LangChain y LangGraph y presenta sus análisis mediante una interfaz web.
**Stack:** HTML
**Repo:** https://github.com/Y-Research-SBU/QuantHarness

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres estudiar la coordinación de agentes sobre señales de precio
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `recharts`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=dataviz,react,typescript

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
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=analytics,dataviz,typescript

**Qué es:** Pensada para analistas que escriben SQL y quieren compartir resultados rápido con el equipo.
**Stack:** Python, TypeScript, PostgreSQL, Redis
**Repo:** https://github.com/getredash/redash

**Instalación** [~]: `git clone https://github.com/getredash/redash && cd redash && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** tu equipo trabaja con SQL y quiere compartir rápido
**Evita si:** necesitas BI con permisos finos; mira `superset`
**Alternativas (elige una):** `metabase`, `superset`

## `stocks-analyst`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,jupyter notebook

**Qué es:** Scripts para recopilar recomendaciones de analistas bursátiles y preparar datos para su evaluación histórica. Extrae recomendaciones de sitios externos y organiza matrices para compararlas con resultados posteriores.
**Stack:** Jupyter Notebook
**Repo:** https://github.com/omerdr/stocks

**Instalación** [+]: `Copiar la skill a la carpeta de skills de tu agente (p.ej. .claude/skills/stocks/). Si necesitas el código: git clone https://github.com/omerdr/stocks`
_Material de referencia/playbook; no es una dependencia runtime._

**Elige si:** quieres estudiar el rendimiento histórico de recomendaciones publicadas
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `streamlit`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=ui,dataviz,python

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
role=platform · exec=local · setup=medium · mcp=False · prov=— · tags=analytics,dataviz,python,docker

**Qué es:** Conecta tus bases SQL, crea gráficos y dashboards sin código o con SQL Lab, con control de acceso.
**Stack:** Python, React, Docker
**Repo:** https://github.com/apache/superset

**Instalación** [~]: `git clone https://github.com/apache/superset && cd superset && docker compose up -d`
_Requiere Docker; el compose puede variar — revisa docker-compose.yml._

**Elige si:** quieres BI empresarial abierto
**Evita si:** buscas algo muy fácil para no técnicos; mira `metabase`
**Combina con:** `duckdb`, `wrenai`
**Alternativas (elige una):** `metabase`, `redash`

## `tradingagents`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agent,finance,llm,multiagent,trading,python

**Qué es:** Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading. Coordina roles que consultan datos, comparan argumentos y generan resultados de investigación.
**Stack:** Python, Docker, pyproject.toml
**Repo:** https://github.com/TauricResearch/TradingAgents

**Instalación** [+]: `Crear cuenta / API key en el proveedor (no self-host).`
_Servicio gestionado; no se clona._

**Elige si:** quieres estudiar arquitecturas multiagente aplicadas a investigación de mercados
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `umami`
role=platform · exec=local · setup=easy · mcp=False · prov=— · tags=analytics,typescript,docker

**Qué es:** Mide visitas, campañas, eventos, conversiones e ingresos en un panel simple, cumpliendo GDPR.
**Stack:** TypeScript, Next.js, PostgreSQL
**Repo:** https://github.com/umami-software/umami

**Instalación** [~]: `git clone https://github.com/umami-software/umami && cd umami && (pnpm install || npm install)`
_Proyecto Node; usa pnpm si hay pnpm-lock.yaml._

**Elige si:** quieres analítica web simple y privada
**Evita si:** necesitas analítica de producto avanzada; mira `posthog`
**Alternativas (elige una):** `plausible`, `matomo`

## `uplot`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=dataviz,javascript

**Qué es:** Apuesta por hacer una sola cosa (líneas/áreas temporales) mejor que ninguna.
**Stack:** JavaScript
**Repo:** https://github.com/leeoniya/uPlot

**Instalación** [~]: `npm install uplot   (o: pnpm add uplot)`
_Nombre npm puede diferir de 'uPlot'; verifica en npmjs.com._

**Elige si:** priorizas velocidad y peso del bundle
**Evita si:** necesitas tipos de gráfico variados (echarts)
**Combina con:** `swr`

## `wrenai`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,local · tags=analytics,data,agents,python

**Qué es:** Define tu modelo de datos una vez y los usuarios (o agentes) preguntan en lenguaje natural para obtener SQL, gráficos y respuestas.
**Stack:** Python, TypeScript, Rust
**Repo:** https://github.com/Canner/WrenAI

**Instalación** [~]: `git clone https://github.com/Canner/WrenAI && cd WrenAI && (uv sync || pip install -r requirements.txt)`
_Proyecto Python; usa uv si hay pyproject.toml/uv.lock._

**Elige si:** quieres text-to-SQL confiable para el negocio
**Evita si:** solo analizas un CSV; mira `pandas-ai`
**Combina con:** `superset`, `duckdb`
**Alternativas (elige una):** `pandas-ai`
