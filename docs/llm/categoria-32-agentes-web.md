# Alexandría para agentes · Herramientas de navegación para agentes

Categoría 32 «Navegadores y automatización web» › subcategoría `agentes-web`. 8 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=32&sub=agentes-web · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `browser-use` | Librería Python para que los LLM usen un navegador real y actúen en páginas sin… | 2 Intermedio | 73 | MIT (OSI permisiva) | recomendado |
| `agent-browser` | CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias… | 1 Básico | 63 | Apache-2.0 (OSI permisiva) | recomendado |
| `stagehand` | SDK de Browserbase para automatizar el navegador mezclando código con acciones… | 2 Intermedio | 61 | MIT (OSI permisiva) | alternativa |
| `browser-harness` | Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu… | 1 Básico | 60 | MIT (OSI permisiva) | alternativa |
| `skyvern` | Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. | 2 Intermedio | 60 | AGPL-3.0 (OSI copyleft) | alternativa |
| `nanobrowser` | Extensión de Chrome con un agente de IA que navega, hace clic y rellena… | 1 Básico | 59 | Apache-2.0 (OSI permisiva) | sin grupo |
| `playwright-cli` | Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les… | 1 Básico | 57 | Apache-2.0 (OSI permisiva) | alternativa |
| `steel-browser` | API de navegador autoalojable para agentes y apps: sesiones de Chrome con… | 2 Intermedio | 56 | Apache-2.0 (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### browser-use (`browser-use`)

- **Repo:** https://github.com/browser-use/browser-use · MIT · nivel 2 · 73/100 · recomendado en «Agentes que navegan la web»
- **Qué es:** Browser Use, agente de navegador open source de browser-use. La librería Python es MIT; la inferencia y los navegadores alojados son de pago. Es muy popular (~121k estrellas, v1.0.6).
- **Cuándo elegirlo:** Casos: Extraer información de una web propia; Probar navegación con un agente.
- **Requisitos:** nivel 2: preparación media, requiere programar con él; Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba; hardware prerequisites; API de IA: opcional; Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `uv add 'browser-use==1.0.6'` — fuente: https://github.com/browser-use/browser-use/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un navegador de prueba y solicita leer una página sin enviar formularios ni usar cuentas personales Éxito: Puedes revisar pestaña, contexto y resultado
- **Combina con:** `claude-code` [20/terminal], `ollama` [8/motores], `pydantic-ai` [3/py], `sandbox` [22/infra], `openmanus` [3/py], `steel-browser`
- **Alternativas:** `stagehand`, `skyvern`, `browser-harness`, `computer-use-preview`, `playwright-mcp`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): computer-use-preview, stagehand, skyvern, playwright-mcp, browser-harness. La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta.

### agent-browser (`agent-browser`)

- **Repo:** https://github.com/vercel-labs/agent-browser · Apache-2.0 · nivel 1 · 63/100 · recomendado en «CLIs de navegador para agentes»
- **Qué es:** agent-browser, CLI nativa en Rust para que agentes controlen un navegador comando a comando, de Vercel Labs. Licencia Apache-2.0. Creado en enero de 2026, tiene ~52k estrellas (v0.43.0).
- **Cuándo elegirlo:** Casos: Verificar una interfaz; Preparar capturas y consultas de una página.
- **Requisitos:** nivel 1: preparación sencilla; Node; Chrome for Testing o navegador configurado; agente opcional; hardware prerequisites; API de IA: no; Node; Chrome for Testing o navegador configurado; agente opcional.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/vercel-labs/agent-browser/blob/main/README.md

  ```bash
  npm install -g agent-browser
  agent-browser install           # download Chrome for Testing (first time only)
  ```
- **Primera prueba propuesta (no ejecutada):** Abre una página propia y consulta el árbol de accesibilidad antes de actuar Éxito: Puedes identificar referencias de elementos y cambios tras una acción
- **Combina con:** `claude-code` [20/terminal], `lightpanda` [32/motores-web], `chrome-devtools-mcp` [5/servidores]
- **Alternativas:** `playwright-cli`
- **Riesgos y avisos:** Alternativas (elige una): playwright-cli. Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales.

### Stagehand (`stagehand`)

- **Repo:** https://github.com/browserbase/stagehand · MIT · nivel 2 · 61/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Stagehand, SDK para agentes de navegador de Browserbase. Licencia MIT. Es maduro y activo (~26k estrellas, v3.x).
- **Cuándo elegirlo:** Casos: Prototipar extracción estructurada; Automatizar un formulario de prueba.
- **Requisitos:** nivel 2: preparación sencilla, requiere programar con él, requiere clave de API; Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba; hardware prerequisites; API de IA: sí; Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pnpm add @browserbasehq/stagehand 'zod@~4.4.3'` — fuente: https://github.com/browserbase/stagehand/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Extrae dos campos de una página propia y contrasta la estructura con el contenido visible Éxito: Puedes comprobar datos y acciones del navegador
- **Combina con:** `claude-code` [20/terminal], `lightpanda` [32/motores-web], `firecrawl` [4/crawlers], `steel-browser`
- **Alternativas:** `browser-use`, `skyvern`, `browser-harness`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): browser-use, skyvern. La nube de Browserbase es de pago. El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación.

### Browser Harness (`browser-harness`)

- **Repo:** https://github.com/browser-use/browser-harness · MIT · nivel 1 · 60/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Browser Harness, harness con el que Claude Code, Codex o Cursor usan tu Chrome real con tu sesión iniciada, de browser-use. Licencia MIT. Creado en abril de 2026 (~19k estrellas, v0.1.13); ahora es el motor de Browser Use y se recomienda…
- **Cuándo elegirlo:** Casos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio.
- **Requisitos:** nivel 1: preparación sencilla; Browser Use CLI actual; Chrome y perfil de prueba; cliente agente; hardware prerequisites; API de IA: no; Browser Use CLI actual; Chrome y perfil de prueba; cliente agente.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/browser-use/browser-harness/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un perfil de prueba y solicita solo leer el título de una página Éxito: Puedes identificar qué navegador y sesión expone al agente
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `gemini-cli` [20/terminal]
- **Alternativas:** `browser-use`, `stagehand`, `skyvern`, `playwright-mcp`, `chrome-devtools-mcp`
- **Riesgos y avisos:** Alternativas (elige una): playwright-mcp, chrome-devtools-mcp, browser-use. Riesgo: acceso del agente a sesiones autenticadas. Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer.

### Skyvern (`skyvern`)

- **Repo:** https://github.com/Skyvern-AI/skyvern · AGPL-3.0 · nivel 2 · 60/100 · alternativa en «Agentes que navegan la web»
- **Qué es:** Skyvern, automatización de flujos web con LLMs y visión por computador, de Skyvern-AI. Licencia AGPL-3.0, con versión cloud gestionada. Tiene ~23k estrellas (v1.0.58).
- **Cuándo elegirlo:** Casos: Automatizar un flujo propio; Evaluar extracción basada en visión.
- **Requisitos:** nivel 2: preparación media; Python; browser; proveedor o modelo local Ollama; flujo de prueba; hardware prerequisites; API de IA: opcional; Python; browser; proveedor o modelo local Ollama; flujo de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** `pip install "skyvern[server]"` — fuente: https://github.com/Skyvern-AI/skyvern/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Define una tarea de lectura de página y revisa acciones y extracción antes de permitir envíos Éxito: Puedes contrastar los pasos con la web
- **Combina con:** `playwright` [32/bibliotecas], `ollama` [8/motores], `activepieces` [1/motores]
- **Alternativas:** `browser-use`, `stagehand`, `browser-harness`, `computer-use-preview`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): browser-use, stagehand, computer-use-preview. Telemetría activa por defecto. Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios.

### Nanobrowser (`nanobrowser`)

- **Repo:** https://github.com/nanobrowser/nanobrowser · Apache-2.0 · nivel 1 · 59/100
- **Qué es:** Extensión de código abierto (Apache-2.0), gratuita y alternativa abierta a agentes web comerciales. Muy activa.
- **Cuándo elegirlo:** Casos: automatizar tareas repetitivas en webs donde ya tienes la sesión iniciada; investigar y resumir información de varias páginas desde el panel lateral. Evítalo si necesitas una herramienta estable y auditada para datos sensibles.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; TypeScript, package.json; hardware model_dependent; API de IA: opcional; Un sistema compatible y una copia de datos o archivos para la primera prueba..
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/nanobrowser/nanobrowser.git` — fuente: https://github.com/nanobrowser/nanobrowser/blob/master/README.md
- **Primera prueba propuesta (no ejecutada):** Instala Nanobrowser desde la Chrome Web Store, configura una clave de API o Ollama y pide una tarea sencilla en el panel lateral. Éxito: El agente abre las páginas y realiza la tarea en una pestaña propia.
- **Combina con:** `ollama` [8/motores], `llama-cpp` [8/motores], `vllm` [23/serving], `puppeteer` [32/bibliotecas]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Con modelos locales, el README recomienda tareas simples y un contexto de 16k tokens o más.

### playwright-cli (`playwright-cli`)

- **Repo:** https://github.com/microsoft/playwright-cli · Apache-2.0 · nivel 1 · 57/100 · alternativa en «CLIs de navegador para agentes»
- **Qué es:** Playwright CLI, CLI de Playwright con skills para agentes de código, de Microsoft. Licencia Apache-2.0. Tiene ~15k estrellas (v0.1.x).
- **Cuándo elegirlo:** Casos: Probar un flujo con un agente; Registrar una secuencia de navegación.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node; navegador; agente con shell; aplicación de prueba; hardware prerequisites; API de IA: no; Node; navegador; agente con shell; aplicación de prueba.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/microsoft/playwright-cli/blob/main/README.md

  ```bash
  npm install -g @playwright/cli@latest
  playwright-cli --help
  ```
- **Primera prueba propuesta (no ejecutada):** Instala sus skills y abre una página de prueba para obtener snapshot antes de pulsar un control Éxito: Puedes usar referencias del snapshot y comprobar el resultado
- **Combina con:** `playwright` [32/bibliotecas], `claude-code` [20/terminal], `playwright-mcp` [5/servidores]
- **Alternativas:** `agent-browser`
- **Riesgos y avisos:** Alternativas (elige una): agent-browser. Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo.

### Steel Browser (`steel-browser`)

- **Repo:** https://github.com/steel-dev/steel-browser · Apache-2.0 · nivel 2 · 56/100
- **Qué es:** Proyecto de código abierto (Apache-2.0) de Steel, la base autoalojable de su servicio comercial Steel Cloud. Muy activo.
- **Cuándo elegirlo:** Casos: dar a un agente de IA un navegador aislado y persistente sin montar infraestructura; extraer páginas o capturas mediante una API REST propia.
- **Requisitos:** nivel 2: preparación media; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: no.
- **Instalación (documentada en la fuente; no ejecutada):** `docker run -p 3000:3000 -p 9223:9223 ghcr.io/steel-dev/steel-browser` — fuente: https://github.com/steel-dev/steel-browser/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Ejecuta el contenedor con Docker y abre la interfaz en `http://localhost:3000/ui` o llama a la API en el puerto 3000. Éxito: Puedes crear una sesión y conectar Puppeteer o Playwright a ella.
- **Combina con:** `puppeteer` [32/bibliotecas], `playwright` [32/bibliotecas], `selenium` [32/bibliotecas], `browser-use`, `stagehand`, `webdriverio` [32/bibliotecas]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-32-agentes-web.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Herramientas de navegación para agentes», lee `docs/alexandria/categoria-32-agentes-web.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-32-agentes-web.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
