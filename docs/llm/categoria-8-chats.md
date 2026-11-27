# Alexandría para agentes · Interfaces de chat auto-hospedadas

Categoría 8 «Chats, modelos locales y espacios privados» › subcategoría `chats`. 9 repos. Generado el 2026-11-27 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=8&sub=chats · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `open-webui` | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI… | 1 Básico | 74 | Open WebUI License (BSD-3-Clause + cláusula de marca) (source-available) | recomendado |
| `cherry-studio` | App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de… | 1 Básico | 72 | AGPL-3.0 (OSI copyleft) | alternativa |
| `lobehub` | Espacio de trabajo con super-agentes y una interfaz de chat moderna… | 2 Intermedio | 70 | LobeHub Community License (Apache-2.0 + condiciones) (source-available) | alternativa |
| `librechat` | Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola… | 2 Intermedio | 69 | MIT (OSI permisiva) | alternativa |
| `jan` | Aplicación de escritorio para conversar con modelos locales y configurar… | 1 Básico | 66 | Apache-2.0 (OSI permisiva) | alternativa |
| `nextchat` | Cliente de chat de IA ligero y multiplataforma (web, escritorio y móvil) para… | 2 Intermedio | 64 | MIT (OSI permisiva) | alternativa |
| `chatbox` | Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos… | 1 Básico | 52 | GPL-3.0 (OSI copyleft) | alternativa |
| `sillytavern` | Interfaz local avanzada para chatear con LLM: une muchas APIs, personajes, rol… | 2 Intermedio | 52 | AGPL-3.0 (OSI copyleft) | sin grupo |
| `textgen` | App open source para LLM locales con texto, visión, herramientas y API… | 2 Intermedio | 51 | AGPL-3.0 (OSI copyleft) | alternativa |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Open WebUI (`open-webui`)

- **Repo:** https://github.com/open-webui/open-webui · Open WebUI License (BSD-3-Clause + cláusula de marca) · nivel 1 · 74/100 · recomendado en «Interfaces de chat con LLM»
- **Qué es:** Open WebUI, plataforma de chat con IA autoalojada y extensible, diseñada para poder funcionar sin conexión, de Open WebUI Inc. (creada por Timothy Jaeryang Baek).
- **Cuándo elegirlo:** Casos: Unificar chats de modelos locales; Crear una interfaz compartida para un equipo.
- **Requisitos:** nivel 1: preparación sencilla; Docker; Ollama accesible o proveedor remoto; volumen persistente; hardware prerequisites; API de IA: opcional; Docker; Ollama accesible o proveedor remoto; volumen persistente.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/open-webui/open-webui/blob/main/README.md

  ```bash
  docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
  ```
- **Primera prueba propuesta (no ejecutada):** Conecta un modelo y conversa sobre un texto ficticio antes de cargar documentos privados Éxito: Puedes ver el modelo seleccionado y conservar una conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `searxng` [4/busqueda]
- **Alternativas:** `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `chatbox`, `textgen`, `anything-llm`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): librechat, lobehub, anything-llm, textgen. La cláusula de marca limita el rebranding: revisa LICENSE antes de redistribuirlo con otra…. Instalar la interfaz no instala todos los modelos; confirma que Docker puede alcanzar el servidor de inferencia.

### Cherry Studio (`cherry-studio`)

- **Repo:** https://github.com/CherryHQ/cherry-studio · AGPL-3.0 · nivel 1 · 72/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Estación de trabajo de IA de escritorio para Windows, macOS y Linux, de CherryHQ, con app móvil aparte. La edición comunitaria es AGPL-3.0 (el uso comercial se permite cumpliendo la AGPL; hay licencia comercial y una edición Enterprise)…
- **Cuándo elegirlo:** Casos: Comparar respuestas de varios modelos; Organizar una base documental de prueba.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio; hardware prerequisites; API de IA: opcional; Instalador para Windows, macOS o Linux; proveedor o Ollama/LM Studio.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://cherryai.com/docs/en/getting-started/quick-start/
- **Primera prueba propuesta (no ejecutada):** Configura un modelo y prueba una pregunta sobre una nota ficticia en un espacio de trabajo Éxito: Puedes comprobar el proveedor y la respuesta usada en la conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `lobehub`, `librechat`, `jan`, `nextchat`, `chatbox`, `textgen`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): jan, lobehub. Los agentes pueden ejecutar comandos: revisa sus permisos. Es una app multiproveedor; escoger Anthropic u OpenAI no la convierte en sesión de Claude Code o Codex.

### LobeHub (`lobehub`)

- **Repo:** https://github.com/lobehub/lobehub · LobeHub Community License (Apache-2.0 + condiciones) · nivel 2 · 70/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Plataforma de agentes de código abierto de LobeHub, antes conocida como Lobe Chat, que se presenta como «superagentes en tu equipo». Su README indica Apache 2.0, aunque GitHub no reconoce la licencia como estándar [DATO NO VERIFICADO…
- **Cuándo elegirlo:** Casos: Organizar agentes para tareas de equipo; Conectar un agente de código a un espacio de trabajo.
- **Requisitos:** nivel 2: preparación sencilla, varios servicios con Docker Compose; Docker y Compose; modelo; servicios de la ruta elegida; hardware prerequisites; API de IA: depends; Docker y Compose; modelo; servicios de la ruta elegida.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/lobehub/lobehub/blob/canary/README.md

  ```bash
  mkdir lobehub && cd lobehub
  bash <(curl -fsSL https://lobe.li/setup.sh) -l en
  docker compose up -d
  ```
- **Primera prueba propuesta (no ejecutada):** Crea un asistente de prueba y distingue su modelo del agente externo que puedas conectar Éxito: Puedes identificar qué proveedor atiende cada conversación
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `cherry-studio`, `librechat`, `jan`, `nextchat`, `chatbox`, `textgen`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): open-webui, librechat, cherry-studio. SearXNG ya viene en su Compose; no instales otro aparte. Las skills portables y conectar un agente externo son funciones distintas; la página de integración consultada aún está en migración documental.

### LibreChat (`librechat`)

- **Repo:** https://github.com/LibreChat-AI/LibreChat · MIT · nivel 2 · 69/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Plataforma de chat con IA de código abierto (MIT) y autoalojable, del equipo LibreChat-AI, con agentes, MCP y autenticación multiusuario empresarial. Muy activa (v0.8.8 descrita en el README; sin releases formales en GitHub).
- **Cuándo elegirlo:** Casos: Unificar proveedores en una interfaz; Crear asistentes con herramientas y archivos.
- **Requisitos:** nivel 2: preparación media; Ruta de despliegue elegida; base de datos; proveedor u Ollama; hardware prerequisites; API de IA: opcional; Ruta de despliegue elegida; base de datos; proveedor u Ollama.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://www.librechat.ai/docs
- **Primera prueba propuesta (no ejecutada):** Conecta un proveedor y prueba un agente sin herramientas antes de añadir archivos Éxito: Puedes identificar el modelo y revisar la conversación
- **Combina con:** `litellm` [23/serving], `ollama` [8/motores], `langfuse` [23/observabilidad], `llama-cpp` [8/motores], `pgvector` [6/vectores], `exo` [8/motores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `jan`, `nextchat`, `chatbox`, `textgen`
- **Riesgos y avisos:** Alternativas (elige una): open-webui, lobehub. Meilisearch, pgvector y RAG API ya vienen en su Compose. Sus agentes y MCP funcionan dentro de LibreChat; no acreditan usar una suscripción de otro editor para ejecutarlo.

### Jan (`jan`)

- **Repo:** https://github.com/janhq/jan · Apache-2.0 · nivel 1 · 66/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Aplicación de escritorio de código abierto presentada como reemplazo de ChatGPT, de Menlo Research (janhq). Licencia Apache 2.0 según su README (GitHub no la detecta como estándar); activa, con versiones frecuentes (v0.8.8).
- **Cuándo elegirlo:** Casos: Conversar con un modelo privado; Comparar un modelo local con una API.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador de escritorio oficial; RAM y disco; modelo compatible; hardware prerequisites; API de IA: opcional; Instalador de escritorio oficial; RAM y disco; modelo compatible.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/janhq/jan` — fuente: https://github.com/janhq/jan/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Desde la app descarga un modelo pequeño y prueba una conversación local Éxito: Ves el modelo cargado y puedes repetir la consulta sin proveedor remoto
- **Combina con:** `llmfit` [8/motores], `ollama` [8/motores], `playwright-mcp` [5/servidores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `nextchat`, `chatbox`, `textgen`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Alternativas (elige una): cherry-studio, textgen, chatbox. Para comenzar usa la distribución de escritorio; make dev y yarn son rutas para desarrollar el código de Jan.

### NextChat (`nextchat`)

- **Repo:** https://github.com/ChatGPTNextWeb/NextChat · MIT · nivel 2 · 64/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Cliente de chat de código abierto (MIT), antes ChatGPT-Next-Web, muy popular. Su organización ofrece además un servicio SaaS de pago por uso; el repositorio sigue siendo el cliente autoalojable.
- **Cuándo elegirlo:** Casos: desplegar un chat privado con tu propia clave para un equipo pequeño; usar un modelo autoalojado compatible con OpenAI desde una interfaz web ligera.
- **Requisitos:** nivel 2: preparación sencilla, requiere clave de API; TypeScript, Dockerfile, docker-compose.yml, package.json; API de IA: sí.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ChatGPTNextWeb/NextChat/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Despliega NextChat con Docker o Vercel usando tu clave de API y abre un chat. Éxito: El chat responde con el modelo configurado y el historial queda en el navegador.
- **Combina con:** `localai` [8/motores], `litellm` [23/serving], `fastmcp` [5/sdk]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `chatbox`, `textgen`
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Alternativas (elige una): lobehub, chatbox. Protege el despliegue con la variable CODE si es público.

### chatbox (`chatbox`)

- **Repo:** https://github.com/chatboxai/chatbox · GPL-3.0 · nivel 1 · 52/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Cliente de escritorio para ChatGPT, Claude y otros LLM, en su edición comunitaria de código abierto (GPLv3) de chatboxai; el código se sincroniza con la versión Pro. Activo (v1.24.4).
- **Cuándo elegirlo:** Casos: Conversar con varios proveedores; Probar un modelo local desde escritorio.
- **Requisitos:** nivel 1: preparación sencilla, app o instalador listo para usar; Instalador Community para tu sistema; proveedor o instancia Ollama; hardware prerequisites; API de IA: opcional; Instalador Community para tu sistema; proveedor o instancia Ollama.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/chatboxai/chatbox.git` — fuente: https://github.com/chatboxai/chatbox/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Conecta un proveedor y guarda una conversación con una nota ficticia Éxito: Puedes identificar el modelo y recuperar el chat
- **Combina con:** `ollama` [8/motores], `litellm` [23/serving], `localai` [8/motores]
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `textgen`
- **Riesgos y avisos:** Alternativa (elige una): jan. No confundas la edición comunitaria con los servicios comerciales ni un proveedor Claude con Claude Code.

### SillyTavern (`sillytavern`)

- **Repo:** https://github.com/SillyTavern/SillyTavern · AGPL-3.0 · nivel 2 · 52/100
- **Qué es:** Interfaz de usuario local de código abierto (AGPL-3.0), nacida en 2023 como fork de TavernAI 1.2.8 y mantenida por una comunidad de más de 300 contribuyentes. No ofrece servicios alojados ni rastrea datos de usuario según el proyecto.
- **Cuándo elegirlo:** Casos: escribir historias o partidas de rol con personajes y memoria persistente; probar el mismo prompt contra varios modelos locales y remotos.
- **Requisitos:** nivel 2: preparación media; JavaScript, Dockerfile, package.json; hardware model_dependent; API de IA: opcional.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/SillyTavern/SillyTavern -b release` — fuente: https://docs.sillytavern.app/installation/windows/
- **Primera prueba propuesta (no ejecutada):** Instala SillyTavern con Node.js 20+, conéctalo a un backend local como KoboldCpp u Ollama y abre un chat. Éxito: El chat responde con el modelo conectado y la conversación se guarda en tu equipo.
- **Combina con:** `koboldcpp` [8/motores], `ollama` [8/motores], `comfyui` [11/interfaces], `kokoro` [29/tts], `textgen`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. La curva de aprendizaje es alta por diseño; las tarjetas de personaje de terceros pueden contener prompts no deseados.

### Text Generation WebUI (`textgen`)

- **Repo:** https://github.com/oobabooga/textgen · AGPL-3.0 · nivel 2 · 51/100 · alternativa en «Interfaces de chat con LLM»
- **Qué es:** Aplicación de escritorio para LLM locales, de código abierto (AGPL-3.0) y sin telemetría, de oobabooga (antes text-generation-webui). Madura y con versiones regulares (v4.9).
- **Cuándo elegirlo:** Casos: Probar modelos GGUF sin una API remota; Servir un endpoint local para otra app.
- **Requisitos:** nivel 2: instaladores de un clic por sistema; Distribución portable apropiada a tu GPU o CPU; modelo GGUF; hardware prerequisites; API de IA: no; Distribución portable apropiada a tu GPU o CPU; modelo GGUF.
- **Instalación (documentada en la fuente; no ejecutada):** `docker compose up --build` — fuente: https://github.com/oobabooga/textgen/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Carga un modelo pequeño en la app y revisa texto generado y consumo de memoria Éxito: Puedes identificar backend, modelo y memoria utilizada
- **Combina con:** `librechat`, `llmfit` [8/motores], `unsloth` [24/entrenamiento], `sillytavern`
- **Alternativas:** `open-webui`, `cherry-studio`, `lobehub`, `librechat`, `jan`, `nextchat`, `chatbox`
- **Riesgos y avisos:** AGPL: si lo modificas y lo expones en red, debes publicar tus cambios. Alternativas (elige una): jan, open-webui. Antes conocida por rutas text-generation-webui; usa la distribución que corresponda a tu hardware y distingue API de inferencia de token de autenticación.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-8-chats.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Interfaces de chat auto-hospedadas», lee `docs/alexandria/categoria-8-chats.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-8-chats.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
