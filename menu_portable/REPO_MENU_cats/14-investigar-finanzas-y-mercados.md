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

## `backtrader`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,python

**Qué es:** Biblioteca de Python para definir estrategias y estudiar su comportamiento mediante backtesting de datos de mercado.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/mementum/backtrader

**Instalación** [+]: `pip install backtrader`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Biblioteca de Python para definir estrategias y estudiar su comportamiento mediante backtesting de datos de mercado.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Alternativas (elige una):** `nautilus-trader`

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

## `ccxt`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=bots,library,python

**Qué es:** Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading.
**Stack:** Python, Dockerfile, docker-compose.yml, package.json, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ccxt/ccxt

**Instalación** [+]: `pip install ccxt`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

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

## `company-pixel-office`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,javascript

**Qué es:** Demostración de una oficina de trading en pixel art para estudiar su interfaz y la representación visual de un equipo.
**Stack:** JavaScript
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ATK-zk/company-pixel-office

**Instalación** [?]: `Seguir la instalación original: https://github.com/ATK-zk/company-pixel-office/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Demostración de una oficina de trading en pixel art para estudiar su interfaz y la representación visual de un equipo.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

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

## `finrl`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=cuant,framework,jupyter-notebook

**Qué es:** Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.
**Stack:** Jupyter Notebook, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La inferencia o el entrenamiento local documentado no necesita una API de IA alojada; sí necesita preparar sus modelos y dependencias.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. El proyecto documenta ejecución local de modelos. Descarga pesos compatibles y revisa sus condiciones de uso.
- Coste: Sin pago a un modelo en la ruta básica. La ruta local no tiene factura por llamada a un modelo remoto. Sí consume hardware, energía y almacenamiento, y puede requerir licencias o acceso a pesos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Memoria y GPU según el modelo. RAM, disco, VRAM y aceleración dependen del modelo y del backend; no se promete rendimiento sin una prueba.
**Repo:** https://github.com/AI4Finance-Foundation/FinRL

**Instalación** [?]: `Seguir la instalación original: https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `freqtrade`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=bots,app,python

**Qué es:** Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/freqtrade/freqtrade

**Instalación** [?]: `Seguir la instalación original: https://github.com/freqtrade/freqtrade/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

## `hummingbot`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=bots,app,python

**Qué es:** Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/hummingbot/hummingbot

**Instalación** [?]: `Seguir la instalación original: https://github.com/hummingbot/hummingbot/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución

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

## `lumibot`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,python

**Qué es:** Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Lumiwealth/lumibot

**Instalación** [?]: `Seguir la instalación original: https://github.com/Lumiwealth/lumibot/blob/dev/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

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

## `nautilus-trader`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,rust

**Qué es:** Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.
**Stack:** Rust, Cargo.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/nautechsystems/nautilus_trader

**Instalación** [?]: `Seguir la instalación original: https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Alternativas (elige una):** `backtrader`

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

## `pixel-hedge-fund`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,svelte

**Qué es:** Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.
**Stack:** Svelte, package.json
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/jaypolanco96/pixel-hedge-fund

**Instalación** [?]: `Seguir la instalación original: https://github.com/jaypolanco96/pixel-hedge-fund/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `pixelfund-ai`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,typescript

**Qué es:** Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.
**Stack:** TypeScript, docker-compose.yml, package.json
**Acceso y costes:**
- API de IA: API: por confirmar. El README describe agentes y simulación, pero no resuelve qué acceso a modelos exige cada proveedor. Revisa la guía SETUP y su configuración antes de asumir coste cero.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Ejecución con modelos locales por confirmar. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Coste por confirmar. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/kyjwang/PixelFund-AI

**Instalación** [?]: `Seguir la instalación original: https://github.com/kyjwang/PixelFund-AI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `py-clob-client`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=bots,library,python

**Qué es:** Cliente Python antiguo para la API de órdenes de Polymarket; está archivado y conviene revisar su sucesor.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Polymarket/py-clob-client

**Instalación** [?]: `Seguir la instalación original: https://github.com/Polymarket/py-clob-client/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Cliente Python antiguo para la API de órdenes de Polymarket; está archivado y conviene revisar su sucesor.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Alternativas (elige una):** `py-sdk`

## `py-sdk`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=bots,library,python

**Qué es:** SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Polymarket/py-sdk

**Instalación** [?]: `Seguir la instalación original: https://github.com/Polymarket/py-sdk/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Alternativas (elige una):** `py-clob-client`

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

## `vectorbt`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,python

**Qué es:** Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.
**Stack:** Python, Dockerfile, pyproject.toml
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/polakowo/vectorbt

**Instalación** [?]: `Seguir la instalación original: https://github.com/polakowo/vectorbt/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `vibe-trading`
role=app · exec=hybrid · setup=medium · mcp=False · prov=local · tags=agentes,agent,python

**Qué es:** Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/HKUDS/Vibe-Trading

**Instalación** [?]: `Seguir la instalación original: https://github.com/HKUDS/Vibe-Trading/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.
**Evita si:** necesitas una instalación inmediata sin revisar las dependencias y condiciones de la distribución
