# Alexandría para agentes · Bots y conexiones a exchanges

Categoría 14 «Investigar finanzas y mercados» › subcategoría `bots`. 6 repos. Generado el 2026-11-26 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=14&sub=bots · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `ccxt` | Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar… | 2 Intermedio | 81 | MIT (OSI permisiva) | sin grupo |
| `freqtrade` | Bot de trading de criptomonedas con herramientas para preparar estrategias… | 2 Intermedio | 79 | GPL-3.0 (OSI copyleft) | sin grupo |
| `hummingbot` | Software para desarrollar y ejecutar bots de trading de criptomonedas mediante… | 2 Intermedio | 69 | Apache-2.0 (OSI permisiva) | sin grupo |
| `py-sdk` | SDK Python de Polymarket para integrar funciones de su plataforma mediante las… | 2 Intermedio | 54 | MIT (OSI permisiva) | sin grupo |
| `open-sol-bot` | Bot abierto de Solana que reúne seguimiento de operaciones y funciones de… | 3 Avanzado | 43 | Apache-2.0 (OSI permisiva) | sin grupo |
| `binance-trader` | Bot experimental de Python para estudiar estrategias y automatización con la… | 2 Intermedio | 33 | — (sin licencia detectada) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### ccxt (`ccxt`)

- **Repo:** https://github.com/ccxt/ccxt · MIT · nivel 2 · 81/100
- **Qué es:** CCXT, librería que unifica las APIs de más de 100 exchanges de criptomonedas y mercados de predicción. Licencia MIT. Es muy madura (~45k estrellas, v4.5.92).
- **Cuándo elegirlo:** Casos: Unificar consultas de varios mercados; Construir una integración de datos de exchange.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Node o paquete de tu lenguaje; exchange elegido; credenciales solo para funciones privadas; hardware prerequisites; API de IA: no; Node o paquete de tu lenguaje; exchange elegido; credenciales solo para funciones privadas.
- **Instalación (documentada en la fuente; no ejecutada):** `npm install ccxt` — fuente: https://github.com/ccxt/ccxt/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Consulta mercados públicos y verifica símbolo, precisión y límites sin habilitar trading Éxito: Puedes contrastar metadatos con la documentación del exchange
- **Combina con:** `freqtrade`, `vectorbt` [14/cuant], `claude-code` [20/terminal]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero: usa claves sin permiso de retiro. El MCP stdio deja capacidades sensibles como opt-in; instalar la biblioteca no exige habilitar órdenes ni retiros.

### freqtrade (`freqtrade`)

- **Repo:** https://github.com/freqtrade/freqtrade · GPL-3.0 · nivel 2 · 79/100
- **Qué es:** Freqtrade, bot de trading de criptomonedas en Python. Licencia GPL-3.0. Es muy maduro (~57k estrellas, 2026.10).
- **Cuándo elegirlo:** Casos: Comparar una regla en datos históricos; Evaluar una estrategia en simulación.
- **Requisitos:** nivel 2: preparación media; Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run; hardware prerequisites; API de IA: opcional; Docker o entorno de la guía; datos; estrategia de ejemplo; modo dry-run.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install freqtrade` — fuente: https://github.com/freqtrade/freqtrade/blob/develop/docs/installation.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta un backtest pequeño y revisa comisiones y sesgos antes de pasar a dry-run Éxito: Puedes reproducir operaciones simuladas y su configuración
- **Combina con:** `ccxt`, `vectorbt` [14/cuant], `grafana` [10/bi]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero alto: empieza en dry-run. Backtest y dry-run son fases distintas; no conectes resultados históricos con una promesa de rendimiento futuro.

### hummingbot (`hummingbot`)

- **Repo:** https://github.com/hummingbot/hummingbot · Apache-2.0 · nivel 2 · 69/100
- **Qué es:** Hummingbot, framework open source para diseñar y ejecutar bots de trading en exchanges centralizados y descentralizados. Licencia Apache-2.0. Es maduro (~21k estrellas, v2.17.0) y recibe patrocinio de exchanges mediante acuerdos de broker.
- **Cuándo elegirlo:** Casos: Estudiar un conector de exchange; Evaluar un bot en un entorno de práctica.
- **Requisitos:** nivel 2: preparación media; Conda o Docker; dependencias de compilación; conector y estrategia de prueba; hardware prerequisites; API de IA: no; Conda o Docker; dependencias de compilación; conector y estrategia de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/hummingbot/hummingbot/blob/master/README.md

  ```bash
  # Clone the repository
  git clone https://github.com/hummingbot/hummingbot.git
  cd hummingbot

  # Create the conda environment, build extensions, and expose the `hbot` CLI
  make install

  # Activate the environment
  conda activate hummingbot
  hbot --help
  ```
- **Primera prueba propuesta (no ejecutada):** Comprueba la instalación con ayuda del CLI y configura una estrategia en paper trade según su guía Éxito: Puedes distinguir ejecución simulada y conexiones reales
- **Combina con:** `ccxt`, `claude-code` [20/terminal], `grafana` [10/bi]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero alto; los patrocinios de exchanges pueden sesgar la oferta de conectores. El CLI y Gateway tienen papeles distintos; instalar el código no deja preparada una estrategia segura ni verificada.

### py-sdk (`py-sdk`)

- **Repo:** https://github.com/Polymarket/py-sdk · MIT · nivel 2 · 54/100
- **Qué es:** SDK oficial de Polymarket para Python (`polymarket-client`). Licencia MIT. Es reciente y pequeño (~150 estrellas, polymarket-client-v0.18.0).
- **Cuándo elegirlo:** Casos: Estudiar la API pública de Polymarket; Preparar una migración desde el cliente antiguo.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv o pip; API y permisos según función; consulta de datos públicos; hardware prerequisites; API de IA: no; Python y uv o pip; API y permisos según función; consulta de datos públicos.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add polymarket-client` — fuente: https://github.com/Polymarket/py-sdk/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Enumera datos públicos de un mercado y revisa su esquema sin autenticar una wallet Éxito: Puedes contrastar identificadores y datos con la fuente
- **Combina con:** `ccxt`, `nautilus-trader` [14/cuant], `activepieces` [1/motores]
- **Riesgos y avisos:** Sin alternativas declaradas. Riesgo financiero: no es asesoramiento de inversión. El paquete se llama polymarket-client; datos públicos y funciones autenticadas de cuenta o wallet tienen requisitos separados.

### open-sol-bot (`open-sol-bot`)

- **Repo:** https://github.com/ChainBuff/open-sol-bot · Apache-2.0 · nivel 3 · 43/100
- **Qué es:** OpenSolBot, bot de trading en la cadena Solana, de ChainBuff. Licencia Apache-2.0. Es pequeño (~400 estrellas, v0.2.1) y su último cambio es de diciembre de 2025; su README está en chino.
- **Cuándo elegirlo:** Casos: Estudiar un bot de seguimiento on-chain; Revisar una integración de Telegram con blockchain.
- **Requisitos:** nivel 3: preparación pesada, varios servicios con Docker Compose; Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones; hardware prerequisites; API de IA: no; Dependencias y Docker según guía; RPC Solana; configuración Telegram; wallet solo para operaciones.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up -d` — fuente: https://github.com/ChainBuff/open-sol-bot/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Examina configuración y rutas de órdenes antes de conectar una wallet o habilitar seguimiento Éxito: Puedes identificar las acciones que consultarían datos y las que moverían fondos
- **Combina con:** `grafana` [10/bi], `activepieces` [1/motores], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Sin alternativas declaradas. No apto para producción, según su autor. Riesgo muy alto con claves privadas. Riesgo financiero: no es asesoramiento de inversión. Es un bot con capacidad de ejecución; no se confirma una ruta de paper trading en las fuentes revisadas.

### binance-trader (`binance-trader`)

- **Repo:** https://github.com/yasinkuyu/binance-trader · — · nivel 2 · 33/100
- **Qué es:** Binance Trader, bot experimental de Python para operar en Binance, de @yasinkuyu. El README declara MIT pero el repo no tiene archivo de licencia que GitHub detecte. Tiene ~3k estrellas y su última versión (v1.1.0) es de enero de 2026.
- **Cuándo elegirlo:** Casos: Estudiar una estrategia de ejemplo; Analizar cómo se conecta un bot a un exchange.
- **Requisitos:** nivel 2: preparación media; Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado; hardware prerequisites; API de IA: no; Python y dependencias históricas; API Binance solo para funciones privadas; entorno aislado.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/yasinkuyu/binance-trader/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Examina la configuración y localiza las llamadas de lectura y de creación de órdenes sin activar el bot Éxito: Puedes identificar qué credenciales y acciones afectarán una cuenta
- **Combina con:** `ccxt`, `vectorbt` [14/cuant], `coolify` [22/infraestructura]
- **Riesgos y avisos:** Sin alternativas declaradas. Proyecto experimental. Riesgo financiero: no es asesoramiento de inversión. Bot experimental con documentación antigua; no se confirma que sus endpoints funcionen hoy ni que tenga una simulación completa.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-14-bots.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Bots y conexiones a exchanges», lee `docs/alexandria/categoria-14-bots.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-14-bots.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
