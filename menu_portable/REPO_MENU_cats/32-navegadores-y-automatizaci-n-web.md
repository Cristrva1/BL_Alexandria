# 32. Navegadores y automatización web — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `agent-browser`
role=app · exec=local · setup=easy · mcp=True · prov=— · tags=navegador,rust

**Qué es:** CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes.
**Stack:** Node; Chrome for Testing o navegador configurado; agente opcional
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El CLI y MCP no requieren modelo propio; el agente y proveedores remotos tienen costes independientes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Incluye skill portable y MCP stdio; descargar el browser es un paso separado y el perfil de pruebas evita mezclar sesiones personales
- Coste: Sin pago a un modelo en la ruta básica. El CLI y MCP no requieren modelo propio; el agente y proveedores remotos tienen costes independientes
- Equipo: Preparación según la ruta elegida. Node; Chrome for Testing o navegador configurado; agente opcional
**Repo:** https://github.com/vercel-labs/agent-browser

**Instalación** [+]:

```
npm install -g agent-browser
agent-browser install           # download Chrome for Testing (first time only)
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Verificar una interfaz; Preparar capturas y consultas de una página
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una página propia y consulta el árbol de accesibilidad antes de actuar
**Qué comprobar:** Puedes identificar referencias de elementos y cambios tras una acción
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `lightpanda`, `chrome-devtools-mcp`
**Alternativas (elige una):** `playwright-cli`

## `awesome-chrome-devtools`
role=directory · exec=local · setup=easy · mcp=False · prov=— · tags=navegador,awesome,awesome-list

**Qué es:** Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol.
**Stack:** Navegador; necesidad de depuración o automatización
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Consultar la lista no usa IA; cada proyecto enlazado tiene sus condiciones
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Un directorio que enlaza servidores MCP no es por sí mismo un servidor ni una integración con un agente
- Coste: Sin pago a un modelo en la ruta básica. Consultar la lista no usa IA; cada proyecto enlazado tiene sus condiciones
- Equipo: Preparación según la ruta elegida. Navegador; necesidad de depuración o automatización
**Repo:** https://github.com/ChromeDevTools/awesome-chrome-devtools

**Instalación** [?]:

```
Consultar el material original; elegir un ejemplo antes de instalar.
```

_Una referencia no se instala como un servicio único._

**Elige si:** Tu objetivo encaja con estos ejemplos: Encontrar una herramienta de depuración; Explorar clientes de DevTools Protocol
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escoge una herramienta de CDP y revisa su repositorio y función antes de instalar
**Qué comprobar:** Puedes distinguir protocolo, cliente y extensión
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `puppeteer`, `chrome-devtools-mcp`, `lightpanda`

## `browser-harness`
role=runtime · exec=local · setup=easy · mcp=True · prov=— · tags=browser,coding-agent,python

**Qué es:** Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada.
**Stack:** Browser Use CLI actual; Chrome y perfil de prueba; cliente agente
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El acceso al navegador propio no necesita API de modelo adicional; el agente y Cloud opcional se pagan aparte
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Ahora es el motor de Browser Use y el README recomienda su CLI; conectar una sesión autenticada concede acceso a lo que esa sesión puede hacer
- Coste: El coste depende del proveedor o la ruta. El acceso al navegador propio no necesita API de modelo adicional; el agente y Cloud opcional se pagan aparte
- Equipo: Preparación según la ruta elegida. Browser Use CLI actual; Chrome y perfil de prueba; cliente agente
**Repo:** https://github.com/browser-use/browser-harness

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/browser-use/browser-harness/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un agente con un browser propio; Inspeccionar una página autenticada de laboratorio
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un perfil de prueba y solicita solo leer el título de una página
**Qué comprobar:** Puedes identificar qué navegador y sesión expone al agente
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `browser-use`, `claude-code`, `codex`
**Alternativas (elige una):** `playwright-mcp`, `chrome-devtools-mcp`

## `browser-use`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,browser,python

**Qué es:** Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos.
**Stack:** Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. La biblioteca MIT permite navegador y modelo locales; los defaults del ejemplo usan gateway y browser Cloud facturados
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. La versión actual integra browser-harness y registra skills para Claude/Codex y MCP; una sesión con cookies puede actuar con los permisos de esa cuenta
- Coste: El coste depende del proveedor o la ruta. La biblioteca MIT permite navegador y modelo locales; los defaults del ejemplo usan gateway y browser Cloud facturados
- Equipo: Preparación según la ruta elegida. Python y uv; Chrome o browser Cloud; agente o proveedor; perfil de prueba
**Repo:** https://github.com/browser-use/browser-use

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/browser-use/browser-use/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Extraer información de una web propia; Probar navegación con un agente
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Conecta un navegador de prueba y solicita leer una página sin enviar formularios ni usar cuentas personales
**Qué comprobar:** Puedes revisar pestaña, contexto y resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `browser-harness`, `claude-code`, `ollama`
**Alternativas (elige una):** `computer-use-preview`, `stagehand`, `skyvern`, `playwright-mcp`

## `camofox-browser`
role=runtime · exec=hybrid · setup=medium · mcp=True · prov=— · tags=navegador,ai-agent,anti-bot,antidetect-browser,automation,bot-detection,browser-automation,cloudflare-bypass

**Qué es:** Servidor de automatización de navegador basado en Camoufox para ofrecer navegación a agentes.
**Stack:** Node o Docker; browser descargado; servidor REST; adapter MCP opcional; sitio de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El browser y adaptador no requieren API de modelo; hosting, proxy y agente tienen costes separados
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP stdio documenta Claude Code, Codex y Antigravity y necesita el servidor REST activo; stealth no garantiza acceso ni compatibilidad universal con las políticas de un sitio
- Coste: Sin pago a un modelo en la ruta básica. El browser y adaptador no requieren API de modelo; hosting, proxy y agente tienen costes separados
- Equipo: Preparación según la ruta elegida. Node o Docker; browser descargado; servidor REST; adapter MCP opcional; sitio de prueba
**Repo:** https://github.com/jo-inc/camofox-browser

**Instalación** [+]:

```
git clone https://github.com/jo-inc/camofox-browser && cd camofox-browser
npm install && npm start
# -> http://localhost:9377
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar automatización de una web propia; Evaluar una herramienta de navegación para agentes
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Arranca el servidor y consulta una página propia con snapshot antes de conectar cuentas
**Qué comprobar:** Puedes distinguir REST server, MCP adapter y sesión del browser
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `openclaw`, `yt-dlp`, `hermes-agent`

## `lightpanda`
role=runtime · exec=local · setup=easy · mcp=True · prov=— · tags=browser,scraping

**Qué es:** Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome.
**Stack:** Binario compatible o Docker; agente o proveedor opcional; sitio de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. El navegador y scripts deterministas no usan tokens; el agente integrado admite API, modelos locales y Codex con su cuenta
- Claude Code: Herramienta MCP para el agente
- Codex: Integración documentada por el proyecto
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelos locales documentados. Ofrece MCP stdio y HTTP; su compatibilidad con páginas no es idéntica a un navegador completo y menor consumo no garantiza funcionar en toda web
- Coste: El coste depende del proveedor o la ruta. El navegador y scripts deterministas no usan tokens; el agente integrado admite API, modelos locales y Codex con su cuenta
- Equipo: Preparación según la ruta elegida. Binario compatible o Docker; agente o proveedor opcional; sitio de prueba
**Repo:** https://github.com/lightpanda-io/browser

**Instalación** [?]:

```
Seguir la instalación original: https://github.com/lightpanda-io/browser/blob/main/README.md
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Preparar navegación headless; Explorar un agente con modelo local
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Ejecuta una consulta simple sin LLM y compara el DOM con la página esperada
**Qué comprobar:** Puedes identificar la sesión y el resultado antes de probar autonomía
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `puppeteer`, `playwright`, `stagehand`

## `playwright`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=automation,browser,typescript

**Qué es:** Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.
**Stack:** Node; navegadores descargados; aplicación de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. El MCP es el proyecto compañero playwright-mcp y el CLI otra superficie; instala la ruta adecuada en lugar de confundir biblioteca, skill y servidor
- Coste: Sin pago a un modelo en la ruta básica. Los tests y control básico no necesitan API de IA; agente y servicios de browser Cloud son independientes
- Equipo: Preparación según la ruta elegida. Node; navegadores descargados; aplicación de prueba
**Repo:** https://github.com/microsoft/playwright

**Instalación** [+]:

```
npm i -D @playwright/test
npx playwright install
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un formulario; Crear regresiones de una web
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Escribe un test que abra una página local y compruebe un título
**Qué comprobar:** Puedes distinguir fallo de aserción y fallo de arranque del navegador
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright-mcp`, `playwright-cli`, `lightpanda`, `crawlee`
**Alternativas (elige una):** `puppeteer`, `selenium`

## `playwright-cli`
role=skill · exec=hybrid · setup=easy · mcp=False · prov=— · tags=browser,typescript

**Qué es:** Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto.
**Stack:** Node; navegador; agente con shell; aplicación de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. El CLI no necesita API de IA propia; el agente usa su modelo o plan
- Claude Code: Dentro del agente: skills o instrucciones
- Codex: Dentro del agente: skills o instrucciones
- Antigravity: Dentro del agente: skills o instrucciones
- Modelos locales: La función básica no necesita un modelo. Los hosts compatibles pueden leer las skills instaladas; control por CLI y MCP son superficies distintas y las sesiones deben separarse al trabajar en paralelo
- Coste: El coste depende del proveedor o la ruta. El CLI no necesita API de IA propia; el agente usa su modelo o plan
- Equipo: Preparación según la ruta elegida. Node; navegador; agente con shell; aplicación de prueba
**Repo:** https://github.com/microsoft/playwright-cli

**Instalación** [+]:

```
npm install -g @playwright/cli@latest
playwright-cli --help
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Probar un flujo con un agente; Registrar una secuencia de navegación
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Instala sus skills y abre una página de prueba para obtener snapshot antes de pulsar un control
**Qué comprobar:** Puedes usar referencias del snapshot y comprobar el resultado
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `claude-code`, `playwright-mcp`
**Alternativas (elige una):** `agent-browser`

## `puppeteer`
role=library · exec=local · setup=easy · mcp=True · prov=— · tags=browser,scraping,typescript

**Qué es:** Librería de Google para controlar Chrome y Firefox desde Node.js.
**Stack:** Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. La biblioteca no exige API de IA; servicios remotos y modelo del agente tienen sus costes
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: La función básica no necesita un modelo. Puppeteer descarga Chrome y puppeteer-core no; el MCP recomendado es chrome-devtools-mcp, un proyecto compañero que se configura aparte
- Coste: Sin pago a un modelo en la ruta básica. La biblioteca no exige API de IA; servicios remotos y modelo del agente tienen sus costes
- Equipo: Preparación según la ruta elegida. Node; Chrome compatible o navegador propio con puppeteer-core; página de prueba
**Repo:** https://github.com/puppeteer/puppeteer

**Instalación** [+]:

```
npm i puppeteer # Downloads compatible Chrome during installation.
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar una captura; Extraer datos de una página propia
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una página de prueba y consulta su título o captura antes de añadir interacciones
**Qué comprobar:** Puedes comprobar navegador y salida obtenida
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `lightpanda`, `chrome-devtools-mcp`, `awesome-chrome-devtools`
**Alternativas (elige una):** `playwright`, `selenium`

## `selenium`
role=library · exec=local · setup=medium · mcp=False · prov=— · tags=browser,java,python

**Qué es:** Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes.
**Stack:** Lenguaje y bindings elegidos; navegador compatible; app de prueba
**Acceso y costes:**
- API de IA: Sin clave propia de API de IA en la ruta básica. No necesita modelos ni API de IA; infraestructura o servicios de pruebas Cloud se costean aparte
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. El README raíz está dirigido a contribuidores; para utilizar Selenium sigue el manual de usuario y no cambies políticas de Windows para compilar todo el proyecto
- Coste: Sin pago a un modelo en la ruta básica. No necesita modelos ni API de IA; infraestructura o servicios de pruebas Cloud se costean aparte
- Equipo: Preparación según la ruta elegida. Lenguaje y bindings elegidos; navegador compatible; app de prueba
**Repo:** https://github.com/SeleniumHQ/selenium

**Instalación** [?]:

```
Seguir la instalación original: https://selenium.dev/documentation/
```

_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar pruebas funcionales; Comparar comportamiento entre navegadores
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Abre una página de prueba y verifica un elemento mediante WebDriver
**Qué comprobar:** Puedes comprobar que la sesión controla el navegador correcto
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `mitmproxy`, `n8n`, `claude-code`
**Alternativas (elige una):** `playwright`, `puppeteer`

## `skyvern`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=browser,automation,python

**Qué es:** Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles.
**Stack:** Python; browser; proveedor o modelo local Ollama; flujo de prueba
**Acceso y costes:**
- API de IA: API de IA opcional. Autoalojar no incluye inferencia; API o Ollama según configuración y browser o Cloud tienen costes propios
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Antigravity: Integración no documentada
- Modelos locales: Modelos locales documentados. Usa LLM y visión; evitar selectores frágiles no garantiza funcionar sin errores en todos los sitios
- Coste: El coste depende del proveedor o la ruta. Autoalojar no incluye inferencia; API o Ollama según configuración y browser o Cloud tienen costes propios
- Equipo: Preparación según la ruta elegida. Python; browser; proveedor o modelo local Ollama; flujo de prueba
**Repo:** https://github.com/Skyvern-AI/skyvern

**Instalación** [+]:

```
pip install "skyvern[server]"
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Automatizar un flujo propio; Evaluar extracción basada en visión
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Define una tarea de lectura de página y revisa acciones y extracción antes de permitir envíos
**Qué comprobar:** Puedes contrastar los pasos con la web
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `playwright`, `ollama`, `n8n`
**Alternativas (elige una):** `browser-use`, `stagehand`, `computer-use-preview`

## `stagehand`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic · tags=browser,agents,typescript

**Qué es:** SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural.
**Stack:** Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba
**Acceso y costes:**
- API de IA: API de IA necesaria. Modelo y Browserbase pueden cobrar por uso; SDK, navegador local y MCP hospedado son rutas distintas
- Claude Code: Herramienta MCP para el agente
- Codex: Herramienta MCP para el agente
- Antigravity: Herramienta MCP para el agente
- Modelos locales: Modelo local no documentado. El MCP remoto documentado necesita cuenta y clave Browserbase; usar Claude Code o Codex para programar no aporta créditos de navegación
- Coste: El coste depende del proveedor o la ruta. Modelo y Browserbase pueden cobrar por uso; SDK, navegador local y MCP hospedado son rutas distintas
- Equipo: Preparación según la ruta elegida. Node o Python; modelo y navegador según ruta; clave Browserbase para MCP hospedado; sitio de prueba
**Repo:** https://github.com/browserbase/stagehand

**Instalación** [+]:

```
pnpm add @browserbasehq/stagehand 'zod@~4.4.3'
```

_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** Tu objetivo encaja con estos ejemplos: Prototipar extracción estructurada; Automatizar un formulario de prueba
**Evita si:** Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo
**Primera prueba propuesta:** Extrae dos campos de una página propia y contrasta la estructura con el contenido visible
**Qué comprobar:** Puedes comprobar datos y acciones del navegador
Revisión documental individual; instalación no ejecutada por Alexandría.
**Combina con:** `claude-code`, `lightpanda`, `firecrawl`
**Alternativas (elige una):** `browser-use`, `skyvern`
