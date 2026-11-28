# Alexandría para agentes · Modelos y backtesting cuantitativo

Categoría 14 «Investigar finanzas y mercados» › subcategoría `cuant`. 9 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=14&sub=cuant · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `openbb` | Plataforma abierta de datos financieros (ODP): conecta fuentes públicas y con… | 2 Intermedio | 74 | Apache-2.0 (OSI permisiva) | sin grupo |
| `nautilus-trader` | Motor de trading y backtesting con arquitectura orientada a eventos para… | 2 Intermedio | 71 | LGPL-3.0 (OSI copyleft) | sin grupo |
| `yfinance` | Biblioteca Python no oficial para descargar datos de mercado y fundamentales de… | 2 Intermedio | 70 | Apache-2.0 (OSI permisiva) | sin grupo |
| `qlib` | Plataforma de Microsoft para investigación cuantitativa con datos, modelos y… | 3 Avanzado | 65 | MIT (OSI permisiva) | sin grupo |
| `lumibot` | Framework de Python para desarrollar estrategias, realizar backtesting y… | 2 Intermedio | 56 | GPL-3.0 (OSI copyleft) | sin grupo |
| `vectorbt` | Biblioteca de análisis cuantitativo para explorar señales y comparar… | 2 Intermedio | 56 | Apache-2.0 + Commons Clause (source-available) | recomendado |
| `finrl` | Biblioteca y ejemplos para investigar estrategias de trading mediante… | 3 Avanzado | 54 | MIT (OSI permisiva) | sin grupo |
| `backtesting-py` | Framework ligero de Python para hacer backtesting de estrategias de trading… | 2 Intermedio | 52 | AGPL-3.0 (OSI copyleft) | alternativa |
| `prediction-market-backtesting` | Añade ejemplos y componentes de backtesting para analizar mercados de… | 2 Intermedio | 32 | MIT y LGPL-3.0-or-later según archivo (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### OpenBB Open Data Platform (`openbb`)

- **Repo:** https://github.com/openbq-org/OpenBB · Apache-2.0 · nivel 2 · 74/100
- **Qué es:** Conjunto de herramientas de datos de código abierto (Apache-2.0) creado por OpenBB. Desde octubre de 2026 lo custodia OpenBQ, una organización sin ánimo de lucro anunciada por OpenBB y liderada desde BrightQuery; por eso el repositorio…
- **Cuándo elegirlo:** Casos: descargar series de precios o datos macro en un DataFrame para análisis; dar a un agente acceso a datos financieros mediante el servidor MCP de OpenBB.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install openbb` — fuente: https://github.com/openbq-org/OpenBB/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install openbb` y descarga el histórico de precios de un símbolo con `obb.equity.price.historical`. Éxito: Obtienes un DataFrame con fechas y precios del proveedor configurado.
- **Combina con:** `claude-code` [20/terminal], `jupyterlab` [25/datos], `vectorbt`, `backtesting-py`
- **Riesgos y avisos:** El README todavía enlaza a OpenBB-finance/OpenBB; la API de GitHub redirige el mismo repositorio (id 323048702) a openbq-org/OpenBB, y openbb.co confirma el….

### nautilus_trader (`nautilus-trader`)

- **Repo:** https://github.com/nautechsystems/nautilus_trader · LGPL-3.0 · nivel 2 · 71/100
- **Qué es:** NautilusTrader, motor de trading y backtesting de alto rendimiento nativo en Rust con API de Python, de Nautech Systems. Licencia LGPL-3.0. Es muy activo (~32k estrellas, v1.231.0).
- **Cuándo elegirlo:** Casos: Estudiar un motor orientado a eventos; Comparar simulaciones con datos registrados.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba; hardware prerequisites; API de IA: no; CPython 3.13–3.15 para wheels v2 revisadas; entorno virtual; datos de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U nautilus_trader --pre` — fuente: https://github.com/nautechsystems/nautilus_trader/blob/develop/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta un ejemplo de backtest de la misma versión v2 y revisa su secuencia de eventos Éxito: Puedes reproducir órdenes y fills simulados con configuración fija
- **Combina con:** `polars` [25/datos], `marimo` [25/apps], `ccxt` [14/bots], `py-sdk` [14/bots]
- **Riesgos y avisos:** Sin alternativas declaradas. Curva de aprendizaje alta; la rama 2.0 aún es prerelease. La rama y docs revisadas son v2 RC y piden --pre; sin él se instala v1 con otra API; el autor desaconseja RC para capital real.

### yfinance (`yfinance`)

- **Repo:** https://github.com/ranaroussi/yfinance · Apache-2.0 · nivel 2 · 70/100
- **Qué es:** Biblioteca de código abierto (Apache-2.0) creada por Ran Aroussi, muy usada en investigación y educación. No está afiliada ni respaldada por Yahoo, Inc.
- **Cuándo elegirlo:** Casos: descargar históricos de precios para un estudio o backtest; obtener fundamentales y dividendos de una cartera en un cuaderno.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install yfinance` — fuente: https://github.com/ranaroussi/yfinance/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install yfinance` y descarga un año de precios de un símbolo con `Ticker(...).history`. Éxito: Obtienes un DataFrame con precios OHLC, volumen y fechas.
- **Combina con:** `vectorbt`, `backtesting-py`, `jupyterlab` [25/datos]
- **Riesgos y avisos:** Para usos profesionales, considera un proveedor de datos con licencia.

### qlib (`qlib`)

- **Repo:** https://github.com/microsoft/qlib · MIT · nivel 3 · 65/100
- **Qué es:** Qlib, plataforma de investigación cuantitativa orientada a IA de Microsoft. Licencia MIT. Es madura (~50k estrellas, v0.9.8).
- **Cuándo elegirlo:** Casos: Comparar modelos sobre datos temporales; Investigar un pipeline cuantitativo reproducible.
- **Requisitos:** nivel 3: preparación pesada; Python compatible con baseline; datos históricos; dependencias del modelo; hardware prerequisites; API de IA: opcional; Python compatible con baseline; datos históricos; dependencias del modelo.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install pyqlib` — fuente: https://github.com/microsoft/qlib/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta una baseline pequeña sobre un periodo de prueba separado y revisa predicciones y evaluación Éxito: Puedes reproducir resultados sin mezclar datos futuros
- **Combina con:** `mlflow` [23/observabilidad], `finrl`, `marimo` [25/apps], `finceptterminal` [14/agentes], `machine-learning-for-trading` [14/aprender]
- **Riesgos y avisos:** Sin alternativas declaradas. Revisa la guía de migración de artefactos antes de actualizar desde el código. Los baselines no comparten siempre versiones de Python; los cambios recientes del recorder requieren revisar la migración.

### lumibot (`lumibot`)

- **Repo:** https://github.com/Lumiwealth/lumibot · GPL-3.0 · nivel 2 · 56/100
- **Qué es:** LumiBot, framework de Python para crear bots y agentes de trading, de Lumiwealth. Licencia GPL-3.0. Tiene ~2k estrellas (v4.6.73) y promociona su nube BotSpot y su MCP.
- **Cuándo elegirlo:** Casos: Comparar una estrategia de reglas; Estudiar decisiones de una estrategia AI en backtest.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python >=3.10; datos históricos; proveedor solo para estrategia AI; broker solo si lo eliges; hardware prerequisites; API de IA: opcional; Python >=3.10; datos históricos; proveedor solo para estrategia AI; broker solo si lo eliges.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install lumibot` — fuente: https://github.com/Lumiwealth/lumibot/blob/dev/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el ejemplo de reglas sobre historia y revisa operaciones y costes del backtest Éxito: Puedes reproducir la estrategia sin llamadas AI ni órdenes reales
- **Combina con:** `claude-code` [20/terminal], `ollama` [8/motores], `vectorbt`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Sin alternativas declaradas. Riesgo financiero; el README empuja hacia servicios de pago de la empresa. El asistente que escribe código y los agentes dentro de la estrategia son procesos distintos; no comparten automáticamente presupuesto.

### vectorbt (`vectorbt`)

- **Repo:** https://github.com/polakowo/vectorbt · Apache-2.0 + Commons Clause · nivel 2 · 56/100 · recomendado en «Backtesting en Python»
- **Qué es:** VectorBT, toolkit de Python para investigación de trading a escala, de @polakowo. Licencia Apache-2.0 con Commons Clause, «fair-code» que no permite vender el software (GitHub muestra NOASSERTION).
- **Cuándo elegirlo:** Casos: Comparar indicadores en una serie; Explorar sensibilidad de una regla histórica.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas; hardware prerequisites; API de IA: no; Python; dependencias compatibles; serie histórica; comisiones y frecuencia definidas.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install -U vectorbt` — fuente: https://github.com/polakowo/vectorbt/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Evalúa unas pocas combinaciones y reserva un periodo fuera de muestra Éxito: Puedes revisar parámetros, operaciones y resultados separados de entrenamiento
- **Combina con:** `ccxt` [14/bots], `freqtrade` [14/bots], `marimo` [25/apps]
- **Alternativas:** `backtesting-py`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia no OSI: revisa las condiciones de uso y redistribución. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Commons Clause: no es open source según la OSI. Probar muchas combinaciones aumenta el riesgo de sobreajuste; sus mensajes comerciales no acreditan una ventaja en tu caso.

### FinRL (`finrl`)

- **Repo:** https://github.com/AI4Finance-Foundation/FinRL · MIT · nivel 3 · 54/100
- **Qué es:** FinRL, el framework open source de aprendizaje por refuerzo para finanzas, de AI4Finance Foundation. Licencia MIT; la marca FinRL pertenece a FinRL LLC.
- **Cuándo elegirlo:** Casos: Estudiar entornos de RL financiero; Comparar políticas en simulación histórica.
- **Requisitos:** nivel 3: preparación pesada, requiere programar con él; Python y dependencias de la guía; datos; entorno de entrenamiento; hardware prerequisites; API de IA: no; Python y dependencias de la guía; datos; entorno de entrenamiento.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/AI4Finance-Foundation/FinRL/blob/master/README.md

  ```bash
  git clone https://github.com/AI4Finance-Foundation/FinRL.git
  cd FinRL

  pip install -e .
  ```
- **Primera prueba propuesta (no ejecutada):** Ejecuta un ejemplo pequeño de aprendizaje por refuerzo y evalúa en un periodo distinto Éxito: Puedes contrastar recompensas, operaciones simuladas y datos de prueba
- **Combina con:** `qlib`, `machine-learning-for-trading` [14/aprender], `vectorbt`
- **Riesgos y avisos:** Sin alternativas declaradas. Uso académico: no es asesoramiento financiero. El autor enlaza FinRL-X como evolución; mantén versiones y documentación correspondientes a este repositorio.

### Backtesting.py (`backtesting-py`)

- **Repo:** https://github.com/kernc/backtesting.py · AGPL-3.0 · nivel 2 · 52/100 · alternativa en «Backtesting en Python»
- **Qué es:** Biblioteca de backtesting de código abierto (AGPL-3.0) creada por kernc. Madura, con ritmo de cambios bajo (último push en agosto de 2026).
- **Cuándo elegirlo:** Casos: probar una estrategia de cruce de medias sobre datos históricos; optimizar parámetros de una estrategia y ver el resultado en un gráfico interactivo.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él; Python, pyproject.toml, requirements.txt, setup.py; API de IA: no; Un entorno de desarrollo compatible con el lenguaje y los requisitos del README..
- **Instalación (documentada en la fuente; no ejecutada):** `pip install backtesting` — fuente: https://github.com/kernc/backtesting.py/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala con `pip install backtesting` y ejecuta el ejemplo SmaCross de la documentación. Éxito: Obtienes estadísticas del backtest y un gráfico interactivo con operaciones.
- **Combina con:** `yfinance`, `jupyterlab` [25/datos], `claude-code` [20/terminal], `openbb`
- **Alternativas:** `vectorbt`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): vectorbt. Los resultados de backtest no anticipan resultados reales.

### Prediction Market Backtesting (`prediction-market-backtesting`)

- **Repo:** https://github.com/evan-kolberg/prediction-market-backtesting · MIT y LGPL-3.0-or-later según archivo · nivel 2 · 32/100
- **Qué es:** Añade ejemplos y componentes de backtesting para analizar mercados de predicción con datos y estrategias históricas.
- **Cuándo elegirlo:** Casos: Comparar dos supuestos de comisiones con datos pasados.; Medir cómo cambia una simulación si mueves el intervalo de prueba.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python, Cargo.toml, Makefile; API de IA: no; Entorno compatible con NautilusTrader y datos históricos de una muestra..
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://evan-kolberg.github.io/prediction-market-backtesting/license/
- **Primera prueba propuesta (no ejecutada):** Ejecuta el ejemplo introductorio con pocos datos históricos y sin credenciales de trading. Éxito: Obtienes un resultado reproducible para el conjunto de datos utilizado.
- **Riesgos y avisos:** Usa solo simulación. La licencia y atribuciones tienen alcances distintos por componente; lee las notas antes de redistribuir.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-14-cuant.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Modelos y backtesting cuantitativo», lee `docs/alexandria/categoria-14-cuant.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-14-cuant.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
