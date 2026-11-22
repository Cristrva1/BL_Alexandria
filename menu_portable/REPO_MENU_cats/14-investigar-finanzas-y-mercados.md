# 14. Investigar finanzas y mercados — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `autohedge`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=— · tags=finanzas,ai,blackrock,finance,goldmansachs,hedgefund,jpmorgan,ml

**Qué es:** Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado.
**Stack:** Python; credenciales de modelo y herramientas; entorno de investigación sin fondos
**Acceso y costes:**
- API de IA: API de IA necesaria. El ejemplo pide claves OpenAI o Anthropic y Jupiter; operaciones y proveedores pueden tener comisiones y consumo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El README incluye WALLET_PRIVATE_KEY; no es una simple app de lectura y no se ha verificado aquí una simulación aislada
- Coste: El coste depende del proveedor o la ruta. El ejemplo pide claves OpenAI o Anthropic y Jupiter; operaciones y proveedores pueden tener comisiones y consumo
- Equipo: Preparación según la ruta elegida. Python; credenciales de modelo y herramientas; entorno de investigación sin fondos
**Repo:** https://github.com/The-Swarm-Corporation/AutoHedge

**Instalación** [+]:

```
pip install -U autohedge
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar coordinación de analistas y riesgo; Revisar el diseño de un pipeline de trading
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Revisa la configuración de agentes y sus herramientas antes de ejecutar un flujo de análisis de prueba
**Qué comprobar:** Puedes distinguir consulta, decisión y funciones que enviarían operaciones
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `langgraph`, `vectorbt`

## `backtesting-py`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=finanzas,python,library

**Qué es:** Framework ligero de Python para hacer backtesting de estrategias de trading sobre datos OHLC, con optimización y gráficos interactivos.
**Stack:** Python, pyproject.toml, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/kernc/backtesting.py

**Instalación** [+]:

```
pip install backtesting
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: probar una estrategia de cruce de medias sobre datos históricos; optimizar parámetros de una estrategia y ver el resultado en un gráfico interactivo
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install backtesting` y ejecuta el ejemplo SmaCross de la documentación.
**Qué comprobar:** Obtienes estadísticas del backtest y un gráfico interactivo con operaciones.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `yfinance`, `jupyterlab`, `claude-code`, `openbb`
**Alternativas (elige una):** `vectorbt`

## `binance-trader`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,arbitrage,binance,bitcoin,btc,cryptocurrency,trade,python

**Qué es:** Bot experimental de Python para estudiar estrategias y automatización con la API de Binance.
**Stack:** Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa LLM; operaciones, datos, red y exchange tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Bot experimental con documentación antigua; no se confirma que sus endpoints funcionen hoy ni que tenga una simulación completa
- Coste: El coste depende del proveedor o la ruta. No usa LLM; operaciones, datos, red y exchange tienen costes propios
- Equipo: Preparación según la ruta elegida. Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado
**Repo:** https://github.com/yasinkuyu/binance-trader

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/yasinkuyu/binance-trader/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una estrategia de ejemplo; Analizar cómo se conecta un bot a un exchange
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Examina la configuración y localiza las llamadas de lectura y de creación de órdenes sin activar el bot
**Qué comprobar:** Puedes identificar qué credenciales y acciones afectarán una cuenta
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `vectorbt`, `coolify`

## `ccxt`
role=library · exec=local · setup=medium · mcp=True · prov=— · tags=bots,library,python

**Qué es:** Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading.
**Stack:** Node o paquete de tu lenguaje; exchange elegido; credenciales solo para funciones privadas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo; comisiones, datos y planes del exchange o servicios tienen costes propios
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP stdio deja capacidades sensibles como opt-in; instalar la biblioteca no exige habilitar órdenes ni retiros
- Coste: El coste depende del proveedor o la ruta. No necesita modelo; comisiones, datos y planes del exchange o servicios tienen costes propios
- Equipo: Preparación según la ruta elegida. Node o paquete de tu lenguaje; exchange elegido; credenciales solo para funciones privadas
**Repo:** https://github.com/ccxt/ccxt

**Instalación** [+]:

```
npm install ccxt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Unificar consultas de varios mercados; Construir una integración de datos de exchange
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta mercados públicos y verifica símbolo, precisión y límites sin habilitar trading
**Qué comprobar:** Puedes contrastar metadatos con la documentación del exchange
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `freqtrade`, `vectorbt`, `claude-code`

## `daily-stock-analysis`
role=app · exec=cloud · setup=medium · mcp=False · prov=openai,google · tags=analytics,agents,python

**Qué es:** Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario.
**Stack:** Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Ollama sirve para despliegue local; Actions normalmente usa API Cloud; datos, modelos y notificaciones tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El panel generado no verifica por sí solo la exactitud financiera; una ejecución programada necesita infraestructura aunque tenga cupo gratuito
- Coste: El coste depende del proveedor o la ruta. Ollama sirve para despliegue local; Actions normalmente usa API Cloud; datos, modelos y notificaciones tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras
**Repo:** https://github.com/ZhuLinsen/daily_stock_analysis

**Instalación** [+]:

```
# 克隆项目
git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis

# 安装依赖
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar un resumen de investigación; Comparar noticias y datos de una lista de seguimiento
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza un símbolo de ejemplo sin activar envíos y contrasta fechas y datos del informe
**Qué comprobar:** Puedes separar precios observados, fuentes y texto generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `activepieces`, `litellm`

## `dexter`
role=app · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,typescript

**Qué es:** Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis.
**Stack:** Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Ollama ofrece una ruta local; datos de mercado y modelos remotos pueden exigir claves y cuotas propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Su comparación con Claude Code describe una experiencia de agente; no documenta que use el plan de Claude Code
- Coste: El coste depende del proveedor o la ruta. Ollama ofrece una ruta local; datos de mercado y modelos remotos pueden exigir claves y cuotas propias
- Equipo: Preparación según la ruta elegida. Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros
**Repo:** https://github.com/virattt/dexter

**Instalación** [+]:

```
git clone https://github.com/virattt/dexter.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar investigación de una empresa; Comparar explicaciones con documentos fuente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta un dato histórico concreto y abre su fuente antes de aceptar la síntesis
**Qué comprobar:** Puedes comprobar periodo, unidad y procedencia del dato
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `tradingagents`, `langfuse`

## `finceptterminal`
role=app · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,ai-agents,algorithmic-trading,bloomberg-terminal,cpp,finance,financial-markets,fintech

**Qué es:** Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes.
**Stack:** Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Tiene planes, créditos y edición Enterprise; BYOK y Ollama son rutas distintas; el instalador no incluye todos los datos y modelos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Verifica los módulos y límites de tu edición; la marca y ciertos derechos comerciales tienen condiciones adicionales
- Coste: El coste depende del proveedor o la ruta. Tiene planes, créditos y edición Enterprise; BYOK y Ollama son rutas distintas; el instalador no incluye todos los datos y modelos
- Equipo: Preparación según la ruta elegida. Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba
**Repo:** https://github.com/Fincept-Corporation/FinceptTerminal

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Explorar indicadores de varios mercados; Comparar información económica de fuentes distintas
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre un panel de investigación y comprueba proveedor y hora de sus datos antes de activar AI
**Qué comprobar:** Puedes distinguir datos observados y análisis generado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ollama`, `qlib`, `ccxt`

## `fingpt`
role=runtime · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,python,model,training

**Qué es:** Proyecto de LLM financieros abiertos de AI4Finance: modelos ajustados con LoRA, datos y recetas para análisis de sentimiento y tareas financieras.
**Stack:** Jupyter Notebook, requirements.txt, setup.py
**Acceso y costes:**
- API de IA: API de IA opcional. El proyecto describe rutas locales y remotas. Las funciones seleccionadas determinan modelos, credenciales y consumos.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Existe una ruta local documentada. Revisa qué componentes cubre: no equivale a ejecutar todas las funciones sin servicios remotos.
- Coste: El coste depende del proveedor o la ruta. La ruta local consume recursos del equipo; las APIs y servicios remotos aplican sus cuotas o tarifas. Una integración de suscripción, cuando esté documentada, consume los límites de ese plan. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Memoria y GPU según el modelo. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/AI4Finance-Foundation/FinGPT

**Instalación** [+]:

```
git clone https://github.com/AI4Finance-Foundation/FinGPT.git
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: clasificar el sentimiento de noticias financieras con un modelo ajustado; reproducir un ajuste LoRA barato sobre datos financieros para investigación
**Evita si:** no tienes el hardware o no aceptas la licencia de los pesos
**Primera prueba propuesta:** Sigue el SETUP del repositorio y ejecuta el ejemplo de análisis de sentimiento con la ruta por API o un modelo local pequeño.
**Qué comprobar:** El script devuelve etiquetas de sentimiento para frases financieras de ejemplo.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `transformers`, `peft`, `pytorch`

## `finrl`
role=library · exec=local · setup=heavy · mcp=False · prov=local · tags=cuant,framework,jupyter-notebook

**Qué es:** Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones.
**Stack:** Python y dependencias de la guía; datos; entorno de entrenamiento
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El aprendizaje local no requiere API LLM; datos, entrenamiento y brokers tienen costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El autor enlaza FinRL-X como evolución; mantén versiones y documentación correspondientes a este repositorio
- Coste: El coste depende del proveedor o la ruta. El aprendizaje local no requiere API LLM; datos, entrenamiento y brokers tienen costes separados
- Equipo: Preparación según la ruta elegida. Python y dependencias de la guía; datos; entorno de entrenamiento
**Repo:** https://github.com/AI4Finance-Foundation/FinRL

**Instalación** [+]:

```
git clone https://github.com/AI4Finance-Foundation/FinRL.git
cd FinRL

pip install -e .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar entornos de RL financiero; Comparar políticas en simulación histórica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un ejemplo pequeño de aprendizaje por refuerzo y evalúa en un periodo distinto
**Qué comprobar:** Puedes contrastar recompensas, operaciones simuladas y datos de prueba
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `qlib`, `machine-learning-for-trading`, `vectorbt`

## `freqtrade`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=bots,app,python

**Qué es:** Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simulación.
**Stack:** Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run
**Acceso y costes:**
- API de IA: API de IA opcional. El bot básico no exige LLM; FreqAI, datos, infraestructura y exchanges tienen requisitos y costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Backtest y dry-run son fases distintas; no conectes resultados históricos con una promesa de rendimiento futuro
- Coste: El coste depende del proveedor o la ruta. El bot básico no exige LLM; FreqAI, datos, infraestructura y exchanges tienen requisitos y costes separados
- Equipo: Preparación según la ruta elegida. Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run
**Repo:** https://github.com/freqtrade/freqtrade

**Instalación** [+]:

```
pip install freqtrade
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar una regla en datos históricos; Evaluar una estrategia en simulación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un backtest pequeño y revisa comisiones y sesgos antes de pasar a dry-run
**Qué comprobar:** Puedes reproducir operaciones simuladas y su configuración
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `vectorbt`, `grafana`

## `hummingbot`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=bots,app,python

**Qué es:** Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias configurables.
**Stack:** Conda o Docker; dependencias de compilación; conector y estrategia de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere LLM; datos, red, servidores y operaciones reales pueden cobrar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El CLI y Gateway tienen papeles distintos; instalar el código no deja preparada una estrategia segura ni verificada
- Coste: El coste depende del proveedor o la ruta. No requiere LLM; datos, red, servidores y operaciones reales pueden cobrar
- Equipo: Preparación según la ruta elegida. Conda o Docker; dependencias de compilación; conector y estrategia de prueba
**Repo:** https://github.com/hummingbot/hummingbot

**Instalación** [+]:

```
# Clone the repository
git clone https://github.com/hummingbot/hummingbot.git
cd hummingbot

# Create the conda environment, build extensions, and expose the `hbot` CLI
make install

# Activate the environment
conda activate hummingbot
hbot --help
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un conector de exchange; Evaluar un bot en un entorno de práctica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Comprueba la instalación con ayuda del CLI y configura una estrategia en paper trade según su guía
**Qué comprobar:** Puedes distinguir ejecución simulada y conexiones reales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `claude-code`, `grafana`

## `lumibot`
role=library · exec=local · setup=medium · mcp=True · prov=— · tags=cuant,framework,python

**Qué es:** Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con brokers.
**Stack:** Python >=3.10; datos históricos; proveedor solo para estrategia AI; broker solo si lo eliges
**Acceso y costes:**
- API de IA: API de IA opcional. Las reglas no necesitan modelo; AI consume proveedor; BotSpot conecta gratis pero uso alojado depende del plan y los datos pueden cobrar
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El asistente que escribe código y los agentes dentro de la estrategia son procesos distintos; no comparten automáticamente presupuesto
- Coste: El coste depende del proveedor o la ruta. Las reglas no necesitan modelo; AI consume proveedor; BotSpot conecta gratis pero uso alojado depende del plan y los datos pueden cobrar
- Equipo: Preparación según la ruta elegida. Python >=3.10; datos históricos; proveedor solo para estrategia AI; broker solo si lo eliges
**Repo:** https://github.com/Lumiwealth/lumibot

**Instalación** [+]:

```
pip install lumibot
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar una estrategia de reglas; Estudiar decisiones de una estrategia AI en backtest
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta el ejemplo de reglas sobre historia y revisa operaciones y costes del backtest
**Qué comprobar:** Puedes reproducir la estrategia sin llamadas AI ni órdenes reales
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `ollama`, `vectorbt`

## `machine-learning-for-trading`
role=directory · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,artificial-intelligence,backtesting,data-science,deep-learning,finance,investment

**Qué es:** Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias.
**Stack:** Docker o entorno del capítulo; datasets; cuaderno elegido
**Acceso y costes:**
- API de IA: API de IA opcional. Material abierto no significa libro, datasets, cómputo o proveedores gratis; comienza con conjuntos gratuitos
- Claude Code: Depende del recurso o la configuración
- Codex: Depende del recurso o la configuración
- Antigravity: Depende del recurso o la configuración
- Modelos locales: Modelos locales documentados. Es material de aprendizaje con ejemplos y skills; cada capítulo o recurso define su entorno y cliente compatible
- Coste: El coste depende del proveedor o la ruta. Material abierto no significa libro, datasets, cómputo o proveedores gratis; comienza con conjuntos gratuitos
- Equipo: Preparación según la ruta elegida. Docker o entorno del capítulo; datasets; cuaderno elegido
**Repo:** https://github.com/stefan-jansen/machine-learning-for-trading

**Instalación** [+]:

```
docker compose up ml4t
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender investigación cuantitativa; Estudiar costes y sesgos de un backtest
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Reproduce un notebook introductorio con datos gratuitos y separa entrenamiento y prueba temporal
**Qué comprobar:** Puedes explicar los supuestos y reproducir una métrica fuera de muestra
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `qlib`, `vectorbt`, `marimo`, `finrl`

## `nautilus-trader`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,rust

**Qué es:** Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias.
**Stack:** CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM; datos, infraestructura y conectores tienen costes separados
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La rama y docs revisadas son v2 RC y piden --pre; sin él se instala v1 con otra API; el autor desaconseja RC para capital real
- Coste: Sin pago a un modelo en la ruta básica. No necesita LLM; datos, infraestructura y conectores tienen costes separados
- Equipo: Preparación según la ruta elegida. CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba
**Repo:** https://github.com/nautechsystems/nautilus_trader

**Instalación** [+]:

```
pip install -U nautilus_trader --pre
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un motor orientado a eventos; Comparar simulaciones con datos registrados
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un ejemplo de backtest de la misma versión v2 y revisa su secuencia de eventos
**Qué comprobar:** Puedes reproducir órdenes y fills simulados con configuración fija
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `polars`, `marimo`, `ccxt`, `py-sdk`

## `open-sol-bot`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=finanzas,blockchain,solana,telegram-bot,trader,transaction,python

**Qué es:** Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado.
**Stack:** Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM; RPC, red y operaciones pueden cobrar; las claves de wallet son distintas de una API de IA
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es un bot con capacidad de ejecución; no se confirma una ruta de paper trading en las fuentes revisadas
- Coste: El coste depende del proveedor o la ruta. No necesita LLM; RPC, red y operaciones pueden cobrar; las claves de wallet son distintas de una API de IA
- Equipo: Preparación según la ruta elegida. Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones
**Repo:** https://github.com/ChainBuff/open-sol-bot

**Instalación** [+]:

```
docker compose up -d
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un bot de seguimiento on-chain; Revisar una integración de Telegram con blockchain
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Examina configuración y rutas de órdenes antes de conectar una wallet o habilitar seguimiento
**Qué comprobar:** Puedes identificar las acciones que consultarían datos y las que moverían fondos
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `grafana`, `activepieces`, `coolify`

## `openbb`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=finanzas,python,data,mcp

**Qué es:** Plataforma abierta de datos financieros (ODP): conecta fuentes públicas y con licencia una vez y las expone a Python, Excel, APIs REST y servidores MCP.
**Stack:** Python
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/openbq-org/OpenBB

**Instalación** [+]:

```
pip install openbb
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: descargar series de precios o datos macro en un DataFrame para análisis; dar a un agente acceso a datos financieros mediante el servidor MCP de OpenBB
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install openbb` y descarga el histórico de precios de un símbolo con `obb.equity.price.historical`.
**Qué comprobar:** Obtienes un DataFrame con fechas y precios del proveedor configurado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `jupyterlab`, `vectorbt`, `backtesting-py`

## `polyweather`
role=app · exec=local · setup=easy · mcp=False · prov=—

**Qué es:** Reúne datos meteorológicos y de mercados de predicción para explorar cómo las previsiones afectan a contratos relacionados con el clima.
**Stack:** Python, Dockerfile, docker-compose.yml, pyproject.toml, requirements.txt
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. Autoalojar consume tu equipo; las fuentes y la edición o servicio alojado pueden exigir condiciones o tarifas propias.
- Equipo: Equipo normal; revisar dependencias. Docker Compose o el entorno documentado y fuentes meteorológicas o de mercado de prueba.
**Repo:** https://github.com/yangyuan-zhen/PolyWeather

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/yangyuan-zhen/PolyWeather/blob/d3a02039208f88860cbe02e0846a8a23783b220a/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Contrastar una previsión con un mercado de ejemplo.; Comparar dos lugares con datos públicos sin abrir operaciones.
**Evita si:** necesitas una instalación sin cuentas ni dependencias adicionales
**Primera prueba propuesta:** Abre una vista de datos de prueba y compara fechas de previsión y mercado.
**Qué comprobar:** Puedes identificar la fuente, zona y fecha de los datos mostrados.
Revisión documental individual; instalación no ejecutada por Alexandría.

## `prediction-market-backtesting`
role=library · exec=local · setup=medium · mcp=False · prov=—

**Qué es:** Añade ejemplos y componentes de backtesting para analizar mercados de predicción con datos y estrategias históricas.
**Stack:** Python, Cargo.toml, Makefile
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La primera prueba descrita no llama a un modelo generativo ni exige una clave de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. Sin pago a un modelo en esta ruta; los recursos, cuentas externas o despliegue elegidos pueden tener costes.
- Equipo: Equipo normal; revisar dependencias. Entorno compatible con NautilusTrader y datos históricos de una muestra.
**Repo:** https://github.com/evan-kolberg/prediction-market-backtesting

**Instalación** [?]:

```
Seguir la instalación original: https://evan-kolberg.github.io/prediction-market-backtesting/license/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar dos supuestos de comisiones con datos pasados.; Medir cómo cambia una simulación si mueves el intervalo de prueba.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Ejecuta el ejemplo introductorio con pocos datos históricos y sin credenciales de trading.
**Qué comprobar:** Obtienes un resultado reproducible para el conjunto de datos utilizado.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `nautilus-trader`

## `py-sdk`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=bots,library,python

**Qué es:** SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondientes.
**Stack:** Python y uv o pip; API y permisos según función; consulta de datos públicos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM; cuentas, red y operaciones de la plataforma tienen condiciones y posibles costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El paquete se llama polymarket-client; datos públicos y funciones autenticadas de cuenta o wallet tienen requisitos separados
- Coste: El coste depende del proveedor o la ruta. No necesita LLM; cuentas, red y operaciones de la plataforma tienen condiciones y posibles costes propios
- Equipo: Preparación según la ruta elegida. Python y uv o pip; API y permisos según función; consulta de datos públicos
**Repo:** https://github.com/Polymarket/py-sdk

**Instalación** [+]:

```
uv add polymarket-client
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar la API pública de Polymarket; Preparar una migración desde el cliente antiguo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Enumera datos públicos de un mercado y revisa su esquema sin autenticar una wallet
**Qué comprobar:** Puedes contrastar identificadores y datos con la fuente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `nautilus-trader`, `activepieces`

## `qlib`
role=platform · exec=local · setup=heavy · mcp=False · prov=— · tags=finanzas,algorithmic-trading,auto-quant,deep-learning,finance,fintech,investment,machine-learning

**Qué es:** Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias.
**Stack:** Python compatible con baseline; datos históricos; dependencias del modelo
**Acceso y costes:**
- API de IA: API de IA opcional. El núcleo ML no exige LLM; datos licenciados, cómputo y automatización externa pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Los baselines no comparten siempre versiones de Python; los cambios recientes del recorder requieren revisar la migración
- Coste: El coste depende del proveedor o la ruta. El núcleo ML no exige LLM; datos licenciados, cómputo y automatización externa pueden costar
- Equipo: Preparación según la ruta elegida. Python compatible con baseline; datos históricos; dependencias del modelo
**Repo:** https://github.com/microsoft/qlib

**Instalación** [+]:

```
pip install pyqlib
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar modelos sobre datos temporales; Investigar un pipeline cuantitativo reproducible
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una baseline pequeña sobre un periodo de prueba separado y revisa predicciones y evaluación
**Qué comprobar:** Puedes reproducir resultados sin mezclar datos futuros
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mlflow`, `finrl`, `marimo`, `finceptterminal`, `machine-learning-for-trading`

## `quantharness`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agentic-ai,large-language-models,html

**Qué es:** Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de trading.
**Stack:** Python; checkout; datos; modelo con entrada de imagen y credenciales
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada pide API LLM con visión; datos, agentes múltiples y evaluación acumulan consumo
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. El resultado de investigación no acredita ejecución HFT ni rendimiento futuro; no se confirma aquí un backend local compatible con todo el flujo
- Coste: El coste depende del proveedor o la ruta. La ruta documentada pide API LLM con visión; datos, agentes múltiples y evaluación acumulan consumo
- Equipo: Preparación según la ruta elegida. Python; checkout; datos; modelo con entrada de imagen y credenciales
**Repo:** https://github.com/Y-Research-SBU/QuantHarness

**Instalación** [+]:

```
pip install -r requirements.txt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar agentes que interpretan gráficos; Comparar componentes de un análisis experimental
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Reproduce una evaluación histórica pequeña y revisa los gráficos que recibe cada agente
**Qué comprobar:** Puedes separar datos del periodo, análisis visual y decisión generada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `langchain`, `langfuse`

## `tradingagents`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,agent,finance,llm,multiagent,trading,python

**Qué es:** Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading.
**Stack:** Python; proveedor u Ollama; datos; configuración del grafo
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Admite Ollama y servidores compatibles, además de APIs; datos y múltiples llamadas por análisis pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. La investigación multiagente no equivale a rentabilidad validada ni a un motor listo para operar capital
- Coste: El coste depende del proveedor o la ruta. Admite Ollama y servidores compatibles, además de APIs; datos y múltiples llamadas por análisis pueden costar
- Equipo: Preparación según la ruta elegida. Python; proveedor u Ollama; datos; configuración del grafo
**Repo:** https://github.com/TauricResearch/TradingAgents

**Instalación** [+]:

```
git clone https://github.com/TauricResearch/TradingAgents.git
cd TradingAgents

pip install .
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar debate entre agentes financieros; Comparar proveedores sobre la misma muestra histórica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Analiza un periodo histórico pequeño y revisa fuentes y mensajes de cada especialista
**Qué comprobar:** Puedes identificar qué evidencia apoya cada conclusión y el coste de llamadas
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `langgraph`, `ollama`, `dexter`

## `vectorbt`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,python

**Qué es:** Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado.
**Stack:** Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No exige LLM; usa Apache-2.0 con Commons Clause y ofrece productos comerciales distintos; datos y cómputo cuestan según ruta
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Probar muchas combinaciones aumenta el riesgo de sobreajuste; sus mensajes comerciales no acreditan una ventaja en tu caso
- Coste: El coste depende del proveedor o la ruta. No exige LLM; usa Apache-2.0 con Commons Clause y ofrece productos comerciales distintos; datos y cómputo cuestan según ruta
- Equipo: Preparación según la ruta elegida. Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas
**Repo:** https://github.com/polakowo/vectorbt

**Instalación** [+]:

```
pip install -U vectorbt
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar indicadores en una serie; Explorar sensibilidad de una regla histórica
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Evalúa unas pocas combinaciones y reserva un periodo fuera de muestra
**Qué comprobar:** Puedes revisar parámetros, operaciones y resultados separados de entrenamiento
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `ccxt`, `freqtrade`, `marimo`
**Alternativas (elige una):** `backtesting-py`

## `vibe-trading`
role=app · exec=hybrid · setup=medium · mcp=True · prov=local · tags=agentes,agent,python

**Qué es:** Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables.
**Stack:** Python; proveedor o modelo local; fuente de datos; entorno de investigación
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Modelos, fuentes y herramientas tienen costes por ruta; el paquete incluye MCP stdio; una ruta local requiere configuración adicional
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Las referencias Codex OAuth no garantizan todas las funciones de cada cuenta; usa la guía de proveedores y límites de la versión
- Coste: El coste depende del proveedor o la ruta. Modelos, fuentes y herramientas tienen costes por ruta; el paquete incluye MCP stdio; una ruta local requiere configuración adicional
- Equipo: Preparación según la ruta elegida. Python; proveedor o modelo local; fuente de datos; entorno de investigación
**Repo:** https://github.com/HKUDS/Vibe-Trading

**Instalación** [+]:

```
pip install vibe-trading-ai
vibe-trading init
vibe-trading
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar sensibilidad de una estrategia; Organizar artefactos de investigación reproducibles
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Guarda una investigación histórica y repítela variando solo comisiones y deslizamiento
**Qué comprobar:** Puedes comparar supuestos y resultados sin cambiar los datos de entrada
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `openclaw`, `vectorbt`

## `yfinance`
role=library · exec=local · setup=easy · mcp=False · prov=— · tags=finanzas,python,library,data

**Qué es:** Biblioteca Python no oficial para descargar datos de mercado y fundamentales de Yahoo! Finance en DataFrames de pandas.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La función básica es software o material que no necesita llamar a un modelo de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Sin pago a un modelo en la ruta básica. No exige consumo de un modelo en esa ruta. Revisar licencia, alojamiento, cuentas y servicios externos. Datos de mercado, brokers y exchanges pueden exigir cuentas, cuotas, comisiones o fondos. Una simulación o backtest no acredita rentabilidad ni una conexión real lista.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/ranaroussi/yfinance

**Instalación** [+]:

```
pip install yfinance
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: descargar históricos de precios para un estudio o backtest; obtener fundamentales y dividendos de una cartera en un cuaderno
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código
**Primera prueba propuesta:** Instala con `pip install yfinance` y descarga un año de precios de un símbolo con `Ticker(...).history`.
**Qué comprobar:** Obtienes un DataFrame con precios OHLC, volumen y fechas.
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `vectorbt`, `backtesting-py`, `jupyterlab`
