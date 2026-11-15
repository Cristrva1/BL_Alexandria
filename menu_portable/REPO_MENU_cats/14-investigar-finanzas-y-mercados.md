# 14. Investigar finanzas y mercados — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `autohedge`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=— · tags=finanzas,ai,blackrock,finance,goldmansachs,hedgefund,jpmorgan,ml

**Qué es:** Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. Distribuye análisis y decisiones entre agentes con funciones especializadas y herramientas de mercado.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/The-Swarm-Corporation/AutoHedge

**Instalación** [?]: `Seguir la instalación original: https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar una arquitectura de agentes para investigación de trading
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `binance-trader`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,arbitrage,binance,bitcoin,btc,cryptocurrency,trade,python

**Qué es:** Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. Consulta precios y procesa reglas de estrategia mediante scripts de prueba y ejecución.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/yasinkuyu/binance-trader

**Instalación** [?]: `Seguir la instalación original: https://github.com/yasinkuyu/binance-trader/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar cómo se estructura un bot experimental conectado a Binance
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `chartanalyst`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=finanzas,python

**Qué es:** Experimento de aprendizaje profundo que usa redes convolucionales para reconocer patrones en gráficos bursátiles. Convierte ventanas de precios en representaciones que una CNN usa para clasificar patrones.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/huima58/chartAnalyst

**Instalación** [?]: `Seguir la instalación original: https://github.com/huima58/chartAnalyst/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar aprendizaje sobre imágenes de series financieras
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `crypto-trader`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,algorithm,bitcoin,bot,coinbase,exchange-api,gemini,market

**Qué es:** Biblioteca de Python con bindings de la API de Gemini y un ejemplo de estrategia de criptomonedas. Expone operaciones de la API del exchange y tipos para construir solicitudes y órdenes.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/pirate/crypto-trader

**Instalación** [?]: `Seguir la instalación original: https://github.com/pirate/crypto-trader/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres consultar una implementación sencilla de integración con Gemini
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `daily-stock-analysis`
role=app · exec=cloud · setup=medium · mcp=False · prov=openai,google · tags=analytics,agents,python

**Qué es:** Combina datos de mercado, noticias en tiempo real y análisis con LLM para generar reportes automáticos por Telegram, Slack, correo o WeChat. Puede correr gratis con GitHub Actions.
**Stack:** Python, GitHub Actions
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/ZhuLinsen/daily_stock_analysis

**Instalación** [?]: `Seguir la instalación original: https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un análisis bursátil diario automatizado
**Evita si:** buscas asesoría financiera: esto no lo es
**Combina con:** `n8n`

## `dexter`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,typescript

**Qué es:** Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. Ejecuta tareas de investigación con herramientas y modelos y organiza la evidencia obtenida.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/virattt/dexter

**Instalación** [?]: `Seguir la instalación original: https://github.com/virattt/dexter/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres experimentar con investigación financiera asistida por un agente
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `finceptterminal`
role=app · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,ai-agents,algorithmic-trading,bloomberg-terminal,cpp,finance,financial-markets,fintech

**Qué es:** Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. Combina módulos de mercado y análisis en una aplicación de escritorio con integraciones de datos.
**Stack:** C++, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Fincept-Corporation/FinceptTerminal

**Instalación** [?]: `Seguir la instalación original: https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres explorar una terminal abierta de investigación y datos financieros
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `intellitrader`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,binance,bitcoin,bot,crypto,cryptocurrencies,cryptocurrency,trading-bot

**Qué es:** Bot configurable de criptomonedas con componentes de simulación, señales y conexión a exchanges. Aplica una configuración de estrategias y proveedores para observar o ejecutar operaciones.
**Stack:** C#
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/jazzonaut/IntelliTrader

**Instalación** [?]: `Seguir la instalación original: https://github.com/jazzonaut/IntelliTrader/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar la arquitectura de un bot con modo de trading virtual
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `machine-learning-for-trading`
role=directory · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,artificial-intelligence,backtesting,data-science,deep-learning,finance,investment

**Qué es:** Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. Recorre un flujo de investigación desde la obtención de datos hasta pruebas y despliegue de modelos.
**Stack:** Jupyter Notebook, Docker, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/stefan-jansen/machine-learning-for-trading

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres aprender un proceso de investigación de trading basado en datos
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `open-sol-bot`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,blockchain,solana,telegram-bot,trader,transaction,python

**Qué es:** Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. Conecta servicios de la cadena y componentes de aplicación para seguir eventos y procesar operaciones.
**Stack:** Python, Docker, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/ChainBuff/open-sol-bot

**Instalación** [?]: `Seguir la instalación original: https://github.com/ChainBuff/open-sol-bot/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar automatización y seguimiento de transacciones en Solana
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `qlib`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,auto-quant,deep-learning,finance,fintech,investment,machine-learning

**Qué es:** Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. Organiza preparación de datos, entrenamiento, predicción y backtesting en pipelines de investigación.
**Stack:** Python, Docker, pyproject.toml, Node.js
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/microsoft/qlib

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/qlib/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** necesitas experimentar con modelos y evaluaciones cuantitativas reproducibles
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `quantharness`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agentic-ai,large-language-models,html

**Qué es:** Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading. Coordina agentes con LangChain y LangGraph y presenta sus análisis mediante una interfaz web.
**Stack:** HTML
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/Y-Research-SBU/QuantHarness

**Instalación** [?]: `Seguir la instalación original: https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar la coordinación de agentes sobre señales de precio
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `stocks-analyst`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,jupyter notebook

**Qué es:** Scripts para recopilar recomendaciones de analistas bursátiles y preparar datos para su evaluación histórica. Extrae recomendaciones de sitios externos y organiza matrices para compararlas con resultados posteriores.
**Stack:** Jupyter Notebook
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica.
- Coste: Sin pago a un modelo en la ruta básica. La ruta básica no exige un LLM. Exchanges, brokers, datos de mercado y ejecución real pueden requerir cuentas, tarifas o fondos; los ejemplos no acreditan rentabilidad.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/omerdr/stocks

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** quieres estudiar el rendimiento histórico de recomendaciones publicadas
**Evita si:** necesitas resultados operativos validados en vez de material de investigación

## `tradingagents`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agent,finance,llm,multiagent,trading,python

**Qué es:** Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading. Coordina roles que consultan datos, comparan argumentos y generan resultados de investigación.
**Stack:** Python, Docker, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/TauricResearch/TradingAgents

**Instalación** [?]: `Seguir la instalación original: https://github.com/TauricResearch/TradingAgents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres estudiar arquitecturas multiagente aplicadas a investigación de mercados
**Evita si:** necesitas resultados operativos validados en vez de material de investigación
