# Alexandría para agentes · Agentes de investigación financiera

Categoría 14 «Investigar finanzas y mercados» › subcategoría `agentes`. 9 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=14&sub=agentes · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

## Instrucciones para el agente

1. **Lee primero el proyecto**: README, manifiestos (package.json, pyproject, go.mod, docker-compose), infraestructura y lo que ya está instalado. Identifica el problema concreto antes de elegir herramienta.
2. **Propón de 1 a 3 candidatos** de esta lista con motivos ligados al proyecto (qué resuelve, por qué encaja, qué exige). Si nada encaja, dilo; no fuerces una elección.
3. **Nunca instales, clones, descargues ni ejecutes nada sin aprobación explícita del usuario** para ese repo y ese comando. Muestra el comando exacto y dónde se ejecutará antes de pedirla.
4. **Prefiere el `recomendado` de cada grupo de similares**; elige una alternativa solo si su «Cuándo elegirlo» encaja mejor.
5. **Señala los riesgos**: herramientas de uso dual u ofensivo (solo en sistemas propios o con autorización escrita) y licencias BSL, Elastic, SSPL, AGPL u open-core (funciones de pago).
6. **Usa solo los comandos de instalación de este archivo o de la fuente citada.** Si pone «sin comando en el catálogo», lee la fuente oficial y cita la URL; no inventes comandos.
7. Ten en cuenta el nivel de complejidad (1 Básico … 4 Experto) frente a la experiencia del usuario y el entorno disponible.
8. Las fichas son una revisión documental: ningún proyecto se instaló ni se ejecutó al catalogarlo. Comprueba la versión, la licencia y los requisitos en la fuente antes de recomendar. Cualquier prueba activa exige alcance autorizado y un laboratorio separado de producción.

## Tabla de decisión

| Repo | Para qué | Nivel | Puntuación | Licencia | Papel |
|---|---|---|---:|---|---|
| `daily-stock-analysis` | Sistema que analiza acciones de varios mercados con LLM y envía un tablero de… | 2 Intermedio | 78 | MIT (OSI permisiva) | sin grupo |
| `tradingagents` | Framework experimental que organiza agentes de análisis financiero, debate y… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `vibe-trading` | Agente de investigación y trabajo con estrategias de trading que utiliza… | 2 Intermedio | 71 | MIT (OSI permisiva) | sin grupo |
| `finceptterminal` | Terminal de análisis financiero que reúne datos, investigación, paneles y… | 3 Avanzado | 63 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `fingpt` | Proyecto de LLM financieros abiertos de AI4Finance: modelos ajustados con LoRA… | 3 Avanzado | 54 | MIT (OSI permisiva) | sin grupo |
| `dexter` | Agente de investigación financiera que planifica consultas, obtiene datos de… | 2 Intermedio | 50 | — (sin licencia detectada) | sin grupo |
| `autohedge` | Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de… | 3 Avanzado | 45 | MIT (OSI permisiva) | sin grupo |
| `quantharness` | Sistema experimental de agentes LLM que combina indicadores técnicos, patrones… | 2 Intermedio | 45 | MIT (OSI permisiva) | sin grupo |
| `polyweather` | Reúne datos meteorológicos y de mercados de predicción para explorar cómo las… | 2 Intermedio | — | AGPL-3.0 | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### daily_stock_analysis (`daily-stock-analysis`)

- **Repo:** https://github.com/ZhuLinsen/daily_stock_analysis · MIT · nivel 2 · 78/100
- **Qué es:** Sistema de análisis inteligente de acciones con LLM (股票智能分析系统), de @ZhuLinsen. Licencia MIT. Es muy popular (~73k estrellas, v3.34.0) y su README, principalmente en chino, incluye patrocinios de proveedores de modelos.
- **Cuándo elegirlo:** Casos: Preparar un resumen de investigación; Comparar noticias y datos de una lista de seguimiento.
- **Requisitos:** nivel 2: preparación media; Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras; hardware prerequisites; API de IA: depends; Python; proveedor LLM u Ollama; fuentes de datos; notificaciones solo si las configuras.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/ZhuLinsen/daily_stock_analysis/blob/main/README.md

  ```bash
  # 克隆项目
  git clone https://github.com/ZhuLinsen/daily_stock_analysis.git && cd daily_stock_analysis
  
  # 安装依赖
  pip install -r requirements.txt
  ```
- **Primera prueba propuesta (no ejecutada):** Analiza un símbolo de ejemplo sin activar envíos y contrasta fechas y datos del informe Éxito: Puedes separar precios observados, fuentes y texto generado
- **Combina con:** `ollama` [8/motores], `activepieces` [1/motores], `litellm` [23/serving]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión. El panel generado no verifica por sí solo la exactitud financiera; una ejecución programada necesita infraestructura aunque tenga cupo gratuito.

### TradingAgents (`tradingagents`)

- **Repo:** https://github.com/TauricResearch/TradingAgents · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** TradingAgents, framework multiagente con LLM para trading financiero, de Tauric Research. Licencia Apache-2.0. Es muy popular (~123k estrellas, v0.7.1) y su README promociona Trading-R1, en acceso anticipado.
- **Cuándo elegirlo:** Casos: Estudiar debate entre agentes financieros; Comparar proveedores sobre la misma muestra histórica.
- **Requisitos:** nivel 2: preparación media; Python; proveedor u Ollama; datos; configuración del grafo; hardware prerequisites; API de IA: depends; Python; proveedor u Ollama; datos; configuración del grafo.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/TauricResearch/TradingAgents/blob/main/README.md

  ```bash
  git clone https://github.com/TauricResearch/TradingAgents.git
  cd TradingAgents
  
  pip install .
  ```
- **Primera prueba propuesta (no ejecutada):** Analiza un periodo histórico pequeño y revisa fuentes y mensajes de cada especialista Éxito: Puedes identificar qué evidencia apoya cada conclusión y el coste de llamadas
- **Combina con:** `langgraph` [3/py], `ollama` [8/motores], `dexter`
- **Riesgos y avisos:** Sin alternativas declaradas. Herramienta de investigación. Riesgo financiero: no es asesoramiento de inversión. La investigación multiagente no equivale a rentabilidad validada ni a un motor listo para operar capital.

### Vibe-Trading (`vibe-trading`)

- **Repo:** https://github.com/HKUDS/Vibe-Trading · MIT · nivel 2 · 71/100
- **Qué es:** Vibe-Trading, agente personal de investigación de trading de la organización HKUDS. Licencia MIT. Es muy activo (~38k estrellas, v0.1.19).
- **Cuándo elegirlo:** Casos: Probar sensibilidad de una estrategia; Organizar artefactos de investigación reproducibles.
- **Requisitos:** nivel 2: preparación media; Python; proveedor o modelo local; fuente de datos; entorno de investigación; hardware prerequisites; API de IA: depends; Python; proveedor o modelo local; fuente de datos; entorno de investigación.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/HKUDS/Vibe-Trading/blob/main/README.md

  ```bash
  pip install vibe-trading-ai
  vibe-trading init
  vibe-trading
  ```
- **Primera prueba propuesta (no ejecutada):** Guarda una investigación histórica y repítela variando solo comisiones y deslizamiento Éxito: Puedes comparar supuestos y resultados sin cambiar los datos de entrada
- **Combina con:** `claude-code` [20/terminal], `openclaw` [21/asistentes], `vectorbt` [14/cuant]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión. Las referencias Codex OAuth no garantizan todas las funciones de cada cuenta; usa la guía de proveedores y límites de la versión.

### FinceptTerminal (`finceptterminal`)

- **Repo:** https://github.com/Fincept-Corporation/FinceptTerminal · AGPL-3.0 · nivel 3 · 63/100
- **Qué es:** Fincept Terminal, terminal nativo de escritorio para investigación financiera, de Fincept Corporation. Licencia AGPL-3.0 o posterior, con una edición Enterprise propietaria de pago. Es popular (~34k estrellas, v4.5.2).
- **Cuándo elegirlo:** Casos: Explorar indicadores de varios mercados; Comparar información económica de fuentes distintas.
- **Requisitos:** nivel 3: preparación pesada; Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba; hardware prerequisites; API de IA: opcional; Instalador oficial para tu sistema; cuenta o claves según módulo; datos de prueba.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/Fincept-Corporation/FinceptTerminal/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre un panel de investigación y comprueba proveedor y hora de sus datos antes de activar AI Éxito: Puedes distinguir datos observados y análisis generado
- **Combina con:** `ollama` [8/motores], `qlib` [14/cuant], `ccxt` [14/bots]
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. El README se centra en vender la edición Enterprise. Riesgo financiero: no es asesoramiento de inversión. Verifica los módulos y límites de tu edición; la marca y ciertos derechos comerciales tienen condiciones adicionales.

### FinGPT (`fingpt`)

- **Repo:** https://github.com/AI4Finance-Foundation/FinGPT · MIT · nivel 3 · 54/100
- **Qué es:** Proyecto de código abierto (MIT) de la AI4Finance Foundation, ligado a investigación académica. Activo, aunque gran parte del contenido son cuadernos y recetas.
- **Cuándo elegirlo:** Casos: clasificar el sentimiento de noticias financieras con un modelo ajustado; reproducir un ajuste LoRA barato sobre datos financieros para investigación. Evítalo si no tienes el hardware o no aceptas la licencia de los pesos.
- **Requisitos:** nivel 3: preparación pesada; Jupyter Notebook, requirements.txt, setup.py; hardware model_dependent; API de IA: opcional; Entorno compatible, pesos y licencias del modelo, y recursos de CPU, RAM o GPU suficientes para la variante elegida..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/AI4Finance-Foundation/FinGPT.git` — fuente: https://github.com/AI4Finance-Foundation/FinGPT/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Sigue el SETUP del repositorio y ejecuta el ejemplo de análisis de sentimiento con la ruta por API o un modelo local pequeño. Éxito: El script devuelve etiquetas de sentimiento para frases financieras de ejemplo.
- **Combina con:** `transformers` [24/entrenamiento], `peft` [24/entrenamiento], `pytorch` [24/entrenamiento]
- **Riesgos y avisos:** Los resultados de benchmarks del README corresponden a configuraciones concretas; verifica antes de usar en decisiones.

### dexter (`dexter`)

- **Repo:** https://github.com/virattt/dexter · — · nivel 2 · 50/100
- **Qué es:** Dexter, agente autónomo de investigación financiera de @virattt. El README declara MIT, pero GitHub no detecta licencia. Es popular (~28k estrellas, v1.1.0).
- **Cuándo elegirlo:** Casos: Preparar investigación de una empresa; Comparar explicaciones con documentos fuente.
- **Requisitos:** nivel 2: preparación media; Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros; hardware prerequisites; API de IA: depends; Runtime y gestor de la guía; proveedor u Ollama; acceso a datos financieros.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/virattt/dexter.git` — fuente: https://github.com/virattt/dexter/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta un dato histórico concreto y abre su fuente antes de aceptar la síntesis Éxito: Puedes comprobar periodo, unidad y procedencia del dato
- **Combina con:** `ollama` [8/motores], `tradingagents`, `langfuse` [23/observabilidad]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Depende de APIs de datos de pago. Riesgo financiero: no es asesoramiento de inversión. Su comparación con Claude Code describe una experiencia de agente; no documenta que use el plan de Claude Code.

### AutoHedge (`autohedge`)

- **Repo:** https://github.com/The-Swarm-Corporation/AutoHedge · MIT · nivel 3 · 45/100
- **Qué es:** AutoHedge, «fondo de cobertura autónomo» de agentes de The Swarm Corporation. Licencia MIT. Tiene ~7k estrellas (sin releases) y su último cambio es de mayo de 2026.
- **Cuándo elegirlo:** Casos: Estudiar coordinación de analistas y riesgo; Revisar el diseño de un pipeline de trading.
- **Requisitos:** nivel 3: preparación pesada, requiere clave de API; Python; credenciales de modelo y herramientas; entorno de investigación sin fondos; hardware prerequisites; API de IA: sí; Python; credenciales de modelo y herramientas; entorno de investigación sin fondos.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U autohedge` — fuente: https://github.com/The-Swarm-Corporation/AutoHedge/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Revisa la configuración de agentes y sus herramientas antes de ejecutar un flujo de análisis de prueba Éxito: Puedes distinguir consulta, decisión y funciones que enviarían operaciones
- **Combina con:** `ccxt` [14/bots], `langgraph` [3/py], `vectorbt` [14/cuant]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo muy alto: opera con una clave privada real de forma autónoma. Riesgo financiero: no es asesoramiento de inversión. El README incluye WALLET_PRIVATE_KEY; no es una simple app de lectura y no se ha verificado aquí una simulación aislada.

### QuantHarness (`quantharness`)

- **Repo:** https://github.com/Y-Research-SBU/QuantHarness · MIT · nivel 2 · 45/100
- **Qué es:** QuantHarness, sistema multiagente con LLM para trading de alta frecuencia guiado por precios, de investigadores de Stony Brook, CMU, UBC, Yale y Fudan. Licencia MIT.
- **Cuándo elegirlo:** Casos: Estudiar agentes que interpretan gráficos; Comparar componentes de un análisis experimental.
- **Requisitos:** nivel 2: preparación media, requiere clave de API; Python; checkout; datos; modelo con entrada de imagen y credenciales; hardware prerequisites; API de IA: sí; Python; checkout; datos; modelo con entrada de imagen y credenciales.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -r requirements.txt` — fuente: https://github.com/Y-Research-SBU/QuantHarness/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Reproduce una evaluación histórica pequeña y revisa los gráficos que recibe cada agente Éxito: Puedes separar datos del periodo, análisis visual y decisión generada
- **Combina con:** `langgraph` [3/py], `langchain` [3/py], `langfuse` [23/observabilidad]
- **Riesgos y avisos:** Sin alternativas declaradas. Prototipo académico. Riesgo financiero: no es asesoramiento de inversión. El resultado de investigación no acredita ejecución HFT ni rendimiento futuro; no se confirma aquí un backend local compatible con todo el flujo.

### PolyWeather (`polyweather`)

- **Repo:** https://github.com/yangyuan-zhen/PolyWeather · AGPL-3.0 · nivel 2 · —/100
- **Qué es:** Reúne datos meteorológicos y de mercados de predicción para explorar cómo las previsiones afectan a contratos relacionados con el clima.
- **Cuándo elegirlo:** Casos: Contrastar una previsión con un mercado de ejemplo.; Comparar dos lugares con datos públicos sin abrir operaciones.
- **Requisitos:** nivel 2: preparación sencilla, app o instalador listo para usar, varios servicios con Docker Compose; Python, Dockerfile, docker-compose.yml, pyproject.toml, requirements.txt; API de IA: no; Docker Compose o el entorno documentado y fuentes meteorológicas o de mercado de prueba..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/yangyuan-zhen/PolyWeather/blob/d3a02039208f88860cbe02e0846a8a23783b220a/README.md
- **Primera prueba propuesta (no ejecutada):** Abre una vista de datos de prueba y compara fechas de previsión y mercado. Éxito: Puedes identificar la fuente, zona y fecha de los datos mostrados.
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La ficha se limita al análisis; datos, servicios externos y condiciones comerciales se revisan por separado. El código indicado es AGPL-3.0.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-14-agentes.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Agentes de investigación financiera», lee `docs/alexandria/categoria-14-agentes.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-14-agentes.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
