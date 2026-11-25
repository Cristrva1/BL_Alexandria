# Configurar IA, prompts y servicios

Generado desde `data/handbook.json`. Guías de orientación documental; no acreditan instalación ni rendimiento. Las plantillas son originales de Alexandría.

Revisión: 2026-11-25. Los precios, planes y versiones pueden cambiar.

## Índice

### Agentes para programar

- [Codex](#codex)
- [Claude Code](#claude-code)
- [Antigravity](#antigravity)
- [DeepSeek Harness (DSH)](#deepseek-harness)
- [Qwen Code](#qwen-code)
- [Kimi Code](#kimi-code)
- [Command Code](#command-code)
- [OpenCode](#opencode)
- [T3 Code](#t3code)
- [Aider](#aider)
- [Cline](#cline)
- [Cursor](#cursor)
- [DeepAI Code](#deepai-code)

### Modelos y proveedores

- [DeepSeek: modelos y API](#deepseek-api)
- [Qwen: modelos locales o API](#qwen-modelos)
- [MiniMax](#minimax)
- [GLM / Z.AI](#glm)
- [Grok: API de modelos](#grok-api)
- [Jev de TypeSafe AI](#jev-typesafe)
- [Gemini 4 Carbon](#gemini-carbon)
- [OpenAI Responses API en segundo plano](#openai-background)

### Agentes personales y trabajo delegado

- [Hermes Agent](#hermes)
- [Devin](#devin)
- [Muse de Meta](#muse)
- [Grok Bot](#grok-bot)
- [OpenClaw](#openclaw)
- [agentes.chat Cloud](#agentes-chat-servicio)
- [Hermes Plugin Hackathon](#hermes-plugin-hackathon)
- [Tabletop de Google Labs](#google-tabletop)

### IA local y servidores de modelos

- [Ollama](#ollama)
- [vLLM](#vllm)
- [llama.cpp](#llamacpp)
- [LM Studio](#lmstudio)
- [Open WebUI](#openwebui)
- [Arete-27B de Nous Research](#nous-arete-27b)
- [Qwen3.8-27B adaptado para pi y OpenCode](#qwen-harness-adapters)
- [NVIDIA Nemotron 3.5 Bolt E4B](#nemotron-bolt)
- [Gemma 4 en tu equipo](#gemma-local)

### Android, iPhone y automatizaciones

- [Atajos de Apple](#atajos)
- [Tasker](#tasker)
- [MacroDroid](#macrodroid)
- [Termux](#termux)
- [Android Debug Bridge (ADB)](#adb)
- [scrcpy](#scrcpy)
- [DSH Android](#dsh-android)
- [DSH iOS](#dsh-ios)
- [Appium](#appium)
- [Maestro](#maestro)

### Código, publicación y despliegue

- [GitHub](#github)
- [GitHub Pages](#github-pages)
- [GitHub Actions](#github-actions)
- [Vercel](#vercel)
- [Railway](#railway)
- [Cloudflare](#cloudflare)
- [Modulify](#modulify)
- [Cloudflare for Startups](#cloudflare-startups)
- [DNSHE](#dnshe)
- [WebMCP y MCP según Chrome](#chrome-webmcp)

### Datos, usuarios e integraciones

- [Supabase](#supabase)
- [Activepieces: flujos e integraciones](#activepieces-servicio)
- [Neon](#neon)
- [Redis](#redis)
- [treg Jobs API](#treg-jobs-api)

### Servidores y contenedores

- [VPS: servidor virtual](#vps)
- [Hostinger y tipos de hosting](#hostinger)
- [Docker](#docker)
- [Docker Compose](#compose)
- [Caddy](#caddy)
- [Coolify](#coolify)
- [Boat](#boat-sandboxes)

### Acceso remoto, copias y operación

- [Tailscale](#tailscale)
- [OpenSSH](#openssh)
- [Uptime Kuma](#uptime-kuma)
- [Restic](#restic)
- [Tailscale con Grok Bot y MCP privado](#tailscale-grok-mcp)

### Cursos y diseño de sistemas

- [AI Harness Crash Course de Google Cloud Tech](#google-ai-harness-curso)
- [Designed to Scale](#designed-to-scale)
- [Neural Networks: Zero to Hero](#karpathy-zero-to-hero)

### Seguridad defensiva y análisis

- [OWASP Cheat Sheet Series](#owasp-cheat-sheets)
- [VirusTotal para agentes](#virustotal-ai)
- [roadmap.sh Cyber Security](#roadmap-ciberseguridad)
- [PortSwigger Web Security Academy](#portswigger-academy)
- [MITRE ATT&CK](#mitre-attack-defensa)

## Mi primer proyecto con un agente

Pasar de una carpeta de prueba a un cambio que puedas revisar.

1. [Codex](#codex): Si ya tienes acceso a Codex, comienza aquí; Claude Code o Antigravity son alternativas, no instalaciones obligatorias.
2. [GitHub](#github): Guarda el cambio en una rama y revisa su diff antes de integrarlo.

**Comprueba:** Un cambio pequeño pasa su comprobación y sabes cómo volver atrás.

Elige un agente primero y añade extensiones cuando una tarea las justifique.

## Probar IA local sin montar todo un servidor

Identificar modelo, memoria y salida antes de añadir más piezas.

1. [Ollama](#ollama): Prueba primero un modelo pequeño en la herramienta; LM Studio es otra ruta de interfaz.
2. [Open WebUI](#openwebui): Añade esta interfaz solo si necesitas sus funciones después de que el motor ya responda.

**Comprueba:** Conoces el modelo utilizado y distingues dónde se ejecuta cada etapa.

No se garantiza que toda la tarea sea offline; herramientas, documentos o búsquedas pueden usar servicios.

## Mi primera automatización Android

Automatizar un evento sencillo con una regla fácil de detener.

1. [MacroDroid](#macrodroid): Crea una macro de aviso; Tasker es una alternativa cuando necesitas otra lógica.
2. [Android Debug Bridge (ADB)](#adb): Consulta esta ruta solo si tu tarea necesita control desde un ordenador; no es requisito de toda macro.

**Comprueba:** El evento real produce una sola acción y puedes desactivar el flujo.

No añadas control por pantalla o IA cuando un disparador y una regla bastan.

## Mi primer atajo de iPhone

Construir primero la acción manual y después el disparador.

1. [Atajos de Apple](#atajos): Comprueba que la app expone la acción y prueba con una entrada ficticia.

**Comprueba:** Puedes ejecutar el atajo y sabes cuándo pide confirmación.

DSH iOS y Appium son rutas técnicas distintas para pruebas, con requisitos de ordenador.

## Programar desde Android o iPhone

Manejar una sesión en el equipo donde ya funciona tu proyecto.

1. [T3 Code](#t3code): Usa el cliente móvil y acceso remoto oficial después de autenticar un agente en el ordenador.
2. [OpenSSH](#openssh): SSH es otra ruta de terminal; puede apoyarse en Tailscale si necesitas una red privada.

**Comprueba:** Recuperas la sesión y puedes identificar el equipo y la carpeta remotos.

Son rutas alternativas. Esto no automatiza la interfaz del propio teléfono.

## Publicar una web estática

Compartir HTML, CSS y JavaScript con un enlace.

1. [GitHub](#github): Guarda los archivos construidos y comprueba enlaces bajo el prefijo del repositorio.
2. [GitHub Pages](#github-pages): Publica y espera el despliegue; prueba el enlace sin sesión.

**Comprueba:** El enlace público carga la nueva versión y sus assets.

Si necesitas secretos, datos privados o un servidor persistente, añade un backend adecuado.

## Una aplicación web con usuarios y datos

Separar la interfaz del almacenamiento y sus permisos.

1. [Supabase](#supabase): Prepara datos y acceso de dos usuarios ficticios en un entorno de prueba.
2. [Vercel](#vercel): Publica un preview con las variables del entorno y prueba un recorrido que lea y escriba datos.

**Comprueba:** Cada usuario ve solo sus datos y el preview completa la tarea.

Estos servicios no se sustituyen: cumplen capas diferentes y tienen cuentas y límites propios.

## Operar un servicio en tu servidor

Poder desplegar, observar y recuperar una aplicación con datos.

1. [VPS: servidor virtual](#vps): Dimensiona una prueba y documenta acceso y recuperación.
2. [Docker Compose](#compose): Revisa puertos, variables y volúmenes antes de arrancar el stack.
3. [Restic](#restic): Restaura una copia en una carpeta o entorno separado.
4. [Uptime Kuma](#uptime-kuma): Prueba caída y recuperación desde un punto que siga operativo.

**Comprueba:** El servicio responde y una restauración reproduce sus datos de prueba.

Una VPS requiere mantenimiento continuo; si no quieres operarlo, compara una plataforma administrada.

## Revisar permisos y alertas de mi aplicación

Identifica qué puede ver cada rol, documenta controles y decide qué registros servirían para revisar un incidente.

1. [OWASP Cheat Sheet Series](#owasp-cheat-sheets): Elige un control y escribe qué debe poder hacer cada rol.
2. [PortSwigger Web Security Academy](#portswigger-academy): Convierte las reglas de autenticación y permisos en criterios de aceptación.
3. [MITRE ATT&CK](#mitre-attack-defensa): Con un registro ficticio, relaciona una señal conocida con una acción de revisión.

**Comprueba:** Puedes mostrar cómo comprobar cada control y quién revisaría una alerta.

Haz el ejercicio con una app propia o ficticia y datos de muestra.

<a id="codex"></a>

## Codex

**Tipo:** Agente de código

Trabaja sobre un proyecto desde CLI, editor o escritorio; las superficies y permisos pueden variar.

### Antes de empezar

- Una carpeta de proyecto con Git
- El cliente oficial para tu sistema y una cuenta o API admitida

### Primera prueba

1. Instala la superficie que vas a usar siguiendo la guía oficial; evita configurar varias a la vez.
2. Abre una copia de prueba del proyecto. Autentica con ChatGPT o API y comprueba cuál está activa.
3. Pide explicar un archivo y proponer un cambio pequeño. Revisa el diff y una prueba antes de integrarlo.

**Qué comprobar:** El cambio queda identificado en Git y la prueba indicada termina con el resultado esperado.

**Cuenta y compatibilidad:** ChatGPT y API son métodos de acceso distintos. Para instrucciones duraderas usa AGENTS.md; las opciones del cliente se configuran según su superficie.

**Costes:** El plan, cuotas y método de autenticación determinan el consumo. Una API de tu aplicación conserva su propia facturación.

### Mejoras después de la primera prueba

- Escribe en AGENTS.md cómo arrancar y verificar el proyecto.
- Usa una skill para procedimientos repetidos y un conector o MCP para datos vivos; añade solo lo que necesites.
- Aplica ajustes del proyecto en .codex/config.toml cuando esa superficie los admita y conserva una copia anterior.

### Límites

- Una configuración local no habilita por sí misma funciones cloud, conectores o permisos de una organización.

### Comando: Consultar opciones del cliente

Dónde: Terminal, con Codex CLI ya instalado

```text
codex --help
```

Muestra ayuda; no inicia una tarea.

[Fuente del comando](https://learn.chatgpt.com/docs/cli/reference)

Fichas del catálogo: [codex](fichas/codex.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://learn.chatgpt.com/docs/config-file/config-basic) · 2026-11-15
- [Autenticación y sesiones](https://learn.chatgpt.com/docs/auth) · 2026-11-15

<a id="claude-code"></a>

## Claude Code

**Tipo:** Agente de código

Lee un repositorio, modifica archivos y ejecuta herramientas desde un entorno de desarrollo.

### Antes de empezar

- Cliente oficial de Claude Code
- Una carpeta de prueba y una ruta de autenticación admitida

### Primera prueba

1. Sigue el instalador oficial para tu sistema y abre el agente en la carpeta del proyecto.
2. Comprueba cuenta y proveedor. Pide un mapa breve del proyecto antes de editar.
3. Haz un cambio de texto o una corrección pequeña, revisa el diff y ejecuta la comprobación del proyecto.

**Qué comprobar:** Puedes explicar qué archivo cambió y reproducir la comprobación.

**Cuenta y compatibilidad:** Separa el inicio de sesión de Claude de una configuración con API o proveedor externo. Las instrucciones del proyecto van en CLAUDE.md.

**Costes:** Planes y APIs tienen límites propios. Cambiar el proveedor puede cambiar quién factura y qué datos recibe.

### Mejoras después de la primera prueba

- Mantén CLAUDE.md breve, con comandos y decisiones del proyecto.
- Añade una skill o plugin por necesidad y verifica que se carga.
- Usa hooks para comprobaciones concretas después de probarlos en una copia.

### Límites

- Un catálogo de skills no se instala como si fuera una sola aplicación; revisa cada paquete y su cliente.

Fichas del catálogo: [claude-code](fichas/claude-code.md) · [claude-plugins-official](fichas/claude-plugins-official.md) · [awesome-claude-code](fichas/awesome-claude-code.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://code.claude.com/docs/en/overview) · 2026-11-15

<a id="antigravity"></a>

## Antigravity

**Tipo:** Entorno de desarrollo con agentes

Organiza trabajo con agentes en las superficies App, CLI o IDE de Google Antigravity.

### Antes de empezar

- Una cuenta y sistema admitidos por la versión actual
- Proyecto de prueba con instrucciones de arranque

### Primera prueba

1. Elige App, CLI o IDE en la guía oficial e instala esa superficie.
2. Abre un proyecto pequeño y revisa sus permisos, cuenta y modelo disponibles.
3. Pide una mejora acotada y comprueba el archivo y el resultado desde la propia aplicación.

**Qué comprobar:** Puedes localizar el cambio y repetir su verificación sin depender de la conversación.

**Cuenta y compatibilidad:** El acceso se gestiona en Antigravity. Una API de Gemini u otro proveedor para tu aplicación es otra configuración.

**Costes:** Revisa el plan y las cuotas actuales de la cuenta. Los servicios externos del proyecto se pagan aparte.

### Mejoras después de la primera prueba

- Añade reglas del espacio de trabajo con contexto breve.
- Convierte una rutina útil en una skill antes de instalar colecciones completas.
- Define qué evidencia debe entregar un agente al finalizar.

### Límites

- No intercambies configuraciones entre App, CLI e IDE sin comprobar que la documentación las comparte.

Fichas del catálogo: [antigravity-cli](fichas/antigravity-cli.md) · [antigravity-awesome-skills](fichas/antigravity-awesome-skills.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://antigravity.google/docs/getting-started) · 2026-11-15

<a id="deepseek-harness"></a>

## DeepSeek Harness (DSH)

**Tipo:** Harness de agentes

Un entorno extensible por plugins para construir y ejecutar agentes; es distinto de los modelos DeepSeek.

### Antes de empezar

- Node.js y requisitos de la versión actual
- Cuenta o proveedor de modelo elegido

### Primera prueba

1. Lee el inicio rápido oficial y elige Web UI o desarrollo desde código.
2. Inicia el perfil de prueba y configura un proveedor por la ruta documentada.
3. Pide una tarea sobre un archivo de ejemplo; después añade un solo plugin si hace falta.

**Qué comprobar:** La interfaz abre y una tarea mínima devuelve un resultado que puedes inspeccionar.

**Cuenta y compatibilidad:** DSH es el harness; el proveedor, su clave y los plugins son capas separadas. Los plugins ZSeven-W son de terceros.

**Costes:** Código, llamadas al modelo, servidor y servicios de los plugins tienen costes independientes.

### Mejoras después de la primera prueba

- Mantén perfiles separados para pruebas y uso habitual.
- Revisa herramientas y permisos después de instalar un plugin.
- Guarda versiones y una forma de volver al perfil anterior.

### Límites

- Instalar un plugin no implica que sus dependencias o dispositivos ya estén preparados.

### Comando: Probar la interfaz web

Dónde: Terminal con Node y requisitos de DSH

```text
npx @deepseek-ai/dsh web
```

Descarga o ejecuta el paquete e inicia un servidor local. Revisa versión y origen antes de ejecutarlo.

[Fuente del comando](https://github.com/deepseek-ai/deepseek-harness)

Fichas del catálogo: [deepseek-harness](fichas/deepseek-harness.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/deepseek-ai/deepseek-harness) · 2026-11-15

<a id="qwen-code"></a>

## Qwen Code

**Tipo:** Agente de código

Usa un agente de terminal o superficies compatibles para trabajar en código con un proveedor configurado.

### Antes de empezar

- Instalador oficial o requisitos de Node del inicio rápido
- Una cuenta o clave de la plataforma que vayas a seleccionar

### Primera prueba

1. Instala Qwen Code por una de las rutas oficiales para tu sistema.
2. Abre qwen y usa /auth para elegir cuenta, plan o proveedor; selecciona la región correcta.
3. Pide explicar y corregir un ejemplo pequeño; revisa el diff y el consumo.

**Qué comprobar:** El diagnóstico identifica el proveedor esperado y el cambio pasa su prueba.

**Cuenta y compatibilidad:** Qwen Code es el cliente; Qwen también nombra una familia de modelos. El menú actual ofrece métodos de cuenta, planes y proveedores externos.

**Costes:** No asumas que conserva antiguas cuotas OAuth gratuitas. Consulta las condiciones del método seleccionado.

### Mejoras después de la primera prueba

- Guarda instrucciones y comandos propios en el ámbito .qwen que corresponda.
- Usa /doctor para revisar la configuración.
- Compara modelos con la misma tarea y criterio de aceptación.

### Límites

- Los endpoints de China e internacional y los planes no son intercambiables por cambiar el idioma.

### Comando: Elegir autenticación

Dónde: Dentro de una sesión interactiva de Qwen Code

```text
/auth
```

Abre el menú de autenticación. No es un comando de PowerShell.

[Fuente del comando](https://github.com/QwenLM/qwen-code/blob/main/docs/users/quickstart.md)

### Comando: Revisar configuración

Dónde: Dentro de Qwen Code

```text
/doctor
```

Revisa la configuración actual del cliente.

[Fuente del comando](https://github.com/QwenLM/qwen-code/blob/main/docs/users/quickstart.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/QwenLM/qwen-code/blob/main/docs/users/quickstart.md) · 2026-11-15

<a id="kimi-code"></a>

## Kimi Code

**Tipo:** Agente de código

El cliente de programación de Moonshot; conviene distinguirlo del chat Kimi y de su API.

### Antes de empezar

- La versión vigente de Kimi Code
- Cuenta o credencial admitida por esa versión

### Primera prueba

1. Empieza en la documentación actual de Kimi Code y comprueba la migración si vienes de kimi-cli.
2. Instala el cliente indicado y completa su login para la plataforma correcta.
3. Pide un cambio mínimo con un test; consulta el uso antes de una tarea larga.

**Qué comprobar:** La versión y la cuenta están identificadas y puedes revisar el cambio en Git.

**Cuenta y compatibilidad:** El plan del chat, Kimi Code y las APIs Moonshot pueden tener accesos y cuotas diferentes.

**Costes:** Confirma membresía, cuota y proveedor en el panel; no deduzcas el precio del cliente a partir de un modelo anunciado.

### Mejoras después de la primera prueba

- Consulta /usage cuando esté disponible en tu versión.
- Separa configuración del proyecto y credenciales.
- Usa el mismo ejemplo para comparar antes y después de cambiar modelo.

### Límites

- La documentación de kimi-cli incluye avisos de migración: evita mezclar comandos de generaciones distintas.

### Comando: Consultar versión

Dónde: Terminal, con la CLI correspondiente instalada

```text
kimi --version
```

Muestra la versión; comprueba primero si tu instalación migró a Kimi Code.

[Fuente del comando](https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/faq.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/MoonshotAI/kimi-cli/blob/main/docs/en/reference/kimi-command.md) · 2026-11-15

<a id="command-code"></a>

## Command Code

**Tipo:** Agente de código y proveedor

Un agente orientado a modelos abiertos, con servicio y planes propios.

### Antes de empezar

- Node/npm si eliges esa instalación
- Cuenta y acceso al modelo o plan elegidos

### Primera prueba

1. Entra en commandcode.ai y sigue su instalación oficial.
2. Configura una cuenta y comprueba el modelo seleccionado y su consumo.
3. Prueba una corrección de un solo archivo y revisa cambios y pruebas antes de ampliar la tarea.

**Qué comprobar:** La tarea usa el modelo previsto y deja un diff comprensible.

**Cuenta y compatibilidad:** Su cuenta y créditos no equivalen a tu plan de Claude o ChatGPT. Comprueba por separado el agente y su API de proveedor.

**Costes:** Consulta créditos incluidos, vencimiento y uso adicional en el plan actual; no uses cifras de publicaciones antiguas.

### Mejoras después de la primera prueba

- Define convenciones del proyecto y revisa las reglas aprendidas.
- Mide las correcciones que necesitas con una tarea repetible.
- Revisa consumo antes de permitir sesiones largas.

### Límites

- Los modelos disponibles y los créditos incluidos dependen del plan; confirma la ruta antes de migrar un proyecto.

### Comando: Instalación mediante npm

Dónde: Terminal con Node/npm

```text
npm i -g command-code
```

Descarga e instala globalmente el cliente. Consulta antes requisitos y versión.

[Fuente del comando](https://commandcode.ai/)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://commandcode.ai/) · 2026-11-15

<a id="opencode"></a>

## OpenCode

**Tipo:** Agente de código

Agente abierto con interfaz de terminal, escritorio o web y selección de proveedores.

### Antes de empezar

- La versión actual de OpenCode
- Proyecto Git y proveedor de modelo

### Primera prueba

1. Usa la documentación de anomalyco y elige una única superficie de instalación.
2. Conecta el proveedor y revisa modelo y permisos antes de ejecutar herramientas.
3. Haz una tarea corta, inspecciona el diff y ejecuta su comprobación.

**Qué comprobar:** Puedes identificar el proveedor y repetir la tarea sin cambiar de entorno.

**Cuenta y compatibilidad:** La autenticación depende del proveedor. El código del agente abierto no incluye todas las inferencias.

**Costes:** Servicios del proveedor y planes de modelos se revisan aparte del coste del cliente.

### Mejoras después de la primera prueba

- Añade instrucciones, skills o comandos según la documentación de tu versión.
- Instala MCP solo cuando necesites una herramienta concreta.
- Guarda la configuración anterior antes de cambiar de proveedor.

### Límites

- Existe un repositorio antiguo con el mismo nombre. Las guías actuales enlazan anomalyco/opencode.

### Comando: Instalación npm de la versión actual

Dónde: Terminal con Node/npm

```text
npm install -g @opencode/cli
```

Instala globalmente la CLI indicada por la documentación actual; no es el paquete histórico.

[Fuente del comando](https://opencode.ai/docs/)

Fichas del catálogo: [opencode](fichas/opencode.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://opencode.ai/docs/) · 2026-11-15

<a id="t3code"></a>

## T3 Code

**Tipo:** Interfaz para agentes

Una interfaz para manejar agentes y proyectos desde ordenador o teléfono; no sustituye su autenticación.

### Antes de empezar

- Un agente compatible ya instalado y autenticado
- Git y un proyecto de prueba

### Primera prueba

1. Descarga T3 Code desde su enlace oficial para tu sistema.
2. Conecta un agente instalado, por ejemplo Codex o Claude Code, siguiendo Provider setup.
3. Abre una tarea pequeña y revisa diff y prueba antes de commit o push.

**Qué comprobar:** El agente conectado completa una tarea y puedes ver los archivos afectados.

**Cuenta y compatibilidad:** T3 Code organiza agentes existentes; cada agente y proveedor conserva su sesión y condiciones.

**Costes:** Revisa por separado el cliente, la suscripción del agente y APIs externas.

### Mejoras después de la primera prueba

- Usa un worktree por cambio cuando ese flujo esté configurado.
- Configura acceso remoto siguiendo su guía y prueba primero en tu red.
- Identifica qué equipo debe permanecer encendido.

### Límites

- Controlar una sesión desde el móvil no equivale a automatizar las aplicaciones del teléfono.

### Comando: Instalación en Windows

Dónde: PowerShell en Windows con WinGet disponible

```text
winget install T3Tools.T3Code
```

Instala T3 Code; el agente se instala y autentica por separado.

[Fuente del comando](https://github.com/pingdotgg/t3code)

Fichas del catálogo: [t3code](fichas/t3code.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/pingdotgg/t3code) · 2026-11-15

<a id="aider"></a>

## Aider

**Tipo:** Agente de código en terminal

Trabaja con cambios de código y Git desde una conversación de terminal.

### Antes de empezar

- Python y requisitos del instalador actual
- Repositorio de prueba y un proveedor compatible

### Primera prueba

1. Sigue la instalación aislada oficial de Aider.
2. Configura el proveedor sin publicar la clave y añade solo los archivos necesarios.
3. Solicita una corrección pequeña y revisa commit, diff y pruebas.

**Qué comprobar:** Puedes revisar y revertir el cambio con Git.

**Cuenta y compatibilidad:** Admite proveedores y rutas locales documentadas; tener un chat de pago no acredita una API para Aider.

**Costes:** El consumo depende del modelo o del equipo local; comprueba el soporte del modelo antes de descargarlo.

### Mejoras después de la primera prueba

- Usa convenciones de código del proyecto.
- Configura lint y pruebas útiles.
- Reduce el conjunto de archivos cuando la tarea sea pequeña.

### Límites

- Una librería o modelo compatible con API puede no ofrecer la misma calidad de edición.

Fichas del catálogo: [aider](fichas/aider.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://aider.chat/docs/install.html) · 2026-11-15

<a id="cline"></a>

## Cline

**Tipo:** Agente en editor, CLI o escritorio

Ayuda a leer y editar archivos y utilizar herramientas desde una superficie de desarrollo.

### Antes de empezar

- La aplicación o extensión oficial elegida
- Cuenta o proveedor configurado

### Primera prueba

1. Elige escritorio, CLI o extensión desde la documentación oficial.
2. Abre una carpeta de prueba y revisa proveedor, permisos y herramientas disponibles.
3. Pide explicar un archivo y corregir un caso pequeño; inspecciona las acciones y el resultado.

**Qué comprobar:** El cambio queda visible y la comprobación puede repetirse.

**Cuenta y compatibilidad:** La superficie de Cline y la inferencia son capas distintas. Revisa qué proveedor usará cada tarea.

**Costes:** Cliente abierto no significa llamadas de IA ilimitadas. Modelos locales consumen tus recursos.

### Mejoras después de la primera prueba

- Añade reglas del proyecto en el formato de la versión elegida.
- Prueba un MCP antes de conectar muchos servicios.
- Revisa los permisos de ejecución que habilitas.

### Límites

- No des por hecho que una extensión y la aplicación de escritorio comparten toda su configuración.

Fichas del catálogo: [cline](fichas/cline.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.cline.bot/) · 2026-11-15

<a id="cursor"></a>

## Cursor

**Tipo:** Editor con agentes

Un editor con asistencia y agentes para desarrollar sobre tu repositorio.

### Antes de empezar

- Cliente oficial y cuenta
- Proyecto pequeño con un comando de comprobación

### Primera prueba

1. Descarga el editor oficial e inicia sesión.
2. Abre el proyecto y revisa modelos, reglas y permisos disponibles en tu cuenta.
3. Completa una tarea corta y revisa el diff y la prueba.

**Qué comprobar:** Puedes explicar qué cambió y cuánto uso consumió la tarea.

**Cuenta y compatibilidad:** Comprueba qué superficie y plan utilizas. Una cuenta Cursor, un Bot y una API externa tienen condiciones específicas.

**Costes:** Los modelos, límites y uso adicional dependen del plan actual.

### Mejoras después de la primera prueba

- Escribe reglas por proyecto y evita reglas globales que no aplican.
- Usa ejemplos concretos y criterios de aceptación.
- Revisa el consumo antes de trabajos persistentes.

### Límites

- El acceso a una función en un tutorial no prueba que esté habilitada en tu cuenta.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://cursor.com/docs) · 2026-11-15

<a id="deepseek-api"></a>

## DeepSeek: modelos y API

**Tipo:** Proveedor de modelos

Ofrece modelos a través de una API; el harness DSH es otra pieza.

### Antes de empezar

- Una aplicación o agente compatible
- Cuenta de API y presupuesto de prueba

### Primera prueba

1. Lee Your First API Call y elige el modelo disponible para tu cuenta.
2. Configura base URL y autenticación según el formato documentado, fuera del repositorio.
3. Prueba una solicitud pequeña y comprueba respuesta, uso y errores.

**Qué comprobar:** Tu aplicación muestra el proveedor esperado y registra el consumo de la prueba.

**Cuenta y compatibilidad:** Las rutas OpenAI-compatible y Anthropic-compatible tienen configuración propia. Consulta las integraciones oficiales con cada agente.

**Costes:** Consulta el tarifario del modelo y las funciones adicionales. Una suscripción de otro agente no paga automáticamente esta API.

### Mejoras después de la primera prueba

- Fija el modelo de una evaluación antes de comparar.
- Añade límites de salida y reintentos acotados.
- Separa credenciales de prueba y producción.

### Límites

- Pesos descargables, chat web y API no tienen necesariamente la misma licencia, límites o modelo.

Fichas del catálogo: [deepseek-v3](fichas/deepseek-v3.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://api-docs.deepseek.com/) · 2026-11-15

<a id="qwen-modelos"></a>

## Qwen: modelos locales o API

**Tipo:** Familia de modelos

Modelos de lenguaje y multimodales; elige una variante y un motor compatibles con tu tarea.

### Antes de empezar

- La ficha exacta del modelo
- Un motor local compatible o una cuenta de proveedor

### Primera prueba

1. Define si necesitas texto, visión u otra capacidad.
2. Elige una variante según memoria, formato y licencia; sigue la ruta oficial de inferencia.
3. Evalúa el mismo ejemplo pequeño y guarda modelo, cuantización y resultado.

**Qué comprobar:** Puedes identificar exactamente qué variante ejecutaste y repetir la prueba.

**Cuenta y compatibilidad:** Qwen Code es un cliente diferente. Los modelos pueden ejecutarse en motores documentados como Ollama, llama.cpp o vLLM.

**Costes:** Local implica equipo y energía; una API aplica su tarifa. La licencia se consulta en la ficha de cada variante.

### Mejoras después de la primera prueba

- Mide memoria y latencia con tu propio ejemplo.
- Compara cuantizaciones sin cambiar a la vez el prompt.
- Verifica soporte de herramientas si lo vas a usar como agente.

### Límites

- No existe una cantidad de RAM universal válida para toda la familia Qwen.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://qwen.readthedocs.io/en/latest/) · 2026-11-15

<a id="minimax"></a>

## MiniMax

**Tipo:** Proveedor y agente

Modelos y servicios de IA con planes y rutas para agentes de programación.

### Antes de empezar

- Cuenta MiniMax y un producto elegido
- Identificar si usarás API estándar, plan o MiniMax Code

### Primera prueba

1. Lee las opciones actuales de su plataforma y escoge una sola ruta.
2. Para otro agente, sigue su integración oficial sin mezclar claves ni endpoints de planes distintos.
3. Haz una tarea corta y confirma proveedor y consumo en ambos lados.

**Qué comprobar:** El agente usa MiniMax y el panel identifica la ruta de facturación prevista.

**Cuenta y compatibilidad:** La plataforma documenta integraciones con herramientas externas. Esa configuración no utiliza automáticamente la suscripción de Anthropic o ChatGPT.

**Costes:** API y planes pueden tener claves, cuotas y productos incluidos distintos. Consulta las condiciones actuales.

### Mejoras después de la primera prueba

- Guarda una copia de la configuración previa al cambiar de proveedor.
- Revisa variables que puedan sobrescribir el ajuste.
- Compara una tarea corta antes de adoptarlo para todo.

### Límites

- No copies ajustes de Claude Code directamente a Codex u otro cliente: sus formatos y APIs pueden diferir.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://platform.minimax.io/docs/m-plan/claude-code) · 2026-11-15

<a id="glm"></a>

## GLM / Z.AI

**Tipo:** Proveedor y familia de modelos

GLM es una familia de modelos; Z.AI ofrece acceso y planes para utilizarlos desde aplicaciones y agentes.

### Antes de empezar

- Cuenta y clave del producto correcto
- Cliente compatible con la integración que vas a seguir

### Primera prueba

1. Abre el inicio rápido y distingue la API estándar del Coding Plan.
2. Configura el modelo y endpoint de esa ruta en el cliente elegido.
3. Ejecuta una prueba mínima y comprueba la cuota o el cobro en la plataforma.

**Qué comprobar:** La respuesta y el panel corresponden al modelo y producto que elegiste.

**Cuenta y compatibilidad:** Una clave o plan para programación no equivale necesariamente a acceso general para cualquier aplicación.

**Costes:** Consulta modelo, cuota, región y restricciones del plan; no se fija un precio en esta guía.

### Mejoras después de la primera prueba

- Usa la integración oficial específica de tu agente.
- Guarda la configuración anterior para revertir.
- Comprueba herramientas y salida estructurada si tu flujo las necesita.

### Límites

- El nombre GLM no demuestra que una herramienta tenga una integración nativa con tu sesión.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.z.ai/guides/overview/quick-start) · 2026-11-15

<a id="grok-api"></a>

## Grok: API de modelos

**Tipo:** Proveedor de modelos

Acceso programático a modelos de xAI; se diferencia de Grok Bot y de las interfaces de chat.

### Antes de empezar

- Aplicación compatible y cuenta de API
- Modelo y presupuesto de prueba

### Primera prueba

1. Abre la guía API actual y elige un modelo y capacidades admitidos.
2. Configura la credencial por la ruta del cliente y conserva el secreto fuera del código.
3. Haz una solicitud pequeña y comprueba uso y resultado.

**Qué comprobar:** La aplicación usa la API prevista y puedes consultar su consumo.

**Cuenta y compatibilidad:** Planes, créditos y métodos de acceso pueden vincularse bajo condiciones concretas; verifica tu cuenta y no los presupongas.

**Costes:** Consulta la tarifa de la API y las condiciones del plan que la habilita.

### Mejoras después de la primera prueba

- Separa generación, búsqueda y otras capacidades al medir costes.
- Prueba el soporte de herramientas antes de tareas autónomas.
- Mantén un límite de trabajo por ejecución.

### Límites

- Una conversación en Grok o una sesión de Bot no prueba que tu aplicación tenga acceso de API.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.x.ai/docs/overview) · 2026-11-15

<a id="hermes"></a>

## Hermes Agent

**Tipo:** Agente personal extensible

Un agente de NousResearch con herramientas, skills y formas de acceso a proveedores.

### Antes de empezar

- Requisitos del instalador oficial y entorno persistente si lo necesitas
- Proveedor de IA elegido

### Primera prueba

1. Sigue el inicio rápido del repositorio NousResearch/hermes-agent.
2. Configura proveedor y prueba una conversación sin conectar todavía canales personales.
3. Dale una tarea con entrada, salida y condición de parada; revisa el resultado y el uso.

**Qué comprobar:** Puedes repetir una tarea pequeña y localizar su salida y configuración.

**Cuenta y compatibilidad:** Las herramientas y canales son conexiones adicionales. Que un proveedor aparezca en el menú no acredita que tu plan lo cubra.

**Costes:** Revisa inferencia, servidor y servicios conectados por separado.

### Mejoras después de la primera prueba

- Convierte una rutina probada en una skill pequeña.
- Añade un canal cada vez y verifica su destinatario.
- Conserva copias de configuración y estado antes de actualizar.

### Límites

- Una interfaz comunitaria llamada Hermes Desktop no es el mismo producto ni demuestra afiliación oficial.

Fichas del catálogo: [hermes-agent](fichas/hermes-agent.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/NousResearch/hermes-agent) · 2026-11-15

<a id="devin"></a>

## Devin

**Tipo:** Agente de desarrollo alojado

Delega tareas de ingeniería con un entorno de trabajo y revisión de resultados.

### Antes de empezar

- Cuenta Devin y acceso autorizado al repositorio
- Una tarea pequeña con criterios de aceptación

### Primera prueba

1. Configura un repositorio y su entorno según el onboarding oficial.
2. Pide una corrección con instrucciones de instalación y pruebas del proyecto.
3. Revisa la sesión, evidencia y propuesta de cambio antes de integrarla.

**Qué comprobar:** La propuesta puede revisarse en código y reproduce los criterios solicitados.

**Cuenta y compatibilidad:** Devin es un servicio propio; una suscripción a otro agente no establece acceso.

**Costes:** Consulta unidades, límites y plan vigentes; el alcance y duración afectan al trabajo consumido.

### Mejoras después de la primera prueba

- Añade conocimiento útil del repositorio.
- Divide tareas por resultados verificables.
- Define qué debe entregar cuando encuentre un bloqueo.

### Límites

- Un resultado redactado no sustituye las pruebas del proyecto ni una revisión del cambio.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.devin.ai/get-started/devin-intro) · 2026-11-15

<a id="muse"></a>

## Muse de Meta

**Tipo:** Agente personal alojado

El agente personal de Meta para tareas y servicios conectados, accesible mediante sus interfaces oficiales.

### Antes de empezar

- Cuenta y disponibilidad del servicio en tu región
- Una tarea de prueba sin datos sensibles

### Primera prueba

1. Accede a muse.ai y revisa el producto, disponibilidad y cuenta.
2. Define una tarea pequeña y el momento en que quieres revisar el resultado.
3. Conecta solo el servicio necesario y comprueba el registro de acciones antes de ampliar el uso.

**Qué comprobar:** Puedes ver qué hizo el agente, qué queda pendiente y qué acción solicita tu aprobación.

**Cuenta y compatibilidad:** Muse utiliza su propio servicio y computadora cloud. Revisa disponibilidad, cuenta y conexiones en sus interfaces oficiales.

**Costes:** Comprueba el plan y sus límites actuales. No se presupone incluido en otra suscripción de IA.

### Mejoras después de la primera prueba

- Especifica entrada, resultado y regla de parada.
- Revisa las cuentas conectadas y los accesos que ya no uses.
- Empieza con borradores y amplía el alcance tras comprobar el resultado.

### Límites

- No confundir con repositorios de terceros llamados Muse Spark, ni asumir que controla todas las apps del teléfono.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://muse.ai/) · 2026-11-15

<a id="grok-bot"></a>

## Grok Bot

**Tipo:** Agente personal alojado

Agentes con una computadora cloud para realizar tareas en servicios y aplicaciones.

### Antes de empezar

- Cuenta y plan elegibles según la documentación actual
- Una tarea breve y un servicio de prueba

### Primera prueba

1. Accede desde la página oficial de Grok Bot y comprueba tu plan.
2. Crea un Bot con un objetivo acotado y configura una conexión necesaria.
3. Revisa su trabajo, el registro y el uso antes de programar una rutina.

**Qué comprobar:** La tarea deja una salida comprobable y el consumo aparece en la cuenta correcta.

**Cuenta y compatibilidad:** Según la FAQ, The X Subscription incluye Grok Bot en Premium, Super y Ultra. También admite algunos planes heredados de Cursor. Comprueba el acceso de tu cuenta.

**Costes:** En The X Subscription usa la cuota semanal compartida con Cursor y las apps de Grok. La FAQ describe prepago para consumo adicional. En planes heredados, el sobreconsumo depende de la configuración de Cursor.

### Mejoras después de la primera prueba

- Sustituye sondeos innecesarios por eventos cuando el servicio lo permita.
- Da una condición de parada y un formato de entrega.
- Revisa consumo por Bot antes de ampliar tareas recurrentes.
- Usa el directorio comunitario para descubrir ideas y comprueba el autor, las conexiones solicitadas y los permisos antes de importar un bot.

### Límites

- Los Bots de una cuenta pueden compartir su computadora cloud; revisa esa frontera al conectar cuentas.
- Las entradas del directorio son aportaciones de terceros. Empieza con una tarea ficticia y una cuenta de prueba si decides importar una.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.x.ai/grok-bot/faq) · 2026-11-22
- [Directorio comunitario de bots y apps](https://grok-bot.directory/) · 2026-11-22

<a id="openclaw"></a>

## OpenClaw

**Tipo:** Agente personal autoalojable

Un agente configurable con canales, herramientas y proveedores para trabajo personal.

### Antes de empezar

- Entorno admitido por la versión actual
- Proveedor y espacio de prueba

### Primera prueba

1. Sigue el onboarding oficial con una instalación de prueba.
2. Elige proveedor y revisa configuración y permisos antes de conectar canales.
3. Ejecuta una tarea acotada y verifica el destinatario y la salida.

**Qué comprobar:** Puedes rastrear una tarea y detenerla sin depender de una sesión de chat.

**Cuenta y compatibilidad:** Autoalojar el agente no implica inferencia local. Cuenta del proveedor y canales se configuran por separado.

**Costes:** Modelo, servidor, mensajería y otros servicios pueden cobrar por separado.

### Mejoras después de la primera prueba

- Conecta un canal cada vez.
- Versiona configuración sin secretos.
- Prueba actualizaciones con copia de estado y ruta de reversión.

### Límites

- Un agente persistente necesita un equipo o servicio operativo; cerrar tu PC puede detener un despliegue local.

Fichas del catálogo: [openclaw](fichas/openclaw.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.openclaw.ai/start/getting-started) · 2026-11-15

<a id="ollama"></a>

## Ollama

**Tipo:** Motor y acceso a modelos

Descarga y ejecuta modelos locales y ofrece conexiones con aplicaciones; también puede ofrecer modelos cloud.

### Antes de empezar

- Sistema admitido, disco y memoria para la variante elegida
- Un modelo pequeño compatible con tu tarea

### Primera prueba

1. Descarga Ollama desde su fuente oficial.
2. Elige explícitamente local o cloud y consulta el tamaño del modelo antes de descargar.
3. Prueba una pregunta corta y comprueba qué modelo y servidor está utilizando tu aplicación.

**Qué comprobar:** Identificas el modelo cargado y puedes distinguir una ejecución local de una cloud.

**Cuenta y compatibilidad:** Las integraciones con agentes dependen de la superficie y versión. No todas las funciones de una app cambian de proveedor al conectarla.

**Costes:** Los modelos locales consumen equipo y energía; la ruta cloud tiene sus propias condiciones.

### Mejoras después de la primera prueba

- Empieza con una variante pequeña y mide memoria.
- Conecta una sola aplicación antes de abrir acceso remoto.
- Revisa contexto y concurrencia al aumentar la carga.

### Límites

- Instalar Ollama no garantiza que cualquier modelo quepa ni que todo tu flujo sea offline.

Fichas del catálogo: [ollama](fichas/ollama.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.ollama.com/quickstart) · 2026-11-15

<a id="vllm"></a>

## vLLM

**Tipo:** Servidor de inferencia

Sirve modelos para aplicaciones y varios usuarios; requiere más preparación que un chat de escritorio.

### Antes de empezar

- Hardware y sistema compatibles con el backend elegido
- Pesos, licencia y memoria del modelo

### Primera prueba

1. Consulta la matriz de instalación para tu CPU, GPU u otro acelerador.
2. Prepara un entorno aislado y sigue el quickstart con un modelo admitido.
3. Prueba una solicitud y después mide memoria y latencia con una pequeña concurrencia.

**Qué comprobar:** El servidor responde y conoces el modelo, uso de memoria y límite probado.

**Cuenta y compatibilidad:** Es un motor, no una suscripción de Claude o Codex. Un cliente compatible debe apuntar a su servidor.

**Costes:** Sin tarifa de un proveedor por token en tu motor propio; sí hay equipo, energía, almacenamiento o alquiler de GPU.

### Mejoras después de la primera prueba

- Mide lotes y concurrencia antes de escalar.
- Controla acceso y límites del servidor.
- Conserva la versión del motor y de los pesos de cada evaluación.

### Límites

- Una API compatible no garantiza todas las funciones o esquemas que necesita un agente.

Fichas del catálogo: [vllm](fichas/vllm.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.vllm.ai/en/latest/getting_started/quickstart/) · 2026-11-15

<a id="llamacpp"></a>

## llama.cpp

**Tipo:** Motor de inferencia

Ejecuta modelos en distintos equipos, incluidos formatos cuantizados como GGUF.

### Antes de empezar

- Binario o compilación para tu sistema
- Modelo y cuantización compatibles con la memoria disponible

### Primera prueba

1. Elige el paquete o compilación oficial para tu plataforma.
2. Selecciona un modelo pequeño y lee su licencia y requisitos.
3. Prueba la CLI o servidor documentado y registra la variante y memoria utilizada.

**Qué comprobar:** La respuesta se produce con el archivo de modelo elegido y puedes repetir la ejecución.

**Cuenta y compatibilidad:** No incluye una cuenta de IA comercial. Puede ofrecer un servidor para clientes compatibles.

**Costes:** Equipo, disco y energía; el modelo tiene su propia licencia y posibles condiciones comerciales.

### Mejoras después de la primera prueba

- Compara cuantizaciones con la misma tarea.
- Mide contexto y distribución CPU/GPU.
- Usa las instrucciones de tu versión: los nombres de binarios y comandos han cambiado.

### Límites

- No todos los GGUF incluyen las mismas capacidades ni caben con el mismo contexto.

### Comando: Ejemplo oficial con descarga de modelo

Dónde: Terminal tras preparar la versión que ofrece el comando llama

```text
llama cli -hf ggml-org/Qwen3.5-0.8B-GGUF
```

Descarga pesos y ejecuta un modelo. Comprueba disco, memoria y licencia antes de comenzar.

[Fuente del comando](https://github.com/ggml-org/llama.cpp)

Fichas del catálogo: [llama-cpp](fichas/llama-cpp.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/ggml-org/llama.cpp) · 2026-11-15

<a id="lmstudio"></a>

## LM Studio

**Tipo:** Aplicación para modelos locales

Una interfaz para probar modelos y, según configuración, servirlos a otras aplicaciones.

### Antes de empezar

- Sistema y hardware admitidos
- Espacio para un modelo pequeño

### Primera prueba

1. Instala la aplicación desde lmstudio.ai.
2. Elige una variante adecuada a tu memoria y abre un chat de prueba.
3. Si necesitas integrar una app, activa la función de servidor siguiendo su documentación y prueba una petición.

**Qué comprobar:** Puedes identificar el modelo cargado y obtener una respuesta desde la interfaz elegida.

**Cuenta y compatibilidad:** La aplicación, los pesos y cualquier integración con un agente se revisan por separado.

**Costes:** Consulta las condiciones actuales del producto y las licencias de los pesos; local mantiene costes de equipo.

### Mejoras después de la primera prueba

- Guarda la configuración usada en cada evaluación.
- Mide memoria antes de ampliar contexto.
- Activa el servidor solo cuando una aplicación lo necesite.

### Límites

- Descargar un modelo no prueba compatibilidad con todas las herramientas de un agente.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://lmstudio.ai/docs/app/basics) · 2026-11-15

<a id="openwebui"></a>

## Open WebUI

**Tipo:** Interfaz de chat autoalojable

Una interfaz que conecta con motores como Ollama o proveedores compatibles; no es por sí misma el modelo.

### Antes de empezar

- Entorno de instalación admitido
- Un motor local o proveedor ya funcional

### Primera prueba

1. Elige una ruta oficial de instalación y una carpeta de datos persistentes.
2. Conecta un solo proveedor y crea un usuario de prueba.
3. Haz un chat corto y verifica qué servidor recibe la solicitud.

**Qué comprobar:** La interfaz muestra respuestas del proveedor esperado y conserva el estado que necesitas.

**Cuenta y compatibilidad:** La conexión puede ser local o remota. Una interfaz en tu PC no acredita que el modelo también sea local.

**Costes:** Servidor, inferencia y condiciones de licencia se consultan por separado.

### Mejoras después de la primera prueba

- Prueba usuarios y permisos antes de compartir.
- Guarda copias de datos antes de actualizar.
- Añade documentos o herramientas solo después de verificar el chat básico.

### Límites

- Revisa la licencia actual y las condiciones de uso de marca si vas a redistribuir el producto.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.openwebui.com/getting-started/) · 2026-11-15

<a id="atajos"></a>

## Atajos de Apple

**Tipo:** Automatización iOS

Crea acciones y automatizaciones con las capacidades que iOS y cada aplicación exponen a Atajos.

### Antes de empezar

- iPhone o iPad con Atajos
- Una acción permitida por la app que quieres utilizar

### Primera prueba

1. Crea un atajo manual con una entrada sencilla, como un texto.
2. Añade una acción para mostrar o guardar ese texto y ejecútalo tú mismo.
3. Solo después añade un disparador de automatización y revisa si exige confirmación.

**Qué comprobar:** La acción produce el resultado y sabes cuándo requiere intervención.

**Cuenta y compatibilidad:** La automatización básica no necesita un modelo. Añadir una API de IA requiere una ruta y cuenta propias.

**Costes:** Los servicios o apps llamados pueden tener suscripciones; consulta sus condiciones.

### Mejoras después de la primera prueba

- Explica entrada, acción y salida antes de pedir a una IA que lo diseñe.
- Prueba con datos ficticios.
- Separa las acciones que preparan contenido de las que lo envían.

### Límites

- No equivale a permitir clics ilimitados en cualquier app de iOS ni ejecución permanente en segundo plano.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://support.apple.com/en-gb/guide/shortcuts/apdfbdbd7123/ios) · 2026-11-15

<a id="tasker"></a>

## Tasker

**Tipo:** Automatización Android

Construye perfiles y tareas con disparadores, condiciones y acciones en Android.

### Antes de empezar

- Teléfono Android y aplicación oficial
- Permisos necesarios para una acción concreta

### Primera prueba

1. Instala desde la distribución oficial y crea una tarea manual de prueba.
2. Usa un evento sencillo para mostrar un aviso, con una condición que evite repeticiones.
3. Prueba con pantalla apagada y revisa el ahorro de batería antes de confiar en el disparador.

**Qué comprobar:** La tarea se ejecuta una vez bajo la condición elegida y puedes detenerla.

**Cuenta y compatibilidad:** No requiere IA para las reglas básicas. Plugins y llamadas a IA son piezas adicionales.

**Costes:** Revisa licencia de la app, plugins y APIs opcionales.

### Mejoras después de la primera prueba

- Pon nombre a perfiles y documenta cómo desactivarlos.
- Evita disparadores que generen bucles.
- Exporta una copia antes de cambiar un flujo importante.

### Límites

- Ciertas acciones dependen de la versión de Android, permisos especiales o del fabricante.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://tasker.joaoapps.com/userguide/en/) · 2026-11-15

<a id="macrodroid"></a>

## MacroDroid

**Tipo:** Automatización Android

Crea macros visuales mediante disparadores, acciones y restricciones, sin escribir código.

### Antes de empezar

- Android y aplicación oficial
- Un comportamiento que puedas observar y desactivar

### Primera prueba

1. Crea una macro con un disparador manual.
2. Añade un aviso y una restricción sencilla antes de controlar otras apps.
3. Prueba el evento real y revisa el registro para detectar repeticiones o fallos.

**Qué comprobar:** La macro produce un aviso bajo la condición prevista y no vuelve a dispararse en bucle.

**Cuenta y compatibilidad:** Las macros básicas son reglas; integrar un modelo es otra configuración.

**Costes:** Comprueba diferencias entre versión gratuita, planes y servicios opcionales.

### Mejoras después de la primera prueba

- Empieza con una plantilla entendida, no con un paquete completo.
- Nombra las restricciones y la forma de detener la macro.
- Revisa permisos y batería cuando no se ejecute en segundo plano.

### Límites

- Android y las apps deciden qué acciones están disponibles; no todas las plantillas funcionan igual en cada teléfono.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://macrodroid.com/) · 2026-11-15

<a id="termux"></a>

## Termux

**Tipo:** Terminal Android

Un entorno de terminal y paquetes en Android para tareas de desarrollo y automatización.

### Antes de empezar

- Android compatible
- La distribución y repositorios indicados por el proyecto

### Primera prueba

1. Lee las fuentes de instalación y evita mezclar builds y complementos incompatibles.
2. Instala desde una fuente admitida y prueba un comando sencillo sobre una carpeta de prueba.
3. Para conectarte a un equipo, configura un cliente SSH y prueba una sesión controlada.

**Qué comprobar:** Puedes trabajar en la carpeta prevista y cerrar la conexión sin alterar otros datos.

**Cuenta y compatibilidad:** No incluye un modelo de IA ni control universal de otras apps. Un agente remoto se ejecuta en el equipo al que conectas.

**Costes:** Aplicación y paquetes según sus licencias; servidor, datos móviles e inferencia son independientes.

### Mejoras después de la primera prueba

- Conserva scripts pequeños con instrucciones de uso.
- Usa almacenamiento de prueba antes de automatizar archivos.
- Documenta qué proceso necesita seguir activo.

### Límites

- Las restricciones de Android en segundo plano pueden detener procesos; no es equivalente a una VPS.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/termux/termux-app) · 2026-11-15

<a id="adb"></a>

## Android Debug Bridge (ADB)

**Tipo:** Conexión y depuración Android

Comunica un ordenador con un emulador o dispositivo Android para depuración y herramientas autorizadas.

### Antes de empezar

- Android SDK Platform-Tools
- Dispositivo de prueba y depuración USB autorizada

### Primera prueba

1. Instala Platform-Tools de Android y conecta el dispositivo.
2. Acepta la autorización en tu propio teléfono y lista los dispositivos conectados.
3. Comprueba el identificador antes de usar una herramienta que controle o instale aplicaciones.

**Qué comprobar:** Tu dispositivo aparece como autorizado y puedes distinguirlo de otros conectados.

**Cuenta y compatibilidad:** ADB no necesita modelo ni una suscripción de IA. Un agente que lo use necesita sus propios permisos y proveedor.

**Costes:** La herramienta no introduce una tarifa por llamada de IA; equipo y servicios externos siguen siendo aparte.

### Mejoras después de la primera prueba

- Selecciona el dispositivo explícitamente cuando haya varios.
- Empieza por consultas antes de cambiar estado.
- Revoca la depuración de equipos que ya no utilices.

### Límites

- Depuración USB da capacidades amplias; no habilites control de un teléfono ajeno ni publiques el puerto de depuración.

### Comando: Listar dispositivos

Dónde: Terminal con Android Platform-Tools en PATH

```text
adb devices -l
```

Lista identificadores y estado de autorización de los dispositivos conectados.

[Fuente del comando](https://developer.android.com/tools/adb)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://developer.android.com/tools/adb) · 2026-11-15

<a id="scrcpy"></a>

## scrcpy

**Tipo:** Pantalla y control Android

Muestra y controla la pantalla de Android desde un ordenador; es una herramienta de control, no un agente de IA.

### Antes de empezar

- Ordenador y Android compatibles
- Conexión y autorización descritas en su README

### Primera prueba

1. Descarga scrcpy desde Genymobile y prepara la conexión oficial.
2. Abre una sesión con tu teléfono de prueba.
3. Mueve una pantalla y cierra la sesión para comprobar que el control termina.

**Qué comprobar:** Puedes ver y manejar el dispositivo autorizado y detener la sesión.

**Cuenta y compatibilidad:** Puede complementar pruebas guiadas por una persona o agente, pero no añade razonamiento ni proveedor de IA.

**Costes:** Software abierto; no necesita una API de modelo para compartir la pantalla.

### Mejoras después de la primera prueba

- Usa una conexión local antes de configurar acceso remoto.
- Identifica el dispositivo si conectas varios.
- Comprueba restricciones del fabricante antes de atribuir un fallo a la IA.

### Límites

- Es para Android; no se presenta como una solución de control de iPhone.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/Genymobile/scrcpy) · 2026-11-15

<a id="dsh-android"></a>

## DSH Android

**Tipo:** Plugin de terceros para Android

Conecta DeepSeek Harness con emuladores o Android por USB mediante ADB.

### Antes de empezar

- DSH y Node compatibles con la versión del plugin
- ADB y un emulador o teléfono con depuración autorizada

### Primera prueba

1. Completa primero la conexión del dispositivo con ADB.
2. Instala el plugin ZSeven-W/dsh-android por su ruta documentada en un perfil de prueba.
3. Pide identificar la pantalla y recorrer una acción inocua; revisa la evidencia.

**Qué comprobar:** El plugin identifica el dispositivo correcto y la acción coincide con lo que ves.

**Cuenta y compatibilidad:** Requiere DSH y su proveedor de IA. Es un plugin comunitario, no una función nativa de todos los agentes.

**Costes:** Inferencia y posibles servicios externos aparte del código del plugin.

### Mejoras después de la primera prueba

- Prueba primero en emulador.
- Define una regla de parada ante un estado inesperado.
- Convierte recorridos probados en casos de QA.

### Límites

- Que se registren herramientas no demuestra que ADB o el dispositivo estén listos.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/ZSeven-W/dsh-android) · 2026-11-15

<a id="dsh-ios"></a>

## DSH iOS

**Tipo:** Plugin de terceros para iOS

Permite trabajar con simulador de iOS y rutas documentadas para iPhone conectado por USB desde DSH.

### Antes de empezar

- macOS con Xcode completo y runtime de simulador
- DSH compatible; para teléfono real, preparación adicional del runner

### Primera prueba

1. Prepara primero un simulador con Xcode.
2. Instala el plugin en un perfil DSH de prueba siguiendo su README.
3. Recorre una app de ejemplo y revisa capturas o estado; aborda el dispositivo real después.

**Qué comprobar:** Una acción en el simulador cambia el estado esperado y puedes repetirla.

**Cuenta y compatibilidad:** El plugin usa DSH y su proveedor de IA; el camino al iPhone real no elimina requisitos de Apple y del runner.

**Costes:** Equipo macOS, inferencia y posibles servicios aparte. Revisa requisitos de firma si la ruta elegida los pide.

### Mejoras después de la primera prueba

- Mantén un caso de prueba corto y repetible.
- Distingue claramente simulador y teléfono real.
- Guarda el resultado antes de añadir nuevas herramientas.

### Límites

- No se presenta como una instalación desde Windows ni como control libre de cualquier iPhone.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/ZSeven-W/dsh-ios) · 2026-11-15

<a id="appium"></a>

## Appium

**Tipo:** Automatización de pruebas

Automatiza pruebas de interfaces con drivers por plataforma; requiere preparación técnica.

### Antes de empezar

- Servidor y cliente Appium
- Driver de Android o iOS y sus dependencias

### Primera prueba

1. Sigue el quickstart y elige una sola plataforma.
2. Instala el driver correspondiente y conecta un dispositivo o emulador de prueba.
3. Escribe un caso corto que abra una app, encuentre un elemento y compruebe su estado.

**Qué comprobar:** El mismo test puede ejecutarse otra vez con un resultado claro.

**Cuenta y compatibilidad:** La automatización básica no requiere un modelo. Una IA puede ayudarte a escribir el test, con su propia cuenta.

**Costes:** Código y drivers según licencia; granjas de dispositivos y proveedores cloud pueden cobrar.

### Mejoras después de la primera prueba

- Prefiere identificadores de accesibilidad estables.
- Separa datos de prueba de cuentas personales.
- Conserva logs para diagnosticar fallos intermitentes.

### Límites

- iOS tiene requisitos específicos de macOS, Xcode y firma según el driver y dispositivo.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://appium.io/docs/en/latest/intro/) · 2026-11-15

<a id="maestro"></a>

## Maestro

**Tipo:** Automatización de pruebas

Describe recorridos de interfaz en flujos YAML para probar aplicaciones móviles y web.

### Antes de empezar

- CLI y plataforma admitidas por el quickstart
- App y emulador o dispositivo de prueba

### Primera prueba

1. Sigue el quickstart oficial para tu plataforma.
2. Crea un flujo mínimo con apertura de la app y una comprobación visible.
3. Ejecútalo dos veces y revisa el punto exacto de cualquier fallo.

**Qué comprobar:** El flujo verifica el estado deseado de forma repetible.

**Cuenta y compatibilidad:** El runner de pruebas y la IA que redacta el YAML son piezas distintas.

**Costes:** Distingue ejecución local de servicios cloud y sus condiciones.

### Mejoras después de la primera prueba

- Usa textos o IDs estables para localizar elementos.
- Evita depender de esperas arbitrarias.
- Añade casos de error después del recorrido básico.

### Límites

- Una prueba de tu app no demuestra control general de todo el teléfono o de todas las apps instaladas.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.maestro.dev/) · 2026-11-15

<a id="github"></a>

## GitHub

**Tipo:** Código y colaboración

Guarda el historial y coordina cambios, revisiones e incidencias de un proyecto.

### Antes de empezar

- Cuenta y repositorio
- Git instalado si trabajas en tu equipo

### Primera prueba

1. Crea o abre un repositorio de prueba y revisa su visibilidad.
2. Guarda un cambio pequeño en una rama.
3. Abre un pull request y revisa diff y comprobaciones antes de integrar.

**Qué comprobar:** El historial contiene el cambio y otra persona puede entender la propuesta.

**Cuenta y compatibilidad:** Un agente puede usar una integración o CLI autorizada. Esa conexión no incluye automáticamente alojamiento o inferencia.

**Costes:** Consulta límites de repositorios, almacenamiento y productos usados; Actions, Codespaces y otros servicios tienen condiciones propias.

### Mejoras después de la primera prueba

- Documenta arranque y pruebas en el README.
- Mantén secretos fuera del historial.
- Usa revisiones y ramas para cambios que necesiten evaluación.

### Límites

- Subir código no publica por sí solo una aplicación funcionando.

### Comando: Revisar cambios locales

Dónde: Terminal dentro de un repositorio Git

```text
git status --short
```

Muestra archivos cambiados; no crea commits ni hace push.

[Fuente del comando](https://git-scm.com/docs/git-status)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.github.com/en/get-started) · 2026-11-15

<a id="github-pages"></a>

## GitHub Pages

**Tipo:** Alojamiento estático

Publica HTML, CSS y JavaScript desde un repositorio para consultarlos con un enlace.

### Antes de empezar

- Un sitio estático construido
- Repositorio y permisos de publicación

### Primera prueba

1. Genera el sitio y verifica sus enlaces y rutas locales.
2. Configura Pages con la rama o workflow que corresponda.
3. Espera el despliegue y abre la URL pública sin sesión.

**Qué comprobar:** El enlace público carga la versión nueva y sus archivos sin descargar el repositorio.

**Cuenta y compatibilidad:** Se puede usar con código preparado por cualquier agente; el navegador ejecuta el frontend.

**Costes:** Disponibilidad y límites dependen de visibilidad y plan; dominio propio se gestiona aparte.

### Mejoras después de la primera prueba

- Versiona assets para evitar caché obsoleta.
- Prueba enlaces bajo el prefijo del repositorio.
- Mantén las claves y llamadas privadas en un backend separado.

### Límites

- Pages es estático: no ejecuta un servidor Python, Node persistente ni guarda secretos del backend.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) · 2026-11-15

<a id="github-actions"></a>

## GitHub Actions

**Tipo:** Automatización CI/CD

Ejecuta pruebas, construcciones y despliegues a partir de eventos o calendarios del repositorio.

### Antes de empezar

- Repositorio con un comando reproducible
- Permisos y secretos de entorno necesarios

### Primera prueba

1. Crea un workflow pequeño que ejecute una comprobación.
2. Pruébalo manualmente y revisa logs y artefactos.
3. Añade el evento o calendario cuando el resultado sea fiable.

**Qué comprobar:** Una ejecución queda vinculada a un commit y termina con un resultado comprobable.

**Cuenta y compatibilidad:** El runner ejecuta comandos; un paso con un modelo requiere su propio acceso de IA.

**Costes:** Revisa minutos, runners, almacenamiento y servicios llamados; un calendario no garantiza gratuidad.

### Mejoras después de la primera prueba

- Usa permisos mínimos del token del workflow.
- Evita que dos ejecuciones modifiquen a la vez la misma salida.
- Guarda evidencia y controla reintentos de acciones externas.

### Límites

- Un cron de repositorio no equivale a un servicio que permanece encendido todo el día.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.github.com/en/actions/get-started/understand-github-actions) · 2026-11-15

<a id="vercel"></a>

## Vercel

**Tipo:** Despliegue de aplicaciones

Publica frontends y aplicaciones compatibles con servicios de despliegue y ejecución.

### Antes de empezar

- Proyecto que construya correctamente
- Cuenta, repositorio y variables del entorno

### Primera prueba

1. Importa un proyecto de prueba y confirma framework y comando de build.
2. Configura variables en el entorno correcto y crea un preview.
3. Prueba una ruta real y sus llamadas al backend antes de promover a producción.

**Qué comprobar:** El preview realiza la tarea prevista y sus logs no muestran errores del recorrido.

**Cuenta y compatibilidad:** Un agente ayuda a construir o desplegar; Vercel y los proveedores de IA conservan sus cuentas.

**Costes:** Consulta plan, ejecución, tráfico y servicios de datos o IA; un preview no demuestra coste cero.

### Mejoras después de la primera prueba

- Separa preview y producción.
- Prueba variables y conexiones reales, no solo el build.
- Conserva una versión a la que puedas volver.
- Si eliges eve, compara por separado ejecución, Sandbox, Workflow y uso de modelos por AI Gateway. Prueba primero con un flujo pequeño.

### Límites

- Comprueba las capacidades del runtime antes de mover procesos persistentes o tareas pesadas.

Fichas del catálogo: [eve](fichas/eve.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://vercel.com/docs) · 2026-11-15
- [Presentación oficial de eve 1.0](https://vercel.com/blog/eve-is-now-generally-available) · 2026-11-22
- [Medición y precios de Vercel](https://vercel.com/pricing) · 2026-11-22

<a id="railway"></a>

## Railway

**Tipo:** Plataforma de despliegue

Despliega servicios de aplicación y conecta recursos como bases de datos.

### Antes de empezar

- Proyecto o imagen con un arranque documentado
- Cuenta y estimación de recursos

### Primera prueba

1. Crea un proyecto de prueba desde la ruta oficial.
2. Configura variables, puerto y persistencia si la app guarda datos.
3. Revisa logs y prueba una petición real desde la URL publicada.

**Qué comprobar:** El servicio responde y los datos de prueba sobreviven al reinicio cuando deben persistir.

**Cuenta y compatibilidad:** La cuenta de despliegue y la de IA son independientes. Revisa quién puede acceder a cada entorno.

**Costes:** Recursos y planes se cobran según sus condiciones; revisa uso y límites antes de dejarlo activo.

### Mejoras después de la primera prueba

- Configura healthcheck y límites de recursos.
- Separa entornos y servicios.
- Incluye copias de datos y una ruta de recuperación.

### Límites

- Un despliegue correcto no configura por sí solo backups, permisos o límites de gasto.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.railway.com/quick-start) · 2026-11-15

<a id="supabase"></a>

## Supabase

**Tipo:** Backend y PostgreSQL

Reúne base de datos, autenticación, almacenamiento y otras capacidades para aplicaciones.

### Antes de empezar

- Proyecto de prueba y esquema de datos pequeño
- Decidir servicio alojado o entorno local

### Primera prueba

1. Sigue un inicio rápido para tu framework y crea un entorno de prueba.
2. Configura acceso de usuarios y políticas por propietario; usa claves publicables en clientes y secretos solo en servidor.
3. Comprueba con dos usuarios que cada uno accede únicamente a sus datos.

**Qué comprobar:** El usuario A no puede leer o modificar los datos privados del usuario B.

**Cuenta y compatibilidad:** Una conexión MCP o agente ayuda a configurar, pero no sustituye permisos de base de datos y aplicación.

**Costes:** Revisa base, almacenamiento, tráfico y otras funciones del plan; autoalojar requiere operación propia.

### Mejoras después de la primera prueba

- Versiona los cambios de esquema.
- Prueba políticas de acceso y restauración.
- Distingue claves publicables de claves secretas o service_role.

### Límites

- No publiques claves secretas en el frontend ni habilites acceso general para resolver un error de permisos.

### Comando: Consultar comandos disponibles

Dónde: Terminal con Supabase CLI instalado

```text
supabase --help
```

Muestra ayuda de tu versión; no crea ni modifica una base de datos.

[Fuente del comando](https://supabase.com/docs/reference/cli/introduction)

Fichas del catálogo: [supabase](fichas/supabase.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://supabase.com/docs/guides/getting-started) · 2026-11-15
- [Claves y seguridad](https://supabase.com/docs/guides/api/api-keys) · 2026-11-15

<a id="vps"></a>

## VPS: servidor virtual

**Tipo:** Tipo de infraestructura

Un ordenador virtual remoto donde administras sistema, aplicaciones y datos.

### Antes de empezar

- Tamaño, región y sistema necesarios
- Presupuesto y una forma de recuperación del acceso

### Primera prueba

1. Dimensiona una prueba y compara qué incluye el proveedor.
2. Prepara un usuario de administración y acceso SSH antes de instalar aplicaciones.
3. Despliega un servicio pequeño y verifica acceso, reinicio y copia de datos.

**Qué comprobar:** Puedes conectar, reiniciar el servicio y restaurar una copia de prueba.

**Cuenta y compatibilidad:** Una VPS ejecuta el software; no trae un modelo de IA ni permisos de tus servicios por defecto.

**Costes:** Alquiler, disco, tráfico, copias y posibles IP o GPU según proveedor.

### Mejoras después de la primera prueba

- Documenta actualizaciones y recuperación.
- Usa contenedores cuando simplifiquen la operación.
- Mide carga antes de aumentar el tamaño.

### Límites

- Una VPS barata puede ser insuficiente para un modelo grande; alojar un motor de flujos y servir un LLM tienen requisitos distintos.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.digitalocean.com/products/droplets/) · 2026-11-15

<a id="hostinger"></a>

## Hostinger y tipos de hosting

**Tipo:** Proveedor de alojamiento

Ofrece productos de alojamiento; elige según la aplicación y el control que necesitas.

### Antes de empezar

- Conocer si el sitio es estático, WordPress, Node u otro servicio
- Plan y dominio adecuados al producto

### Primera prueba

1. Compara el tipo de hosting con los requisitos de tu aplicación.
2. Publica primero en una URL de prueba y configura sus variables y rutas.
3. Verifica un recorrido completo y SSL antes de conectar el dominio definitivo.

**Qué comprobar:** La URL responde y la función principal funciona fuera de tu equipo.

**Cuenta y compatibilidad:** Hosting compartido, servicios administrados y VPS tienen capacidades diferentes. Tu agente no sustituye el plan.

**Costes:** Revisa renovación, dominio, recursos, copias y extras; no uses solo la promoción inicial para comparar.

### Mejoras después de la primera prueba

- Guarda una copia antes de publicar.
- Documenta DNS y correo antes de mover un dominio.
- Conserva una ruta para revertir el despliegue.

### Límites

- No todos los planes ejecutan Docker, procesos persistentes o cualquier backend.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://www.hostinger.com/tutorials/what-is-web-hosting) · 2026-11-15

<a id="docker"></a>

## Docker

**Tipo:** Contenedores

Empaqueta aplicaciones y dependencias en contenedores para ejecutar un entorno reproducible.

### Antes de empezar

- Docker Desktop o Engine compatible
- Imagen o proyecto y espacio de datos de prueba

### Primera prueba

1. Instala el producto que corresponda a tu sistema y comprueba que el motor responde.
2. Ejecuta el tutorial oficial en un entorno de prueba.
3. Identifica puertos, volúmenes y variables antes de usar una imagen de aplicación.

**Qué comprobar:** Sabes qué proceso está activo y dónde persisten sus datos.

**Cuenta y compatibilidad:** No requiere IA para contenedores básicos. Modelos, APIs y permisos de un agente siguen siendo independientes.

**Costes:** Consulta condiciones de Docker Desktop y servicios de registro; el hardware o servidor se paga aparte.

### Mejoras después de la primera prueba

- Fija versiones de imágenes y revisa actualizaciones.
- Guarda datos en volúmenes y prueba copias.
- Revisa puertos expuestos y límites de recursos.

### Límites

- Un contenedor no es una copia de seguridad ni demuestra aislamiento adecuado para cualquier código.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.docker.com/get-started/) · 2026-11-15

<a id="compose"></a>

## Docker Compose

**Tipo:** Configuración de varios servicios

Describe servicios, redes y volúmenes de una aplicación en un archivo de configuración.

### Antes de empezar

- Docker con Compose disponible
- Archivo del proyecto y variables necesarias

### Primera prueba

1. Lee cada servicio y distingue sus datos persistentes de su imagen.
2. Valida la configuración sin imprimir secretos.
3. Arranca un stack de prueba y verifica cada servicio y su persistencia.

**Qué comprobar:** El servicio responde y conserva los datos que deben sobrevivir a recreaciones.

**Cuenta y compatibilidad:** Compose coordina procesos; no incluye las cuentas de sus aplicaciones.

**Costes:** Software, imágenes, licencias y servidor tienen condiciones separadas.

### Mejoras después de la primera prueba

- Mantén un ejemplo de variables sin credenciales.
- Documenta cómo detener y recuperar el stack.
- Prueba copias antes de recrear servicios con datos.

### Límites

- Cambiar una etiqueta o recrear un contenedor puede requerir una migración de datos.

### Comando: Validar sin imprimir la configuración

Dónde: Terminal, dentro de la carpeta que contiene el archivo Compose

```text
docker compose config --quiet
```

Valida la configuración sin arrancar el stack ni volcar variables.

[Fuente del comando](https://docs.docker.com/reference/cli/docker/compose/config/)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://docs.docker.com/compose/) · 2026-11-15

<a id="tailscale"></a>

## Tailscale

**Tipo:** Red privada y acceso remoto

Conecta dispositivos autorizados para acceder a servicios sin tratarlos como una web pública.

### Antes de empezar

- Cuenta y clientes compatibles en ambos extremos
- Un servicio de prueba y reglas de acceso

### Primera prueba

1. Sigue el quickstart para unir dos dispositivos propios.
2. Comprueba identidad y conectividad entre ellos.
3. Permite acceso al servicio necesario y prueba desde el segundo dispositivo.

**Qué comprobar:** El dispositivo autorizado llega al servicio previsto con las reglas elegidas.

**Cuenta y compatibilidad:** La red privada no autentica por sí sola todas las aplicaciones. Puede complementar SSH o una interfaz de agente.

**Costes:** Consulta límites de dispositivos, usuarios y uso del plan actual.

### Mejoras después de la primera prueba

- Define quién puede acceder a qué servicio.
- Retira equipos que ya no uses.
- Documenta qué equipo debe seguir encendido.

### Límites

- Usar el móvil como cliente remoto no significa que la IA esté controlando el propio teléfono.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://tailscale.com/docs/how-to/quickstart) · 2026-11-15

<a id="openssh"></a>

## OpenSSH

**Tipo:** Terminal y transferencia remotas

Permite acceder a una terminal remota y transferir archivos mediante protocolos SSH.

### Antes de empezar

- Cliente y servidor SSH
- Usuario autorizado e identidad del equipo remoto

### Primera prueba

1. Comprueba cliente y servidor según tu sistema.
2. Conecta con un usuario de prueba y verifica la identidad del host.
3. Ejecuta una consulta de lectura, cierra la sesión y comprueba que puedes volver a entrar.

**Qué comprobar:** La sesión está en el equipo esperado y puedes abrir y cerrar el acceso de forma controlada.

**Cuenta y compatibilidad:** SSH no incluye un agente de IA. Puedes entrar desde un cliente móvil a un equipo donde ya funcione un agente.

**Costes:** Software según licencia; servidor y conectividad son costes independientes.

### Mejoras después de la primera prueba

- Usa claves con protección y conserva una recuperación de acceso.
- Separa usuarios y permisos.
- No confundas un túnel a un puerto con publicar todo el servidor.

### Límites

- Cambiar la huella de un host requiere comprobar su causa antes de aceptar una nueva identidad.

### Comando: Consultar versión del cliente

Dónde: Terminal con OpenSSH instalado

```text
ssh -V
```

Muestra la versión del cliente; no abre una conexión.

[Fuente del comando](https://man.openbsd.org/ssh)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://www.openssh.org/manual.html) · 2026-11-15

<a id="cloudflare"></a>

## Cloudflare

**Tipo:** DNS, red y plataforma de aplicaciones

Ofrece DNS y productos de publicación, ejecución y conectividad; elige el producto antes de configurarlo.

### Antes de empezar

- Dominio o proyecto de prueba
- Identificar DNS, Workers, Pages o Tunnel según el caso

### Primera prueba

1. Define qué problema quieres resolver sin activar productos innecesarios.
2. Configura una prueba y conserva los registros de DNS y correo existentes.
3. Verifica resolución y recorrido de usuario antes de mover tráfico real.

**Qué comprobar:** El servicio responde en el dominio correcto y el correo sigue funcionando si lo había.

**Cuenta y compatibilidad:** Un agente puede ayudar a gestionar la cuenta con permisos; cada producto mantiene su configuración.

**Costes:** Consulta límites y facturación del producto concreto, no de Cloudflare como un único plan.

### Mejoras después de la primera prueba

- Versiona configuración de aplicaciones cuando sea posible.
- Comprueba variables y rutas en preview.
- Documenta rollback de DNS y despliegue.

### Límites

- Tunnel, proxy DNS y runtime de Workers resuelven problemas distintos y no son sustitutos automáticos.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://developers.cloudflare.com/) · 2026-11-15

<a id="caddy"></a>

## Caddy

**Tipo:** Servidor web y proxy inverso

Sirve contenido o dirige peticiones a aplicaciones con configuración de HTTPS según el despliegue.

### Antes de empezar

- Un servidor y una aplicación local funcionando
- Dominio y conectividad adecuados para la ruta HTTPS elegida

### Primera prueba

1. Sigue el quickstart y configura un sitio de prueba.
2. Apunta el proxy al puerto interno correcto.
3. Verifica la URL externa, certificado y cabeceras del recorrido real.

**Qué comprobar:** La petición llega a la aplicación prevista por la URL que vas a compartir.

**Cuenta y compatibilidad:** No incluye IA ni sustituye la autenticación de la aplicación.

**Costes:** Software y licencias según distribución; servidor y dominio se gestionan aparte.

### Mejoras después de la primera prueba

- Mantén una configuración pequeña y versionada.
- Prueba recargas sin cortar el servicio.
- Distingue fallos del proxy de fallos de la aplicación.

### Límites

- HTTPS protege el transporte; no decide quién puede acceder a una herramienta privada.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://caddyserver.com/docs/quick-starts) · 2026-11-15

<a id="coolify"></a>

## Coolify

**Tipo:** Plataforma de despliegue autoalojable

Una interfaz para administrar despliegues en servidores que siguen necesitando operación.

### Antes de empezar

- Servidor compatible y acceso administrativo
- Repositorio o imagen de prueba

### Primera prueba

1. Sigue la instalación oficial en un servidor de prueba.
2. Conecta un proyecto y configura variables y almacenamiento.
3. Publica una app pequeña y verifica despliegue y recuperación.

**Qué comprobar:** Puedes desplegar una versión y volver a una anterior sin perder datos.

**Cuenta y compatibilidad:** Autoalojar el panel no elimina las cuentas de Git, servidor o proveedores.

**Costes:** Servidor, almacenamiento, copias y posibles servicios de pago aparte.

### Mejoras después de la primera prueba

- Separa proyectos y entornos.
- Documenta dónde están los datos.
- Prueba restauración y actualizaciones antes de producción.

### Límites

- Tener un panel no convierte una VPS en un servicio totalmente administrado.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://coolify.io/docs/) · 2026-11-15

<a id="activepieces-servicio"></a>

## Activepieces: flujos e integraciones

**Tipo:** Automatización entre servicios

Conecta eventos y aplicaciones con flujos visuales y piezas listas; puede incorporar IA como una etapa.

### Antes de empezar

- Cuenta cloud o instalación propia con Docker
- Credenciales de un servicio de prueba

### Primera prueba

1. Elige cloud o autoalojamiento según la documentación.
2. Crea un flujo manual que transforme un dato ficticio.
3. Añade un disparador real cuando hayas comprobado salida, errores y reintentos.

**Qué comprobar:** El evento produce una sola salida y un fallo queda visible sin duplicar la acción.

**Cuenta y compatibilidad:** IA opcional según el flujo; las conexiones con modelos y servicios tienen accesos propios.

**Costes:** Plan cloud o recursos del servidor, más APIs de modelos y servicios conectados.

### Mejoras después de la primera prueba

- Usa credenciales del sistema y entornos separados.
- Limita reintentos e identifica acciones ya realizadas.
- Documenta cómo desactivar el flujo.

### Límites

- Un flujo que envía mensajes o crea registros puede duplicarlos si se repite sin control.

Fichas del catálogo: [activepieces](fichas/activepieces.md)

### Fuentes

- [Documentación oficial del proyecto o servicio](https://www.activepieces.com/docs) · 2026-11-16

<a id="uptime-kuma"></a>

## Uptime Kuma

**Tipo:** Monitorización de disponibilidad

Comprueba disponibilidad de servicios y puede avisar cuando una comprobación cambia de estado.

### Antes de empezar

- Un lugar donde ejecutarlo
- URL o servicio de prueba y canal de aviso

### Primera prueba

1. Instala por la ruta del repositorio oficial.
2. Añade una comprobación sobre una URL de prueba.
3. Provoca una interrupción controlada y verifica recuperación y aviso.

**Qué comprobar:** El monitor distingue caída y recuperación con sus tiempos reales.

**Cuenta y compatibilidad:** No necesita un modelo para una comprobación básica. Los canales de aviso se configuran aparte.

**Costes:** Servidor y servicios de notificación según sus condiciones.

### Mejoras después de la primera prueba

- Comprueba una ruta que refleje el estado útil del servicio.
- Ajusta intervalos y tolerancia a fallos.
- Ejecuta el monitor fuera del mismo fallo que quieres detectar.

### Límites

- Un HTTP 200 no demuestra que un pago, una consulta o todo el recorrido de usuario funcione.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://github.com/louislam/uptime-kuma) · 2026-11-15

<a id="restic"></a>

## Restic

**Tipo:** Copias de seguridad

Crea copias cifradas y snapshots en destinos compatibles para recuperar archivos.

### Antes de empezar

- Origen, destino y espacio suficientes
- Contraseña conservada de forma recuperable

### Primera prueba

1. Sigue la guía con una carpeta ficticia.
2. Crea una copia y restaura a una carpeta distinta.
3. Compara el contenido antes de incluir datos importantes.

**Qué comprobar:** La restauración reproduce los archivos esperados y conoces cómo recuperar la contraseña.

**Cuenta y compatibilidad:** No requiere IA; un agente puede ayudar a preparar el procedimiento sin conocer tu secreto.

**Costes:** Software según licencia y almacenamiento o transferencia del destino.

### Mejoras después de la primera prueba

- Define retención después de medir crecimiento.
- Prueba restauraciones periódicas.
- Conserva copias independientes del equipo de origen.

### Límites

- Un log de copia completada no demuestra que hayas probado una restauración útil.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://restic.readthedocs.io/en/stable/) · 2026-11-15

<a id="neon"></a>

## Neon

**Tipo:** PostgreSQL administrado

Servicio PostgreSQL para una aplicación que necesita datos persistentes y entornos de trabajo.

### Antes de empezar

- Cuenta y proyecto de prueba
- Aplicación con un cliente PostgreSQL

### Primera prueba

1. Crea una base de prueba siguiendo el inicio rápido.
2. Guarda la conexión en las variables del backend.
3. Inserta y consulta datos ficticios desde la aplicación y verifica el entorno correcto.

**Qué comprobar:** La aplicación lee sus datos sin publicar la cadena de conexión.

**Cuenta y compatibilidad:** No es el modelo de IA ni un reemplazo automático de la autenticación de tu app.

**Costes:** Consulta almacenamiento, cómputo y condiciones de actividad y transferencia del plan.

### Mejoras después de la primera prueba

- Separa desarrollo y producción.
- Versiona migraciones.
- Comprueba pooling y copias para tu uso real.

### Límites

- Una cadena de conexión de servidor no se coloca en JavaScript público del navegador.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://neon.com/docs/introduction) · 2026-11-15

<a id="redis"></a>

## Redis

**Tipo:** Memoria de datos, caché y colas

Puede apoyar caché, colas y estados temporales de una aplicación; define primero el uso.

### Antes de empezar

- Instancia local o servicio administrado
- Cliente y datos ficticios

### Primera prueba

1. Elige un caso pequeño, como caché con expiración.
2. Configura la conexión en el backend y verifica una escritura y lectura.
3. Comprueba qué ocurre al expirar la clave o reiniciar el servicio.

**Qué comprobar:** La aplicación se comporta como esperas sin depender de que una caché conserve datos para siempre.

**Cuenta y compatibilidad:** No incluye IA ni sustituye automáticamente una base de datos principal.

**Costes:** Consulta licencia y distribución, memoria, persistencia y plan del proveedor.

### Mejoras después de la primera prueba

- Define expiraciones y límites.
- Mide memoria y política de expulsión.
- Separa caché y datos que no puedes perder.

### Límites

- La durabilidad depende de la configuración; no asumas que todos los datos sobrevivirán a un fallo.

### Fuentes

- [Documentación oficial del proyecto o servicio](https://redis.io/docs/latest/) · 2026-11-15

<a id="agentes-chat-servicio"></a>

## agentes.chat Cloud

**Tipo:** Espacio de trabajo con IA

Reúne al equipo y a sus agentes en canales con memoria compartida y aprobación humana para acciones delicadas.

### Antes de empezar

- Una cuenta de agentes.chat y un canal de ensayo
- Un proveedor de IA admitido, con su sesión o clave según la opción

### Primera prueba

1. Crea un espacio privado de prueba y pega una política ficticia de tres párrafos en su wiki.
2. Configura un agente para responder preguntas sobre la política y limita sus herramientas.
3. Pide una respuesta en el canal y valida con el texto que guardaste.

**Qué comprobar:** El agente responde en el canal correcto usando la política ficticia como fuente.

**Cuenta y compatibilidad:** Servicio web con clientes de escritorio y móvil. El proveedor documenta conexión desde Claude y otros clientes MCP. Consulta la opción de autenticación de cada modelo. El proyecto ofrece autoalojamiento.

**Costes:** Personal desde USD 29/mes en pago mensual o USD 288/año. El consumo de IA se paga por separado. El software autoalojado se ofrece gratis y requiere equipo propio.

### Mejoras después de la primera prueba

- Comprueba quién puede ver lo que el agente guarda antes de invitar a otras personas.

### Límites

- La memoria y los permisos del espacio abarcan a varias personas. Empieza con material ficticio.

Fichas del catálogo: [agentes-chat](fichas/agentes-chat.md)

### Fuentes

- [Producto](https://agentes.chat/) · 2026-11-22
- [Guías de acceso y autoalojamiento](https://agentes.chat/docs) · 2026-11-22
- [Precios de la nube](https://agentes.chat/pricing) · 2026-11-22

<a id="boat-sandboxes"></a>

## Boat

**Tipo:** Máquinas virtuales para desarrollo

Ofrece máquinas Ubuntu que puedes detener, reanudar o clonar para probar código en un entorno separado.

### Antes de empezar

- Cuenta de Boat y un medio de pago para activar la prueba
- Cliente oficial y proyecto de muestra sin credenciales

### Primera prueba

1. Lee la tabla de precios y consulta el tiempo disponible en tu cuenta.
2. Sigue el inicio oficial para crear una sola VM. Ejecuta una prueba pequeña del proyecto y conserva el resultado.
3. Detén la VM y comprueba en el panel el estado y el tiempo facturado.

**Qué comprobar:** La prueba termina en la VM y el panel muestra el entorno detenido.

**Cuenta y compatibilidad:** El proveedor documenta CLI para Windows, macOS y Linux, API para automatizar y uso de Claude Code, Codex u OpenCode dentro de Ubuntu. Autoriza el agente con su proveedor correspondiente.

**Costes:** Prueba de 7 días y 25 horas de cómputo con tarjeta. Mínimo mensual publicado de USD 20. La VM de 4 vCPU y 8 GB figura en USD 0.036/h. La IA tiene su propia facturación.

### Mejoras después de la primera prueba

- Revisa región, red y retención de snapshots antes de guardar código de un equipo.

### Límites

- Las máquinas anunciadas son CPU. Revisa los cargos por arranques adicionales y el alcance de red de la VM.

### Fuentes

- [Producto y compatibilidad](https://boat.dev/) · 2026-11-22
- [Tarifas y medición](https://docs.boat.dev/pricing) · 2026-11-22

<a id="hermes-plugin-hackathon"></a>

## Hermes Plugin Hackathon

**Tipo:** Directorio comunitario

Reúne proyectos del hackathon de Hermes Agent con filtros por función, plataforma, estado y tipo de permiso.

### Antes de empezar

- Navegador para explorar
- Hermes Agent y un perfil de prueba si más adelante evalúas un plugin

### Primera prueba

1. Elige una tarea pequeña como organizar notas ficticias.
2. Filtra por plataforma y abre el pull request del plugin que te interese.
3. Revisa qué archivos toca, qué servicio contacta y qué claves solicita antes de decidir.

**Qué comprobar:** Puedes identificar al autor, el código y los permisos de un candidato a partir de su pull request.

**Cuenta y compatibilidad:** Directorio para Hermes Agent. Cada proyecto declara sus plataformas, servicios y dependencias. Los resultados del directorio se pueden leer sin el agente.

**Costes:** La galería se puede consultar gratis. El coste de un plugin depende del servicio, modelo o clave que use.

### Mejoras después de la primera prueba

- Compara el pull request con la versión que planeas instalar.

### Límites

- La aparición en el hackathon y la integración en el catálogo del evento son señales de procedencia. La revisión de permisos queda a cargo de quien instala.

Fichas del catálogo: [hermes-agent](fichas/hermes-agent.md)

### Fuentes

- [Galería y pull requests](https://aaddrick.com/hermespluginhackathon) · 2026-11-22

<a id="modulify"></a>

## Modulify

**Tipo:** Constructor web con IA

Genera y edita sitios y aplicaciones web desde una descripción y ofrece vista previa y publicación.

### Antes de empezar

- Cuenta de Modulify y navegador
- Texto y recursos de ejemplo para una página sencilla

### Primera prueba

1. Abre un espacio de prueba y elige un sitio de una página.
2. Describe el negocio ficticio, sus secciones y la acción principal que debe verse en el móvil.
3. Comprueba la vista previa y las opciones de publicación antes de asociar un dominio.

**Qué comprobar:** La vista previa muestra las secciones pedidas y la acción principal funciona en una pantalla pequeña.

**Cuenta y compatibilidad:** Editor web con IA y créditos gestionados por Modulify. El flujo de la ficha usa la cuenta del servicio desde el navegador.

**Costes:** Plan gratuito para un sitio con créditos iniciales de una sola vez. La página de precios indica 35 y la documentación 50. Confirma el saldo en tu panel. Starter publica USD 25 al mes o USD 240 al año.

### Mejoras después de la primera prueba

- Anota cuántos créditos consume cada cambio y reutiliza imágenes propias para evitar generaciones innecesarias.

### Límites

- Dominio propio, equipo, publicación y funciones de datos dependen del plan. Consulta el desglose del espacio antes de pagar.

### Fuentes

- [Planes comerciales](https://modulify.ai/pricing) · 2026-11-22
- [Documentación del espacio y créditos](https://modulify.ai/docs/plans/plans) · 2026-11-22

<a id="tailscale-grok-mcp"></a>

## Tailscale con Grok Bot y MCP privado

**Tipo:** Integración de red

Permite a Grok Bot llegar a un servidor MCP dentro de una red Tailscale con autorización ligada al usuario.

### Antes de empezar

- Red Tailscale que administras y acceso a la integración en Grok Bot
- Un servidor MCP de prueba con datos ficticios y una función de solo lectura

### Primera prueba

1. Configura una regla de acceso limitada al servicio de prueba y revisa los recursos visibles para el usuario.
2. Autoriza Tailscale desde las integraciones de Grok Bot. Comprueba el nuevo dispositivo en la red.
3. Pide una consulta de solo lectura y verifica los registros. Revoca la conexión al terminar la prueba.

**Qué comprobar:** La consulta al recurso permitido funciona y el bot carece de acceso a otros recursos de la red de prueba.

**Cuenta y compatibilidad:** Tailscale documenta esta integración en Grok Bot vía OAuth. El servidor MCP puede vivir en un equipo propio. Cada cliente MCP necesita su propia ruta de red y autorización.

**Costes:** Aplican las cuotas del plan Tailscale y las del plan Grok Bot. Tailscale documenta el control por postura personalizada en Premium o Enterprise y reglas por etiqueta en otros planes.

### Mejoras después de la primera prueba

- Limita por servicio, usa una red de prueba y comprueba el efecto de revocar el dispositivo.

### Límites

- El dispositivo hereda la identidad y las políticas del usuario. Revisa el alcance de esas políticas antes de conceder acceso.

Fichas del catálogo: [mcp-inspector](fichas/mcp-inspector.md)

### Fuentes

- [Integración oficial y permisos](https://tailscale.com/blog/oauth-apps-ga) · 2026-11-22
- [Planes de Tailscale](https://tailscale.com/pricing) · 2026-11-22

<a id="cloudflare-startups"></a>

## Cloudflare for Startups

**Tipo:** Programa de créditos

Programa para empresas que quieren financiar consumo inicial de infraestructura Cloudflare.

### Antes de empezar

- Empresa elegible con sitio público y correo del dominio corporativo
- Una estimación de uso y la información que pide el formulario

### Primera prueba

1. Compara los requisitos de tu empresa con los niveles de financiación publicados.
2. Estima qué gastarías en Workers, almacenamiento o entrega y comprueba cuáles están cubiertos.
3. Si cumples los requisitos, solicita acceso y espera el resultado antes de contar con el crédito.

**Qué comprobar:** Puedes identificar tu nivel, servicios cubiertos, vencimiento y cargos que quedarían fuera.

**Cuenta y compatibilidad:** Solicitud web y cuenta de Cloudflare para consumir los créditos aprobados. Workers, Pages y servicios de datos siguen teniendo requisitos propios.

**Costes:** Cloudflare publica créditos de USD 10 000, 100 000 y hasta 350 000 por un año, según nivel y aprobación. Hay límites por producto y cargos por consumo fuera de cobertura.

### Mejoras después de la primera prueba

- Programa una revisión de gasto y el plan después del vencimiento.

### Límites

- La asignación y el uso dependen de criterios, aprobación y términos vigentes.

### Fuentes

- [Niveles, requisitos y usos cubiertos](https://www.cloudflare.com/startups/) · 2026-11-22

<a id="deepai-code"></a>

## DeepAI Code

**Tipo:** Agente de programación

Aplicación de escritorio que lee y edita proyectos con modelos servidos por DeepAI.

### Antes de empezar

- Instalador oficial para macOS, Windows o Linux
- Una copia de un proyecto pequeño y una cuenta DeepAI para los créditos de la cuenta

### Primera prueba

1. Descarga desde la página del producto la versión que corresponde a tu equipo.
2. Abre una copia de prueba. Pide explicar un archivo de configuración y después proponer un cambio pequeño.
3. Comprueba el diff y el gasto de créditos antes de aplicar cambios al proyecto original.

**Qué comprobar:** Puedes asociar una edición con el archivo correcto y verificarla antes de integrarla.

**Cuenta y compatibilidad:** Cliente local con modelos hospedados por DeepAI. La aplicación documenta uso sin clave de API propia. Tu acceso y cuota dependen de la cuenta DeepAI.

**Costes:** Nivel gratuito financiado con anuncios. La página anuncia hasta 250 Theos diarios en la cuenta gratuita para modelos medidos. Los planes de pago amplían la cuota y tienen su propia tarifa.

### Mejoras después de la primera prueba

- Abre una carpeta que solo incluya los archivos de prueba y comprueba qué comandos ejecuta el agente.

### Límites

- La lista de modelos, anuncios, cuotas y disponibilidad pueden cambiar. Revisa el tratamiento de archivos y prompts antes de usar código privado.

### Fuentes

- [Descargas, modelos y créditos](https://deepai.org/chat/ai-code) · 2026-11-22
- [Planes DeepAI](https://deepai.org/pricing) · 2026-11-22

<a id="nous-arete-27b"></a>

## Arete-27B de Nous Research

**Tipo:** Modelo de pesos abiertos

Versión de Qwen3.8-27B ajustada por Nous Research. Su ficha documenta las preferencias incorporadas y permite comparar sus respuestas con las del modelo base.

### Antes de empezar

- Un equipo con memoria y disco suficientes para el formato elegido
- Ficha del modelo, licencia Apache 2.0 y un motor compatible con el formato

### Primera prueba

1. Lee el objetivo del ajuste publicado por Nous y elige un conjunto de preguntas de prueba.
2. Elige los pesos oficiales y fija su revisión. Empieza con un contexto pequeño en un motor que soporte el checkpoint.
3. Compara el resultado con Qwen base usando los mismos datos y condiciones.

**Qué comprobar:** Puedes identificar qué pesos se cargaron y detectar diferencias de comportamiento en tus propios ejemplos.

**Cuenta y compatibilidad:** Pesos Safetensors para ejecución propia con un motor que admita la arquitectura. Verifica de forma independiente cualquier conversión para Ollama, llama.cpp o LM Studio.

**Costes:** Pesos publicados bajo Apache 2.0. La ejecución paga el equipo, electricidad o GPU alquilada. En BF16, 27 mil millones de parámetros ocupan alrededor de 54 GB solo en pesos.

### Mejoras después de la primera prueba

- Lee las limitaciones de la evaluación del autor y conserva tus propios casos de comparación.

### Límites

- Las versiones cuantizadas de terceros requieren verificar su procedencia y pueden cambiar las respuestas. El contexto también ocupa memoria.

### Fuentes

- [Ficha y pesos del editor](https://huggingface.co/NousResearch/Arete-27B) · 2026-11-22
- [Objetivo de entrenamiento y evaluación](https://nousresearch.com/arete) · 2026-11-22

<a id="jev-typesafe"></a>

## Jev de TypeSafe AI

**Tipo:** API de clasificación

Evalúa texto con preguntas numeradas y devuelve respuestas estructuradas que sirven para clasificar tickets, documentos y otros datos.

### Antes de empezar

- Cuenta, clave API de TypeSafe y saldo prepago
- Mensajes ficticios con su categoría esperada

### Primera prueba

1. Prepara tres mensajes inventados de soporte y una pregunta cerrada sobre si hablan de cobros.
2. Sigue System One para enviar el lote de preguntas sobre un solo mensaje y guarda la respuesta.
3. Compara las respuestas con tus etiquetas y revisa el campo de uso.

**Qué comprobar:** La respuesta trae la clave de cada pregunta y el número de tokens de entrada y salida.

**Cuenta y compatibilidad:** API HTTP de TypeSafe con token Bearer. Un agente de código puede ayudarte a integrar la llamada. Jev se autentica con su propia clave y ejecuta en la nube del proveedor.

**Costes:** USD 0.042 por millón de tokens de entrada. TypeSafe publica salida sin cargo y sin crédito de prueba.

### Mejoras después de la primera prueba

- Añade casos ambiguos y un umbral con revisión humana antes de clasificar tickets reales.

### Límites

- Mantén la clave en el servidor y empieza con datos sintéticos. La salida es una predicción que puedes contrastar con etiquetas humanas.

### Fuentes

- [Producto](https://typesafe.ai/) · 2026-11-22
- [System One](https://docs.typesafe.ai/api/system-one) · 2026-11-22
- [Tarifa oficial](https://help.typesafe.ai/articles/5187202169-how-much-does-jev-cost) · 2026-11-22

<a id="dnshe"></a>

## DNSHE

**Tipo:** Subdominios y DNS

Gestiona subdominios para demostraciones y registros DNS desde el panel del proveedor.

### Antes de empezar

- Cuenta DNSHE y un nombre disponible en una zona ofrecida
- Destino de prueba que admita el subdominio

### Primera prueba

1. Lee los términos de subdominios y comprueba el nombre y periodo ofrecidos.
2. Apunta el subdominio a una demostración pública sin datos personales.
3. Verifica que resuelve y que HTTPS responde si el alojamiento lo admite. Guarda la fecha de renovación.

**Qué comprobar:** El nombre resuelve al destino correcto y conoces cómo renovarlo o quitarlo.

**Cuenta y compatibilidad:** Panel DNS en navegador. La ruta de prueba usa DNS estándar y puedes seguirla con cualquier alojamiento que permita configurar ese nombre.

**Costes:** DNSHE anuncia subdominios y DNS gratuitos. El aviso vigente describe un periodo anual para altas gratuitas y renovación manual dentro de los 180 días previos al vencimiento. Cómputo y otros productos se cotizan aparte.

### Mejoras después de la primera prueba

- Usa un dominio bajo control propio cuando la continuidad de la dirección sea crítica.

### Límites

- DNSHE conserva control del dominio principal. Sus términos permiten cambiar o suspender el servicio gratuito.

### Fuentes

- [Servicio](https://www.dnshe.com/) · 2026-11-22
- [Términos del servicio](https://www.dnshe.com/tos.html) · 2026-11-22
- [Renovación anual](https://my.dnshe.com/announcements/6/DNSHE-Free-Domain-Registration-Duration-Adjustment-Notice-Introduction-of-an-Annual-Registration-System.html) · 2026-11-22

<a id="google-tabletop"></a>

## Tabletop de Google Labs

**Tipo:** Experimento colaborativo

Permite proponer una votación o un itinerario interactivo en un espacio compartido de Google Labs.

### Antes de empezar

- Navegador, cuenta Google y acceso aprobado
- La oferta anunciada es para mayores de 18 años en EE. UU. mediante lista de espera

### Primera prueba

1. Abre la página oficial y comprueba si tu cuenta tiene acceso.
2. Empieza con una encuesta ficticia de horarios usando una plantilla.
3. Revisa el alcance del enlace de invitación y comprueba el voto con un colaborador de prueba.

**Qué comprobar:** Las personas autorizadas pueden entrar a la encuesta y ver su actualización.

**Cuenta y compatibilidad:** Experimento web de Google Labs con despliegue por cuenta y región. El flujo documentado usa el navegador y su herramienta integrada.

**Costes:** El anuncio permite solicitar acceso y omite una tarifa pública. Verifica las condiciones que aparezcan en tu cuenta.

### Mejoras después de la primera prueba

- Prueba permisos y visibilidad con material poco sensible antes de adjuntar enlaces o archivos.

### Límites

- La lista de espera, disponibilidad y funciones pueden variar durante el experimento.

### Fuentes

- [Sitio del experimento](https://tabletop.google/about) · 2026-11-22
- [Anuncio y acceso](https://blog.google/innovation-and-ai/models-and-research/google-labs/tabletop/) · 2026-11-22

<a id="google-ai-harness-curso"></a>

## AI Harness Crash Course de Google Cloud Tech

**Tipo:** Curso en video

Introducción al entorno que conecta un modelo con instrucciones, herramientas y controles para completar una tarea.

### Antes de empezar

- Navegador con acceso a YouTube
- Conocer la idea básica de un agente de IA

### Primera prueba

1. Abre el video del canal Google Cloud Tech y anota qué hace cada parte del sistema.
2. Dibuja un ejemplo con una tarea, una herramienta de lectura y una condición de parada.
3. Explica con palabras tuyas cómo comprobarías el resultado antes de permitir otra acción.

**Qué comprobar:** Tu esquema indica qué recibe el agente, qué puede hacer y cómo compruebas su salida.

**Cuenta y compatibilidad:** Video público. El ejercicio sugerido se hace en papel o en un editor y funciona con cualquier agente como referencia.

**Costes:** Consulta del video sin tarifa de API. Si montas un ejemplo en la nube por tu cuenta, sus recursos y modelos pueden tener coste.

### Mejoras después de la primera prueba

- Distingue en el esquema el entorno que ejecuta herramientas y el modelo que decide.

### Límites

- El video es material formativo. Verifica versiones y precios en las guías de cada producto cuando implementes un flujo.

### Fuentes

- [Video de Google Cloud Tech](https://www.youtube.com/watch?v=2C_CefSQEAQ) · 2026-11-22

<a id="designed-to-scale"></a>

## Designed to Scale

**Tipo:** Curso interactivo

Explica conceptos de diseño de sistemas con diagramas animados que recorres paso a paso.

### Antes de empezar

- Navegador con JavaScript habilitado
- Una libreta para dibujar el flujo de un ejemplo

### Primera prueba

1. Abre el curso y avanza por un diagrama.
2. Dibuja una petición de usuario e identifica dónde vive cada componente.
3. Cambia una condición, como que un componente se caiga, y explica qué tendría que pasar.

**Qué comprobar:** Puedes recorrer la solicitud desde el navegador y explicar una decisión de diseño con el diagrama.

**Cuenta y compatibilidad:** Lectura interactiva en navegador. El ejercicio se puede completar con papel y lápiz.

**Costes:** Portada pública sin registro ni muro de pago observado. No se encontró una tarifa publicada para recorrer el curso.

### Mejoras después de la primera prueba

- Repite el ejercicio con tu proyecto y explica qué parte sigue sin cubrir.

### Límites

- El ejemplo sirve para aprender conceptos. Las decisiones de producción necesitan datos de carga y restricciones de tu proyecto.

### Fuentes

- [Curso y diagramas](https://designed-to-scale.vercel.app/) · 2026-11-22

<a id="treg-jobs-api"></a>

## treg Jobs API

**Tipo:** API de vacantes

Consulta vacantes públicas de empleadores y agrega información de empleo de varios proveedores en un servicio alojado.

### Antes de empezar

- Cuenta de treg y credencial propia del servicio
- Nombre de una empresa de prueba y un límite de gasto

### Primera prueba

1. Consulta el precio de la operación para leer el tablón público de un único empleador.
2. Lee una página de resultados y guarda el enlace a la vacante original.
3. Comprueba que sigue abierta en el sitio del empleador y revisa en el panel si hubo un cargo.

**Qué comprobar:** Cada resultado de prueba se puede contrastar con el anuncio original y puedes distinguir las operaciones facturadas.

**Cuenta y compatibilidad:** Servicio de treg con credencial propia. Su documentación presenta uso desde Claude Code y Codex. Para esta ficha basta la consulta de vacantes públicas en el servicio alojado.

**Costes:** Prepago por operación. Publica algunos tablones por USD 0, USD 0.0015 por vacante en búsquedas agregadas y USD 0.01 por consulta de percentiles salariales. Verifica la tarifa de la operación antes de llamarla.

### Mejoras después de la primera prueba

- Guarda el origen y la fecha de cada vacante antes de comparar resultados.

### Límites

- Empieza con anuncios públicos. Evita entregar currículos o información sobre personas al evaluar si el servicio te sirve.

### Fuentes

- [Jobs API y tarifas publicadas](https://treg.to/jobs-api) · 2026-11-22

<a id="qwen-harness-adapters"></a>

## Qwen3.8-27B adaptado para pi y OpenCode

**Tipo:** Adaptadores LoRA

Dos conjuntos de pesos adicionales ajustan el mismo modelo base para clientes distintos de programación asistida.

### Antes de empezar

- Qwen3.8-27B base y el adaptador que corresponda al cliente
- Un servidor compatible, espacio y memoria para base, adaptador y contexto

### Primera prueba

1. Elige pi u OpenCode y abre la ficha correspondiente. Fija la revisión del modelo base y el adaptador.
2. Sigue la ruta documentada para servirlo, por ejemplo con vLLM. Conecta el cliente a la dirección de prueba.
3. Pide una edición inocua en una carpeta temporal y compara el diff con el que propone el modelo base.

**Qué comprobar:** El servidor reporta el adaptador correcto y el cliente modifica únicamente el archivo de prueba esperado.

**Cuenta y compatibilidad:** Las fichas documentan vLLM y llama.cpp con su cliente correspondiente. La ruta con descarga y cómputo propios usa modelos locales. La compatibilidad documentada en estas fuentes cubre pi y OpenCode.

**Costes:** Adaptadores bajo Apache 2.0. Revisa también la licencia del modelo base. Operar el servidor usa disco y equipo o GPU alquilada. Los pesos base BF16 ocupan alrededor de 54 GB antes del contexto.

### Mejoras después de la primera prueba

- Compara resultados y memoria con el modelo base usando la misma tarea y la misma configuración.

### Límites

- El adaptador depende del checkpoint base. Los resultados publicados dependen del cliente y de los parámetros de evaluación.

Fichas del catálogo: [vllm](fichas/vllm.md) · [opencode](fichas/opencode.md) · [llama-cpp](fichas/llama-cpp.md)

### Fuentes

- [Ficha y pasos para pi](https://huggingface.co/harness-hub/Qwen3.8-27B-pi-adapted) · 2026-11-22
- [Ficha y pasos para OpenCode](https://huggingface.co/harness-hub/Qwen3.8-27B-opencode-adapted) · 2026-11-22

<a id="nemotron-bolt"></a>

## NVIDIA Nemotron 3.5 Bolt E4B

**Tipo:** Modelo de pesos abiertos

Modelo multimodal pequeño en parámetros activos con pesos publicados por NVIDIA. Admite ensayos de preguntas sobre imágenes y texto.

### Antes de empezar

- Pesos oficiales y entorno compatible con la variante seleccionada
- Equipo con memoria y disco suficientes y una imagen ficticia o pública

### Primera prueba

1. Abre la ficha oficial y revisa la licencia y variantes. Elige la guía para Transformers o vLLM según tu equipo.
2. Descarga la revisión que usarás y realiza una prueba con una imagen de ejemplo.
3. Limita el contexto y comprueba qué modelo se cargó, cuánta memoria consume y si interpreta bien la imagen.

**Qué comprobar:** La respuesta describe una característica observable de la imagen de prueba y puedes repetirla con los mismos pesos.

**Cuenta y compatibilidad:** La ficha BF16 documenta Transformers y vLLM. El acceso local depende del motor, versión y formato. Revisa una variante oficial específica si vas a usar otro motor.

**Costes:** Pesos sujetos a OpenMDW 1.1. El coste de usar un equipo propio o GPU alquilada es independiente de la descarga.

### Mejoras después de la primera prueba

- Compara la memoria del formato BF16 con una variante compatible de menor precisión antes de cambiar de equipo.

### Límites

- E4B describe parámetros activos. Para estimar memoria cuenta todos los pesos y el contexto de la variante elegida.

Fichas del catálogo: [vllm](fichas/vllm.md)

### Fuentes

- [Ficha oficial, licencia y ejecución](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16) · 2026-11-22

<a id="chrome-webmcp"></a>

## WebMCP y MCP según Chrome

**Tipo:** Guía de integración web

Ayuda a elegir cómo exponer una función de una página a un agente o cómo ofrecer herramientas desde un servidor MCP.

### Antes de empezar

- Navegador para leer y un sitio de prueba si quieres experimentar
- Chrome compatible con la prueba de origen o configuración de desarrollo descrita por Google

### Primera prueba

1. Lee la comparación y elige una función sencilla, como filtrar un listado público.
2. Decide si necesita el estado de la página abierta o si puede ejecutarse desde un servidor independiente.
3. Si pruebas WebMCP, registra solo una acción sin escritura y comprueba en Chrome que se descubre y devuelve el resultado esperado.

**Qué comprobar:** Puedes explicar por qué la acción va en la página o en un servidor y qué cliente puede invocarla.

**Cuenta y compatibilidad:** WebMCP sigue como propuesta con prueba de origen desde Chrome 149 según la guía. Comprueba soporte del navegador y del cliente. MCP de servidor tiene su propia ruta de conexión para cada agente.

**Costes:** Guías y experimento de navegador sin tarifa de lectura. Si usas un modelo hospedado o un servidor MCP externo, estima su gasto por separado.

### Mejoras después de la primera prueba

- Reserva confirmaciones para operaciones con efectos y deja que el sitio siga funcionando para personas sin un agente.

### Límites

- Versiones, permisos y disponibilidad varían según navegador. Revisa la documentación antes de diseñar una dependencia de producción.

Fichas del catálogo: [mcp-inspector](fichas/mcp-inspector.md)

### Fuentes

- [Cuándo usar WebMCP y MCP](https://developer.chrome.com/docs/ai/webmcp/compare-mcp) · 2026-11-22
- [Requisitos y estado en Chrome](https://developer.chrome.com/docs/ai/webmcp) · 2026-11-22

<a id="gemini-carbon"></a>

## Gemini 4 Carbon

**Tipo:** Modelo hospedado

Modelo de Google para tareas largas de razonamiento y desarrollo. Puedes evaluarlo en un problema acotado antes de incorporarlo a un flujo habitual.

### Antes de empezar

- Cuenta de Google con acceso al modelo
- Para API, proyecto con facturación y clave. Para uso en Antigravity, acceso del plan Google AI Ultra según disponibilidad

### Primera prueba

1. Elige si vas a usar la sesión de Antigravity o consumir la API desde tu código.
2. Pide a Carbon revisar un diseño ficticio y devolver tres decisiones con su justificación.
3. Si usas API, revisa el identificador de modelo, uso facturado y límite del proyecto.

**Qué comprobar:** Puedes documentar qué modelo se usó y qué cuenta, cuota o proyecto cubrió esa petición.

**Cuenta y compatibilidad:** Google documenta Gemini API de pago y disponibilidad para Google AI Ultra en Antigravity. El servicio ejecuta el modelo en Google. Claude Code, Codex y los motores locales tienen rutas de acceso propias.

**Costes:** Google anunció una tarifa introductoria de USD 2 por millón de tokens de entrada y USD 10 de salida para la API. Confirma el precio vigente en tu proyecto. La suscripción tiene sus propias cuotas.

### Mejoras después de la primera prueba

- Compara Carbon y un modelo más económico sobre el mismo resultado esperado antes de elegir uno para tareas habituales.

### Límites

- La disponibilidad depende de cuenta, región y plan. Una promoción puede terminar y algunos trabajos consumen tokens de razonamiento.

### Fuentes

- [Guía del desarrollador](https://aistudio.google.com/learn/gemini-4-carbon-developer-guide) · 2026-11-22
- [Anuncio de acceso para desarrolladores](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-4-carbon-developers/) · 2026-11-22
- [Información oficial de precio introductorio](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/) · 2026-11-22

<a id="openai-background"></a>

## OpenAI Responses API en segundo plano

**Tipo:** Guía de API

Inicia una respuesta larga en la API y recupera su estado y resultado desde tu aplicación.

### Antes de empezar

- Proyecto OpenAI API, clave restringida y acceso a un modelo compatible
- Una app de prueba que pueda guardar el identificador de la respuesta

### Primera prueba

1. Con datos ficticios, crea una respuesta con la opción de segundo plano de la guía.
2. Guarda el identificador y consulta el estado con espera entre intentos.
3. Muestra el resultado cuando finalice y conserva los estados de error o cancelación para que puedan revisarse.

**Qué comprobar:** La aplicación guarda un identificador, distingue estados intermedios y finales y muestra una sola respuesta.

**Cuenta y compatibilidad:** Función de la API Responses que requiere acceso con un proyecto API. Un agente de código puede ayudar a integrarla. El modelo se ejecuta en OpenAI.

**Costes:** Consulta las tarifas del modelo, tokens y herramientas elegidas en la API. La sesión de Codex usa su propio acceso. Comprueba créditos aplicables en la facturación del proyecto.

### Mejoras después de la primera prueba

- Cuando la aplicación madure, evalúa eventos de finalización con verificación de firma y manejo de reintentos.

### Límites

- La guía vigente indica almacenamiento temporal de datos, incluso con `store: false` o configuración Zero Data Retention. Revisa las ventanas y controles antes de enviar contenido sensible.

Fichas del catálogo: [openai-python](fichas/openai-python.md)

### Fuentes

- [Modo en segundo plano](https://developers.openai.com/api/docs/guides/background) · 2026-11-22
- [Tarifas de la API](https://developers.openai.com/api/docs/pricing) · 2026-11-22

<a id="owasp-cheat-sheets"></a>

## OWASP Cheat Sheet Series

**Tipo:** Listas de comprobación defensiva

Guías concretas para diseñar autenticación, registros, gestión de secretos y otros controles de seguridad.

### Antes de empezar

- Navegador y un flujo propio que quieras documentar

### Primera prueba

1. Elige una guía, por ejemplo la de autenticación.
2. Toma un control relevante y compáralo con tu diseño. Documenta quién lo aplica y qué evidencia lo demostraría.
3. Añade una prueba pequeña con datos de ejemplo para evitar regresiones.

**Qué comprobar:** La revisión identifica el control, su ubicación y una evidencia que otra persona puede comprobar.

**Cuenta y compatibilidad:** Documentación pública aplicable a distintos lenguajes y marcos. Puedes usarla en el navegador o como referencia al revisar código.

**Costes:** Lectura gratuita. El sitio publica la licencia de sus materiales. No exige una cuenta de IA.

### Mejoras después de la primera prueba

- Convierte los controles que aplican a tu proyecto en parte de la revisión de cambios.

### Límites

- Ajusta cada control al riesgo real y comprueba también la configuración del entorno donde despliegas.

### Fuentes

- [Índice de guías OWASP](https://cheatsheetseries.owasp.org/) · 2026-11-22
- [Guía de autenticación](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · 2026-11-22

<a id="virustotal-ai"></a>

## VirusTotal para agentes

**Tipo:** Conector MCP de análisis defensivo

Consulta informes existentes sobre archivos, dominios o IP y muestra las señales que VirusTotal tiene registradas.

### Antes de empezar

- Cuenta Google para VirusTotal AI y un cliente compatible
- Un dominio público conocido o un hash público que ya tenga informe

### Primera prueba

1. Abre la guía específica de tu cliente y concede solo lectura de informes.
2. Solicita el informe de un dominio público y confirma que la actividad indique una llamada al conector.
3. Revisa la fecha y el enlace del informe. Comprueba dónde se revoca el acceso.

**Qué comprobar:** Ves un informe real devuelto por el conector y puedes identificar la conexión que lo consultó.

**Cuenta y compatibilidad:** VirusTotal publica guías para Claude, Claude Code, Codex y Antigravity CLI, con estado de validación por cliente. OAuth usa cuenta Google. No se necesita clave de la API clásica de VirusTotal.

**Costes:** Cuotas gratuitas publicadas de 60 consultas por minuto y 1 000 por día UTC por cuenta OAuth o token. Hasta los informes repetidos cuentan. El cliente de IA puede tener sus propias cuotas.

### Mejoras después de la primera prueba

- Conserva el hash y la fecha de consulta para que otra persona pueda revisar la misma evidencia.

### Límites

- Empieza con lectura. Subir archivos y enviar URL usan otros permisos y el esquema de compartición estándar de VirusTotal.
- Una detección es una señal que debes interpretar con la procedencia y el comportamiento del archivo.

### Fuentes

- [VirusTotal AI, clientes, cuotas y privacidad](https://ai.virustotal.com/) · 2026-11-22

<a id="roadmap-ciberseguridad"></a>

## roadmap.sh Cyber Security

**Tipo:** Mapa de estudio

Ordena los conceptos de seguridad en un mapa que puedes usar para preparar un plan de estudio.

### Antes de empezar

- Navegador y un tema inicial como redes, autenticación o registros

### Primera prueba

1. Abre el mapa y elige tres conceptos de redes o seguridad defensiva.
2. Anota para qué sirve cada concepto y aplícalo a un sistema ficticio.
3. Marca como siguiente tema aquello que todavía no puedas explicar.

**Qué comprobar:** Tienes un plan corto con orden, ejemplos propios y un criterio de avance.

**Cuenta y compatibilidad:** Mapa público en navegador. La cuenta sirve para guardar avance si quieres usar esa función.

**Costes:** Consulta pública del mapa sin clave de IA. Otros planes o materiales enlazados pueden tener condiciones propias.

### Mejoras después de la primera prueba

- Cruza los temas de autenticación con la lista de comprobación de OWASP cuando revises tu propia aplicación.

### Límites

- Revisa la actualidad de cada recurso externo y enfoca la ruta inicial en protección y monitoreo.

### Fuentes

- [Mapa público](https://roadmap.sh/cyber-security) · 2026-11-22

<a id="portswigger-academy"></a>

## PortSwigger Web Security Academy

**Tipo:** Formación en seguridad web

Material de referencia de PortSwigger para reconocer problemas de autenticación y diseño de permisos en aplicaciones web.

### Antes de empezar

- Navegador y una aplicación propia o ficticia para diseñar su lista de controles

### Primera prueba

1. Escoge en el temario autenticación o control de acceso e identifica qué activo debe protegerse.
2. Dibuja dos roles en una app ficticia y escribe qué acción debe poder realizar cada uno.
3. Convierte cada regla en un criterio de aceptación, incluyendo la respuesta esperada al faltar permisos.

**Qué comprobar:** Tienes una lista de controles y criterios para revisar la autenticación y los roles de tu propia app.

**Cuenta y compatibilidad:** Material público en navegador. La prueba documental usa la aplicación ficticia. Una cuenta de la Academy permite llevar el progreso.

**Costes:** Academy se anuncia gratuita. Las licencias comerciales de Burp Suite son un producto aparte.

### Mejoras después de la primera prueba

- Contrasta tus criterios con las recomendaciones de autenticación y control de acceso de OWASP.

### Límites

- Usa esta ficha para diseño de controles y validación autorizada de tus aplicaciones.

### Fuentes

- [Temario y condiciones de la Academy](https://portswigger.net/web-security) · 2026-11-22
- [Lista defensiva de OWASP para autenticación](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html) · 2026-11-22

<a id="mitre-attack-defensa"></a>

## MITRE ATT&CK

**Tipo:** Base de conocimiento defensiva

Usa un vocabulario común para relacionar casos de detección con comportamientos observados y comprobar qué señales cubre tu equipo.

### Antes de empezar

- Navegador y un registro de seguridad de ejemplo
- Una hoja para anotar qué señal existe y qué falta

### Primera prueba

1. Elige un caso defensivo, como una alerta de uso anómalo de cuenta.
2. Busca el identificador de la técnica que describe la señal y lee sus mitigaciones.
3. Documenta qué registro de tu ejemplo permite detectarla y qué revisión humana harías.

**Qué comprobar:** Cada relación entre señal y técnica trae identificador, fuente del registro y acción defensiva.

**Cuenta y compatibilidad:** Referencia pública usable por equipos con SIEM o con una hoja de cálculo. Para leer y preparar la matriz no necesitas una API.

**Costes:** Consulta web sin cargo. Cualquier coste de almacenamiento, SIEM o monitoreo depende de tu infraestructura.

### Mejoras después de la primera prueba

- Registra versión de la matriz y revisa cambios antes de actualizar una regla.

### Límites

- La terminología organiza observaciones. El contexto y la evidencia siguen siendo necesarios para concluir qué pasó.

### Fuentes

- [Base oficial ATT&CK](https://attack.mitre.org/) · 2026-11-22

<a id="gemma-local"></a>

## Gemma 4 en tu equipo

**Tipo:** Guía de modelos locales

Elige una variante de Gemma 4 y pruébala en Ollama para responder preguntas de texto desde tu computadora.

### Antes de empezar

- Ollama compatible con Gemma 4.
- Espacio de disco para la descarga y RAM para el modelo y el contexto. Consulta la tabla de variantes antes de elegir.

### Primera prueba

1. Abre la guía de Gemma para Ollama y busca una variante que quepa con margen en tu equipo.
2. Descarga la variante elegida desde la biblioteca de Ollama y abre su chat siguiendo la guía.
3. Pide que extraiga tres datos de un párrafo ficticio. Valida cada dato contra el original.

**Qué comprobar:** El cliente muestra la variante elegida y la respuesta contiene tres datos que se pueden comprobar en el texto.

**Cuenta y compatibilidad:** Ollama ejecuta la variante admitida en el equipo. La guía de Google también documenta llama.cpp y otros motores. Comprueba formatos y versiones para cada ruta.

**Costes:** La prueba local usa los pesos descargados y tu equipo, sin clave de API. La nube y los servicios de inferencia tienen sus propios planes y tarifas.

### Mejoras después de la primera prueba

- Empieza con un contexto corto y anota memoria y tiempo para comparar variantes con el mismo ejemplo.

### Límites

- El tamaño descargado no equivale a memoria en ejecución. Comprueba versión, variante y contexto antes de comparar resultados.

Fichas del catálogo: [ollama](fichas/ollama.md) · [llama-cpp](fichas/llama-cpp.md)

### Fuentes

- [Gemma con Ollama](https://gemma.ai/deployment/ollama/) · 2026-11-25
- [Variantes y condiciones de Gemma 4](https://gemma.ai/models/gemma-4/) · 2026-11-25
- [Etiquetas en Ollama](https://ollama.com/library/gemma4) · 2026-11-25

<a id="karpathy-zero-to-hero"></a>

## Neural Networks: Zero to Hero

**Tipo:** Curso público

Curso de Andrej Karpathy para entender cómo aprende una red y cómo se construye un modelo de lenguaje básico.

### Antes de empezar

- Navegador para consultar el curso.
- Nociones de Python y derivadas para seguir las partes de código.

### Primera prueba

1. Abre la primera lección y elige una operación de la explicación de micrograd.
2. Dibuja cómo el resultado cambia al modificar un número de entrada.
3. Explica con tus palabras por qué ese cambio sirve para ajustar un modelo.

**Qué comprobar:** Puedes explicar qué representa la derivada de tu ejemplo y cómo orienta un ajuste.

**Cuenta y compatibilidad:** Curso en video con recursos de práctica. Puedes seguir la primera actividad con papel o en un cuaderno de Python.

**Costes:** Consulta del temario y videos sin compra obligatoria. Un servicio de cómputo o materiales adicionales pueden tener costes propios.

### Mejoras después de la primera prueba

- Si ya manejas derivadas, continúa con makemore y anota qué diferencia hay entre predecir un carácter y entrenar un modelo completo.

### Límites

- Las prácticas posteriores requieren preparación en Python y pueden depender de bibliotecas y versiones distintas.

### Fuentes

- [Temario y requisitos del autor](https://karpathy.ai/zero-to-hero.html) · 2026-11-25

## Prompts

Sustituye los campos entre corchetes. Revisa la respuesta antes de ejecutar acciones.

### Elegir una herramienta sin instalar de más

Antes de elegir un repo o pagar un plan.

```text
Quiero conseguir [resultado concreto] a partir de [entrada]. Mi experiencia es [nivel], uso [sistema, RAM y GPU si los conozco] y ya tengo acceso a [agentes o planes].
Propón hasta tres puntos de partida. Distingue cliente, modelo, API, servicios y ejecución local. Para cada opción explica una función que me ayude, un requisito que pueda bloquearme, posibles costes y una primera prueba observable.
Consulta las fuentes oficiales actuales. No supongas que una suscripción incluye otra API. Si falta un dato decisivo, indícalo. Recomienda una opción para probar primero con razones y explica qué haría cambiar la elección.
```

**Resultado esperado:** Una lista corta con diferencias y una primera prueba, sin una pila de instalaciones.

### Instalar con acompañamiento

Cuando ya elegiste una herramienta.

```text
Ayúdame a empezar con [herramienta y URL oficial] en [sistema]. Quiero lograr [resultado pequeño]. Mi experiencia es [nivel].
Lee la instalación de la versión actual. Antes de dar un comando, confirma su origen, requisitos, carpeta y tipo de terminal. Separa descargar, instalar dependencias, autenticar, configurar modelos y arrancar.
Guíame una acción cada vez. Explica qué modifica, si descarga archivos y cómo comprobarla. No pidas que pegue claves en la conversación. Si falla, usa el error sin secretos para diagnosticar ese paso; no repitas toda la instalación. Termina cuando la prueba produzca el resultado acordado.
```

**Resultado esperado:** Pasos adaptados al sistema con una comprobación por etapa.

### Resolver un error con evidencia

Cuando una instalación o función falla.

```text
Estoy usando [herramienta y versión] en [sistema]. Quiero [resultado]. El último paso que funcionó fue [paso]. El error, sin secretos, es [mensaje].
Primero localiza la capa que falla: instalación, cuenta, proveedor, red, aplicación o datos. Propón las comprobaciones de lectura mínimas para distinguir dos o tres causas probables. Usa la documentación de esta versión.
Aplica un cambio cada vez y conserva cómo revertirlo. Verifica el recorrido original después de corregirlo. No borres datos ni reinstales todo para ocultar una causa sin demostrarla.
```

**Resultado esperado:** Una causa comprobada o incertidumbre concreta y el siguiente diagnóstico útil.

### Crear instrucciones útiles del proyecto

Cuando el agente repite errores del mismo repositorio.

```text
Revisa este proyecto y prepara instrucciones breves para [AGENTS.md / CLAUDE.md / formato documentado de mi agente]. Incluye propósito, carpetas relevantes, cómo arrancar, pruebas útiles y decisiones que deben conservarse.
Usa comandos existentes y comprueba sus requisitos. No dupliques todo el README ni escribas preferencias genéricas que no aplican. Separa hechos comprobados de preguntas abiertas. Propón el texto y muestra dónde debe ir según el ámbito del cliente.
Verifica el archivo resultante y señala cualquier instrucción que no pudiste comprobar. Convierte un procedimiento largo reutilizable en una propuesta de skill separada.
```

**Resultado esperado:** Un archivo breve y específico que otro colaborador pueda revisar.

### Cambiar de modelo con una prueba y reversión

Antes de modificar la configuración de un cliente.

```text
Quiero probar [proveedor/modelo] en [cliente y versión], conservando una forma de volver a [configuración anterior]. Mi tarea de evaluación será [ejemplo y resultado esperado].
Consulta la integración oficial de ambas partes. Distingue API estándar, coding plan, inicio de sesión y endpoint local. Comprueba qué formato de API, herramientas y permisos necesita mi cliente. No reutilices una clave o endpoint de otro plan sin documentación.
Prepara el cambio en el ámbito más pequeño admitido, con copia de la configuración sin secretos. Haz la misma prueba antes y después y registra resultado, errores, consumo y latencia observados. No declares un ganador por un benchmark ajeno.
```

**Resultado esperado:** Un cambio acotado, una comparación repetible y una vuelta atrás clara.

### Revisar un cambio antes de integrarlo

Antes de commit, merge o publicación.

```text
Revisa [cambio o diff] para comprobar [comportamiento esperado]. Lee el contexto necesario. Busca errores con un caso concreto que los reproduzca y explica su impacto.
Comprueba entradas vacías o extremas, permisos, errores de red y persistencia cuando apliquen. No conviertas preferencias de estilo en fallos funcionales. Ejecuta las comprobaciones relevantes y distingue lo probado de lo inferido.
Entrega primero los problemas que impiden usar el cambio, con ubicación y propuesta de corrección. Si no encuentras problemas, indica el alcance de la revisión y qué sigue sin estar verificado.
```

**Resultado esperado:** Hallazgos concretos o una revisión con límites explícitos.

### Revisar una interfaz para principiantes

Cuando una pantalla funciona pero cuesta entenderla.

```text
Revisa [pantalla] para una persona [experiencia] que quiere [tarea]. Completa el recorrido con datos de prueba y observa dónde necesita adivinar.
Comprueba etiquetas, orden de lectura, teclado, móvil, texto largo, errores y estado sin resultados. Mantén la identidad del producto. Propón las mejoras que reduzcan dudas y pasos, con el motivo de cada una.
Implementa los cambios necesarios y verifica el mismo recorrido en escritorio y móvil. Guarda una captura del resultado. No añadas animaciones o pantallas que no ayuden a completar la tarea.
```

**Resultado esperado:** Un recorrido claro con estados comprobados y evidencia visual.

### Entender acceso y coste antes de ejecutar

Antes de conectar una API o dejar una tarea larga.

```text
Quiero usar [herramienta] mediante [suscripción / API / modelo local] para [volumen y duración aproximados].
Identifica por separado cliente, modelo, alojamiento, almacenamiento y servicios externos. Consulta las condiciones oficiales de mi ruta; no uses una publicación social como tarifa actual. Indica unidades de cobro, límites y datos que faltan para estimar.
Propón una prueba pequeña y un límite de trabajo. Después usa el consumo observado para estimar un rango con sus supuestos. Distingue estimación de factura y no compres créditos ni actives recargas por mí.
```

**Resultado esperado:** Un mapa de costes y una prueba medible, sin promesas de gratuidad.

### Reducir contexto sin perder decisiones

Cuando las sesiones se alargan o repiten lecturas.

```text
Analiza el contexto de esta tarea y prepara un relevo breve que incluya objetivo, decisiones vigentes, archivos modificados, pruebas realizadas y próximo paso concreto.
Conserva incertidumbres y trabajo pendiente. Elimina repeticiones y material que no afecta a la decisión siguiente. Propón qué instrucciones estables deben ir en el proyecto y qué procedimiento merece una skill.
No prometas un porcentaje de ahorro. Si medimos consumo, compara tareas equivalentes. No confundas resumir la conversación con borrar datos del proyecto o detener servicios.
```

**Resultado esperado:** Un relevo que permita continuar sin reconstruir todo el historial.

### Añadir una skill o conexión con un propósito

Antes de instalar una colección de extensiones.

```text
En [cliente y versión] necesito [capacidad]. Determina si basta una instrucción, una skill, un plugin, un MCP o un servicio externo. Explica la diferencia aplicada a esta tarea.
Comprueba repositorio oficial, compatibilidad y método de instalación. Instala o propón una sola pieza con el ámbito y permisos necesarios. No asumas que copiar un repositorio registra todas sus skills.
Verifica que la capacidad aparece y resuelve una prueba pequeña. Documenta qué cuenta utiliza, qué datos recibe, costes y cómo retirar la conexión.
```

**Resultado esperado:** Una extensión justificada y una prueba de que aporta la capacidad necesaria.

### Publicar una aplicación con verificación

Cuando el proyecto funciona localmente.

```text
Quiero publicar [proyecto] en [servicio]. Determina si es sitio estático, frontend con backend, API, proceso persistente o servicio con datos.
Comprueba build, variables, secretos, persistencia y límites del runtime. Prepara primero una URL de prueba y una vuelta atrás. Conserva dominio, DNS y datos existentes.
Verifica desde el navegador el recorrido [tarea concreta], incluyendo backend y lectura de datos. Un build aprobado no basta. Publica según el alcance autorizado y comprueba la URL final y la versión desplegada.
```

**Resultado esperado:** Un enlace útil con el recorrido principal verificado y recuperación documentada.

### Probar que una copia se puede restaurar

Antes de una actualización o cambio con datos.

```text
Prepara un procedimiento de copia para [datos y servicio]. Identifica archivos, volúmenes, base de datos y configuración que deben recuperarse juntos.
Haz la prueba con datos ficticios o una copia autorizada. Restaura en [entorno separado] y comprueba contenido y funcionamiento. No sobrescribas la única copia ni elimines el origen para demostrar la restauración.
Entrega ubicación de copias sin secretos, retención propuesta, requisitos de acceso y pasos de recuperación. Distingue copia creada de restauración comprobada.
```

**Resultado esperado:** Una restauración observada y un procedimiento que otra persona pueda repetir.

### Diseñar una automatización Android

Para elegir entre macros, ADB o un agente.

```text
Quiero que mi Android [acción] cuando [disparador], salvo [restricciones]. Mi dispositivo y versión son [datos]. Quiero detenerlo mediante [método].
Distingue reglas de MacroDroid/Tasker, control desde un ordenador con ADB/scrcpy y un agente que interpreta la pantalla. Elige la solución más simple que cubra la tarea y consulta sus límites en mi versión.
Empieza con una notificación de prueba y datos ficticios. Verifica permisos, segundo plano y batería con el evento real. Añade IA solo si hace falta interpretar contenido. Antes de enviar mensajes, pagar o borrar, deja una revisión explícita.
```

**Resultado esperado:** Un flujo con disparador, restricciones, prueba real y forma de detenerlo.

### Diseñar un atajo de iPhone

Para automatizar una acción que iOS exponga.

```text
Quiero automatizar [tarea] en iPhone con [iOS y app]. La entrada es [dato] y el resultado será [salida].
Comprueba si Atajos o la app exponen las acciones necesarias y si el disparador requiere confirmación. No prometas control libre de toda la interfaz ni ejecución permanente en segundo plano.
Diseña primero un atajo manual que muestre o guarde un dato ficticio. Verifica su resultado antes de añadir la automatización. Si requiere un ordenador, simulador o API externa, explica esos requisitos y costes por separado.
```

**Resultado esperado:** Un atajo viable o el límite concreto que impide esa automatización.

### Trabajar desde el teléfono en un agente remoto

Para continuar una tarea que corre en otro equipo.

```text
Quiero usar [agente] desde [Android o iPhone], pero el proyecto se ejecuta en [equipo o servidor]. Comprueba la ruta remota oficial del cliente o una sesión SSH mediante una red autorizada.
Explica qué equipo debe permanecer encendido, dónde están los archivos, qué cuenta paga la IA y cómo se autentica cada extremo. No lo presentes como control de las apps del teléfono.
Prueba una consulta de lectura en un proyecto ficticio, cierra y recupera la sesión y verifica la identidad del equipo. Documenta cómo desconectar y revocar el acceso.
```

**Resultado esperado:** Una sesión remota comprobada con sus dependencias y límites claros.

### Evaluar modelos con tu trabajo real

Antes de cambiar por una promesa de rendimiento.

```text
Compara [candidatos] para [tarea concreta]. Usa la misma entrada, herramientas, restricciones y criterio de aceptación en todos. Registra modelo, versión, cliente y fecha.
Mide éxito de la tarea, errores, intervenciones, latencia y consumo observado. Separa el rendimiento del modelo del harness y del entorno. Si un candidato no puede usar una herramienta necesaria, indícalo.
Entrega diferencias útiles para elegir, con límites de la prueba y fuentes. No extrapoles un caso a todos los proyectos ni conviertas precios promocionales o benchmarks ajenos en resultados propios.
```

**Resultado esperado:** Una comparación pequeña, reproducible y relevante para tu decisión.

### Simplificar una pantalla hasta lo esencial

Cuando una pantalla funciona pero se siente recargada de textos, etiquetas y adornos.

```text
Revisa [pantalla o ruta] pensando en una sola tarea: [tarea principal]. Antes de cambiar nada, dime qué supones sobre quién la usa y qué necesita ver primero.
Haz un inventario de cada texto, etiqueta, icono y adorno, e indica si ayuda a completar la tarea o solo decora.
Si un elemento existe únicamente para aclarar algo confuso, propón reordenar la pantalla en lugar de sumar más explicaciones.
Elige cambios que beneficien a la vez a quien usa la pantalla, a quien mantiene el código y a un agente que la lea después.
Muéstrame la lista de recortes y cambios de estructura y espera mi visto bueno. No elimines funciones ni textos legales.
Al terminar, entrega capturas antes y después en escritorio y móvil, y confirma que [tarea principal] se sigue completando.
```

**Resultado esperado:** Una pantalla con menos ruido, la lista de lo que se quitó y capturas que demuestran que la tarea sigue funcionando.

Idea de partida: [Pase de diseño limpio y esencial](https://x.com/Voxyz_ai/status/2118720058872701273). Texto reescrito por Alexandría.

### Revisión antes de lanzar con revisores en paralelo

Cuando tu sitio o app está casi listo y quieres encontrar fallos de diseño, móvil, estados y textos antes de mostrarlo.

```text
Quiero revisar [sitio o app] antes de lanzarlo. Reparte el trabajo entre [4 o 5] subagentes, uno por área, y que ninguno edite archivos.
Áreas: coherencia visual (colores, tamaños, espaciados, bordes), uso en móvil, estados de carga, vacío y error, recorrido completo de [recorridos clave] con teclado y ratón, y detalles de publicación (título, descripción, icono, textos de relleno).
Cada hallazgo indica página, archivo probable, cómo reproducirlo y gravedad. Antes de empezar, dime qué supones sobre el público y los navegadores.
Une todo en una sola lista sin duplicados, ordenada por gravedad, y detente hasta que yo elija qué se corrige.
Con mi confirmación, corrige en una pasada solo lo aprobado. No toques textos legales, precios ni datos reales sin preguntarme.
Entrega capturas antes y después de cada corrección y marca lo que no pudiste verificar.
```

**Resultado esperado:** Una lista priorizada de problemas, las correcciones aprobadas aplicadas y capturas que muestran cada cambio.

Idea de partida: [Revisión previa al lanzamiento con subagentes](https://x.com/Voxyz_ai/status/2118720058872701273). Texto reescrito por Alexandría.

### Encontrar por qué una web carga lenta

Cuando tu web tarda en abrir, sobre todo en móvil, y no sabes si la causa son imágenes, código, datos o servidor.

```text
Ayúdame a acelerar [sitio] sin quitar funciones. Empieza midiendo: sobre una compilación de producción o una vista previa, pasa Lighthouse en modo móvil tres veces por [páginas] y anota la mediana.
Luego busca causas por capas, todavía sin editar: imágenes y fuentes, peso del código que se descarga, consultas y respuestas de datos, y ubicación o caché del servidor.
Para cada causa indica archivo, página afectada, mejora esperada y riesgo. Explica en palabras sencillas cada término técnico y dime qué supones cuando no puedas comprobar algo.
Propón un orden de arreglos del menos al más arriesgado y espera mi aprobación.
Pregúntame antes de quitar dependencias, mover la región del servidor o tocar la base de datos. No guardes en caché respuestas ligadas a una persona con sesión iniciada.
Al final, mide igual que al principio y entrégame una tabla con los números de antes y después.
```

**Resultado esperado:** Una tabla de métricas antes y después, con los cambios aplicados y su efecto medido.

Idea de partida: [Auditoría de lentitud de un sitio](https://x.com/Voxyz_ai/status/2118720058872701273). Texto reescrito por Alexandría.

### Recuperar espacio que dejó el trabajo de desarrollo

Cuando el disco se llena y sospechas de dependencias, cachés, contenedores o modelos descargados.

```text
Mi disco en [sistema] está casi lleno. Recorre mi carpeta de usuario mirando solo tamaños: no abras el contenido de ningún archivo y salta [carpetas excluidas], unidades externas y todo lo que pida permisos.
Busca lo que suele acumular el desarrollo: dependencias, cachés de compilación, imágenes de contenedores, entornos virtuales y modelos locales.
Genera una página HTML local con un mapa por tamaño y dos grupos: "se puede limpiar" y "revisar antes". Historiales de agentes, modelos y contenedores siempre van en "revisar antes".
Para cada elemento muestra ruta, tamaño y consecuencia de borrarlo. Indica qué supones cuando no tengas claro su origen.
No borres nada. Cuando yo marque elementos, prepara un script que use el comando de limpieza propio de cada herramienta y déjalo para que yo lo revise y lo ejecute.
Guarda los tamaños con fecha en [archivo de registro] y, la próxima vez, léelo primero para señalar qué creció.
```

**Resultado esperado:** Un mapa de espacio con dos grupos, un script de limpieza revisable y un registro para comparar más adelante.

Idea de partida: [Limpieza de restos de desarrollo](https://x.com/Voxyz_ai/status/2118720058872701273). Texto reescrito por Alexandría.

### Evitar cuelgues y cobros dobles en llamadas externas

Cuando tu app llama a pagos, bases de datos, colas o modelos de IA y quieres que no se quede colgada ni repita operaciones.

```text
Haz un inventario de todas las llamadas que [proyecto] hace hacia fuera: HTTP, base de datos, colas y proveedores de IA, con archivo y línea.
Marca las que no tienen tiempo límite y propón uno razonable, explicando qué valor supones y por qué.
Donde ya haya reintentos, cámbialos a espera exponencial con tope y una variación aleatoria. No añadas reintentos nuevos.
Revisa cada escritura que pueda repetirse: si se ejecuta dos veces, ¿duplica registros o cobra de nuevo? Haz una lista aparte con esos riesgos y cómo volverlas idempotentes.
Comprueba si los grupos de conexiones aguantan [usuarios simultáneos] en el pico; solo informa, no los cambies.
Enséñame el plan antes de editar y no toques nada relacionado con pagos sin mi aprobación. Termina cuando [comando de pruebas] pase y me des la lista de cambios por archivo.
```

**Resultado esperado:** Llamadas con tiempos límite y reintentos seguros, una lista de escrituras con riesgo de duplicarse y pruebas en verde.

Idea de partida: [Llamadas colgadas y cobros dobles](https://x.com/Voxyz_ai/status/2118720058872701273). Texto reescrito por Alexandría.

### Convertir tus correcciones de diseño en reglas

Cuando corriges una y otra vez lo mismo en las interfaces que genera el agente.

```text
Repasa las correcciones de diseño que te pedí en [esta sesión y las N anteriores]. Agrupa las que se repiten: espaciados, tamaños, colores, animaciones, textos.
Para cada grupo redacta una regla corta y comprobable, con su motivo y un ejemplo de antes y después. Nada de reglas vagas como "que se vea mejor".
Dime qué supones cuando una corrección pudo ser un gusto puntual y no una norma.
Propón dónde guardarlas ([DESIGN.md, AGENTS.md o una skill]) y muéstrame el texto exacto antes de escribirlo. No borres reglas existentes; si dos se contradicen, pregúntame.
Para verificar, aplica las reglas a [pantalla de prueba] e indica cuáles se cumplen y cuáles no.
```

**Resultado esperado:** Un conjunto breve de reglas de diseño con motivo y ejemplo, guardado donde el agente lo lea en cada sesión.

Idea de partida: [Skill learn-taste](https://github.com/emilkowalski/skills). Texto reescrito por Alexandría.

### Convertir una idea vaga en requisitos verificables

Antes de pedir una función nueva, cuando solo tienes una idea general de lo que quieres.

```text
Quiero añadir esto a [proyecto]: [idea]. Todavía no escribas código.
Lee las partes del proyecto relacionadas y redacta una especificación breve: a quién sirve, qué problema resuelve, el recorrido principal, los casos límite y qué pasa cuando algo falla.
Cierra con criterios de aceptación que yo pueda comprobar uno a uno sin conocimientos técnicos.
Separa lo que comprobaste en el proyecto de lo que supones. Hazme como máximo cinco preguntas numeradas, cada una con tu respuesta recomendada, sobre decisiones que cambien la función de forma importante.
No crees archivos ni ramas hasta que apruebe la especificación.
```

**Resultado esperado:** Una especificación de una página con criterios de aceptación comprobables y las dudas importantes resueltas.

Idea de partida: [Prompts prácticos para Codex](https://x.com/LDT0545/status/2118441074683445641). Texto reescrito por Alexandría.

### Revisar la accesibilidad con una tabla de antes y después

Cuando quieres que una página se pueda usar con teclado, lector de pantalla y buena legibilidad.

```text
Revisa [página o componente] tomando como guía WCAG 2.2 nivel AA. Si no te indico el público, dime qué supones.
Comprueba contraste del texto (al menos 4.5:1 en texto normal), foco visible, navegación completa con teclado, nombre accesible en botones que solo tienen icono, errores comprensibles y respeto a la preferencia de reducir movimiento.
Primero lista solo los problemas que puedas verificar, a quién afectan y dónde están. Aparta lo que necesite prueba manual con lector de pantalla.
Propón arreglos que respeten el diseño actual y pregúntame antes de cambiar colores de marca o la estructura.
Tras aplicar los aprobados, entrega una tabla con problema, estado previo, estado nuevo y cómo lo comprobaste.
```

**Resultado esperado:** Una tabla de problemas de accesibilidad con su corrección y la forma de verificar cada uno.

Idea de partida: [Prompts concretos de UI/UX](https://x.com/AIExplorerTim/status/2121031543229677574). Texto reescrito por Alexandría.

### Planificar con un modelo potente y delegar la ejecución

En tareas largas, cuando quieres usar el modelo más caro solo para pensar y dejar la implementación a uno más económico.

```text
Vamos a repartir el trabajo de [tarea]. En esta sesión usa el modelo más capaz solo para entender el problema, decidir el enfoque y escribir la especificación.
La especificación incluye objetivo, archivos afectados, pasos, qué no se debe tocar y cómo comprobar el resultado con [comandos de verificación].
Después pasa cada parte a [subagente o agente más económico] con esa especificación. Puedes quedarte las partes más difíciles si explicas por qué.
Antes de delegar, dime qué supones sobre el proyecto y qué partes ves arriesgadas.
Revisa lo que vuelva contra la especificación; si algo no cumple, devuélvelo con la corrección concreta.
Ningún agente puede borrar datos, cambiar dependencias o publicar sin mi aprobación. Al final, resume qué hizo cada uno y el resultado de las comprobaciones.
```

**Resultado esperado:** Una especificación clara, trabajo delegado revisado contra ella y un resumen de quién hizo qué con las comprobaciones superadas.

Idea de partida: [Planificar caro y ejecutar barato](https://x.com/Voxyz_ai/status/2120260216046727370). Texto reescrito por Alexandría.

### Atacar tu plan antes de ejecutarlo (pre-mortem)

Antes de empezar un proyecto o una función grande, para encontrar los puntos débiles del plan.

```text
Haz de adversario de este plan: [plan]. Busco [objetivo] en [plazo].
Primero resúmelo con tus palabras y espera a que confirme que lo entendiste.
Después da por hecho que dentro de [seis meses] salió mal y razona hacia atrás. Revisa en especial: suposiciones sin comprobar, escenarios de fallo olvidados, atajos optimistas y alternativas más simples.
Para las tres causas más probables, indica la señal que la delataría, cuánto costaría y un experimento pequeño y barato para confirmarla o descartarla pronto.
Distingue lo que sabes de lo que supones. No modifiques archivos ni empieces a ejecutar nada.
Termina con un veredicto: seguir, correr antes un experimento concreto o replantear.
```

**Resultado esperado:** Tres riesgos concretos con su señal, coste y experimento, y un veredicto claro sobre el plan.

Idea de partida: [Red team del plan antes de empezar](https://x.com/Voxyz_ai/status/2120260216046727370). Texto reescrito por Alexandría.

### Auditar instrucciones obsoletas de tus agentes

Cuando tus archivos AGENTS.md, CLAUDE.md o reglas crecieron con el tiempo y ya no sabes si el código los respeta.

```text
Trabaja solo leyendo hasta que yo apruebe. Localiza todos los archivos de instrucciones para agentes en [repositorio] y en mi configuración de usuario: AGENTS.md, CLAUDE.md, reglas de editores y similares.
Contrasta cada regla con el código: se cumple (dos ejemplos), se contradice (archivo, línea y número de casos) o no se puede comprobar. Ignora detalles de estilo y céntrate en errores, datos, APIs, registros y pruebas.
Pide a un subagente nuevo, que no haya visto tu análisis, que reabra cada cita y descarte lo que no pueda confirmar.
Aparta las reglas críticas ([secretos, comandos destructivos, rutas protegidas, pruebas antes de terminar]) y propón cómo hacerlas obligatorias con permisos o hooks, mostrando cada cambio como diff.
Si mi archivo de usuario no aclara qué manda cuando instrucción y código chocan, propón una frase breve de prioridad.
Entrega una tabla (regla, qué encontraste, prueba, edición sugerida), indica qué supusiste y espera mi sí antes de editar.
```

**Resultado esperado:** Una tabla de reglas contrastadas con el código, diffs de permisos o hooks y una frase de prioridad lista para aprobar.

Idea de partida: [Instrucciones obsoletas y frase de precedencia](https://x.com/LimestoneHQ/status/2119808229236699466). Texto reescrito por Alexandría.

### Compartir la memoria del proyecto entre agentes

Cuando usas Claude Code y Codex en el mismo repositorio y cada uno olvida lo que aprendió el otro.

```text
Quiero que [Claude Code y Codex] compartan lo aprendido en [repositorio]. Localiza dónde guarda cada uno sus notas de memoria de este proyecto y muéstrame la lista sin moverla.
Antes de copiar nada al repositorio, busca tokens, claves, correos u otros datos personales y enséñamelos para dejarlos fuera.
Propón una carpeta común dentro del repo, por ejemplo [.agents/memory/], con un índice breve, y una línea para AGENTS.md (y CLAUDE.md si existe) que pida leer ese índice al empezar y anotar ahí lo nuevo.
Indica qué supones sobre cómo carga la memoria cada herramienta y cita la documentación cuando la uses.
No borres la memoria original hasta que yo confirme que la nueva funciona.
Para verificar, abre una sesión nueva en cada agente y comprueba que ambos citan una nota del índice. Sugiere además una revisión periódica que una duplicados y marque notas viejas.
```

**Resultado esperado:** Una carpeta de memoria común sin secretos, enlazada desde las instrucciones y comprobada en sesiones nuevas de ambos agentes.

Idea de partida: [Memoria compartida entre Claude Code y Codex](https://x.com/Voxyz_ai/status/2118448272742486490). Texto reescrito por Alexandría.

### Crear un repositorio central para skills y guías

Cuando tienes varios proyectos con skills, AGENTS.md y documentos repetidos y quieres una sola fuente.

```text
Ayúdame a montar un repositorio central que reúna mis skills, instrucciones y documentos compartidos y que apunte a mis demás proyectos.
Reunir datos es tarea tuya: inventaría los repositorios bajo [carpeta], saltando dependencias, con ruta, remoto, visibilidad y fecha del último commit. No abras .env ni archivos con secretos.
Clasifica cada skill, instrucción y documento para agentes en un grupo: compartido, duplicado (señala la copia más reciente), propio de un repo o instalado desde un catálogo.
Plantéame las decisiones en rondas de preguntas numeradas, con tu recomendación y de forma que me baste responder sí para aceptarla. Indica qué supones.
Hasta que apruebe la tabla de destinos, solo lees. Al aplicar, usa ramas nuevas, conserva enteras las carpetas de skills y no hagas push: eso lo decido yo.
Termina con un informe por fila: qué se movió, qué ramas creaste y qué dejaste sin hacer y por qué.
```

**Resultado esperado:** Un repositorio central con una sola copia de cada recurso compartido, enlaces a los demás proyectos y un informe de lo aplicado.

Idea de partida: [Patrón Home Repo](https://www.aihero.dev/the-home-repo-pattern). Texto reescrito por Alexandría.

### Averiguar por qué tu computadora va lenta

Cuando la computadora tarda en arrancar o se traba y no sabes qué la frena.

```text
Mi computadora con [sistema] va lenta sobre todo cuando [situación]. Quiero entender la causa antes de tocar nada.
Revisa qué consume más procesador, memoria y disco ahora, qué se abre al encender el equipo y qué ocupa más espacio. Explica cada cosa con palabras sencillas y señala lo que no reconozcas.
Dime qué supones cuando no puedas comprobar algo y separa lo seguro de lo probable.
No cierres programas, no desactives nada y no borres archivos. Dame una lista de cambios propuestos con su efecto esperado y cómo deshacerlos, y aplica únicamente los que yo apruebe.
Antes de cambios grandes, comprueba si hay una copia de seguridad reciente y avísame si falta.
Al final, repite la misma medición y muéstrame la diferencia.
```

**Resultado esperado:** Una explicación clara de qué frena el equipo, cambios aplicados solo con tu permiso y una medición antes y después.

Idea de partida: [Diagnóstico de una computadora lenta](https://x.com/0xKento_/status/2120596502540382661). Texto reescrito por Alexandría.

### Diagnosticar una conexión WiFi lenta o que se corta

Cuando internet va más lento de lo contratado o se desconecta y no sabes si es el equipo, el WiFi o el proveedor.

```text
Tengo contratados [velocidad] y la conexión [va lenta / se corta], sobre todo [cuándo]. Ayúdame a ubicar el problema: este equipo, la red WiFi o el proveedor.
Mide bajada, subida y latencia y compáralas con lo contratado. Revisa qué programas usan la red ahora, el historial de desconexiones de los últimos días y la calidad de la señal y del canal.
Explica cada resultado con palabras sencillas y dime qué supones cuando un dato no esté disponible.
Si hay que entrar al router, abre su página y la contraseña la escribo yo. No cambies ajustes de red, controladores ni el router sin mi permiso; propón cada cambio con la forma de revertirlo.
Entrega un resumen: dónde está la causa más probable, qué pruebas la respaldan y qué medición repetir para confirmar la mejora.
```

**Resultado esperado:** La causa más probable con pruebas medidas y una forma de comprobar si el cambio mejoró la conexión.

Idea de partida: [Diagnóstico del WiFi con un asistente](https://x.com/HeyAirahAi/status/2119046142189269333). Texto reescrito por Alexandría.

### Aprender un tema a fondo con un tutor exigente

Cuando quieres entender de verdad un tema y no solo leer un resumen.

```text
Quiero entender [tema] para [objetivo]. Hoy sé esto: [nivel actual]. Antes de explicar, dime qué supones sobre mi punto de partida y ajústalo con una o dos preguntas.
Construye la explicación desde las ideas básicas, con una analogía cotidiana por concepto y señalando dónde deja de servir cada analogía.
Incluye cómo evolucionó la idea, los errores típicos de principiante y tres preguntas que se haría alguien experto.
Cada pocos pasos, hazme una pregunta para comprobar si lo entendí y no sigas hasta que responda.
Marca qué es consenso, qué está en debate y qué no sabes con seguridad; sugiere dos o tres lecturas de referencia que yo pueda verificar. Si quieres crear archivos o tarjetas de estudio, pregúntame antes.
Al final, pídeme que explique el tema con mis palabras y señala qué me falta.
```

**Resultado esperado:** Una explicación por capas con preguntas de control y una comprobación final de lo que realmente entendiste.

Idea de partida: [Prompts para aprender en profundidad](https://www.instagram.com/p/DeSdMhBicI8/). Texto reescrito por Alexandría.

### Probar tu app con cinco usuarios simulados

Antes de lanzar una app, para descubrir dónde se confundirían o abandonarían tus primeras personas usuarias.

```text
Lanza [5] subagentes que usen [app] en un navegador real como si fueran mis primeros usuarios, con [cuentas de prueba] y en un entorno de prueba.
Perfiles: alguien con prisa que abandona al primer error, alguien desconfiado que lee privacidad y condiciones, alguien en un celular con conexión lenta, alguien que no domina el idioma de la interfaz y alguien que pega texto raro y hace doble clic en todo.
Cada uno intenta [tarea principal] y guarda una captura en cada momento de duda o bloqueo. Indica qué supones sobre cada perfil.
No deben enviar correos, hacer pagos reales, escribir a terceros ni borrar datos; si un paso lo exige, se detienen y lo anotan.
Reúne los hallazgos en una sola lista priorizada, sin duplicados, con perfil, paso, captura y arreglo sugerido. Espera mi aprobación antes de corregir.
Tras corregir, repite la prueba: termina cuando los cinco perfiles completen la tarea.
```

**Resultado esperado:** Una lista priorizada de fricciones con capturas y una segunda ronda en la que los cinco perfiles completan la tarea.

Idea de partida: [Simular a los primeros usuarios con subagentes](https://www.instagram.com/reel/DeuoJOdOdU7/). Texto reescrito por Alexandría.

### Rediseñar un panel con un sistema visual limitado

Cuando un panel o pantalla se ve desordenado y pedir "hazlo más moderno" no da resultados.

```text
Analiza esta captura de [pantalla]. Primero nombra los cinco problemas más graves de jerarquía y densidad de información y cómo afectan a quien la usa.
Define un sistema mínimo: una escala de espaciado, una escala tipográfica y como máximo cinco variables de color. Rehaz la pantalla usando solo eso, sin degradados.
No cambies [lo que no se puede tocar: datos, llamadas a la API, orden de campos]. Dime qué supones sobre la marca y el contenido.
Revisa los anchos [390, 768 y 1440 px]: zonas táctiles de al menos 44 px, sin desplazamiento horizontal y tablas que pasen a tarjetas en pantallas pequeñas.
Antes de reemplazar componentes que comparten otras pantallas, pregúntame.
Entrega capturas en cada ancho y una lista de lo que se rompió y cómo lo arreglaste.
```

**Resultado esperado:** Una pantalla rehecha con un sistema visual corto y capturas en cada ancho que lo demuestran.

Idea de partida: [Prompts concretos de UI/UX](https://x.com/AIExplorerTim/status/2121031543229677574). Texto reescrito por Alexandría.

### Mejorar un formulario para que más gente lo termine

Cuando la gente empieza tu formulario pero lo abandona o comete errores.

```text
Mejora [formulario] con un único objetivo: que más personas lo completen sin errores.
Propón una sola columna, etiquetas visibles encima de cada campo y validación al salir del campo, no con cada tecla. Cada error debe explicar cómo corregirlo.
Añade los estados de foco, deshabilitado, cargando y error, y comprueba que se pueda completar solo con teclado.
No cambies el orden de los campos, los nombres que recibe el servidor ni las llamadas a la API. Dime qué supones sobre quién lo rellena y desde qué dispositivo.
Muéstrame el plan y espera mi aprobación antes de editar; no envíes datos reales al probar.
Verifica con datos de prueba un envío correcto y tres con errores, y entrega capturas de cada estado.
```

**Resultado esperado:** Un formulario más claro con todos sus estados visibles y pruebas de envío correcto y con errores.

Idea de partida: [Formulario orientado a la tasa de finalización](https://x.com/AIExplorerTim/status/2121031543229677574). Texto reescrito por Alexandría.

### Dibujar un mapa sencillo de cómo funciona tu app

Cuando no entiendes bien cómo se conectan las pantallas, archivos y datos de un proyecto propio o heredado.

```text
Lee [proyecto] sin modificar nada y dibuja un mapa de su organización: pantallas, componentes, rutas del servidor, datos y servicios externos.
Pon a cada pieza un nombre descriptivo en lenguaje sencillo junto a su nombre técnico, y muestra qué se conecta con qué.
Elige [una pantalla clave] y sigue su recorrido desde el clic hasta la base de datos. Indica qué supones donde el código no sea claro.
Entrega el mapa como un único archivo HTML local que pueda abrir sin instalar nada. Pregúntame antes de instalar dependencias o crear archivos fuera de [carpeta de salida].
Para comprobarlo, usa el mapa para responder: ¿qué se rompería si cambio [tabla o archivo]? Cita los archivos que lo demuestran.
```

**Resultado esperado:** Un mapa HTML navegable del proyecto y una respuesta de impacto respaldada por archivos concretos.

Idea de partida: [Floorplan: mapa interactivo de una app](https://github.com/haydenschmitty/floorplan). Texto reescrito por Alexandría.

### Encontrar estados ocultos en tu aplicación

Cuando aparecen errores raros porque varias banderas o variables combinan estados que no deberían existir.

```text
Busca en [proyecto] las máquinas de estado implícitas: grupos de banderas, estados de carga, pasos de un asistente o estados de pedido que cambian sin un modelo explícito.
Para cada una, lista los estados posibles, las transiciones, las combinaciones imposibles que hoy el código permite y dónde vive cada pieza.
Prioriza por riesgo para quien usa la app, claridad para quien mantiene el código y facilidad para que un agente lo entienda. Dime qué supones donde el comportamiento no esté claro.
Propón un modelo explícito para las dos o tres más importantes, con un diagrama de estados, y espera mi aprobación antes de refactorizar.
No cambies comportamiento visible sin avisar. Añade pruebas que fallen con las combinaciones imposibles y pasen con el nuevo modelo, y ejecuta [comando de pruebas].
```

**Resultado esperado:** Un inventario de estados ocultos, diagramas de los principales y pruebas que demuestran que ya no se dan estados imposibles.

Idea de partida: [Máquinas de estado implícitas](https://x.com/Voxyz_ai/status/2119444845890617507). Texto reescrito por Alexandría.

### Crear un video demo con las pantallas reales

Cuando terminaste un proyecto y quieres un video corto para presentarlo sin editar a mano.

```text
Crea un video de presentación de [proyecto] de [duración] en formato [horizontal / vertical / cuadrado] con tono [tono].
Primero recorre la app y elige las tres o cuatro funciones que mejor explican su valor. Usa solo pantallas reales: ni capturas inventadas ni cifras que no existan.
Propón un guion por escenas con poco texto en pantalla y dime qué supones sobre el público. Espera a que apruebe el guion.
Usa datos de prueba; no muestres datos personales, claves ni correos reales. Pregúntame antes de instalar herramientas o usar música de licencia dudosa.
Renderiza primero fotogramas de muestra, revísalos en busca de textos cortados o elementos desbordados y solo después el video completo.
No lo des por terminado sin revisar el archivo final; entrega su ruta y la lista de escenas con su segundo de inicio.
```

**Resultado esperado:** Un video corto con pantallas reales, revisado antes de entregarse, y su guion por escenas.

Idea de partida: [Skill brag para videos demo](https://github.com/latent-spaces/brag). Texto reescrito por Alexandría.

### Montar un sistema de videos de producto con código

Cuando necesitas muchas variantes de video de producto con la misma calidad y quieres plantillas reutilizables.

```text
Quiero un sistema reutilizable que genere videos de producto con [herramienta, por ejemplo Remotion] a partir de una ficha de marca.
Mantén los datos de marca y los textos fuera del código de animación. Antes de renderizar, valida que los archivos existen, que los textos caben y que solo se usan afirmaciones de [lista aprobada].
Crea piezas para título, interfaz del producto, presentación de funciones, gráficos y llamada a la acción, con animaciones que dependan solo del número de fotograma.
Admite [9:16, 1:1 y 16:9] y varias versiones de gancho y cierre. Estilo sobrio: tipografía cuidada, pocos colores, sin brillos genéricos ni capturas falsas.
Empieza revisando el proyecto, propón la arquitectura y el formato de la ficha y espera mi visto bueno. Dime qué supones.
Construye primero la demo completa más pequeña, revisa fotogramas por desbordes y solo después renderiza en lote. Pregúntame antes de sobrescribir videos existentes.
Entrega los MP4 y un manifiesto con cada archivo, su formato y la variante usada.
```

**Resultado esperado:** Plantillas de video reutilizables, una demo revisada y un manifiesto con cada archivo entregado.

Idea de partida: [Sistema automatizado de motion design](https://x.com/e1genqq/status/2118440874883391727). Texto reescrito por Alexandría.

### Convertir un pedido creativo en un brief completo

Cuando quieres imágenes o videos de tu producto pero solo tienes una idea general como "fotos premium".

```text
Quiero [piezas: fotos, video corto, animación] de [producto] para [canal]. Antes de generar nada, hazme hasta seis preguntas, de una en una, para convertir esto en un brief.
Cubre público, sensación buscada, escenario, iluminación, encuadre, colores de marca y lo que hay que evitar.
Con mis respuestas, escribe un brief de una página y dime qué supusiste donde no respondí.
Propón tres variantes que cambien una sola cosa cada una (luz, fondo o encuadre) para poder compararlas.
El producto debe ser fiel al real: sin cambiar logotipo, etiqueta, forma ni colores, y sin afirmaciones que no te di. Pregúntame antes de usar caras de personas reales o marcas de terceros.
Entrega el brief y los prompts listos para [herramienta de imagen o video], con una lista para comprobar cada pieza contra el producto real.
```

**Resultado esperado:** Un brief claro, tres variantes comparables y una lista para comprobar que cada pieza respeta el producto.

Idea de partida: [Agente creativo con preguntas aclaratorias](https://www.instagram.com/reel/DfLoqUWOuvy/). Texto reescrito por Alexandría.

### Analizar videos que funcionan sin copiarlos

Cuando quieres entender por qué ciertos videos de tu nicho funcionan antes de planear los tuyos.

```text
Analiza estos videos de [nicho]: [enlaces o transcripciones]. Para cada uno describe el gancho de los primeros segundos, tema, formato, duración, llamada a la acción y métricas visibles.
Si te paso comentarios, resume qué valora o critica la audiencia, sin citar nombres de usuarios.
Busca patrones que se repiten y separa lo que muestran los datos de lo que supones.
Con esos patrones, propón [5] ideas para [mi marca] que aprovechen la estructura con tema, ejemplos y guion originales. No copies frases, imágenes ni música de los videos analizados.
Pregúntame antes de publicar, programar o descargar contenido.
Entrega una tabla de análisis y, para cada idea, qué patrón usa y qué métrica revisaré para saber si funcionó.
```

**Resultado esperado:** Una tabla de patrones de videos exitosos y varias ideas originales con la métrica para evaluarlas.

Idea de partida: [Matriz para analizar videos virales](https://www.instagram.com/reel/Deo5tVWxA3X/). Texto reescrito por Alexandría.

### Convertir la foto de un producto en piezas de anuncio

Cuando cuentas con una imagen auténtica de lo que vendes y quieres varias versiones para redes sin diseñar desde cero.

```text
Tengo esta foto de [producto] y quiero piezas para [red social] en formato [proporción]. Mi mensaje es [oferta o mensaje].
Arma un pequeño menú de estilos con nombre corto que pueda reutilizar: póster minimalista, oferta destacada, escena de uso cotidiano, primer plano de detalle y foto natural estilo cliente.
Para cada estilo escribe un prompt para [herramienta de imagen] que describa fondo, luz, encuadre y espacio para el texto.
El producto debe quedar idéntico: misma forma, etiqueta, logotipo y colores. Dime qué supones sobre la marca y no inventes precios, descuentos ni beneficios.
Pregúntame antes de incluir personas, marcas ajenas o textos legales.
Entrega los prompts y una lista para comparar cada imagen generada con la foto original antes de publicarla.
```

**Resultado esperado:** Un menú de estilos reutilizables con sus prompts y una lista de control para validar cada imagen.

Idea de partida: [Comandos para diseños de producto](https://www.instagram.com/reel/De45-O4Nelr/). Texto reescrito por Alexandría.

### Convertir un plano 2D en un recorrido 3D en el navegador

Cuando tienes el plano de una vivienda o local y quieres un recorrido navegable fiel a sus medidas.

```text
Convierte el plano [archivo] en un recorrido 3D que se abra en el navegador y funcione en móvil.
Pasa primero el plano a datos (muros, aberturas y estancias), dibújalos sobre la imagen original y calcula cuánto coinciden antes de empezar el 3D. Dime qué supones donde el plano no se lea bien.
Construye solo [estancias prioritarias] y deja cerradas las demás. Genera geometría y materiales por código, sin modelos descargados de origen dudoso.
Separa construir de juzgar: tras cada estancia, envía renders y referencias a un subagente revisor recién creado, que conteste sí o no y nombre hasta cinco fallos por gravedad, cada uno con un ajuste medible.
En decisiones de gusto, enséñale dos opciones marcadas A y B para que escoja. Repite hasta obtener un sí.
Pregúntame antes de publicar el recorrido o usar fotos de terceros. Entrega el enlace local, una captura por estancia y el registro del revisor con lo que una persona aún debería comprobar.
```

**Resultado esperado:** Un recorrido 3D fiel al plano, revisado por un crítico independiente, con capturas y notas de revisión.

Idea de partida: [Planos 2D a recorridos 3D](https://x.com/VisualconAI/status/2121591290790052030). Texto reescrito por Alexandría.

### Estudiar decisiones de mercado sin arriesgar dinero

Cuando quieres entender cómo razona un sistema de análisis de mercados con agentes, solo con fines educativos.

```text
Esto es solo para aprender, no para invertir. No conectes cuentas de bróker ni ejecutes órdenes, y no me des recomendaciones personales de inversión.
Configura [herramienta, por ejemplo TradingAgents] en modo de investigación para [activos] y explícame qué papel cumple cada agente y cómo debaten.
Haz una prueba histórica de [periodo] con una decisión por semana y compara cada una con un índice de referencia, teniendo en cuenta costes y el riesgo de sobreajuste.
Dime qué supones en cada paso y qué datos no pudiste verificar. Pregúntame antes de instalar dependencias, programar tareas o configurar accesos a proveedores.
Después, hazme preguntas de tutor sobre por qué el sistema tomó cada decisión y corrige mis respuestas.
Entrega una tabla con decisión, razonamiento resumido y resultado frente al índice, más una advertencia clara de que el rendimiento pasado no predice el futuro.
```

**Resultado esperado:** Una prueba histórica explicada y comparada con un índice, y un cuestionario que muestra si entendiste el razonamiento.

Idea de partida: [TradingAgents: análisis de mercado con varios agentes](https://github.com/TauricResearch/TradingAgents). Texto reescrito por Alexandría.

### Evaluar una idea de negocio con mirada escéptica

Antes de invertir tiempo o dinero en una idea, para conocer sus riesgos y probarla barato.

```text
Evalúa esta idea de negocio con honestidad: [idea]. Dispongo de [tiempo] y [presupuesto] y sé hacer [habilidades].
No prometas ingresos ni uses cifras sin fuente. Cuando estimes algo, da un rango, explica de dónde sale y márcalo como supuesto.
Dime cuánto trabajo exigirá al principio, quién pagaría y por qué, qué usa hoy esa persona en su lugar y los cinco riesgos principales, incluidos los legales y fiscales que debo consultar con un profesional. Señala qué estoy subestimando.
Propón un experimento de [14] días con gasto mínimo para comprobar si alguien pagaría, con la métrica y el umbral que decidirán seguir o parar.
No crees cuentas, páginas ni anuncios por mí; si el experimento lo requiere, pregúntame antes.
Cierra con una recomendación: probar, ajustar la idea o descartarla, y por qué.
```

**Resultado esperado:** Una evaluación sin promesas de ingresos, con riesgos claros y un experimento corto con criterio de decisión.

### Incorporar fuentes nuevas a tu segundo cerebro

Cuando guardas artículos y notas en una carpeta o bóveda y quieres que se conecten con lo que ya sabes.

```text
Quiero que mis notas crezcan conectadas. La fuente nueva es [archivo], en [carpeta de entrada] de mi bóveda.
Antes de escribir, dime qué temas de mi bóveda crees que toca y qué supones sobre su fiabilidad (autoría, fecha, tipo de fuente).
Propón qué notas crear y cuáles ampliar, con los enlaces a notas existentes que añadirías. Si la fuente choca con algo que ya tengo, muéstrame ambas versiones lado a lado.
No borres ni reescribas notas mías sin preguntarme; las ampliaciones van marcadas con fecha y fuente.
Cuando apruebe, aplica los cambios y entrega la lista de archivos tocados, con un enlace a la fuente en cada nota.
Para verificar, elige una nota antigua y demuestra que ahora lleva a la información nueva en dos clics o menos.
```

**Resultado esperado:** Notas nuevas o ampliadas, enlazadas con las existentes, con contradicciones señaladas y una lista de archivos para revisar.

Idea de partida: [Segundo cerebro compilado con un agente](https://x.com/rvaniaaaa/status/2119056971298980112). Texto reescrito por Alexandría.

### Preparar una presentación breve de tu idea

Cuando tienes que explicar un proyecto o negocio en pocos minutos ante clientes, socios o un jurado.

```text
Ayúdame a presentar [idea] ante [público] en [minutos]. Antes de diseñar, dime qué supones que ese público necesita oír para decir que sí.
Propón un esquema de ocho a doce diapositivas que cubra el problema, la solución, para quién es, cómo se sostiene económicamente, avances, equipo, lo que pido y un cierre.
Cada diapositiva lleva una sola idea, como mucho 25 palabras y una nota con lo que diré en voz alta.
Usa solo estos datos: [datos]. Si falta uno, deja un hueco marcado en lugar de inventarlo. No pongas mis datos de contacto salvo que te los indique.
Muéstrame el esquema y espera mi aprobación antes de crear el archivo.
Entrega el archivo y una lista de comprobación: una idea por diapositiva, cada cifra con su fuente y la pregunta que quiero provocar al final.
```

**Resultado esperado:** Un esquema aprobado y una presentación breve sin datos inventados, con notas para quien presenta.

Idea de partida: [Prompts prácticos con herramientas de un asistente](https://x.com/free_ai_guides/status/2118991880914645303). Texto reescrito por Alexandría.

### Investigar a fondo antes de tomar una decisión

Cuando debes elegir entre proveedores, herramientas, mercados o competidores y quieres un informe con fuentes.

```text
Tengo que decidir [decisión]. Mis criterios son [criterios] y ya conozco estas opciones: [opciones].
Primero dime qué información necesitarías para decidir bien y qué supones sobre mi situación.
Busca fuentes públicas y recientes; cada afirmación lleva enlace y fecha. Si dos fuentes discrepan, muéstralas juntas.
Compara las opciones en una tabla con mis criterios y marca cada celda como comprobada o estimada. Describe los riesgos de cada opción y lo que no pudiste averiguar.
No contactes a empresas, no te registres en servicios ni compartas mis datos; si algo lo requiere, pregúntame.
Cierra con una recomendación de una línea y el dato concreto que la haría cambiar.
```

**Resultado esperado:** Un informe con afirmaciones enlazadas, una tabla con datos marcados y una recomendación que dice qué la cambiaría.

Idea de partida: [Prompts prácticos con herramientas de un asistente](https://x.com/free_ai_guides/status/2118991880914645303). Texto reescrito por Alexandría.

### Decidir qué partes de un proceso automatizar

Antes de conectar un agente a un proceso que hoy hace una persona.

```text
Mi proceso es [pasos]. Cada paso ocurre [frecuencia], tarda [tiempo] y usa [datos]. Indica qué dejar manual, qué convertir en plantilla, qué preparar como borrador con IA y qué automatizar con reglas. Para cada paso explica el ahorro estimado, qué pasaría si falla y quién puede corregirlo. Conserva aprobación para cambios de dinero, permisos, envíos o borrados. Propón una prueba con datos inventados y un criterio de parada. Haz el análisis por escrito sin conectar sistemas ni ejecutar acciones.
```

**Resultado esperado:** Una tabla por paso y un piloto pequeño con resultado esperado, encargado de revisión y condición de parada.

Idea de partida: [Cuándo conviene usar un agente](https://www.anthropic.com/research/building-effective-agents). Texto reescrito por Alexandría.

### Medir si tu agente reutiliza la caché del contexto

Cuando el agente tarda al abrir respuestas pese a repetir instrucciones y contexto.

```text
Uso [motor, versión y modelo]. Mis dos solicitudes sintéticas son [ejemplos]. Separa las instrucciones estables del texto que cambia por petición. Diseña una comparación en frío y otra con el prefijo repetido, manteniendo iguales el modelo, las herramientas y el tamaño esperado de salida. Indica qué métricas de aciertos de caché y tiempo hasta el primer token expone este motor. Si no hay métricas, infórmalo y separa las hipótesis de los hechos. Propón una forma de conservar permisos, separación entre usuarios y trazabilidad. No ejecutes ni envíes datos del proyecto.
```

**Resultado esperado:** Protocolo de comparación con campos de registro y un criterio para decidir si el cambio produjo una mejora.

Idea de partida: [Caché automática de prefijos de vLLM](https://docs.vllm.ai/en/latest/features/automatic_prefix_caching/). Texto reescrito por Alexandría.

### Medir si tu agente elige la herramienta correcta

Cuando un agente mezcla herramientas parecidas o consume mucho contexto al cargar su catálogo.

```text
Mi agente ofrece [herramientas y permisos]. Con [tareas ficticias], prepara una tabla con la herramienta esperada, las que se le parecen y el permiso mínimo. Diseña una comparación entre mostrar todas y seleccionar un conjunto reducido por tarea. Define cómo contar aciertos, omisiones y pasos extra. Elige una prueba sin acceso real a cuentas. No ejecutes herramientas ni uses datos privados.
```

**Resultado esperado:** Una matriz de casos y un criterio para elegir el catálogo con menos errores y menos pasos.

Idea de partida: [Tool Retrieval de Gemini](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-tool-retrieval/). Texto reescrito por Alexandría.
