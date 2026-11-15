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

## `backtrader`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=cuant,framework,python

**Qué es:** Biblioteca de Python para definir estrategias y estudiar su comportamiento mediante backtesting de datos de mercado.
**Stack:** Python y dependencias compatibles; CSV histórico; matplotlib solo para gráficos
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; fuentes de datos y cómputo pueden costar aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una biblioteca de simulación e integración; los resultados dependen de comisiones, datos y supuestos, no solo de la regla
- Coste: Sin pago a un modelo en la ruta básica. No requiere modelo; fuentes de datos y cómputo pueden costar aparte
- Equipo: Preparación según la ruta elegida. Python y dependencias compatibles; CSV histórico; matplotlib solo para gráficos
**Repo:** https://github.com/mementum/backtrader

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/mementum/backtrader/blob/master/README.rst
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender backtesting por eventos; Comparar supuestos de ejecución de una estrategia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Prueba una regla sencilla sobre un CSV y añade una comisión explícita
**Qué comprobar:** Puedes revisar cada operación y su efecto en el balance simulado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `nautilus-trader`

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

## `chartanalyst`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=finanzas,python

**Qué es:** Experimento de aprendizaje profundo que usa redes convolucionales para reconocer patrones en gráficos bursátiles.
**Stack:** Código Python histórico; Keras antiguo y Theano o TensorFlow; datos CSV
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No usa un servicio LLM; entrenar consume recursos; no hay instalación moderna completa verificada
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. El código inspeccionado utiliza APIs antiguas de Keras y no ofrece un entorno actual fijado; es material de estudio que puede requerir migración
- Coste: Sin pago a un modelo en la ruta básica. No usa un servicio LLM; entrenar consume recursos; no hay instalación moderna completa verificada
- Equipo: Preparación según la ruta elegida. Código Python histórico; Keras antiguo y Theano o TensorFlow; datos CSV
**Repo:** https://github.com/huima58/chartAnalyst

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/huima58/chartAnalyst/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar clasificación de gráficos con redes convolucionales; Practicar separación temporal de datos
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Localiza cómo se convierten gráficos en imágenes y cómo se separan entrenamiento y prueba antes de intentar portar el código
**Qué comprobar:** Puedes explicar entradas, etiquetas y evaluación de la CNN
Revisión documental individual; instalación no ejecutada por Alexandría.

## `company-pixel-office`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,javascript

**Qué es:** Demostración de una oficina de trading en pixel art para estudiar su interfaz y la representación visual de un equipo.
**Stack:** Navegador; servidor estático si ejecutas la fuente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La demo estática no requiere modelo; assets y datos externos mantienen sus licencias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Es una representación de una mesa de trabajo; ver personajes activos no prueba operaciones ni agentes financieros funcionando
- Coste: Sin pago a un modelo en la ruta básica. La demo estática no requiere modelo; assets y datos externos mantienen sus licencias
- Equipo: Preparación según la ruta elegida. Navegador; servidor estático si ejecutas la fuente
**Repo:** https://github.com/ATK-zk/company-pixel-office

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ATK-zk/company-pixel-office/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una visualización de equipo en pixel art; Prototipar un panel de estados narrativo
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre la demo visual y relaciona cada personaje con el estado que muestra
**Qué comprobar:** Puedes distinguir representación de interfaz y actividad realmente documentada
Revisión documental individual; instalación no ejecutada por Alexandría.

## `crypto-trader`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=finanzas,algorithm,bitcoin,bot,coinbase,exchange-api,gemini,market

**Qué es:** Biblioteca de Python con bindings de la API de Gemini y un ejemplo de estrategia de criptomonedas.
**Stack:** Python 3; dependencias del proyecto; credenciales Gemini para consultas privadas
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No requiere modelo; Gemini Exchange, comisiones y servicios tienen condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El clone del README contiene cryto-trader, una errata; usa la URL canónica pirate/crypto-trader y no ejecutes el ejemplo como una simulación supuesta
- Coste: El coste depende del proveedor o la ruta. No requiere modelo; Gemini Exchange, comisiones y servicios tienen condiciones propias
- Equipo: Preparación según la ruta elegida. Python 3; dependencias del proyecto; credenciales Gemini para consultas privadas
**Repo:** https://github.com/pirate/crypto-trader

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/pirate/crypto-trader/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un wrapper de exchange; Revisar una estrategia de umbral sobre datos de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Lee example.py y settings.py y distingue consulta de balance y envío de órdenes sin lanzar el ejemplo
**Qué comprobar:** Puedes reconocer qué hace la estrategia y qué operaciones requieren autenticación
Revisión documental individual; instalación no ejecutada por Alexandría.

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
**Combina con:** `n8n`

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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/virattt/dexter/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar investigación de una empresa; Comparar explicaciones con documentos fuente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Consulta un dato histórico concreto y abre su fuente antes de aceptar la síntesis
**Qué comprobar:** Puedes comprobar periodo, unidad y procedencia del dato
Revisión documental individual; instalación no ejecutada por Alexandría.

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

**Instalación** [?]:

```
Seguir la instalación original: https://www.freqtrade.io/en/stable/docker_quickstart/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Comparar una regla en datos históricos; Evaluar una estrategia en simulación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta un backtest pequeño y revisa comisiones y sesgos antes de pasar a dry-run
**Qué comprobar:** Puedes reproducir operaciones simuladas y su configuración
Revisión documental individual; instalación no ejecutada por Alexandría.

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

## `intellitrader`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,binance,bitcoin,bot,crypto,cryptocurrencies,cryptocurrency,trading-bot

**Qué es:** Bot configurable de criptomonedas con componentes de simulación, señales y conexión a exchanges.
**Stack:** Distribución compatible; configuración de simulación; datos de mercado
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La simulación inicial no requiere claves; exchanges, datos e infraestructura pueden costar
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Virtual trading está documentado como valor inicial, pero revisa tu configuración y versión antes de iniciar una instalación existente
- Coste: El coste depende del proveedor o la ruta. La simulación inicial no requiere claves; exchanges, datos e infraestructura pueden costar
- Equipo: Preparación según la ruta elegida. Distribución compatible; configuración de simulación; datos de mercado
**Repo:** https://github.com/jazzonaut/IntelliTrader

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/jazzonaut/IntelliTrader/blob/master/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar gestión de una cartera ficticia; Comparar señales sin enviar órdenes reales
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Mantén virtual trading activado y observa una operación virtual antes de configurar ninguna clave
**Qué comprobar:** Puedes comprobar que el registro pertenece a la simulación
Revisión documental individual; instalación no ejecutada por Alexandría.

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

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Aprender investigación cuantitativa; Estudiar costes y sesgos de un backtest
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Reproduce un notebook introductorio con datos gratuitos y separa entrenamiento y prueba temporal
**Qué comprobar:** Puedes explicar los supuestos y reproducir una métrica fuera de muestra
Revisión documental individual; instalación no ejecutada por Alexandría.

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
**Alternativas (elige una):** `backtrader`

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

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/ChainBuff/open-sol-bot/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar un bot de seguimiento on-chain; Revisar una integración de Telegram con blockchain
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Examina configuración y rutas de órdenes antes de conectar una wallet o habilitar seguimiento
**Qué comprobar:** Puedes identificar las acciones que consultarían datos y las que moverían fondos
Revisión documental individual; instalación no ejecutada por Alexandría.

## `pixel-hedge-fund`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,svelte

**Qué es:** Demostración de una oficina financiera en pixel art con interfaz de análisis y conexiones configurables a mercados.
**Stack:** Node; SvelteKit; datos de prueba; conexión a fuentes si corresponde
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelo para la interfaz; fuentes e infraestructura pueden tener costes
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La producción no usa el fallback SAMPLE de desarrollo; los errores o datos ausentes deben permanecer visibles
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelo para la interfaz; fuentes e infraestructura pueden tener costes
- Equipo: Preparación según la ruta elegida. Node; SvelteKit; datos de prueba; conexión a fuentes si corresponde
**Repo:** https://github.com/jaypolanco96/pixel-hedge-fund

**Instalación** [+]:

```
cd pixel-hedge-fund   # repo root
npm install
npm run dev -- --port 5173
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una interfaz financiera en pixel art; Mostrar estados y movimientos de una simulación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre la interfaz de desarrollo y comprueba si muestra SAMPLE o datos de un exchange
**Qué comprobar:** Puedes reconocer el origen y la ausencia de datos sin confundirla con un precio cero
Revisión documental individual; instalación no ejecutada por Alexandría.

## `pixelfund-ai`
role=app · exec=local · setup=medium · mcp=False · prov=— · tags=aprender,template,typescript

**Qué es:** Aplicación de simulación bursátil con agentes e interfaz en pixel art para explorar carteras y operaciones virtuales.
**Stack:** Node >=20; npm >=10; Docker o PostgreSQL y Redis; claves opcionales según función
**Acceso y costes:**
- API de IA: API de IA opcional. La interfaz no obliga a modelo; análisis necesita proveedor AI y datos Finnhub para ciertas funciones; consumo y cupos son externos
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelo local no documentado. La guía y env.example distinguen proveedor AI y claves; no se confirma modelo local; autenticación de producción sigue entre tareas de endurecimiento
- Coste: El coste depende del proveedor o la ruta. La interfaz no obliga a modelo; análisis necesita proveedor AI y datos Finnhub para ciertas funciones; consumo y cupos son externos
- Equipo: Preparación según la ruta elegida. Node >=20; npm >=10; Docker o PostgreSQL y Redis; claves opcionales según función
**Repo:** https://github.com/kyjwang/PixelFund-AI

**Instalación** [+]:

```
cp .env.example .env
npm install
npm run dev:all
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar una cartera virtual con ciclo de órdenes; Prototipar una interfaz de comité de inversión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre System Console tras iniciar la app y revisa disponibilidad de base, Redis, datos y AI
**Qué comprobar:** Puedes ver qué componentes están listos y cuáles impiden análisis u operaciones virtuales
Revisión documental individual; instalación no ejecutada por Alexandría.

## `py-clob-client`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=bots,library,python

**Qué es:** Cliente Python antiguo para la API de órdenes de Polymarket; está archivado y conviene revisar su sucesor.
**Stack:** Navegador; código existente solo para planificar migración
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Leer el código no necesita modelo; el cliente ya no es una ruta funcional de operaciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Archivado y declarado no funcional por el autor; no se recomienda instalarlo para integraciones nuevas ni existentes
- Coste: Sin pago a un modelo en la ruta básica. Leer el código no necesita modelo; el cliente ya no es una ruta funcional de operaciones
- Equipo: Preparación según la ruta elegida. Navegador; código existente solo para planificar migración
**Repo:** https://github.com/Polymarket/py-clob-client

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Planificar una migración de SDK; Comprender una integración histórica de Polymarket
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Identifica las llamadas antiguas de un ejemplo y compáralas con la documentación del sucesor oficial
**Qué comprobar:** Puedes preparar una lista de cambios sin intentar conectar el cliente retirado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Alternativas (elige una):** `py-sdk`

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
**Alternativas (elige una):** `py-clob-client`

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

## `stocks-analyst`
role=directory · exec=hybrid · setup=medium · mcp=False · prov=— · tags=finanzas,jupyter notebook

**Qué es:** Scripts para recopilar recomendaciones de analistas bursátiles y preparar datos para su evaluación histórica.
**Stack:** Python y utilidades del proyecto; archivos históricos; acceso permitido a fuentes
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita LLM; fuentes y descargas pueden tener límites y condiciones propias
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La fuente puede conservar historia incompleta; no mezcles datos recopilados hoy con una supuesta disponibilidad histórica
- Coste: Sin pago a un modelo en la ruta básica. No necesita LLM; fuentes y descargas pueden tener límites y condiciones propias
- Equipo: Preparación según la ruta elegida. Python y utilidades del proyecto; archivos históricos; acceso permitido a fuentes
**Repo:** https://github.com/omerdr/stocks

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Estudiar evaluación de recomendaciones públicas; Preparar un dataset temporal para análisis
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Examina el CSV histórico y reproduce una comparación entre recomendación y cotización posterior
**Qué comprobar:** Puedes verificar fecha, horizonte y cálculo de la comparación
Revisión documental individual; instalación no ejecutada por Alexandría.

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
