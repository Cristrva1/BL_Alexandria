# REPO_MENU — Menú portable de la biblioteca de repositorios

[Explorar por áreas prácticas y configuración de asistentes](REPO_AREAS.md).

> Generado: 2026-11-16 · 642 repos curados · Documento 100% para IA.
> COPIA esta carpeta (`menu_portable/`) a la raíz de tu proyecto y
> referencia este archivo desde tu AGENTS.md / system prompt.

---

## INSTRUCCIONES PARA EL AGENTE (léeme entero, soy corto)

Eres un agente que debe elegir qué repositorios instalar/usar para un
proyecto concreto. Tienes un menú curado de **642 repos** de IA y
automatización. Objeto: gastar MÍNIMOS tokens y NO visitar la web.

PROTOCOLO (en orden):

0. **Si el usuario ya describió un proyecto concreto**, parte de las
   `recipes` que coincidan con el producto; no empieces por repos sueltos.
1. **No leas todo.** Este archivo basta para preseleccionar.
2. **Filtra** candidatos por `cat`, `tags`, `role`, `exec`, `setup`, `prov`
   y palabras de `one` (resumen de una línea).
3. **Desempata** con `alt`: si ya elegiste un repo, **descarta sus `alt`**
   (cumplen la misma función, no necesitas dos).
4. **Combina** con `recipes` si el proyecto es un flujo end-to-end.
5. **Considera la herramienta** del usuario (Claude Code, Antigravity,
   Codex, Grok, Deepseek) con la tabla de abajo y el campo opcional
   `agent_tools`. Solo importa para repos `role=skill/directory`.
6. **Solo para finalistas (<8):** abre `REPO_MENU_cats/NN-*.md` para
   desc, `choose_if`, `avoid_if`, `combines_with` y el comando de
   entrada documentada y la primera prueba propuesta.
7. **Instalación:** comando marcado `+` documentado en la fuente · `~` por revisar ·
   `?` solo clone + README.

REGLA CLAVE — herramienta de código ≠ modelo en ejecución:
- El AGENTE/IDE con que CONSTRUYES (Claude Code, Antigravity, Codex…)
  solo importa para repos `role=skill/directory` (catálogos de skills).
- El LLM que tu APP llama EN EJECUCIÓN es el campo `prov`; se configura
  por env vars. La mayoría de repos runtime son AGNÓSTICOS al agente.

LEYENDA de columnas del índice:
`role`: P=plataforma R=runtime L=librería S=skill D=catálogo A=app
`exec`: loc=local cld=cloud hyb=híbrido · `setup`: E=easy M=medium H=heavy
`inst`: +=documentado ~=revisar ?=consultar fuente
`tags` / `prov` / `tools` (`agent_tools`): solo si el repo los declara
`alt`: repos sustitutos (elige uno)

---

## Repos específicos por herramienta de código

| Herramienta | Repos que le sirven |
|---|---|
| Claude Code | `claude-code`, `anthropic-skills`, `claude-plugins-official`, `superpowers`, `awesome-claude-code`, `awesome-claude-skills`, `claude-mem`, `geo-seo-claude`, `agency-agents` |
| Codex | `codex`, `agent-skills`, `antigravity-awesome-skills`, `awesome-agent-skills`, `spec-kit`, `marketingskills`, `taste-skill` |
| Antigravity | `antigravity-awesome-skills`, `awesome-agent-skills`, `prompt-master`, `stitch-skills` |
| gemini-cli | `gemini-cli`, `awesome-agent-skills`, `antigravity-awesome-skills`, `stitch-skills` |
| opencode | `opencode`, `awesome-agent-skills`, `antigravity-awesome-skills`, `prompt-master` |
| Grok | Sin repos específicos: úsalo como proveedor LLM en runtime (los repos agnósticos lo aceptan vía API compatible con OpenAI). |
| Deepseek | `deepseek-v3` |

## Recetas: flujos propuestos

Si el proyecto es un PRODUCTO (no una pieza suelta), parte de una
receta y ajusta. Empieza por su propuesta inicial; el recorrido completo incluye ampliaciones y otras rutas.

### Bot de WhatsApp con IA
**Meta:** Atender y vender por WhatsApp con un agente LLM que guarda leads y pasa la conversación a una persona cuando hace falta.
**Recursos del recorrido completo:** `evolution-api`, `dify`, `chatwoot`, `novu`
**Empieza con:** `evolution-api`, `dify`, `chatwoot`
**Prepara:** Un mensaje enviado desde un número de prueba
**Primera prueba propuesta:** Recibe el mensaje, envíalo al flujo y pide pasar con una persona
**Qué comprobar:** El mensaje llega a la bandeja y puedes responder manualmente
Decide primero la conexión del canal, sus políticas y posibles tarifas; Dify y Evolution se conectan por su integración nativa, sin flujos intermedios
**Cómo:** Evolution API mantiene la sesión de WhatsApp y, mediante su integración nativa con Dify, pasa cada mensaje a una app de Dify (agente o chatflow) que arma el contexto, llama al LLM y guarda el lead. La integración nativa de Evolution con Chatwoot lleva las conversaciones a la bandeja para que responda una persona cuando hace falta. Novu avisa al equipo cuando Dify detecta un lead (por ejemplo, con una herramienta HTTP).

### Pipeline de Reels / video corto
**Meta:** Convertir un guion o un video largo en clips verticales con voz, subtítulos y visuales generados.
**Recursos del recorrido completo:** `whisperx`, `kokoro`, `comfyui`, `real-esrgan`, `remotion`, `ffmpeg`, `moneyprinterturbo`
**Empieza con:** `kokoro`, `remotion`, `ffmpeg`
**Prepara:** Un guion de 20 segundos y dos imágenes propias
**Primera prueba propuesta:** Sintetiza la voz, monta una escena sencilla y exporta un clip
**Qué comprobar:** El archivo reproduce imagen y voz con la duración esperada
WhisperX hace falta si partes de audio; generar imágenes y restaurarlas son ampliaciones, no requisitos de todo video
**Cómo:** Flujo propuesto: WhisperX prepara subtítulos; Kokoro sintetiza narración; ComfyUI genera visuales; Remotion compone y FFmpeg exporta. Comprueba los datos,la duración y la licencia de cada recurso. MoneyPrinterTurbo es otra aplicación con su configuración y costes propios.

### Agente de research profundo
**Meta:** Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
**Recursos del recorrido completo:** `gpt-researcher`, `searxng`, `crawl4ai`, `browser-use`, `markitdown`, `langfuse`
**Empieza con:** `gpt-researcher`, `searxng`
**Prepara:** Una pregunta acotada que puedas contrastar
**Primera prueba propuesta:** Genera un informe breve y abre tres de sus fuentes
**Qué comprobar:** Las fuentes existen y respaldan las afirmaciones del informe
Comprueba el proveedor de modelo y búsqueda; una cita no garantiza que la conclusión sea correcta
**Cómo:** GPT Researcher divide la pregunta en sub-preguntas, busca con SearXNG y pasa las URLs a Crawl4AI, que devuelve Markdown listo para el modelo. Browser Use cubre las páginas que necesitan clics o sesión, y MarkItDown suma tus documentos. Langfuse registra cada llamada para revisar costos y errores. DeerFlow es la alternativa si prefieres un harness con sandbox y más autonomía.

### Workspace privado local soberano
**Meta:** Preparar chat, documentos y memoria con rutas locales, comprobando por separado modelos, herramientas y conexiones externas.
**Recursos del recorrido completo:** `ollama`, `odysseus`, `open-notebook`, `mem0`, `searxng`
**Empieza con:** `ollama`, `odysseus`
**Prepara:** Un modelo que quepa en tu equipo y un archivo de prueba
**Primera prueba propuesta:** Conecta el motor local al espacio de trabajo y prueba una conversación
**Qué comprobar:** Identificas el endpoint del modelo y puedes revisar qué conexiones externas siguen activas
Configura y comprueba también embeddings, herramientas, memoria y búsqueda; local no garantiza ausencia de comunicaciones externas
**Cómo:** Ollama sirve modelos en tu equipo. Conecta una interfaz compatible y prueba primero el chat. Después evalúa documentos, memoria y búsqueda; cada componente requiere su propia configuración y puede abrir conexiones externas.

### Análisis de repos grandes
**Meta:** Que un agente de código entienda una base de código enorme sin gastar todo su contexto.
**Recursos del recorrido completo:** `repomix`, `codegraph`, `gitnexus`, `graphify`, `claude-code`
**Empieza con:** `repomix`, `claude-code`
**Prepara:** Un repo propio y una pregunta concreta sobre su código
**Primera prueba propuesta:** Empaqueta solo una parte y pide ubicar una función con referencias
**Qué comprobar:** Puedes abrir los archivos citados y comprobar la explicación
Revisa exclusiones y secretos antes de compartir código; los grafos son otra ampliación y tienen sus propias licencias
**Cómo:** CodeGraph y graphify construyen índices estructurales que el agente consulta en lugar de leer archivos completos; GitNexus ayuda a recorrer dependencias; Repomix empaqueta solo la parte relevante cuando necesitas pasar código a un chat. Claude Code (o Codex) usa todo eso como contexto barato.

### Marketing de agencia
**Meta:** Operar campañas, contenido y email a escala con agentes y herramientas propias.
**Recursos del recorrido completo:** `marketingskills`, `agency-agents`, `mautic`, `listmonk`, `posthog`
**Empieza con:** `marketingskills`, `listmonk`
**Prepara:** Un borrador de campaña y una lista de prueba con permiso
**Primera prueba propuesta:** Prepara un mensaje y realiza una prueba de envío a una dirección del equipo
**Qué comprobar:** Puedes revisar el texto, la baja y la entrega antes de ampliar destinatarios
Skills y envío son capas distintas; SMTP, dominios, analítica y medios pueden añadir costes
**Cómo:** Las skills y los roles guían a tu agente de código en cada canal; Mautic segmenta y nutre leads; listmonk envía newsletters; PostHog mide conversión y retención. Metabase o Superset sirven si necesitas reportes para clientes.

### Web app moderna con IA
**Meta:** Construir un frontend pulido con chat o funciones de IA integradas.
**Recursos del recorrido completo:** `ui`, `tailwindcss`, `vercel-ai`, `assistant-ui`, `motion`, `recharts`, `swr`
**Empieza con:** `ui`, `tailwindcss`, `vercel-ai`, `assistant-ui`
**Prepara:** Una aplicación de prueba y una ruta de modelo elegida
**Primera prueba propuesta:** Construye una pantalla de chat y envía una pregunta de prueba
**Qué comprobar:** Puedes revisar respuesta, estado de carga y un error de conexión
Motion, gráficos y caché se añaden cuando la función los necesita; revisa API, alojamiento y autenticación por separado
**Cómo:** shadcn/ui y Tailwind dan la base visual; el AI SDK de Vercel resuelve streaming, tool calling y proveedores; assistant-ui aporta la interfaz de chat; Motion anima y Recharts dibuja datos; SWR gestiona el fetching. Para diseñar antes de codificar, prueba Open Design o Penpot.

### Construir una app o servidor MCP
**Meta:** Exponer tus datos o herramientas a Claude, ChatGPT, Cursor y otros agentes con Model Context Protocol.
**Recursos del recorrido completo:** `awesome-mcp-servers`, `fastmcp`, `mcp-typescript-sdk`, `mcp-inspector`, `servers`, `mcp-use`
**Empieza con:** `fastmcp`, `mcp-inspector`
**Prepara:** Una acción de solo lectura y datos de prueba
**Primera prueba propuesta:** Expón una herramienta pequeña y compruébala con el inspector
**Qué comprobar:** La entrada y la salida son las esperadas y el cliente puede descubrir la herramienta
Elige Python o TypeScript para construir la misma capa; añade autenticación y permisos según el entorno antes de compartirla
**Cómo:** Busca en awesome-mcp-servers antes de construir. Si no existe, FastMCP (Python) o el SDK oficial de TypeScript te dan el servidor con poco código; los servidores de referencia muestran cómo modelar tools, recursos y prompts. MCP Inspector valida el servidor antes de conectarlo a Claude Code, Codex o Cursor. mcp-use sirve cuando quieres una app MCP con interfaz propia.

### Documentos → presentaciones
**Meta:** Pasar informes, PDFs o notas a presentaciones editables o slides web.
**Recursos del recorrido completo:** `markitdown`, `docling`, `ppt-master`, `slidev`, `marp`
**Empieza con:** `markitdown`, `ppt-master`
**Prepara:** Un documento breve y el formato de entrega
**Primera prueba propuesta:** Extrae el texto, prepara tres diapositivas y abre la exportación
**Qué comprobar:** El contenido coincide con la fuente y el formato sirve para la entrega
Elige el generador según PowerPoint, PDF o web; la conversión no garantiza que todos los elementos sean editables
**Cómo:** MarkItDown (o Docling si el PDF tiene tablas y columnas) normaliza todo a Markdown. Desde ahí, PPT Master genera un PowerPoint nativo editable, Slidev produce slides web con código y componentes, y Marp exporta a PDF o PPTX con estilos simples.

### ChatGPT privado con modelos locales
**Meta:** Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.
**Recursos del recorrido completo:** `ollama`, `open-webui`, `searxng`, `litellm`
**Empieza con:** `ollama`, `open-webui`
**Prepara:** Un modelo compatible y recursos de equipo suficientes
**Primera prueba propuesta:** Conecta el chat al endpoint local y envía una pregunta
**Qué comprobar:** Puedes identificar el modelo y comprobar dónde se procesa la conversación
Buscadores, herramientas y proveedores opcionales pueden salir a internet; verifica la configuración de cada uno
**Cómo:** Ollama corre los modelos y expone una API compatible con OpenAI; Open WebUI se conecta a ella y añade cuentas de usuario, subida de documentos, búsqueda web vía SearXNG y herramientas. Si algunos usuarios necesitan modelos comerciales, LiteLLM unifica el acceso con control de costos.

### RAG sobre tus documentos
**Meta:** Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
**Recursos del recorrido completo:** `docling`, `llama-index`, `qdrant`, `litellm`, `ragas`, `langfuse`
**Empieza con:** `docling`, `llama-index`
**Prepara:** Un PDF de dos páginas y tres preguntas con respuesta conocida
**Primera prueba propuesta:** Extrae el texto y crea una consulta mínima con un proveedor elegido
**Qué comprobar:** Las respuestas pueden contrastarse con fragmentos del documento
El modelo y los embeddings necesitan configuración propia; almacenamiento vectorial, evaluación y trazas se añaden después
**Cómo:** Docling convierte los documentos en Markdown estructurado; LlamaIndex los fragmenta, genera embeddings y los guarda en Qdrant; en cada pregunta recupera los fragmentos relevantes y llama al modelo vía LiteLLM. Ragas mide si la respuesta usa bien el contexto y Langfuse registra cada consulta. Si prefieres una plataforma con UI, RAGFlow o AnythingLLM cubren el flujo completo.

### Agente de código potenciado
**Meta:** Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.
**Recursos del recorrido completo:** `claude-code`, `superpowers`, `context7`, `serena`, `claude-mem`, `skillspector`
**Empieza con:** `claude-code`, `superpowers`
**Prepara:** Un repo de prueba y una tarea pequeña
**Primera prueba propuesta:** Añade una metodología al agente y pide un cambio con su comprobación
**Qué comprobar:** Puedes revisar el diff y el resultado de la comprobación
La ruta mínima usa Claude Code; compara la compatibilidad de cada complemento antes de adaptarla a Codex o Antigravity
**Cómo:** Superpowers obliga al agente a planificar, escribir pruebas y revisar; Context7 le pasa la documentación vigente de cada librería; Serena le da navegación semántica del código en lugar de leer archivos enteros; claude-mem conserva decisiones entre sesiones. SkillSpector revisa cualquier skill nueva antes de instalarla.

### Agente de voz en tiempo real
**Meta:** Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.
**Recursos del recorrido completo:** `pipecat`, `faster-whisper`, `litellm`, `kokoro`, `livekit-agents`
**Empieza con:** `pipecat`, `faster-whisper`, `kokoro`
**Prepara:** Micrófono, auriculares y un modelo de conversación configurado
**Primera prueba propuesta:** Prueba una frase corta de entrada, respuesta y reproducción
**Qué comprobar:** La transcripción y la voz de salida corresponden a la conversación
Configura también el LLM; transcripción y voz locales no hacen local todo el flujo ni incluyen telefonía
**Cómo:** Pipecat encadena transporte de audio, detección de voz, STT, LLM y TTS con manejo de interrupciones. faster-whisper transcribe, el LLM (vía LiteLLM) decide qué decir y Kokoro lo sintetiza. LiveKit Agents es la alternativa si quieres WebRTC y telefonía SIP resueltos de serie.

### Analítica de producto con IA
**Meta:** Medir el uso de tu producto y responder preguntas de negocio en lenguaje natural.
**Recursos del recorrido completo:** `posthog`, `duckdb`, `wrenai`, `superset`, `umami`
**Empieza con:** `posthog`
**Prepara:** Un sitio de prueba y un evento que puedas provocar
**Primera prueba propuesta:** Registra un evento y compara el resultado con tu acción
**Qué comprobar:** El evento aparece con el nombre y propiedades que esperabas
Empieza por medición; SQL, dashboards y preguntas con IA son ampliaciones con configuración y costes propios
**Cómo:** PostHog captura eventos y embudos; exportas a Parquet y analizas con DuckDB sin montar un warehouse; WrenAI traduce preguntas a SQL sobre tu esquema; Superset publica los dashboards. Si solo necesitas visitas y fuentes de tráfico, Umami o Plausible bastan.

---

## ÍNDICE COMPACTO (1 línea por repo)

Formato: `id` [role|exec|setup|inst] — one — tags:… — prov:… — tools:… — alt:…

### Sin categoría

- `guia` [D|loc|E|?] — Guía editorial original de la biblioteca, hoy integrada en las fichas de cada repo. — tags: learning
- `tools` [D|loc|E|?] — Carpeta interna de herramientas auxiliares del hub; no es un producto para instalar. — tags: skills

### 1. Automatizar procesos y crear herramientas internas (17)
Detalle: `REPO_MENU_cats/01-automatizar-procesos-y-crear-herramientas-internas.md`

- `activepieces` [P|hyb|M|?] — Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flu — tags: automation,typescript,docker
- `airflow` [P|loc|H|?] — Orquestador de workflows de la Apache Software Foundation: DAGs en Python con planificador, workers, reintento — tags: automation,data,python,docker — alt: prefect,dagster,kestra
- `appsmith` [P|loc|M|?] — Plataforma low-code para crear paneles de administración y herramientas internas sobre tus APIs y bases. — tags: ui,automation,typescript,docker — alt: tooljet,budibase,nocodb
- `baserow` [P|hyb|E|+] — Base de datos sin código autoalojable (Django y Vue) con constructor de aplicaciones, automatizaciones, dashbo — tags: data,no-code,python,docker — alt: grist-core,teable,nocodb
- `budibase` [P|loc|M|?] — Plataforma open source para apps internas, automatizaciones y agentes de IA sobre tus datos. — tags: automation,agents,docker — alt: appsmith,tooljet,nocodb
- `dagster` [L|loc|M|+] — Orquestador de datos orientado a activos: declaras tablas, modelos o informes como funciones Python y Dagster  — tags: automation,data,python — alt: airflow,prefect,kestra
- `grist-core` [P|hyb|E|+] — Hoja de cálculo relacional autoalojable con fórmulas en Python, columnas tipadas y formato portable basado en  — tags: data,spreadsheet,docker,python — alt: baserow,teable,nocodb
- `huginn` [P|loc|M|+] — Sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como u — tags: automation,ruby,docker — alt: node-red
- `kestra` [P|loc|M|+] — Orquestador declarativo de workflows en YAML para datos, infraestructura y procesos de negocio. — tags: automation,data,java,docker — alt: windmill,trigger-dev,airflow,prefect,dagster
- `nocodb` [P|loc|E|+] — Alternativa auto-hospedable a Airtable que convierte bases SQL en hojas de cálculo colaborativas. — tags: data,automation,docker — alt: appsmith,budibase,grist-core,baserow,teable
- `node-red` [P|loc|E|?] — Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. — tags: automation,javascript,docker — alt: huginn
- `prefect` [L|loc|E|+] — Framework de orquestación en Python: convierte scripts en flujos con decoradores, reintentos, caché, programac — tags: automation,data,python — alt: airflow,dagster,kestra
- `teable` [P|hyb|M|?] — Base de datos colaborativa sin código sobre PostgreSQL, con vistas tipo hoja, formularios, automatizaciones y  — tags: data,no-code,typescript,docker — alt: grist-core,baserow,nocodb
- `temporal` [P|loc|M|+] — Plataforma de ejecución duradera: workflows en código que sobreviven a fallos, con reintentos, temporizadores  — tags: automation,go,server,agents
- `tooljet` [P|loc|M|?] — Plataforma low-code para herramientas internas, dashboards y flujos, con generación de apps por IA. — tags: ui,automation,docker — alt: appsmith,budibase
- `trigger-dev` [P|hyb|M|?] — Plataforma para tareas en segundo plano y agentes de IA duraderos escritos en TypeScript. — tags: automation,agents,typescript — alt: windmill,kestra
- `windmill` [P|loc|M|+] — Plataforma code-first de workflows, scripts y apps internas, auto-hospedable y muy rápida. — tags: automation,agents,rust,docker — alt: kestra,trigger-dev

### 2. Skills, plugins y métodos para agentes (30)
Detalle: `REPO_MENU_cats/02-skills-plugins-y-m-todos-para-agentes.md`

- `agent-skills` [S|loc|E|+] — Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar — tags: skills,coding-agent — alt: superpowers
- `agent-toolkit` [S|cld|E|+] — Conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documen — tags: agents,skills,python
- `andrej-karpathy-skills` [S|cld|E|+] — Instrucciones para declarar supuestos, simplificar cambios y comprobar objetivos al programar, inspiradas en o — tags: skills,coding-agent
- `anthropic-skills` [S|cld|E|+] — Colección oficial de skills de Anthropic para Claude: ejemplos, skills de documentos Office/PDF y la especific — tags: skills,docs,pdf,coding-agent,python — prov: anthropic
- `antigravity-awesome-skills` [S|hyb|E|+] — Biblioteca de skills para varios agentes con selección revisable y distribución desde GitHub; antes llamada An — tags: skills,coding-agent,mcp,javascript — alt: awesome-agent-skills,awesome-claude-skills,wshobson-agents
- `autoskills` [A|loc|E|+] — CLI que detecta tecnologías de un proyecto y selecciona skills de IA desde un registro de referencia. — tags: catalogos,ruby
- `awesome-agent-skills` [D|hyb|E|?] — Lista curada de más de 1.000 skills de equipos oficiales (Anthropic, Vercel, Stripe, Supabase...) y de la comu — tags: skills,coding-agent,agents — alt: antigravity-awesome-skills,awesome-claude-skills
- `awesome-agents` [D|hyb|E|?] — Directorio de herramientas y proyectos abiertos para construir y operar agentes de inteligencia artificial. — tags: catalogos
- `awesome-claude-code` [D|cld|E|?] — Lista curada de recursos para Claude Code: skills, plugins, hooks, status lines, orquestadores, clientes alter — tags: coding-agent,skills,agents — prov: anthropic — alt: awesome-claude-skills
- `awesome-claude-skills` [D|cld|E|?] — Lista curada de Composio con más de 1.000 skills y plugins para Claude y otros agentes, más un plugin para con — tags: skills,automation,coding-agent — prov: anthropic — alt: awesome-agent-skills,antigravity-awesome-skills,awesome-claude-code
- `awesome-copilot` [S|cld|E|+] — Colección comunitaria de GitHub con agentes, instrucciones, skills, hooks y plugins para personalizar GitHub C — tags: skills,coding-agent,prompts,mcp
- `bmad-method` [S|loc|E|+] — Metodología ágil con agentes especializados (analista, PM, arquitecto, dev) para desarrollar con IA. — tags: coding-agent,skills,agents — alt: spec-kit
- `book-to-skill` [S|loc|M|+] — Herramientas para convertir un libro técnico en PDF en una skill que un agente pueda consultar durante el trab — tags: metodologia,skill,python
- `claude-code-hooks-mastery` [D|loc|E|?] — Ejemplos y material para aprender a configurar hooks de Claude Code y ejecutar comprobaciones en su flujo de t — tags: metodologia,reference,python
- `claude-plugins-official` [S|cld|E|?] — Marketplace oficial de Anthropic con plugins para ampliar las herramientas y flujos de trabajo de Claude Code. — tags: skills,coding-agent,mcp — prov: anthropic — alt: wshobson-agents
- `claude-token-efficient` [S|loc|E|+] — Instrucciones para reducir la verbosidad de Claude Code y medir el coste de respuestas y contexto. — tags: metodologia,python — tools: claude-code
- `codex-plugin-cc` [S|cld|E|+] — Plugin oficial de OpenAI para usar Codex desde Claude Code en revisiones y tareas delegadas. — tags: metodologia,javascript — prov: openai — tools: claude-code
- `ecc` [S|loc|H|+] — Sistema de skills, hooks y configuración para agentes de código, con rutas nativas y adaptadores cuya capacida — tags: automation,skills,javascript — alt: superclaude-framework,superpowers,gstack
- `elephant-goldfish-model` [S|loc|M|+] — Plugin con instrucciones para diseñar y revisar software con agentes mediante contextos y perspectivas complem — tags: metodologia,skill,python
- `gemini-skills` [S|hyb|E|+] — Skills oficiales de Google para ayudar a agentes a trabajar con la API, los SDK y los modelos de Gemini. — tags: catalogos,gemini,gemini-api,skills,python — prov: google
- `google-skills` [S|loc|M|+] — Colección de skills para trabajar con productos y tecnologías de Google desde agentes de programación compatib — tags: catalogos,skill,python
- `grok-plugin-claude-code` [S|cld|E|+] — Plugin de terceros para delegar tareas de Claude Code a Grok CLI mediante comandos y un agente auxiliar. — tags: metodologia,ai-agents,claude-code,grok,grok-cli,plugin,xai,javascript — prov: xai — tools: claude-code
- `gstack` [S|loc|M|+] — Conjunto de skills y herramientas para organizar planificación, implementación, revisión y pruebas con Claude  — tags: metodologia,skill,typescript — alt: superclaude-framework,superpowers,ecc
- `plugins` [D|loc|E|?] — Especificación y colección oficial de plugins de Cursor para estudiar e instalar extensiones de ese agente. — tags: catalogos,reference,typescript
- `ponytail` [S|loc|E|+] — Skill que hace que tu agente de código piense como un senior minimalista: el mejor código es el que no escribe — tags: skills,coding-agent
- `skills` [S|cld|E|+] — Skills de ingeniería de Matt Pocock para trabajar sobre requisitos, diseño, implementación y revisión, con plu — tags: skills,coding-agent
- `spec-kit` [S|loc|E|?] — Kit de GitHub para desarrollo guiado por especificaciones con agentes de código. — tags: coding-agent,skills,python — alt: bmad-method,claude-task-master
- `superclaude-framework` [S|hyb|M|+] — Framework de configuración que añade comandos, roles y metodologías de trabajo a Claude Code. — tags: metodologia,python — tools: claude-code — alt: superpowers,ecc,gstack
- `superpowers` [S|cld|E|+] — Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseg — tags: skills,coding-agent — alt: agent-skills,superclaude-framework,ecc,gstack
- `wshobson-agents` [S|hyb|E|+] — Colección de plugins, agentes y skills con adaptadores documentados para Claude Code, Codex, Antigravity y otr — tags: skills,coding-agent,agents,python — alt: claude-plugins-official,antigravity-awesome-skills,agency-agents

### 3. Construir agentes y coordinar equipos de IA (34)
Detalle: `REPO_MENU_cats/03-construir-agentes-y-coordinar-equipos-de-ia.md`

- `adk-python` [L|hyb|E|+] — Kit de Google para construir, evaluar y desplegar agentes en Python, optimizado para Gemini. — tags: agents,python — prov: google,openai,anthropic — alt: langgraph,openai-agents-python
- `ag2` [L|cld|M|+] — Framework AG2 actual para agentes y redes de colaboración en Python; AG2 Classic conserva por separado la API  — tags: automation,agents,python
- `agent-framework` [R|hyb|M|+] — Framework de Microsoft para agentes y workflows multiagente en Python y .NET, sucesor de AutoGen y Semantic Ke — tags: agents,python — prov: openai,anthropic
- `agentscope` [L|hyb|M|+] — Framework de agentes en Python de origen Alibaba: agentes ReAct, multiagente, herramientas MCP, sandbox, voz e — tags: agents,python,mcp,framework
- `agno` [R|hyb|E|?] — Framework y runtime de agentes en Python con memoria, conocimiento y equipos multiagente. — tags: agents,memory,python — prov: openai,anthropic,google,local — alt: crewai,langgraph
- `autogpt` [P|hyb|H|+] — Plataforma para crear, desplegar y ejecutar agentes de IA continuos con un constructor visual de bloques. — tags: agents,automation,python — prov: openai,anthropic — alt: sim,langflow
- `awesome-langgraph` [D|cld|E|?] — Repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. — tags: automation,agents,javascript
- `camel` [L|hyb|E|+] — Framework multiagente de investigación para generar datos sintéticos, automatizar tareas y simular sociedades  — tags: agents,python,research,framework
- `chatdev` [A|hyb|M|+] — Plataforma multiagente sin código de OpenBMB: configura equipos de agentes por roles; la versión 1.0 simulaba  — tags: agents,python,research
- `claude-agent-sdk-python` [L|hyb|M|+] — SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación  — tags: py,framework,python
- `crewai` [L|cld|E|+] — Framework para orquestar "crews" de agentes con roles y tareas. — tags: automation,agents,python — alt: langgraph,agno,metagpt
- `deepagents` [R|hyb|E|+] — Arnés de agentes de LangChain listo para usar, con planificación, subagentes y sistema de archivos. — tags: agents,python — prov: anthropic,openai — alt: openai-agents-python
- `dify` [P|hyb|M|?] — Plataforma integral para construir apps de IA con backend y UI listos. — tags: automation,agents,python,docker — alt: sim,ragflow
- `dspy` [L|hyb|M|+] — Framework de Stanford para programar modelos de lenguaje en vez de escribir prompts a mano. — tags: prompts,evaluation,python — prov: openai,anthropic,local — alt: promptfoo
- `haystack` [L|hyb|M|+] — Framework de deepset para pipelines de RAG y agentes listos para producción. — tags: rag,agents,python — prov: openai,anthropic,local — alt: llama-index,langchain
- `hermes-agent-self-evolution` [L|cld|M|+] — Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GE — tags: experimentos,python
- `jev-fraud` [L|hyb|M|+] — Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude. — tags: experimentos,template,typescript
- `langchain` [L|cld|M|+] — Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). — tags: agents,automation,python — alt: llama-index,haystack
- `langchain4j` [L|hyb|M|?] — Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la — tags: ts,anthropic,chatgpt,chroma,embeddings,gemini,gpt,huggingface
- `langflow` [A|hyb|M|+] — Constructor visual de flujos LLM/agentes construido sobre LangChain. — tags: automation,agents,python,docker — alt: sim,autogpt
- `langgraph` [R|hyb|M|+] — Framework de LangChain para agentes con estado como grafos, con persistencia, human-in-the-loop y streaming. — tags: agents,python — prov: openai,anthropic,google,local — alt: crewai,openai-agents-python,pydantic-ai,adk-python,agno
- `langgraphjs` [R|hyb|M|+] — Versión TypeScript de LangGraph para agentes con estado como grafos en Node o el navegador. — tags: agents,typescript — alt: mastra,vercel-ai
- `llama-index` [L|hyb|E|+] — Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. — tags: rag,agents,python — prov: openai,anthropic,local — alt: haystack,langchain
- `llm-council` [P|hyb|M|+] — "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. — tags: agents,python
- `mastra` [L|hyb|E|+] — Framework TypeScript para agentes, workflows, RAG y evaluaciones, de los creadores de Gatsby. — tags: agents,rag,typescript — prov: openai,anthropic,google,local — alt: langgraphjs,vercel-ai
- `metagpt` [R|cld|M|+] — Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. — tags: py,agent,gpt,llm,metagpt,multi-agent,python — alt: crewai
- `mirofish` [P|hyb|H|+] — Motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar  — tags: agents,python
- `openai-agents-python` [L|hyb|E|+] — SDK ligero de OpenAI para flujos multiagente con traspasos, guardrails y trazas integradas. — tags: agents,python — prov: openai — alt: pydantic-ai,langgraph,smolagents,deepagents,adk-python
- `openevolve` [R|cld|H|+] — Agente de codificación evolutivo que optimiza algoritmos por simulación genética. — tags: automation,agents,python
- `openmanus` [A|hyb|M|?] — Agente general de código abierto inspirado en Manus: planifica tareas y usa navegador, Python y archivos media — tags: agents,python,browser
- `pydantic-ai` [L|hyb|E|+] — Framework de agentes del equipo de Pydantic, tipado de punta a punta y compatible con cualquier modelo. — tags: agents,python — prov: openai,anthropic,google,local — alt: openai-agents-python,smolagents,langgraph
- `sim` [P|hyb|M|+] — Espacio colaborativo para construir, desplegar y monitorear agentes y workflows de IA con un lienzo visual. — tags: agents,automation,typescript — prov: openai,anthropic,local — alt: langflow,dify,autogpt
- `smolagents` [L|hyb|E|+] — Librería mínima de Hugging Face para agentes que razonan escribiendo y ejecutando código Python. — tags: agents,python — prov: openai,local — alt: pydantic-ai,openai-agents-python
- `vercel-ai` [L|hyb|E|+] — Toolkit TypeScript de Vercel para apps con IA: streaming, herramientas, agentes y UI de chat. — tags: agents,ui,typescript,react — prov: openai,anthropic,google,local — alt: langgraphjs,mastra

### 4. Buscar, extraer y monitorear información web (28)
Detalle: `REPO_MENU_cats/04-buscar-extraer-y-monitorear-informaci-n-web.md`

- `agent-reach` [A|loc|E|?] — CLI que da a tu agente acceso de lectura y búsqueda a Twitter, Reddit, YouTube, GitHub y más sin pagar APIs. — tags: scraping,research,python
- `archivebox` [A|loc|E|?] — Archivador web auto-hospedado que guarda páginas en HTML, PDF, capturas y medios. — tags: scraping,data,python,docker
- `awesome-web-scraping` [D|hyb|E|?] — Directorio de bibliotecas, herramientas y recursos para scraping web y procesamiento de datos. — tags: crawlers,captcha-bypass,captcha-recaptcha,crawler,crawling,crawling-framework,crawling-python,crawling-tool
- `changedetection` [A|loc|E|+] — Monitor de cambios en páginas web con alertas por email, Slack, Telegram y más. — tags: scraping,notifications,python,docker
- `colly` [L|loc|E|?] — Framework de scraping y crawling para Go: callbacks por selector, límites por dominio, caché, cookies y ejecuc — tags: scraping,go,library
- `crawl4ai` [L|loc|M|+] — Librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pen — tags: scraping,python — alt: jina-reader
- `crawlee` [L|loc|M|+] — Framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navega — tags: scraping,typescript
- `crawlee-python` [L|loc|M|+] — Versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosist — tags: scraping,python
- `defuddle` [L|loc|M|+] — Biblioteca para extraer el contenido principal de una página y convertirlo en texto o Markdown utilizable. — tags: crawlers,library,typescript
- `firecrawl` [P|cld|M|+] — Plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio — tags: scraping,typescript,docker — alt: jina-reader
- `freshrss` [P|loc|E|?] — Agregador de noticias RSS autoalojado, ligero y multiusuario, con API para apps móviles, WebSub, extracción po — tags: research,rss,php,docker — alt: miniflux
- `gallery-dl` [A|loc|E|+] — Programa de línea de comandos para descargar galerías y colecciones de imágenes de muchos sitios, con nombres  — tags: scraping,python,image,cli
- `instaloader` [L|loc|E|+] — Herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles,  — tags: vision,scraping,python
- `jina-reader` [P|cld|E|+] — Servicio que convierte cualquier URL en Markdown listo para LLM con solo anteponer r.jina.ai. — tags: scraping,rag,typescript — alt: firecrawl,crawl4ai
- `katana` [A|loc|E|+] — Crawler web de ProjectDiscovery en Go, en modo estándar o headless, con análisis de JavaScript, control de alc — tags: scraping,go,security,cli
- `last30days-skill` [S|cld|E|+] — Skill para agentes que investiga un tema en Reddit, X, YouTube, HN, Polymarket y la web de los últimos 30 días — tags: research,skills,python — alt: social-media-research-skills
- `llm-scraper` [L|hyb|E|+] — Librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el — tags: scraping,typescript — alt: maxun
- `maxun` [P|loc|M|?] — Plataforma sin código para convertir sitios web en APIs y hojas de datos entrenando robots de extracción. — tags: scraping,automation,typescript — alt: scrapegraph-ai,llm-scraper
- `miniflux` [P|loc|E|?] — Lector de feeds minimalista y rápido en Go sobre PostgreSQL, con privacidad, búsqueda de texto completo y más  — tags: research,rss,go,docker — alt: freshrss
- `rsshub` [P|loc|E|?] — Generador de feeds RSS para miles de webs y redes sin RSS propio; instancia pública o autoalojada con Docker. — tags: research,rss,typescript,docker
- `scrapegraph-ai` [L|hyb|M|+] — Framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué e — tags: scraping,python — alt: maxun
- `scrapling` [L|loc|M|+] — Librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica  — tags: automation,scraping,python
- `scrapy` [L|loc|M|+] — Framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesam — tags: scraping,python
- `searxng` [P|loc|E|?] — Metabuscador libre y privado que agrega resultados de muchos buscadores, ideal como buscador para agentes. — tags: search,research,python,docker
- `spotdl` [A|loc|E|+] — CLI que toma listas y canciones de Spotify, busca coincidencias en YouTube y las descarga con carátula, letras — tags: audio,python,cli
- `vane` [A|loc|E|+] — Motor de respuestas con IA auto-hospedado, alternativa abierta a Perplexity (antes Perplexica). — tags: search,research,local,typescript — prov: openai,local — alt: gpt-researcher
- `wallabag` [P|loc|M|?] — Aplicación autoalojada para guardar páginas web y leerlas más tarde sin distracciones, con apps móviles y exte — tags: research,read-later,php,docker
- `yt-dlp` [A|loc|E|?] — Descargador de audio y video por línea de comandos compatible con miles de sitios. — tags: video,audio,scraping,python

### 5. Conectar herramientas con MCP (23)
Detalle: `REPO_MENU_cats/05-conectar-herramientas-con-mcp.md`

- `annas-mcp` [R|hyb|M|?] — Servidor MCP y CLI de Go para buscar y recuperar documentos desde Anna's Archive y sus espejos. — tags: servidores,annas-archive,cli,mcp-server,go
- `awesome-mcp-clients` [D|loc|E|?] — Lista curada de clientes que soportan Model Context Protocol: apps, IDEs y agentes. — tags: mcp
- `awesome-mcp-servers` [D|hyb|E|?] — Directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos  — tags: automation,mcp
- `blender-mcp` [R|loc|E|+] — Plugin comunitario para controlar Blender 3D con cualquier LLM a través de MCP. — tags: mcp,design,python — prov: mcp
- `chrome-devtools-mcp` [R|loc|E|?] — Servidor MCP oficial de Chrome que da a los agentes las DevTools: consola, red y rendimiento. — tags: mcp,browser,typescript — prov: mcp — alt: playwright-mcp,browser-harness
- `context7` [R|cld|E|+] — Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. — tags: mcp,docs,typescript — prov: mcp
- `fastmcp` [L|loc|E|+] — La forma rápida y pythónica de crear servidores y clientes MCP, con auth, despliegue y pruebas. — tags: mcp,python — prov: mcp — alt: mcp-python-sdk
- `figma-context-mcp` [R|hyb|E|?] — Servidor MCP que entrega a los agentes de código el layout de tus diseños de Figma para implementarlos. — tags: mcp,design,ui,typescript — prov: mcp
- `ghidramcp` [R|loc|M|+] — Servidor MCP que conecta asistentes con funciones de Ghidra para consultar y analizar programas binarios. — tags: servidores,mcp,java
- `github-mcp-server` [R|hyb|E|?] — Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. — tags: mcp,code,go — prov: mcp
- `mcp` [D|hyb|M|?] — Directorio de servidores MCP oficiales de Google, ejemplos y orientación para desplegarlos en Google Cloud. — tags: mcp
- `mcp-for-beginners` [D|loc|E|?] — Curso abierto de Microsoft para aprender MCP con ejemplos en .NET, Java, TypeScript, JavaScript y Python. — tags: mcp,learning
- `mcp-inspector` [A|loc|E|+] — Herramienta oficial para probar y depurar servidores MCP desde una interfaz web. — tags: mcp,evaluation,typescript
- `mcp-neo4j` [R|hyb|M|?] — Servidores experimentales de Neo4j Labs para consultar grafos, memoria y recursos Aura desde clientes MCP. — tags: mcp,python — alt: neo4j-mcp
- `mcp-python-sdk` [L|loc|E|+] — SDK oficial de Python para crear servidores y clientes del Model Context Protocol. — tags: mcp,python — prov: mcp — alt: fastmcp
- `mcp-typescript-sdk` [L|loc|E|+] — SDK oficial de TypeScript para crear servidores y clientes del Model Context Protocol. — tags: mcp,typescript — prov: mcp — alt: mcp-use
- `mcp-use` [L|hyb|M|+] — Framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de — tags: automation,mcp,typescript — alt: mcp-typescript-sdk
- `neo4j-mcp` [R|loc|M|+] — Servidor MCP oficial de Neo4j para que un asistente lea el esquema de un grafo y ejecute consultas Cypher de l — tags: mcp,graph,neo4j,cypher,go — alt: mcp-neo4j
- `playwright-mcp` [R|loc|E|+] — Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. — tags: mcp,browser,typescript — prov: mcp — alt: chrome-devtools-mcp,browser-use,browser-harness
- `public-apis` [D|cld|E|?] — Directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyect — tags: mcp,python
- `serena` [R|loc|E|+] — Toolkit MCP que da a tu agente búsqueda y edición semántica de código, como un IDE. — tags: mcp,coding-agent,code,python — prov: mcp — alt: codegraph,gitnexus,codebase-memory-mcp,graphify
- `servers` [D|hyb|M|?] — Colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enl — tags: mcp,typescript
- `unity-mcp` [R|loc|M|?] — Servidor MCP que permite a un asistente operar escenas, scripts y recursos dentro de un proyecto del editor Un — tags: servidores,mcp,c

### 6. Memoria, RAG y búsqueda de conocimiento (23)
Detalle: `REPO_MENU_cats/06-memoria-rag-y-b-squeda-de-conocimiento.md`

- `agentic-rag-for-dummies` [L|hyb|M|+] — Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama. — tags: rag,template,jupyter-notebook — prov: local
- `agentmemory` [L|hyb|E|+] — Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida  — tags: agents,memory,typescript — alt: engram,supermemory,claude-mem
- `chroma` [R|loc|E|+] — Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. — tags: vector-db,rag,rust — alt: qdrant,pgvector,milvus,faiss
- `claude-mem` [S|loc|E|+] — Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. — tags: memory,coding-agent,mcp,typescript — prov: anthropic,mcp — alt: engram,agentmemory
- `cognee` [L|hyb|E|+] — Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. — tags: memory,rag,python — prov: openai,local — alt: graphiti,mem0,graphrag,letta
- `dsh-noema` [L|loc|M|?] — Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. — tags: memoria,plugin,typescript
- `engram` [R|loc|E|?] — Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. — tags: memory,mcp,coding-agent,go — prov: mcp — alt: claude-mem,agentmemory
- `faiss` [L|loc|M|?] — Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. — tags: vector-db,python,cpp — alt: qdrant,chroma
- `graphiti` [L|hyb|M|+] — Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. — tags: memory,rag,python — prov: openai,anthropic — alt: cognee,graphrag
- `graphrag` [L|hyb|M|?] — Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lu — tags: rag,python — alt: graphiti,cognee,lightrag
- `letta` [P|hyb|M|+] — Harness de agentes con estado (Letta Code, antes MemGPT): memoria, identidad y skills que el propio agente ree — tags: memory,agents,typescript — prov: openai,anthropic,local — alt: mem0,cognee
- `lightrag` [L|hyb|M|+] — RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. — tags: rag,python — prov: openai,local — alt: graphrag,ragflow,pageindex
- `mem0` [L|hyb|E|+] — Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y — tags: memory,python — alt: letta,cognee,supermemory
- `mempalace` [L|loc|E|+] — Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin envia — tags: memory,python
- `milvus` [R|loc|H|?] — Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. — tags: vector-db,rag,go,docker — alt: qdrant,chroma,pgvector
- `onyx` [A|hyb|M|?] — Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. — tags: rag,agent,python — prov: local — alt: anything-llm
- `openviking` [P|hyb|H|+] — Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. — tags: memoria,server,python — prov: local
- `pageindex` [L|cld|E|+] — Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. — tags: rag,docs,python — prov: openai — alt: lightrag
- `pgvector` [L|loc|E|?] — Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. — tags: vector-db,postgres,rag — alt: qdrant,chroma,milvus
- `qdrant` [R|loc|E|+] — Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. — tags: vector-db,rag,rust,docker — alt: milvus,chroma,pgvector,faiss
- `ragflow` [P|loc|H|?] — Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. — tags: rag,docs,agents,docker — prov: openai,local — alt: dify,lightrag
- `supermemory` [P|hyb|E|+] — Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. — tags: memory,rag,typescript — alt: mem0,agentmemory
- `turbovec` [L|loc|E|+] — Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación  — tags: automation,vector-db,rust

### 7. Entender código y comprobar su calidad (11)
Detalle: `REPO_MENU_cats/07-entender-c-digo-y-comprobar-su-calidad.md`

- `ast-grep` [A|loc|E|+] — CLI en Rust para búsqueda estructural, lint y reescritura de código usando patrones que parecen código. — tags: code,security,rust — alt: semgrep
- `cli` [A|cld|E|?] — CLI oficial de GitHub para trabajar con PRs, issues, Actions y repos desde la terminal. — tags: code,go
- `codebase-memory-mcp` [R|loc|E|?] — Motor local de inteligencia de código que conecta código, docs e infraestructura en un grafo persistente para  — tags: code,mcp,memory — prov: mcp — alt: codegraph,gitnexus,serena,graphify
- `codegraph` [R|loc|E|+] — CLI que indexa tu código en local para que los asistentes de IA entiendan estructura y flujo sin leer cada arc — tags: code,typescript — alt: codebase-memory-mcp,serena,gitnexus,graphify
- `floorplan` [S|loc|M|+] — Herramienta para que Claude o Codex genere un mapa interactivo y explicado de las partes y relaciones de un pr — tags: codigo,skill,javascript
- `gitnexus` [A|hyb|E|+] — Herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar  — tags: code,typescript — alt: repomix,codebase-memory-mcp,serena,codegraph,graphify
- `graphify` [R|hyb|M|+] — CLI y skill que convierten código y documentos en un grafo consultable; el código se analiza localmente con AS — tags: code,python — alt: codegraph,gitnexus,serena,codebase-memory-mcp
- `openai-python` [L|cld|E|+] — SDK oficial de OpenAI para Python, tipado, con chat, embeddings, imágenes, audio y Responses API. — tags: code,python
- `repomix` [A|loc|E|+] — Empaqueta un repositorio entero en un solo archivo listo para pasarlo a un LLM. — tags: code,coding-agent,typescript — alt: gitnexus
- `swe-bench` [L|loc|H|+] — Benchmark para evaluar si los modelos resuelven issues reales de GitHub. — tags: evaluation,coding-agent,python
- `tree-sitter` [L|loc|M|?] — Sistema de parsing incremental para herramientas de programación, base de editores y agentes de código. — tags: code,rust

### 8. Chats, modelos locales y espacios privados (26)
Detalle: `REPO_MENU_cats/08-chats-modelos-locales-y-espacios-privados.md`

- `airllm` [R|loc|H|+] — Biblioteca para ejecutar modelos de lenguaje en hardware limitado mediante carga y procesamiento de sus compon — tags: motores,engine,jupyter-notebook — prov: local
- `anything-llm` [A|loc|E|?] — App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. — tags: rag,agents,local,javascript — prov: openai,anthropic,local — alt: open-webui,khoj,private-gpt,onyx
- `chatbox` [A|hyb|E|?] — Cliente de chat de escritorio para usar distintos proveedores de LLM y modelos locales desde una interfaz comú — tags: chats,assistant,chatbot,chatgpt,claude,claude-code,copilot,deepseek — alt: jan
- `cherry-studio` [A|hyb|E|?] — App de escritorio que reúne muchos proveedores de IA, agentes y herramientas de productividad. — tags: chatbot,agents,typescript — prov: openai,anthropic,google,local — alt: jan,lobehub
- `exo` [R|loc|M|+] — Ejecuta modelos grandes repartiéndolos entre varios equipos de tu casa u oficina. — tags: inference,local,python — prov: local
- `freetoken` [R|loc|H|+] — Herramientas para servir modelos de IA en hardware local mediante las rutas de inferencia y aceleración del pr — tags: motores,engine,python — prov: local
- `hermes-desktop` [A|loc|E|?] — App de escritorio que envuelve al agente Hermes en una interfaz nativa. — tags: agents,ui,typescript
- `jan` [A|loc|E|?] — Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma i — tags: chatbot,local,rust — prov: local,openai — alt: cherry-studio,textgen,chatbox
- `khoj` [A|hyb|M|?] — Segundo cerebro con IA auto-hospedable: responde desde tus notas y la web, con agentes y automatizaciones. — tags: research,rag,agents,python — prov: openai,anthropic,local — alt: anything-llm,surfsense
- `librechat` [A|hyb|M|?] — Clon mejorado de ChatGPT con agentes, MCP y todos los proveedores en una sola interfaz auto-hospedada. — tags: chatbot,agents,typescript,docker — prov: openai,anthropic,google,local — alt: open-webui,lobehub
- `llama-cpp` [R|loc|M|?] — Motor de inferencia en C/C++ que corre LLM cuantizados en CPU y GPU de casi cualquier equipo. — tags: inference,local,cpp — prov: local — alt: ollama,llamafile,localai
- `llamafile` [R|loc|E|?] — Distribuye y ejecuta un LLM como un solo archivo ejecutable en cualquier sistema operativo. — tags: inference,local,cpp — prov: local — alt: ollama,llama-cpp
- `llmfit` [A|hyb|E|+] — Inspector de hardware que estima qué modelos de lenguaje y cuantizaciones caben en tu CPU, RAM y GPU. — tags: inference,local,rust
- `lobehub` [A|hyb|E|+] — Espacio de trabajo con super-agentes y una interfaz de chat moderna, multi-proveedor y extensible. — tags: chatbot,agents,typescript — prov: openai,anthropic,google,local — alt: open-webui,librechat,cherry-studio
- `localai` [R|loc|M|+] — Servidor de IA local compatible con la API de OpenAI para texto, imagen, voz y video, sin GPU obligatoria. — tags: inference,local,go,docker — prov: local — alt: ollama,llama-cpp
- `magnitude` [R|loc|H|+] — Motor de inferencia local que adapta su ejecución al hardware y ofrece conexiones para agentes y aplicaciones. — tags: motores,engine,rust — prov: local
- `notebooklm-mcp-cli` [R|cld|E|+] — CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde termi — tags: mcp,notebooks,python
- `notebooklm-py` [L|cld|E|?] — API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuen — tags: notebooks,research,python
- `odysseus` [P|loc|H|+] — Workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por age — tags: agents,local,python,docker
- `ollama` [R|loc|E|?] — La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. — tags: inference,local,go — prov: local — alt: llama-cpp,localai,llamafile
- `open-notebook` [A|loc|M|?] — Clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y ge — tags: notebooks,research,typescript,docker — alt: deeptutor,surfsense
- `open-webui` [A|loc|E|+] — Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. — tags: chatbot,local,rag,docker — prov: openai,local — alt: librechat,lobehub,anything-llm,textgen
- `private-gpt` [P|loc|M|?] — Capa de API completa para apps de IA privadas sobre modelos locales: RAG, herramientas y MCP. — tags: rag,local,python — prov: local,openai — alt: anything-llm
- `surfsense` [A|hyb|M|?] — Alternativa abierta y privada a NotebookLM que investiga, transforma y edita tus documentos. — tags: research,rag,notebooks,python — prov: openai,local — alt: open-notebook,khoj
- `textgen` [A|loc|M|?] — App open source para LLM locales con texto, visión, herramientas y API compatible con OpenAI y Anthropic. — tags: chatbot,local,inference,python — prov: local — alt: jan,open-webui
- `transformers.js` [L|loc|M|+] — Biblioteca de Hugging Face que ejecuta modelos Transformers de texto, visión y audio en JavaScript. — tags: motores,browser,javascript,transformers,webml

### 9. Diseñar y construir interfaces web (29)
Detalle: `REPO_MENU_cats/09-dise-ar-y-construir-interfaces-web.md`

- `ai-website-cloner-template` [L|loc|M|?] — Plantilla para que un agente de código estudie una web de referencia y prepare una implementación de su interf — tags: ia-ui,template,typescript
- `ant-design` [L|loc|E|+] — Lenguaje de diseño empresarial y librería de componentes React de Ant Group. — tags: ui,react,typescript — alt: mui,ui
- `assistant-ui` [L|loc|E|+] — Librería React y TypeScript para interfaces de chat con IA de calidad producción. — tags: ui,chatbot,react,typescript — alt: copilotkit
- `copilotkit` [L|hyb|E|+] — Stack frontend para agentes y UI generativa en React, creadores del protocolo AG-UI. — tags: ui,agents,react,typescript — prov: openai,anthropic — alt: assistant-ui
- `daisyui` [L|loc|E|?] — La librería de componentes más popular para Tailwind CSS, con clases semánticas y temas. — tags: ui,design,javascript — alt: ui
- `excalidraw` [A|loc|E|?] — Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. — tags: design,docs,typescript — alt: tldraw,mermaid
- `flexoki` [D|loc|E|?] — Paleta de color para texto, código e interfaces que puede servir de referencia al definir un sistema visual. — tags: estilos,reference,css
- `heroui` [L|loc|E|+] — Librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, da — tags: ui,typescript — alt: mui
- `json-render` [L|hyb|M|+] — Framework para generar interfaces desde una representación JSON y un catálogo de componentes definido por el d — tags: ia-ui,library,typescript
- `konva` [L|loc|M|+] — Biblioteca de canvas para construir editores gráficos, diagramas e interfaces con formas y objetos interactivo — tags: componentes,library,typescript
- `lucide` [L|loc|E|?] — Librería de más de 1500 iconos SVG consistentes, con paquetes para React, Vue y más. — tags: ui,design,typescript
- `magicui` [L|loc|E|?] — Librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces mod — tags: ui — alt: react-bits
- `mui` [L|loc|E|?] — Librería de componentes React completa que implementa Material Design de Google. — tags: ui,react,javascript — alt: ant-design,ui,heroui
- `normalize.css` [L|loc|E|+] — Hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. — tags: ui,design
- `onlook` [A|loc|E|?] — Editor visual con IA para construir, estilar y editar apps React y Tailwind como en Figma. — tags: design,ui,coding-agent,typescript — prov: anthropic — alt: open-design
- `open-design` [A|hyb|M|+] — Espacio de diseño colaborativo con IA que genera, maqueta y anima interfaces desde lenguaje natural. — tags: agents,design,typescript — alt: onlook
- `openui` [L|hyb|E|+] — Estándar abierto de Thesys para UI generativa: el LLM responde con interfaces, no solo texto. — tags: ui,agents,typescript
- `penpot` [A|loc|H|?] — Plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que qui — tags: design,docker
- `plasmic` [A|hyb|M|+] — Builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin per — tags: design,typescript
- `radix-primitives` [L|loc|E|?] — Componentes React sin estilos y accesibles para construir sistemas de diseño propios. — tags: ui,react,typescript
- `react-bits` [L|loc|E|+] — La mayor colección open source de componentes React animados e interactivos para webs llamativas. — tags: ui,react,javascript — alt: magicui
- `screenshot-to-code` [A|cld|E|?] — Convierte capturas, mockups o diseños de Figma en código limpio HTML, Tailwind, React o Vue. — tags: ui,vision,code,python — prov: openai,anthropic,google — alt: stitch-sdk
- `stitch-sdk` [L|cld|E|+] — SDK de Google Labs para generar pantallas de UI desde texto y extraer su HTML y capturas por código. — tags: ui,design,typescript — prov: google — alt: screenshot-to-code
- `swr` [L|loc|E|?] — Librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los reva — tags: ui,typescript — alt: tanstack-query
- `tailwindcss` [L|loc|E|?] — Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directame — tags: ui,design,typescript
- `tanstack-query` [L|loc|E|?] — Biblioteca para obtener, cachear, sincronizar y actualizar datos del servidor en React, Vue, Solid, Svelte, An — tags: frontend,data-fetching,cache,typescript — alt: swr
- `tldraw` [L|loc|E|+] — SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. — tags: design,ui,react,typescript — alt: excalidraw
- `ui` [L|loc|E|?] — Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de in — tags: ui,typescript — alt: mui,ant-design,daisyui
- `ui-sdk` [L|loc|M|+] — Colección de comportamientos y recursos para que agentes construyan interfaces con patrones de interacción def — tags: ia-ui,library,typescript

### 10. Dashboards, analítica y mapas (21)
Detalle: `REPO_MENU_cats/10-dashboards-anal-tica-y-mapas.md`

- `awesome-dataviz` [D|cld|E|?] — Directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad — tags: automation,dataviz,javascript
- `chart-js` [L|loc|E|?] — Librería JavaScript para dibujar gráficos en canvas dentro de una página o aplicación web. — tags: dataviz,javascript — alt: echarts,recharts
- `d3` [L|loc|M|?] — Librería JavaScript para visualizaciones de datos a medida con SVG, Canvas y HTML. — tags: dataviz,javascript — alt: echarts
- `data-analyst-roadmap` [D|loc|E|?] — Hoja de ruta para aprender análisis de datos, con tecnologías, capacidades y orientación de carrera. — tags: recursos,blogs,businessintelligence,courses,data,dataanalysis,dataanalyst,excel
- `echarts` [L|loc|M|?] — Librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gr — tags: dataviz,typescript — alt: d3,chart-js,recharts
- `gods-eye-view` [A|loc|M|+] — Visualizador geoespacial en un globo 3D que reúne fuentes abiertas para explorar información espacial en el na — tags: osint,app,javascript — alt: osiris
- `grafana` [P|loc|E|?] — Plataforma de visualización y observabilidad para métricas, logs y trazas de múltiples fuentes. — tags: observability,dataviz,typescript,docker
- `matomo` [P|loc|M|?] — Alternativa open source a Google Analytics con control total de los datos. — tags: analytics,php — alt: umami,plausible
- `metabase` [P|hyb|M|?] — Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos  — tags: analytics,dataviz,docker — alt: superset,redash
- `odm` [A|loc|M|+] — Herramientas para convertir fotografías aéreas en mapas, nubes de puntos, modelos 3D y modelos de elevación. — tags: geoespacial,app,python
- `osiris` [A|hyb|M|+] — Panel OSINT que combina mapas, noticias, vuelos, sismos y otras fuentes públicas de eventos globales. — tags: osint,typescript — alt: gods-eye-view
- `plausible` [P|hyb|M|?] — Analítica web ligera, sin cookies y centrada en la privacidad, en la nube o auto-hospedada. — tags: analytics,docker — alt: umami,matomo
- `posthog` [P|hyb|H|+] — Plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session re — tags: analytics,python,docker
- `pythia` [P|loc|H|+] — Plataforma local que reúne fuentes de actualidad y genera escenarios con motores de inteligencia y predicción. — tags: osint,typescript
- `recharts` [L|loc|E|+] — Librería de gráficos para React construida con D3, declarativa y componible. — tags: dataviz,react,typescript — alt: chart-js,echarts
- `redash` [P|loc|M|?] — Herramienta para consultar cualquier fuente de datos con SQL, visualizar y compartir dashboards. — tags: analytics,dataviz,typescript — alt: metabase,superset
- `superset` [P|loc|M|?] — Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. — tags: analytics,dataviz,python,docker — alt: metabase,redash
- `umami` [P|loc|E|+] — Analítica web y de producto respetuosa con la privacidad, sin cookies, alternativa a Google Analytics. — tags: analytics,typescript,docker — alt: plausible,matomo
- `uplot` [L|loc|E|?] — Biblioteca compacta de gráficos de series temporales en JavaScript, orientada a renderizar datos con Canvas y  — tags: dataviz,javascript
- `webodm` [P|loc|H|?] — Interfaz para procesar fotografías aéreas y obtener mapas y modelos con el ecosistema de OpenDroneMap. — tags: geoespacial,server,python
- `wrenai` [P|hyb|M|+] — BI generativo: convierte preguntas en SQL fiable a través de una capa semántica gobernada. — tags: analytics,data,agents,python — prov: openai,local

### 11. Generar y editar imágenes con IA (8)
Detalle: `REPO_MENU_cats/11-generar-y-editar-im-genes-con-ia.md`

- `codeformer` [L|loc|M|?] — Modelo para restaurar rostros en fotos antiguas, borrosas o dañadas. — tags: image,vision,python
- `comfyui` [R|loc|H|+] — Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. — tags: image,python — alt: wan2gp
- `diffusers` [L|loc|H|+] — Librería de Hugging Face para ejecutar y entrenar modelos de difusión de imagen, video y audio desde código. — tags: image,python
- `flux2` [R|loc|H|+] — Código oficial de inferencia de los modelos abiertos FLUX.2 de Black Forest Labs para generar y editar imágene — tags: image,python — prov: local
- `invokeai` [A|loc|H|?] — Suite profesional y unificada para Stable Diffusion que combina una UI web pulida con canvas por capas, inpain — tags: image,typescript — alt: krita-ai-diffusion
- `krita-ai-diffusion` [A|loc|M|?] — Plugin para generar y editar imágenes con IA dentro de Krita, con inpainting y outpainting. — tags: image,design,python — prov: local — alt: invokeai
- `real-esrgan` [R|loc|M|+] — Modelo y herramientas de superresolución para ampliar y mejorar visualmente imágenes o video, con posible gene — tags: image,python
- `rembg` [L|loc|E|+] — Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. — tags: image,python

### 12. Editar, grabar y generar video (15)
Detalle: `REPO_MENU_cats/12-editar-grabar-y-generar-video.md`

- `ai-youtube-shorts-generator` [A|hyb|M|+] — Pipeline de Python que extrae clips verticales de videos de YouTube mediante transcripción y selección de mome — tags: generativo,2short-ai-alternative,ai-clip-generator,ai-clipping,auto-clip,auto-crop,highlight-detection,klap-alternative
- `concat` [A|loc|M|?] — Editor de video local con interfaz y mecanismos de automatización mediante JSON-RPC y herramientas MCP. — tags: edicion,app,rust
- `davinci-resolve-mcp` [R|loc|M|+] — Servidor MCP que deja a un agente de IA controlar DaVinci Resolve: montaje, media pool, color, Fusion y render — tags: video,mcp,agents,python — prov: mcp
- `ffmpeg` [A|loc|E|?] — Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier forma — tags: video,audio,automation,cpp
- `hunyuanvideo` [R|loc|H|?] — Modelo abierto de Tencent de 13B parámetros para generar video a partir de texto, con pesos y código de infere — tags: video,inference,local,python — prov: local — alt: wan2-2,hunyuanvideo-1-5
- `hunyuanvideo-1-5` [R|hyb|H|?] — Modelo de video de Tencent de 8,3B parámetros que genera clips desde texto o imagen en 480p y 720p con GPU de  — tags: video,inference,local,python — prov: local — alt: hunyuanvideo,wan2-2
- `lossless-cut` [A|loc|E|?] — App de escritorio para cortar, unir y remuxar video y audio sin recodificar, en segundos y sin perder calidad. — tags: video,audio,ui,typescript
- `moneyprinterturbo` [A|hyb|M|+] — App que genera videos cortos a partir de un tema: guion con LLM, material de stock, voz, subtítulos y música e — tags: video,automation,tts,python — prov: openai,anthropic,google,local — alt: openmontage,videofy-minimal,short-video-factory
- `obs-studio` [A|loc|E|?] — App de escritorio libre para grabar pantalla y transmitir en directo, con escenas, fuentes y mezcla de audio e — tags: video,audio,ui,cpp
- `opencut` [A|hyb|M|?] — Editor de video abierto cuya versión clásica puede probarse en la web mientras el proyecto principal se reescr — tags: video,ui,typescript,rust
- `openrv` [A|loc|E|?] — Reproductor de revisión de video y secuencias de imágenes para comparar tomas y revisar trabajo audiovisual. — tags: edicion,app,c
- `short-video-factory` [A|hyb|M|?] — Aplicación de escritorio para crear videos cortos de producto combinando guion, narración, clips y subtítulos. — tags: generativo,ai,automatic,automation,clipping,cross-platform,desktop,linux — alt: moneyprinterturbo
- `videolingo` [A|hyb|M|+] — App para reconocer voz, traducir subtítulos y preparar doblaje, con ASR local por defecto y proveedores config — tags: video,stt,tts,python — prov: openai — alt: omnivoice-studio
- `wan2-2` [R|loc|H|+] — Familia de modelos abiertos de Alibaba para generar video desde texto, imagen o voz, con arquitectura MoE y li — tags: video,inference,local,python — prov: local — alt: hunyuanvideo,hunyuanvideo-1-5
- `wan2gp` [A|loc|H|?] — App web local que reúne modelos abiertos de video, imagen, audio y 3D (Wan, LTX, Hunyuan, Flux) para GPU modes — tags: video,image,tts,local,python — prov: local,mcp — alt: comfyui

### 13. PDF, OCR y procesamiento de documentos (19)
Detalle: `REPO_MENU_cats/13-pdf-ocr-y-procesamiento-de-documentos.md`

- `docling` [L|loc|E|+] — Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. — tags: docs,pdf,ocr,python — alt: marker,mineru,unstructured,olmocr
- `docuseal` [P|loc|H|+] — Aplicación para preparar formularios y gestionar la firma electrónica de documentos, con opciones de despliegu — tags: pdf,server,ruby
- `marker` [L|loc|E|+] — Convierte PDF a Markdown y JSON de forma rápida y precisa, con tablas, fórmulas y código. — tags: docs,pdf,python — alt: docling,mineru,pdf-craft
- `markitdown` [L|loc|E|?] — Utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, a — tags: docs,python
- `mineru` [A|loc|M|+] — Convierte PDFs y documentos de Office complejos en Markdown o JSON para flujos con agentes. — tags: docs,pdf,ocr,python — alt: docling,marker
- `ocrmypdf` [A|loc|E|?] — Añade una capa de texto OCR a PDFs escaneados para poder buscarlos y copiarlos. — tags: ocr,pdf,python
- `olmocr` [A|loc|H|+] — Toolkit de Allen AI que convierte PDFs en texto limpio con un modelo de visión, a gran escala. — tags: ocr,pdf,python — prov: local — alt: paddleocr,docling,unlimited-ocr
- `paddleocr` [L|loc|M|?] — Toolkit de OCR ligero y potente que convierte imágenes y PDFs en datos estructurados para IA. — tags: ocr,docs,python — alt: tesseract,olmocr,unlimited-ocr
- `pandoc` [A|loc|E|?] — Conversor universal de documentos entre Markdown, Word, HTML, LaTeX, EPUB y decenas de formatos. — tags: docs
- `paperless-ngx` [P|loc|H|?] — Gestor documental autoalojado para importar, reconocer texto, buscar y archivar documentos escaneados. — tags: gestion,server,python
- `pdf-craft` [L|hyb|M|+] — Herramienta para convertir libros escaneados en PDF a documentos editables mediante rutas de OCR y procesamien — tags: ocr,library,python — prov: local — alt: marker
- `pdf-inspector` [L|loc|E|+] — Librería en Rust que clasifica PDFs (texto o escaneado) y extrae su texto con coordenadas. — tags: pdf,docs,rust
- `pdfcraft` [A|loc|E|?] — Conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y co — tags: pdf,typescript — alt: stirling-pdf
- `pdfding` [A|loc|E|?] — Gestor, visor y editor de PDF autoalojado (AGPL-3.0) con colecciones, etiquetas, anotaciones y progreso de lec — tags: pdf,docker
- `pdfmathtranslate` [A|hyb|E|+] — Traduce papers en PDF conservando el formato, fórmulas y figuras, con versión bilingüe. — tags: pdf,docs,python — prov: openai,google,local
- `stirling-pdf` [A|loc|E|+] — Aplicación web auto-hospedada para editar, unir, dividir, convertir y firmar PDFs. — tags: pdf,docker — alt: pdfcraft
- `tesseract` [A|loc|E|?] — Motor de OCR de código abierto que reconoce texto en imágenes y documentos escaneados mediante modelos de idio — tags: ocr,cpp — alt: paddleocr
- `unlimited-ocr` [L|loc|H|+] — Modelo de Baidu para parsear documentos largos de una sola pasada con visión. — tags: ocr,docs,python — alt: olmocr,paddleocr
- `unstructured` [L|hyb|M|?] — ETL open source que transforma documentos complejos en datos estructurados para LLM. — tags: docs,data,python — alt: docling

### 14. Investigar finanzas y mercados (19)
Detalle: `REPO_MENU_cats/14-investigar-finanzas-y-mercados.md`

- `autohedge` [R|cld|H|+] — Experimento de agentes coordinados para análisis de mercado, riesgo y flujos de trading automatizado. — tags: finanzas,ai,blackrock,finance,goldmansachs,hedgefund,jpmorgan,ml
- `binance-trader` [A|cld|M|?] — Bot experimental de Python para estudiar estrategias y automatización con la API de Binance. — tags: finanzas,arbitrage,binance,bitcoin,btc,cryptocurrency,trade,python
- `ccxt` [L|loc|M|+] — Biblioteca que unifica APIs de exchanges para consultar mercados y desarrollar integraciones de trading. — tags: bots,library,python
- `daily-stock-analysis` [A|cld|M|+] — Sistema que analiza acciones de varios mercados con LLM y envía un tablero de decisiones diario. — tags: analytics,agents,python — prov: openai,google
- `dexter` [A|cld|M|?] — Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. — tags: finanzas,typescript
- `finceptterminal` [A|hyb|H|?] — Terminal de análisis financiero que reúne datos, investigación, paneles y herramientas de agentes. — tags: finanzas,ai-agents,algorithmic-trading,bloomberg-terminal,cpp,finance,financial-markets,fintech
- `finrl` [L|loc|H|+] — Biblioteca y ejemplos para investigar estrategias de trading mediante aprendizaje por refuerzo y simulaciones. — tags: cuant,framework,jupyter-notebook — prov: local
- `freqtrade` [A|loc|M|?] — Bot de trading de criptomonedas con herramientas para preparar estrategias, hacer backtesting y operar en simu — tags: bots,app,python
- `hummingbot` [A|loc|M|+] — Software para desarrollar y ejecutar bots de trading de criptomonedas mediante conectores y estrategias config — tags: bots,app,python
- `lumibot` [L|loc|M|+] — Framework de Python para desarrollar estrategias, realizar backtesting y conectar simulación u operación con b — tags: cuant,framework,python
- `machine-learning-for-trading` [D|hyb|H|?] — Material y código de Machine Learning for Trading para estudiar datos, modelos y evaluación de estrategias. — tags: finanzas,algorithmic-trading,artificial-intelligence,backtesting,data-science,deep-learning,finance,investment
- `nautilus-trader` [L|loc|M|+] — Motor de trading y backtesting con arquitectura orientada a eventos para investigar y desarrollar estrategias. — tags: cuant,framework,rust
- `open-sol-bot` [P|hyb|H|?] — Bot abierto de Solana que reúne seguimiento de operaciones y funciones de trading automatizado. — tags: finanzas,blockchain,solana,telegram-bot,trader,transaction,python
- `py-sdk` [L|loc|M|+] — SDK Python de Polymarket para integrar funciones de su plataforma mediante las APIs y credenciales correspondi — tags: bots,library,python
- `qlib` [P|loc|H|+] — Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. — tags: finanzas,algorithmic-trading,auto-quant,deep-learning,finance,fintech,investment,machine-learning
- `quantharness` [R|cld|M|+] — Sistema experimental de agentes LLM que combina indicadores técnicos, patrones y tendencias para análisis de t — tags: finanzas,agentic-ai,large-language-models,html
- `tradingagents` [R|cld|M|+] — Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de tradi — tags: finanzas,agent,finance,llm,multiagent,trading,python
- `vectorbt` [L|loc|M|+] — Biblioteca de análisis cuantitativo para explorar señales y comparar estrategias sobre datos de mercado. — tags: cuant,framework,python
- `vibe-trading` [A|hyb|M|+] — Agente de investigación y trabajo con estrategias de trading que utiliza modelos y componentes configurables. — tags: agentes,agent,python — prov: local

### 15. Organizar notas, archivos y servicios personales (27)
Detalle: `REPO_MENU_cats/15-organizar-notas-archivos-y-servicios-personales.md`

- `40-questions` [D|loc|E|?] — Colección de preguntas para revisar un año o una década y reflexionar sobre objetivos, hábitos y decisiones pe — tags: personal,reference
- `adguardhome` [P|loc|H|?] — Servidor DNS para filtrar anuncios y rastreadores de los dispositivos de una red desde una configuración centr — tags: privacidad,server,typescript
- `ai-job-search` [S|loc|M|?] — Proyecto basado en Claude Code para evaluar vacantes, adaptar currículums y preparar cartas e entrevistas de e — tags: personal,skill,python
- `anytype-ts` [A|loc|E|?] — Cliente de escritorio de Anytype para organizar notas, objetos y relaciones en un espacio de conocimiento pers — tags: notas,app,typescript — alt: appflowy
- `appflowy` [A|hyb|E|?] — Espacio de trabajo para notas, wikis y proyectos colaborativos, con funciones de IA y opciones de alojamiento  — tags: notas,app,dart — alt: anytype-ts
- `audiobookshelf` [P|loc|H|?] — Servidor personal para organizar audiolibros y podcasts, escuchar contenido y conservar el progreso de reprodu — tags: lectura,server,javascript
- `bitwarden-clients` [A|loc|E|?] — Clientes oficiales de Bitwarden para gestionar credenciales y utilizar funciones como compartir información co — tags: privacidad,app,typescript
- `claude-obsidian` [S|loc|M|+] — Instrucciones para que Claude Code clasifique, enlace y consulte fuentes dentro de una bóveda de notas de Obsi — tags: notas,skill,python — alt: obsidian-second-brain
- `cleanyourtv` [A|loc|M|?] — Herramienta para revisar y retirar aplicaciones preinstaladas de dispositivos Android TV o Google TV mediante  — tags: personal,app,python
- `home-assistant` [P|loc|H|?] — Motor de Home Assistant para conectar dispositivos y automatizar acciones del hogar con control local. — tags: domotica,server,python
- `jsoncanvas` [D|loc|E|?] — Especificación abierta de JSON Canvas para describir nodos y conexiones de un lienzo visual en un archivo. — tags: notas,reference,javascript
- `karakeep` [P|hyb|H|?] — Gestor autoalojado de marcadores, notas e imágenes con búsqueda y funciones opcionales de clasificación median — tags: notas,server,typescript
- `kepano-obsidian` [L|loc|M|?] — Plantilla de una bóveda de Obsidian para estudiar una forma de organizar notas e información personal. — tags: notas,template,reference
- `nextcloud-server` [P|hyb|H|?] — Servidor de Nextcloud para almacenar y compartir archivos, contactos y calendarios en infraestructura propia. — tags: workspaces,cloud,collaboration,decentralized,design,distributed,enterprise,federation
- `obsidian-clipper` [A|loc|E|?] — Extensión oficial para capturar páginas y fragmentos de la web y guardarlos como notas en Obsidian. — tags: notas,app,typescript
- `obsidian-help` [D|loc|E|?] — Documentación oficial de Obsidian para aprender sus funciones, configuración y formas de organizar una bóveda. — tags: notas,reference,javascript
- `obsidian-importer` [A|loc|E|?] — Plugin oficial para convertir datos de otras aplicaciones en archivos Markdown que puedes abrir en Obsidian. — tags: notas,app,typescript
- `obsidian-minimal` [A|loc|E|?] — Tema configurable de Obsidian para ajustar la apariencia y reducir distracciones al trabajar con notas. — tags: notas,app,css
- `obsidian-releases` [A|loc|E|?] — Repositorio de distribución de Obsidian y sus listados de plugins y temas; no contiene el código completo de l — tags: notas,app,reference
- `obsidian-sample-plugin` [L|loc|M|?] — Plantilla oficial para programar un plugin de Obsidian con una estructura inicial y configuración de desarroll — tags: notas,template,typescript
- `obsidian-second-brain` [S|loc|M|+] — Sistema de memoria y notas en Markdown para compartir contexto de trabajo entre agentes y una bóveda de Obsidi — tags: notas,skill,python — alt: claude-obsidian
- `obsidian-skills` [S|loc|M|+] — Skills para que un agente trabaje con Obsidian y sus formatos de notas, bases de datos y lienzos. — tags: notas,skill,shell
- `openmaic` [A|hyb|M|+] — Aplicación educativa con varios agentes que prepara clases y actividades mediante modelos y recursos configura — tags: aprendizaje,agent,typescript — prov: local
- `optimizerduck` [A|loc|E|?] — Aplicación para revisar y ajustar opciones de rendimiento, privacidad y configuración de un equipo con Windows — tags: personal,app,c
- `syncthing` [A|loc|E|?] — Aplicación para sincronizar archivos entre dispositivos directamente y controlar qué carpetas se comparten. — tags: archivos,app,go
- `universal-android-debloater-next-generation` [A|loc|M|?] — Interfaz para revisar y retirar paquetes preinstalados de dispositivos Android mediante ADB y listas de aplica — tags: personal,app,rust
- `vaultwarden` [P|loc|H|?] — Servidor no oficial compatible con clientes Bitwarden para alojar una bóveda de credenciales en infraestructur — tags: privacidad,server,rust

### 16. Analizar software y comprobar su seguridad (26)
Detalle: `REPO_MENU_cats/16-analizar-software-y-comprobar-su-seguridad.md`

- `angr` [L|loc|M|?] — Plataforma en Python para analizar programas binarios mediante técnicas como ejecución simbólica y análisis de — tags: reversing,library,python
- `apktool` [A|loc|M|?] — Herramienta para decodificar recursos y reconstruir paquetes APK de Android durante el análisis de una aplicac — tags: reversing,app,java
- `awesome-ai-reverse-engineering` [D|loc|E|?] — Directorio de herramientas de ingeniería inversa y análisis de software que pueden trabajar con agentes de IA. — tags: referencias,reference
- `awesome-reverse-engineering` [D|loc|E|?] — Directorio de herramientas y recursos para aprender análisis de binarios, aplicaciones, firmware y protocolos. — tags: referencias,reference,python
- `bla` [A|loc|M|+] — Herramientas para aplicar protecciones y comprobar superficies de software frente a análisis automatizado por  — tags: defensa,app,typescript
- `craft-anything` [A|hyb|M|+] — Herramientas para estudiar cómo funciona una aplicación y ayudar a construir una implementación propia con age — tags: agentes,app,rust — prov: local
- `cybersecurity-skills` [S|hyb|E|+] — Biblioteca comunitaria de skills para análisis de seguridad, defensa y pruebas autorizadas con Claude Code, Co — tags: cybersecurity,seguridad,skills,claude-code,codex,comunidad
- `defending-code-reference-harness` [S|cld|M|+] — Arnés de referencia de Anthropic con skills para modelar amenazas, escanear, priorizar y parchear vulnerabilid — tags: security,skills,coding-agent — prov: anthropic
- `dnspy` [A|loc|E|?] — Depurador y editor de ensamblados .NET para inspeccionar y analizar aplicaciones de esa plataforma. — tags: depuracion,app,c
- `frida` [A|loc|M|?] — Herramientas de instrumentación dinámica para observar y modificar el comportamiento de programas durante su e — tags: reversing,app,meson
- `ghidra` [A|loc|M|?] — Conjunto de herramientas para desensamblar, descompilar y analizar programas y su estructura binaria. — tags: reversing,app,java — alt: radare2
- `ilspy` [A|loc|E|?] — Descompilador de .NET para explorar ensamblados y estudiar el código y metadatos de aplicaciones compatibles. — tags: reversing,app,c
- `imhex` [A|loc|E|?] — Editor hexadecimal para inspeccionar archivos binarios, identificar estructuras y describir formatos mediante  — tags: reversing,app,c
- `jadx` [A|loc|M|?] — Descompilador de archivos DEX y APK para explorar código Java reconstruido y recursos de aplicaciones Android. — tags: reversing,app,java
- `k6` [A|loc|M|?] — Herramienta de pruebas de carga para medir cómo responden aplicaciones y servicios bajo distintos niveles de t — tags: pruebas,app,go
- `mitmproxy` [A|loc|M|?] — Proxy interactivo para inspeccionar tráfico HTTP y HTTPS al depurar aplicaciones o realizar pruebas autorizada — tags: pruebas,app,python
- `radare2` [A|loc|M|?] — Conjunto de herramientas de consola para inspeccionar, desensamblar y depurar programas y archivos binarios. — tags: reversing,app,c — alt: rizin,ghidra
- `raddebugger` [A|loc|E|?] — Depurador gráfico nativo para inspeccionar procesos, código y memoria durante el análisis de programas. — tags: depuracion,app,c
- `rea` [S|loc|M|+] — Herramientas e instrucciones para estudiar el comportamiento y la estructura de software mediante agentes de c — tags: agentes,skill,typescript
- `rizin` [A|loc|M|?] — Herramientas para analizar binarios y estudiar programas mediante desensamblado, depuración y otras funciones  — tags: reversing,app,c — alt: radare2
- `security-audit-skill` [S|hyb|M|+] — Skill de Cloudflare que organiza auditorías de código con búsqueda, validación independiente y hallazgos estru — tags: metodologia,javascript
- `semgrep` [A|loc|E|+] — Análisis estático ligero para muchos lenguajes con reglas que se parecen al código. — tags: security,code — alt: ast-grep
- `shannon` [A|hyb|M|+] — Agente para analizar código y comprobar vulnerabilidades de aplicaciones web y APIs dentro de un alcance autor — tags: agentes,agent,typescript — prov: local — alt: strix
- `skillspector` [A|cld|E|+] — Herramienta que audita skills de agentes y detecta comandos peligrosos, exfiltración o prompts ocultos. — tags: skills,coding-agent,python
- `strix` [A|hyb|M|?] — Agente de pruebas de seguridad para aplicaciones, con rutas de API, modelos locales y acceso documentado de Ch — tags: agentes,agent,python — prov: local — alt: shannon
- `x64dbg` [A|loc|E|?] — Depurador de Windows para inspeccionar programas en ejecución y estudiar instrucciones, memoria y llamadas. — tags: depuracion,app,c

### 17. WhatsApp, mensajería y chatbots (10)
Detalle: `REPO_MENU_cats/17-whatsapp-mensajer-a-y-chatbots.md`

- `baileys` [L|loc|E|?] — Librería TypeScript que habla el protocolo de WhatsApp Web por WebSocket, sin navegador. — tags: whatsapp,chatbot,typescript — alt: whatsapp-web-js,waha
- `botpress` [L|hyb|M|+] — Hub de SDKs, CLI e integraciones para desarrollar y desplegar conexiones en el ecosistema Botpress. — tags: chatbot,agents,typescript
- `evolution-api` [P|loc|H|?] — API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. — tags: automation,whatsapp,typescript,docker — alt: whatsapp-web-js,waha
- `fluxer` [P|hyb|M|?] — Aplicación de mensajería instantánea y llamadas de voz para comunidades, con código abierto y opciones de aloj — tags: whatsapp,chatbot,typescript
- `openwa` [P|loc|E|+] — Gateway autoalojado de WhatsApp con API, panel de sesiones y servidor MCP HTTP opcional, del proyecto rmyndhar — tags: whatsapp,chatbot,typescript
- `typebot` [P|loc|M|?] — Constructor visual de chatbots conversacionales, auto-hospedable, para web, WhatsApp y más. — tags: chatbot,automation,typescript
- `waha` [P|loc|E|+] — API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. — tags: whatsapp,automation,docker — alt: evolution-api,whatsapp-web-js,baileys
- `whatsapp-agentkit` [S|hyb|E|+] — Instrucciones y scripts que guían a Claude Code para construir un bot de WhatsApp; el bot resultante necesita  — tags: agents,automation,python
- `whatsapp-web-js` [L|loc|E|+] — Librería Node.js que automatiza WhatsApp controlando WhatsApp Web en un navegador headless. — tags: whatsapp,chatbot,javascript — alt: baileys,waha,evolution-api
- `whatsmeow` [L|hyb|M|?] — Biblioteca de Go para interactuar con el protocolo multidispositivo de WhatsApp Web. — tags: whatsapp,go,golang,whatsapp-web

### 18. CRM, ventas y marketing (13)
Detalle: `REPO_MENU_cats/18-crm-ventas-y-marketing.md`

- `cal.diy` [P|hyb|H|?] — Edición comunitaria de Cal.com para experimentar con agendas y reservas en una instalación propia. — tags: motores,next-auth,nextjs,open-source,postgresql,prisma,t3-stack,tailwindcss
- `chatwoot` [P|loc|H|?] — Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, e — tags: automation,crm,ruby,docker
- `cloud-mail` [P|loc|H|?] — Plataforma de correo basada en servicios de Cloudflare para gestionar buzones y funciones de mensajería de un  — tags: marketing,server,javascript
- `compai-crm` [P|cld|H|+] — CRM de Comp AI diseñado alrededor de agentes que investigan contactos, organizan tareas y registran evidencia. — tags: crm,typescript
- `erpnext` [P|loc|H|+] — ERP 100 % libre sobre Frappe con contabilidad, inventario, CRM, nómina y manufactura. — tags: crm,python — alt: odoo
- `listmonk` [P|loc|M|+] — Gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depe — tags: automation,email,go,docker
- `mautic` [P|loc|H|?] — Plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites com — tags: automation,email,php
- `novu` [P|hyb|M|?] — Infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y ch — tags: automation,email,typescript
- `odoo` [P|loc|H|?] — Suite ERP y CRM de código abierto con módulos de ventas, inventario, contabilidad y web. — tags: crm,python,postgres — alt: erpnext
- `open-seo` [P|loc|H|?] — Aplicación de análisis SEO que consulta datos de buscadores mediante DataForSEO y permite alojamiento propio. — tags: marketing,server,typescript
- `postiz-app` [P|hyb|H|?] — Plataforma para preparar, programar y gestionar publicaciones en redes sociales, con integraciones y funciones — tags: marketing,server,typescript
- `sellbird` [A|loc|M|+] — Plataforma de prospección por correo que documenta el uso de sesiones de Claude Code o Codex para sus agentes. — tags: marketing,agent,python
- `twenty-main` [P|hyb|H|?] — CRM open-source orientado a equipos técnicos, pensado como alternativa moderna a Salesforce/HubSpot que modela — tags: automation,crm,typescript,docker

### 19. Aprender IA y escribir mejores prompts (28)
Detalle: `REPO_MENU_cats/19-aprender-ia-y-escribir-mejores-prompts.md`

- `12-factor-agents` [D|hyb|E|?] — Guía de 12 principios de ingeniería para construir agentes con LLM fiables en producción, inspirada en las 12  — tags: agents,learning,prompts,typescript
- `500-ai-agents-projects` [D|hyb|E|?] — Colección de casos de uso y agentes autocontenidos, junto con enlaces a implementaciones externas. — tags: guias,ai-agents,genai,python
- `agents-towards-production` [D|cld|M|+] — Colección de 28 tutoriales con código para llevar agentes de IA a producción: memoria, despliegue, seguridad,  — tags: agents,learning,notebooks,python — prov: openai,local
- `ai-agents-for-beginners` [D|cld|M|?] — Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar a construir agentes de IA, tra — tags: agents,learning,notebooks,python — prov: openai,local
- `ai-engineering-hub` [D|hyb|E|?] — Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificia — tags: guias,agents,ai,llms,machine-learning,mcp,rag,jupyter notebook
- `awesome-harness-engineering` [D|loc|E|?] — Directorio de herramientas y patrones para diseñar el entorno, memoria, evaluación y permisos de agentes de IA — tags: guias,reference,python
- `awesome-llm-apps` [D|hyb|M|?] — Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos multiagente, RAG, voz, MCP y sk — tags: agents,rag,learning,python — prov: openai,anthropic,google,local — alt: openai-cookbook,claude-cookbooks
- `awesome-machine-learning` [D|hyb|E|?] — Directorio de frameworks, bibliotecas y recursos de machine learning organizado por lenguaje y tema. — tags: aprender,python
- `chatgpt-dan` [D|cld|E|?] — Archivo de prompts históricos de roleplay y jailbreak atribuidos a versiones antiguas de ChatGPT. — tags: prompts,chatgpt,gpt-3-5,gpt-4,jailbreak,openai,prompt
- `chatgpt-system-prompt` [D|hyb|E|?] — Colección de prompts de GPT y recursos sobre instrucciones de sistema y extracción de prompts. — tags: prompts,gpt,prompt,prompt-engineering,html
- `claude-cookbooks` [D|cld|E|?] — Recetario oficial de Anthropic con notebooks de Python para la API de Claude: tool use, RAG, visión, evals, ca — tags: learning,notebooks,rag,python — prov: anthropic — alt: openai-cookbook,awesome-llm-apps
- `claude-quickstarts` [D|cld|M|?] — Ejemplos oficiales de Anthropic para construir aplicaciones con Claude, herramientas y uso de computadora. — tags: guias,python — prov: anthropic
- `context-engineering` [D|cld|E|?] — Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la informaci — tags: learning,python
- `fabric` [A|hyb|E|+] — CLI con cientos de patrones de prompts para resumir, extraer y transformar texto desde la terminal. — tags: prompts,automation,go — prov: openai,anthropic,local — alt: prompts-chat
- `generative-ai-for-beginners` [D|cld|E|?] — Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificia — tags: learning,prompts,python — alt: llm-course
- `how-to-train-your-gpt` [D|loc|E|+] — Guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librerí — tags: learning
- `llm-course` [D|loc|E|?] — Curso gratuito de Maxime Labonne con rutas y notebooks de Colab para aprender LLM de cero a producción. — tags: learning,training,notebooks — alt: llms-from-scratch,generative-ai-for-beginners
- `llm.c` [L|loc|H|?] — Implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados,  — tags: learning
- `llms-from-scratch` [D|loc|M|+] — Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. — tags: learning,training,python — alt: llm-course
- `loop-engineering` [S|loc|E|+] — Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código en vez de prompts sueltos. — tags: coding-agent,skills,typescript
- `nanochat` [L|loc|M|+] — Pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde e — tags: learning,python
- `openai-cookbook` [D|cld|E|?] — Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos reales. — tags: learning,notebooks,python — alt: claude-cookbooks,awesome-llm-apps
- `prompt-eng-tutorial` [D|cld|E|?] — Tutorial interactivo oficial de Anthropic para aprender ingeniería de prompts con ejercicios. — tags: learning,prompts,notebooks — prov: anthropic — alt: prompt-engineering-guide
- `prompt-engineering-guide` [D|cld|E|?] — Guía de referencia de DAIR.AI sobre prompts, ingeniería de contexto, RAG y agentes. — tags: learning,prompts,rag — alt: prompt-eng-tutorial
- `prompt-master` [S|cld|E|+] — Skill de Claude que ayuda a formular encargos para distintas herramientas de IA; no garantiza ahorro de tokens — tags: skills,prompts
- `prompts-chat` [D|loc|E|?] — La colección comunitaria de prompts más grande (antes Awesome ChatGPT Prompts), auto-hospedable. — tags: prompts,chatbot — alt: fabric
- `system-prompts-and-models-of-ai-tools` [D|hyb|E|?] — Colección de prompts y configuraciones atribuidos a herramientas de IA para estudiar sus patrones de diseño. — tags: prompts,ai,bolt,cluely,copilot,cursor,cursorai,devin
- `train-llm-from-scratch` [D|loc|H|+] — Tutorial y código de PyTorch para construir y entrenar un modelo de lenguaje desde los datos hasta la generaci — tags: aprender,gemini,large-language-models,llm,openai,training,transformers,python

### 20. Programar con agentes de código (17)
Detalle: `REPO_MENU_cats/20-programar-con-agentes-de-c-digo.md`

- `aider` [R|hyb|E|+] — Programación en pareja con IA en la terminal que edita tu repo y hace commits de Git automáticos. — tags: coding-agent,python — prov: openai,anthropic,local — alt: opencode,cline
- `antigravity-cli` [A|hyb|E|?] — Agente de programación de Google para la terminal (agy), con subagentes, MCP y skills; se distribuye en binari — tags: coding,agents,cli,google — prov: google — alt: gemini-cli,claude-code,codex
- `claude-code` [R|cld|E|+] — Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. — tags: coding-agent,agents,mcp,typescript — prov: anthropic,mcp — alt: codex,gemini-cli,opencode,goose,antigravity-cli
- `cline` [R|hyb|E|+] — Agente de código autónomo para VS Code y JetBrains, también como CLI y SDK, con cualquier modelo. — tags: coding-agent,agents,typescript — prov: openai,anthropic,google,local — alt: aider
- `codex` [R|cld|E|+] — Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. — tags: coding-agent,agents,rust — prov: openai,mcp — alt: claude-code,gemini-cli,opencode,antigravity-cli
- `deepseek-harness` [A|hyb|M|+] — Harness de agentes de DeepSeek en vista previa, con arquitectura de plugins, Web UI local y proveedores de mod — tags: agents,coding,plugins,typescript — prov: deepseek,anthropic,openai,local
- `gemini-cli` [R|cld|E|+] — CLI de Google orientado actualmente a Code Assist empresarial; el README remite el acceso individual a Antigra — tags: coding-agent,agents,typescript — prov: google,mcp — alt: claude-code,codex,opencode,antigravity-cli
- `goose` [R|hyb|E|?] — Agente de IA open source, extensible por MCP, que instala, ejecuta, edita y prueba con cualquier LLM. — tags: coding-agent,agents,mcp,rust — prov: openai,anthropic,google,local — alt: opencode,claude-code,open-interpreter
- `mimo-code` [A|hyb|M|?] — Asistente de código de Xiaomi MiMo para la terminal con herramientas de archivos, comandos, Git y memoria pers — tags: coding,ai,ai-agents,cli,mimo,mimo-code,typescript — alt: opencode
- `open-interpreter` [R|loc|E|?] — Agente de código para modelos abiertos como Kimi y GLM, pensado para correr con modelos locales o baratos. — tags: coding-agent,local,rust — prov: openai,local — alt: goose
- `open-swe` [R|cld|M|?] — Robin, fábrica de cambios sobre Deep Agents que despliega con Managed Deep Agents y entrega propuestas revisab — tags: coding-agent,agents,python — prov: anthropic,openai — alt: openhands
- `opencode` [R|hyb|E|+] — Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. — tags: coding-agent,agents,typescript — prov: openai,anthropic,google,local — alt: claude-code,codex,goose,gemini-cli,aider,mimo-code
- `opencode-manager` [A|hyb|M|?] — Interfaz autoalojada para gestionar sesiones de OpenCode, repositorios, terminal y tareas desde web o móvil. — tags: coding,agent,typescript — alt: t3code
- `opencursor` [A|hyb|M|?] — Extensión abierta de VS Code con chat de agente, búsqueda semántica, herramientas y conexión a varios modelos. — tags: coding,agent,ai,code,coder,cursor,extension,ide
- `openhands` [P|hyb|M|+] — Agent Canvas: centro de sesiones autoalojado para OpenHands, Claude Code, Codex y agentes ACP. — tags: agents,automation,typescript,docker — alt: open-swe
- `openidea` [A|loc|E|?] — Entorno de desarrollo con editor, depurador, Git y herramientas para trabajar con código en distintos lenguaje — tags: coding,app,typescript
- `t3code` [A|loc|E|?] — Interfaz para controlar desde web, móvil o escritorio los agentes de código que ya corren en tu máquina. — tags: coding-agent,ui,typescript — alt: opencode-manager

### 21. Asistentes e investigación con agentes (17)
Detalle: `REPO_MENU_cats/21-asistentes-e-investigaci-n-con-agentes.md`

- `agentes-chat` [A|hyb|M|?] — Espacio de trabajo autoalojado con canales, mensajes y agentes de IA que colaboran con personas y herramientas — tags: asistentes,agent,typescript
- `autoresearch` [P|hyb|M|+] — Experimento para iterar sobre entrenamiento de nanochat con un agente de código y una GPU NVIDIA. — tags: research,agents,python
- `deeptutor` [A|hyb|M|+] — Sistema de tutoría con agentes que personaliza el aprendizaje a partir de tus documentos. — tags: learning,agents,rag,python — prov: openai,local — alt: open-notebook
- `deer-flow` [P|hyb|M|+] — Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. — tags: automation,research,python,docker
- `gpt-researcher` [P|hyb|M|?] — Agente autónomo que investiga en línea y consolida reportes citados y estructurados. — tags: automation,research,python,docker — alt: storm,vane,local-deep-research
- `hello-halo` [A|hyb|E|?] — Asistente de escritorio con manejo de archivos, navegador y rutas de acceso con cuentas de IA o proveedores AP — tags: asistentes,agent,typescript
- `hermes-agent` [A|loc|M|?] — Asistente de Nous Research con memoria, skills y herramientas; usa proveedores remotos o endpoints locales con — tags: agents,python — alt: openclaw,mercury-agent
- `local-deep-research` [P|hyb|M|?] — Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes  — tags: research,academia,anthropic,arxiv,brave,deep-research,encryption,home-automation — alt: gpt-researcher
- `mercury-agent` [A|hyb|E|+] — Agente personal 24/7 con permisos estrictos, presupuesto de tokens y acceso por CLI, Telegram o web. — tags: agents,chatbot,typescript — alt: openclaw,hermes-agent
- `multica` [P|hyb|M|?] — Workspace para asignar y revisar trabajo de agentes de código mediante sus CLI y cuentas propias. — tags: agents,go — alt: paperclip
- `openbot` [A|hyb|H|?] — Espacio autoalojable de CopilotKit para compañeros de IA con navegador propio, permisos, aprobaciones y audito — tags: agents,computer-use,ag-ui,mcp,typescript — prov: openai,anthropic,google,local — alt: opendots
- `openclaw` [A|hyb|M|?] — Asistente personal de IA que corre en tus dispositivos y te atiende por WhatsApp, Telegram, Slack y más. — tags: agents,chatbot,typescript — prov: anthropic,openai,local — alt: hermes-agent,mercury-agent
- `opendots` [A|hyb|M|+] — Interfaz abierta de asistentes persistentes que requiere CopilotKit Intelligence, alojado, evaluado localmente — tags: asistentes,agent,typescript — alt: openbot
- `paperclip` [P|hyb|H|?] — Servidor y panel para organizar equipos de agentes con objetivos, tareas, presupuestos e historial de trabajo. — tags: asistentes,acpx,agent-orchestration,agent-skills,agentic-ai,ai-agents,ai-engineering,ai-governance — alt: multica
- `ruflo` [P|hyb|H|+] — Harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude — tags: automation,agents,typescript
- `social-media-agent` [R|cld|M|+] — Agente de LangChain que convierte enlaces en publicaciones para redes sociales con revisión humana antes de pu — tags: asistentes,typescript
- `storm` [R|hyb|M|+] — Sistema de Stanford que investiga un tema en la web y escribe un informe largo con citas, al estilo Wikipedia. — tags: research,agents,python — prov: openai — alt: gpt-researcher

### 22. Infraestructura, despliegue y herramientas para agentes (16)
Detalle: `REPO_MENU_cats/22-infraestructura-despliegue-y-herramientas-para-agentes.md`

- `agent-desktop` [A|loc|M|+] — CLI y biblioteca que permiten a un agente leer el árbol de accesibilidad y operar aplicaciones de escritorio. — tags: infra,accessibility,accessibility-api,ai-agents,automation,cli,computer-use,computer-use-agent
- `agent-protocol` [D|loc|E|?] — Especificación de LangChain para exponer cualquier agente con una API estándar de ejecuciones, hilos y estado. — tags: agents,python
- `casaos` [P|loc|H|?] — Entorno para administrar un servidor personal, instalar aplicaciones y organizar servicios y archivos doméstic — tags: infraestructura,server,go — alt: coolify
- `claude-task-master` [A|hyb|M|+] — Sistema de gestión de tareas con IA que prepara y organiza trabajo de desarrollo mediante CLI y servidor MCP. — tags: infra,agent,javascript — alt: spec-kit
- `composio` [P|cld|E|?] — Plataforma con más de 1000 integraciones con autenticación gestionada para que tus agentes actúen en apps real — tags: agents,mcp,automation,typescript — prov: openai,anthropic,mcp
- `computer-use-preview` [R|cld|M|+] — Implementación de referencia de Google para que Gemini vea la pantalla y opere interfaces web. — tags: browser,agents,python — prov: google — alt: browser-use,skyvern
- `coolify` [P|loc|H|?] — Plataforma autoalojada para desplegar aplicaciones, sitios, bases de datos y otros servicios en servidores pro — tags: infraestructura,server,php — alt: casaos
- `e2b` [P|cld|E|+] — Sandboxes en la nube, seguros y rápidos, para que tus agentes ejecuten código y usen herramientas. — tags: agents,security,python — alt: sandbox
- `free-for-dev` [D|cld|E|?] — Directorio de servicios de infraestructura y desarrollo que ofrecen planes o niveles gratuitos. — tags: recursos,awesome-list,free-for-developers,html
- `freedomain` [D|cld|E|?] — Recursos de registro de dominios y aprendizaje práctico de DNS publicados por DigitalPlat. — tags: recursos,digitalplat,dns,dns-tutorial,documentation,domain,domain-platform,domain-registration
- `masterdnsvpn` [A|hyb|M|?] — Implementación en Go de un túnel que transporta tráfico TCP mediante consultas y respuestas DNS. — tags: redes,dns,dns-client,dns-proxy,dns-server,dns-tunnel,dns-tunneling,dnstt
- `nemoclaw` [P|hyb|H|?] — Stack de referencia de NVIDIA para ejecutar agentes como OpenClaw o Hermes de forma más segura en sandboxes. — tags: agents,security,typescript — alt: sandbox
- `nodeterm` [A|loc|M|?] — Gestor visual de terminales y sesiones de agentes sobre un lienzo de nodos con organización por proyecto. — tags: infra,adhd,agent-orchestration,ai-agents,canvas,claude-code,codex,coding-agents
- `sandbox` [P|hyb|M|+] — Entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un m — tags: agents,automation,python,docker — alt: nemoclaw,e2b
- `shepherd` [L|loc|M|+] — Capa de ejecución que registra acciones y estado de un agente para permitir reproducir, bifurcar y revisar sus — tags: infra,framework,python
- `supabase` [P|loc|H|?] — Plataforma de desarrollo con PostgreSQL, autenticación, almacenamiento y otras funciones de backend para aplic — tags: infraestructura,server,typescript

### 23. Operar, evaluar y medir modelos de IA (19)
Detalle: `REPO_MENU_cats/23-operar-evaluar-y-medir-modelos-de-ia.md`

- `backdoor` [R|hyb|M|+] — Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. — tags: serving,ai,anthropic,claude,claude-code,deepseek,llm,ollama — alt: omniroute,claude-code-router,litellm
- `claude-code-router` [P|hyb|H|+] — Pasarela para configurar proveedores y modelos y enrutar el trabajo de agentes mediante un punto de control lo — tags: serving,server,typescript — alt: omniroute,backdoor,litellm
- `claude-code-usage-monitor` [A|loc|M|+] — Monitor de uso de Claude Code que presenta consumo, previsiones y avisos a partir de la información disponible — tags: observabilidad,app,python
- `deepeval` [L|hyb|E|+] — Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. — tags: evaluation,python — prov: openai — alt: ragas,promptfoo
- `guardrails` [L|hyb|M|+] — Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. — tags: security,chatbot,python
- `headroom` [L|hyb|E|+] — Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder  — tags: automation,llmops,python — alt: rtk
- `langfuse` [P|hyb|M|+] — Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llama — tags: automation,observability,typescript,docker — alt: phoenix,opik,mlflow
- `litellm` [L|hyb|E|+] — Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato d — tags: inference,llmops,python,docker — alt: omniroute,claude-code-router,backdoor
- `loguru` [L|loc|E|+] — Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin  — tags: observability,evaluation,python
- `mlflow` [P|loc|E|+] — Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. — tags: observability,training,evaluation,python — alt: langfuse
- `omniroute` [P|hyb|H|?] — Pasarela local para conectar proveedores de IA, enrutar solicitudes y gestionar cuotas y alternativas de acces — tags: serving,server,typescript — prov: local — alt: claude-code-router,backdoor,litellm
- `opik` [P|loc|M|+] — Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. — tags: observability,evaluation,python — alt: langfuse,phoenix
- `phoenix` [P|loc|E|+] — Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. — tags: observability,evaluation,python — alt: langfuse,opik
- `promptfoo` [A|loc|E|+] — CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. — tags: evaluation,security,typescript — prov: openai,anthropic,google,local — alt: deepeval,ragas,dspy
- `ragas` [L|hyb|E|+] — Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. — tags: evaluation,rag,python — prov: openai — alt: deepeval,promptfoo
- `rtk` [A|loc|E|+] — Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código — tags: tokens,agentic-coding,ai-coding,anthropic,claude-code,cli,command-line-tool,cost-reduction — alt: headroom
- `sglang` [R|loc|H|+] — Framework de servicio de alto rendimiento para LLM y modelos multimodales. — tags: inference,python — prov: local — alt: vllm
- `tensorrt-llm` [L|loc|H|?] — Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes esp — tags: serving,blackwell,cuda,llm-serving,moe,pytorch,python
- `vllm` [R|loc|H|+] — Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. — tags: inference,python — prov: local — alt: sglang

### 24. Modelos abiertos y entrenamiento (14)
Detalle: `REPO_MENU_cats/24-modelos-abiertos-y-entrenamiento.md`

- `bionemo-recipes` [D|loc|H|?] — Recetas y checkpoints de NVIDIA para entrenar y adaptar modelos fundacionales de biología a escala. — tags: entrenamiento,drug-discovery,gpu,machine-learning,pytorch,python
- `cosmos` [R|hyb|H|?] — Plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos — tags: inference
- `deepseek-v3` [R|hyb|H|?] — Modelo de lenguaje abierto de DeepSeek (671B parámetros, MoE) para chat, código y razonamiento; se usa por su  — tags: llm,inference,python
- `kimi-k2-7-code` [R|hyb|H|?] — Modelo de Moonshot AI orientado a programación y uso de herramientas; sus pesos oficiales se publican en Huggi — tags: kimi,moonshot,modelo,programacion,pesos-abiertos,huggingface — prov: local
- `laya` [R|loc|H|+] — Motor de decisiones que clasifica texto o selecciona opciones mediante modelos y resultados estructurados. — tags: modelos,model,python — prov: local
- `llama-factory` [A|loc|M|+] — Fine-tuning unificado de más de 100 LLM y modelos de visión con interfaz web sin código. — tags: training,python — prov: local — alt: unsloth
- `nemotron` [D|loc|H|?] — Centro de recursos de NVIDIA para la familia de modelos abiertos Nemotron: recetas, datasets y ejemplos. — tags: training,inference — prov: local
- `peft` [L|loc|M|+] — Librería de Hugging Face para fine-tuning eficiente de parámetros como LoRA. — tags: training,python
- `pytorch` [L|loc|M|?] — Framework de deep learning con tensores y redes neuronales dinámicas acelerados en GPU. — tags: training,python — alt: tensorflow
- `tensorflow` [L|loc|H|+] — Framework de aprendizaje automático para construir, entrenar y desplegar modelos mediante Python y otros entor — tags: entrenamiento,deep-learning,deep-neural-networks,distributed,machine-learning,ml,neural-network,python — alt: pytorch
- `timesfm` [L|loc|M|+] — Modelos preentrenados de Google para pronóstico de series temporales; las licencias de los pesos cambian por v — tags: data,analytics,python
- `transformers` [L|loc|E|+] — Librería de Hugging Face para usar y entrenar modelos de texto, visión y audio de última generación. — tags: training,inference,python
- `trl` [L|loc|M|+] — Librería de Hugging Face para entrenar LLM con aprendizaje por refuerzo: SFT, DPO, GRPO y más. — tags: training,python
- `unsloth` [A|loc|M|+] — App y herramientas para ejecutar y adaptar modelos localmente, con conexiones a agentes y proveedores opcional — tags: training,local,python — prov: local — alt: llama-factory

### 25. Procesar datos y trabajar con notebooks (12)
Detalle: `REPO_MENU_cats/25-procesar-datos-y-trabajar-con-notebooks.md`

- `apache-iceberg` [L|loc|M|?] — Formato abierto de tablas analíticas de la Apache Software Foundation; este repositorio es la implementación d — tags: data,lakehouse,table-format,java — alt: delta-lake,hudi
- `awesome-bigdata` [D|cld|E|?] — Directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para des — tags: data
- `dash` [L|loc|M|?] — Framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con compone — tags: automation,ui,python
- `delta-lake` [L|loc|M|?] — Capa de almacenamiento con transacciones ACID sobre Parquet para montar un lakehouse con Spark, Flink, Trino y — tags: data,lakehouse,table-format,scala — alt: apache-iceberg,hudi
- `duckdb` [L|loc|E|?] — Base de datos analítica en proceso, muy rápida, que consulta CSV, Parquet y JSON con SQL. — tags: data,analytics,cpp — alt: polars
- `globalbuildingatlas` [D|loc|H|?] — Dataset global y código de procesamiento de edificios con polígonos, alturas y modelos tridimensionales LoD1. — tags: datos,python
- `gradio` [L|loc|E|+] — Librería Python para crear y compartir apps web de modelos de ML en minutos. — tags: ui,python — alt: streamlit
- `hudi` [P|hyb|H|?] — Plataforma lakehouse de Apache para ingestión incremental y gestión de tablas sobre almacenamiento de datos. — tags: datos,apacheflink,apachehudi,apachespark,bigdata,data-integration,datalake,hudi — alt: apache-iceberg,delta-lake
- `jupyterlab` [A|loc|E|+] — Entorno web de Project Jupyter con notebooks, terminal, editor de texto y explorador de archivos, ampliable me — tags: notebooks,data,python,typescript — alt: marimo
- `marimo` [A|loc|E|+] — Notebook reactivo de Python que se guarda como script, se versiona en Git y se publica como app. — tags: notebooks,data,python — alt: jupyterlab
- `polars` [L|loc|E|+] — Motor de consultas y DataFrames en Rust con API Python para procesar datos tabulares. — tags: data,python,rust — alt: duckdb
- `streamlit` [L|loc|E|+] — Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin t — tags: ui,dataviz,python — alt: gradio

### 26. Animación, gráficos y creación 3D (19)
Detalle: `REPO_MENU_cats/26-animaci-n-gr-ficos-y-creaci-n-3d.md`

- `animejs` [L|loc|E|?] — Motor de animación JavaScript ligero para CSS, SVG, DOM y objetos. — tags: ui,design,javascript — alt: gsap,motion
- `awesome-cad` [D|loc|E|?] — Directorio de programas, bibliotecas y recursos de diseño asistido por computadora organizados por especialida — tags: creacion-3d,reference
- `blender` [A|loc|E|?] — Código de Blender, la aplicación para modelar, animar, renderizar y editar escenas y contenido tridimensional. — tags: creacion-3d,app,c
- `filament` [L|loc|M|?] — Motor de renderizado físicamente basado para integrar gráficos 3D en aplicaciones móviles, web y de escritorio — tags: creacion-3d,library,c
- `gsap` [L|loc|M|+] — Librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincro — tags: ui,design,javascript — alt: animejs
- `meshoptimizer` [L|loc|M|+] — Biblioteca para optimizar geometría y reducir el coste de almacenar y renderizar mallas tridimensionales. — tags: creacion-3d,library,c
- `motion` [L|loc|E|+] — Librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteraccio — tags: ui,design,typescript — alt: animejs
- `ozz-animation` [L|loc|M|?] — Biblioteca C++ y herramientas para preparar y reproducir animación esquelética dentro de motores y aplicacione — tags: creacion-3d,library,c
- `pencil` [A|loc|E|?] — Aplicación para crear animación 2D dibujada a mano mediante herramientas de dibujo y una línea de tiempo. — tags: edicion,app,c
- `pixelfx` [L|loc|M|?] — Colección de efectos de pixel art hechos con código y una skill para ayudar a generar efectos propios. — tags: animacion,library,javascript
- `planck-js` [L|loc|M|?] — Motor de física 2D para simular cuerpos, colisiones y uniones dentro de juegos o aplicaciones JavaScript. — tags: animacion,library,typescript
- `react-three-fiber` [L|loc|M|+] — Renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. — tags: ui,design,typescript
- `react-three-rapier` [L|loc|M|?] — Integración del motor de física Rapier con React Three Fiber para añadir simulación a escenas tridimensionales — tags: animacion,library,typescript
- `regl` [L|loc|M|+] — Biblioteca funcional para organizar comandos de renderizado WebGL y dibujar gráficos acelerados en una aplicac — tags: animacion,library,javascript
- `scenejs` [L|loc|M|+] — Biblioteca JavaScript para crear y controlar animaciones mediante líneas de tiempo y propiedades de elementos. — tags: animacion,library,typescript
- `three.js` [L|loc|M|?] — Biblioteca JavaScript para escenas 3D interactivas con renderizadores WebGL y WebGPU. — tags: ui,design,javascript
- `warp` [L|loc|H|+] — Framework de NVIDIA para kernels y simulación física en CPU o GPU; no es un modelo ni un terminal. — tags: entrenamiento,cuda,differentiable-programming,gpu,gpu-acceleration,nvidia,nvidia-warp,python
- `webgl-noise` [L|loc|M|?] — Rutinas de ruido procedural para shaders de WebGL, útiles para crear texturas y efectos visuales en tiempo rea — tags: animacion,library,c
- `zdog` [L|loc|M|?] — Motor de gráficos pseudo-3D que permite dibujar y animar ilustraciones sencillas mediante canvas o SVG. — tags: animacion,library,javascript

### 27. Skills de diseño, contenido y especialidades (36)
Detalle: `REPO_MENU_cats/27-skills-de-dise-o-contenido-y-especialidades.md`

- `3dviz-pro-max` [S|loc|M|?] — Skill para convertir ideas en escenas y visualizaciones 3D con Three.js o Blender desde un agente de código. — tags: skills,skill,javascript — alt: threejs-skills
- `agency-agents` [S|hyb|E|?] — Colección de más de 230 agentes especialistas (ingeniería, diseño, marketing, ventas, producto) para Claude Co — tags: agents,prompts,skills,coding-agent — alt: wshobson-agents
- `anatomy` [S|loc|M|+] — Skill para crear ilustraciones isométricas e interactivas de máquinas y sistemas con SVG y efectos visuales op — tags: skills,skill,javascript
- `arcads-claude-code` [S|cld|M|+] — Pack de skills para Claude Code y Cursor que crea anuncios en video e imagen con la API de Arcads (Seedance, S — tags: video,image,skills,python
- `blender-skills` [S|loc|M|+] — Skills para guiar a un agente por modelado y preparación de escenas en Blender mediante herramientas y conexio — tags: creacion-3d,skill,typescript
- `claude-seo` [S|loc|M|+] — Skills de Claude Code para revisar SEO técnico, contenido, presencia en buscadores de IA y otros aspectos de u — tags: dominio,skill,python — alt: geo-seo-claude
- `creative-architect` [S|hyb|E|+] — Plugin de dirección de arte para Claude Code: prepara fotos de producto, UGC y anuncios con proveedores de ima — tags: direccion-de-arte,fotos-producto,ugc,claude-code,creative-architect — prov: anthropic,openai
- `design-dna` [S|loc|M|+] — Skill para analizar referencias visuales, extraer decisiones de diseño y generar interfaces con un estilo cohe — tags: skills,skill,javascript
- `design.md` [L|cld|E|+] — Especificación y CLI para documentar identidad visual en DESIGN.md,validar tokens y comparar versiones. — tags: skills,design,typescript
- `dream-loop` [S|loc|M|?] — Skill que combina Blender, generación de imágenes y revisión por un agente para preparar visuales tridimension — tags: skills,skill,javascript
- `financial-services` [S|cld|M|+] — Plugins, skills y conectores de Anthropic para flujos de investigación y trabajo en servicios financieros. — tags: dominio,python — prov: anthropic
- `front-end-checklist` [D|loc|E|?] — Checklist y recursos para revisar aspectos de calidad de un frontend antes de entregarlo. — tags: skills,ai-agent,ai-agents,checklist,css,front-end-developer-tool,front-end-development,frontend
- `genjutsu` [S|loc|M|+] — Skills de diseño y animación para agentes que trabajan con interfaces web, Android y plataformas de Apple. — tags: skills,skill,python
- `geo-seo-claude` [S|cld|E|+] — Skill de Claude Code que audita webs para buscadores con IA (GEO) y SEO clásico, con citabilidad, schema, llms — tags: skills,search,pdf,python — prov: anthropic — alt: claude-seo
- `gsap-skills` [S|loc|M|+] — Skills oficiales con instrucciones y ejemplos para que agentes creen animaciones y utilicen plugins de GSAP. — tags: skills,skill,reference
- `hallmark` [S|loc|M|+] — Skill de diseño para agentes que ayuda a construir interfaces con decisiones visuales más específicas y cohere — tags: skills,skill,css — alt: ui-ux-pro-max-skill,taste-skill,impeccable
- `humanizer` [S|hyb|E|+] — Skill para revisar estilo y claridad de texto conservando su sentido; no prueba autoría humana. — tags: skills,prompts,docs — alt: stop-slop,no-ai-slop
- `i-have-adhd` [S|loc|M|?] — Skill para que un agente presente primero la respuesta y organice su salida con menos distracciones y rodeos. — tags: escritura,skill,python
- `impeccable` [S|cld|E|+] — Vocabulario y playbooks de diseño para agentes, con detector determinista y hooks según herramienta. — tags: skills,design,rust — alt: ui-ux-pro-max-skill,taste-skill,hallmark
- `instagram-agent-skill` [S|loc|M|+] — Skills de Claude para investigar ideas, preparar guiones y revisar contenido y publicaciones de una cuenta de  — tags: dominio,skill,python
- `linkedin-agent-skill` [S|loc|M|+] — Skills de Claude para preparar publicaciones, comentarios y planificación de contenidos de una cuenta de Linke — tags: dominio,skill,python
- `logo-design-skill` [S|loc|M|?] — Skill para diseñar logotipos con un agente, desde la idea y las referencias hasta SVG y comprobaciones de dise — tags: skills,skill,html
- `marketingskills` [S|hyb|E|+] — Colección de más de 50 skills de marketing (CRO, copy, SEO, ads, email, analítica, pricing) para Claude Code,  — tags: skills,analytics,email,search
- `minimalist-entrepreneur-skills` [S|loc|M|+] — Skills basadas en ideas de The Minimalist Entrepreneur para orientar trabajo de negocio y emprendimiento con u — tags: dominio,skill,reference
- `modern-web-guidance` [S|loc|M|+] — Herramienta y skill para que un agente consulte documentación actual sobre prácticas y APIs de desarrollo web. — tags: skills,skill,reference
- `motion-design-skill` [S|loc|M|+] — Skill con principios de ritmo, transiciones y composición del movimiento para diseñar animaciones de interface — tags: skills,skill,reference
- `no-ai-slop` [S|loc|M|+] — Skill para revisar escritura y eliminar patrones repetitivos o frases poco específicas en textos generados con — tags: escritura,skill,python — alt: humanizer,stop-slop
- `scientific-agent-skills` [S|loc|M|+] — Colección de skills y recursos para que agentes realicen tareas de investigación científica con herramientas d — tags: dominio,skill,python
- `skills-emil` [S|cld|E|+] — Colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrolla — tags: skills,design
- `social-media-research-skills` [S|cld|M|+] — Skills para investigar publicaciones, comentarios, competidores y anuncios en redes mediante ScrapeCreators. — tags: dominio,agent-skills,ai-agents,claude-code,claude-skills,competitor-analysis,content-marketing,cursor — tools: claude-code,codex — alt: last30days-skill
- `stitch-skills` [S|cld|E|?] — Colección de skills de agente para trabajar con el servidor MCP de Google Stitch. — tags: skills,design,ui
- `stop-slop` [S|hyb|E|?] — Skill con reglas para eliminar las señales de escritura IA: frases prohibidas, estructuras cliché y una rúbric — tags: skills,prompts,docs — alt: humanizer,no-ai-slop
- `taste-skill` [S|cld|E|+] — Skill design-taste-frontend para dirección visual y revisión de sitios; otros skills del pack antiguo se movie — tags: skills,design,javascript — alt: ui-ux-pro-max-skill,impeccable,hallmark
- `threejs-game-skills` [S|loc|M|+] — Skills para que un agente construya juegos de navegador con Three.js, interfaz y recursos visuales o sonoros o — tags: skills,skill,python
- `threejs-skills` [S|loc|M|+] — Colección de instrucciones para que agentes programen escenas y experiencias 3D en la web con Three.js. — tags: skills,skill,reference — alt: 3dviz-pro-max
- `ui-ux-pro-max-skill` [S|cld|E|+] — Conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para  — tags: skills,design,python — alt: taste-skill,impeccable,hallmark

### 28. Visión artificial, rostros y percepción (17)
Detalle: `REPO_MENU_cats/28-visi-n-artificial-rostros-y-percepci-n.md`

- `4d-humans` [R|loc|H|+] — Implementación de investigación para reconstruir y seguir personas en 3D a partir de imágenes o secuencias de  — tags: vision,model,python — prov: local
- `deep-live-cam` [R|loc|H|+] — Herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video. — tags: vision,image,python — alt: facefusion
- `easymocap` [R|loc|H|?] — Herramientas y ejemplos para capturar y reconstruir movimiento humano a partir de cámaras y secuencias de imág — tags: vision,model,python — prov: local
- `facefusion` [A|loc|M|?] — Plataforma para intercambio y mejora de rostros en imágenes y video. — tags: image,video,vision,python — alt: deep-live-cam
- `insightface` [L|loc|M|?] — Proyecto de análisis facial 2D y 3D: detección, reconocimiento y alineación. — tags: vision,image,python
- `kornia` [L|loc|M|+] — Biblioteca de visión por computador para incorporar geometría, transformaciones y procesamiento de imágenes en — tags: vision,library,python — prov: local
- `label-studio` [P|loc|E|+] — Herramienta de etiquetado de datos multi-tipo: imágenes, texto, audio y video. — tags: data,vision,training,docker
- `liveportrait` [R|loc|H|+] — Sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia — tags: image,vision,python
- `mediapipe` [L|loc|M|?] — Herramientas de aprendizaje automático para tareas de visión y procesamiento de medios en dispositivos y aplic — tags: vision,library,c — prov: local
- `mmpose` [R|loc|H|?] — Herramientas y modelos de estimación de pose, incluidos RTMPose y otras variantes para analizar movimiento hum — tags: vision,model,python — prov: local
- `opencv` [L|loc|E|?] — La librería de visión por computadora de referencia, con miles de algoritmos. — tags: vision,image,cpp,python
- `openpose` [R|loc|H|?] — Sistema de estimación de pose para detectar puntos del cuerpo, manos, rostro y pies en imágenes o video. — tags: vision,model,c — prov: local
- `sam3` [L|loc|H|+] — Tercera versión de Segment Anything de Meta: detecta, segmenta y sigue en imágenes y video todos los objetos q — tags: vision,video,python
- `supervision` [L|loc|E|+] — Herramientas reutilizables de Roboflow para visión: anotar, contar, rastrear y medir. — tags: vision,python
- `tfjs-models` [L|loc|H|?] — Colección de modelos preparados para TensorFlow.js que permite integrar tareas de aprendizaje automático en ap — tags: vision,library,typescript — prov: local
- `ultralytics` [L|loc|E|+] — Modelos YOLO para detección, segmentación, clasificación y pose, fáciles de entrenar y desplegar. — tags: vision,training,python
- `wham` [R|loc|H|?] — Implementación de investigación para reconstruir movimiento humano tridimensional a partir de secuencias de vi — tags: vision,model,python — prov: local

### 29. Audio, transcripción, voz y música (26)
Detalle: `REPO_MENU_cats/29-audio-transcripci-n-voz-y-m-sica.md`

- `ace-step-1.5` [P|loc|H|+] — Modelo y herramientas para generar música localmente a partir de instrucciones, con distintas variantes de tam — tags: musica,text2music,python
- `audiocraft` [L|loc|M|?] — Librería PyTorch de Meta para generar música y efectos de sonido desde texto, con MusicGen, AudioGen y el códe — tags: audio,inference,training,python — prov: local
- `cosyvoice` [L|loc|M|+] — Modelo de voz multilingüe del equipo Qwen con inferencia, entrenamiento y despliegue. — tags: tts,audio,python — prov: local — alt: fish-speech,index-tts
- `dograh` [A|hyb|M|?] — Plataforma para construir agentes de voz con flujos visuales, telefonía y proveedores de voz o modelos configu — tags: voz-agentes,agent,python — alt: pipecat,livekit-agents
- `earshot` [R|hyb|M|+] — Herramientas locales de audio para que un agente escuche, analice y revise sonidos mediante una interfaz MCP. — tags: edicion,mcp,python — prov: local
- `edge-tts` [L|cld|E|+] — Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. — tags: tts,speech-synthesis,text-to-speech,python — alt: kokoro
- `elevenlabs-python` [L|hyb|E|+] — SDK oficial de Python para la API de pago de ElevenLabs: voz sintética, clonación, transcripción, música y age — tags: tts,voice,api,python — prov: elevenlabs
- `faster-whisper` [R|loc|M|+] — Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. — tags: stt,audio,python — alt: whisper-cpp
- `fish-speech` [L|loc|M|?] — Herramientas y modelos de voz Fish Audio con licencias Community o Research según variante. — tags: tts,audio,python — prov: local — alt: cosyvoice,gpt-sovits
- `gpt-sovits` [A|loc|M|+] — Herramientas locales de TTS y adaptación de voz con pocos ejemplos; calidad y requisitos dependen del modelo y — tags: tts,audio,python — prov: local — alt: fish-speech
- `index-tts` [L|loc|M|+] — Sistema de TTS zero-shot de nivel industrial, controlable en duración y emoción. — tags: tts,audio,python — prov: local — alt: cosyvoice
- `kokoro` [L|loc|E|?] — Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles — tags: tts,audio,local — prov: local — alt: luxtts,edge-tts
- `livekit-agents` [R|hyb|M|+] — Framework para agentes de voz y video en tiempo real sobre la infraestructura WebRTC de LiveKit. — tags: audio,agents,video,python — prov: openai,anthropic,google — alt: pipecat,dograh
- `luxtts` [L|loc|E|+] — Modelo de texto a voz con herramientas para sintetizar y adaptar voces en una instalación local. — tags: tts,audio,python — prov: local — alt: kokoro
- `nemo` [L|loc|H|+] — Framework actual de NVIDIA para reconocimiento,síntesis y modelos de voz con recetas de inferencia y entrenami — tags: stt,tts,audio,python — alt: whisperx
- `omnivoice-studio` [A|loc|M|?] — App local de voz con modelos descargables,edición AGPL y una oferta comercial separada. — tags: tts,audio,python — alt: videolingo
- `pipecat` [R|hyb|M|+] — Framework open source para agentes de voz y apps multimodales en tiempo real. — tags: audio,agents,stt,tts,python — prov: openai,anthropic,google — alt: livekit-agents,dograh
- `pyannote-audio` [L|hyb|M|+] — Kit de PyTorch para diarización de hablantes (quién habla y cuándo) con modelos preentrenados y un servicio pr — tags: audio,diarization,pytorch,python — prov: local
- `rnnoise` [R|loc|M|?] — Biblioteca de reducción de ruido de audio que utiliza una red neuronal para mejorar señales de voz localmente. — tags: edicion,model,c — prov: local
- `rubberband` [L|loc|M|?] — Biblioteca de audio para modificar duración y tono de una grabación, integrada como código en otras herramient — tags: edicion,library,c
- `rvc` [A|loc|M|+] — Interfaz y herramientas para convertir una grabación a otra voz mediante modelos locales. — tags: audio,tts,python — prov: local
- `vibevoice` [L|loc|H|?] — Familia de modelos de voz de Microsoft con herramientas para generación y procesamiento de audio. — tags: tts,audio,python — prov: local
- `voxcpm` [R|loc|H|+] — VoxCPM2: modelos y herramientas locales de TTS multilingüe,diseño y adaptación de voz. — tags: tts,audio,python
- `whisper` [R|loc|M|+] — Modelo de OpenAI para convertir habla en texto y traducir audio, con ejecución en tu equipo. — tags: stt,audio,python — alt: whisper-cpp
- `whisper-cpp` [R|loc|E|+] — Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. — tags: stt,audio,local,cpp — prov: local — alt: faster-whisper,whisper
- `whisperx` [R|loc|M|+] — Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. — tags: stt,audio,python — alt: nemo

### 30. Video con código y agentes creativos (21)
Detalle: `REPO_MENU_cats/30-video-con-c-digo-y-agentes-creativos.md`

- `brag` [S|loc|M|+] — Skills para que un agente convierta un proyecto o sitio en un video breve de lanzamiento con composición y mús — tags: programatico,skill,python
- `claude-animated-shorts` [S|loc|M|?] — Skill de Claude para crear cortos animados por código combinando personajes y escenas con Three.js y Remotion. — tags: programatico,skill,typescript
- `huashu-motion` [S|loc|M|+] — Skill para crear videos de presentación de productos con un agente de código, composición, música y revisión v — tags: programatico,skill,javascript
- `hyperframes` [R|loc|E|+] — Framework de HeyGen que convierte HTML, CSS y animaciones en videos MP4 deterministas, pensado para que lo use — tags: video,agents,skills,typescript — prov: mcp — alt: remotion,moviepy
- `lemo-opuscar` [S|loc|M|+] — Biblioteca de estilos para video por código orientada a Claude,con licencias diferentes para código,guías y me — tags: programatico,skill,javascript
- `manim` [L|loc|M|+] — Motor de animación en Python para videos matemáticos explicativos, creado por 3Blue1Brown, con render en OpenG — tags: video,dataviz,learning,python — alt: manim-community
- `manim-community` [L|loc|M|?] — Motor de animación de Python para producir videos explicativos de matemáticas mediante escenas programadas. — tags: programatico,animations,hacktoberfest,manim,math,python — alt: manim
- `mediabunny` [L|loc|M|+] — Biblioteca TypeScript para leer, escribir y convertir archivos de audio y video directamente en aplicaciones w — tags: edicion,library,typescript
- `motionmaxxing` [S|loc|M|+] — Skill para mejorar composición, ritmo y movimiento de videos creados con agentes y herramientas de código. — tags: programatico,skill,javascript
- `moviepy` [L|loc|E|?] — Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efecto — tags: video,audio,automation,python — alt: remotion,hyperframes
- `openfilm` [S|loc|M|+] — Herramientas y skill para que un agente cree proyectos de video y permita editar después sus elementos. — tags: programatico,skill,typescript
- `openmontage` [S|loc|M|+] — Pipelines y herramientas para producir video con un agente,recursos propios,modelos locales o servicios opcion — tags: video,coding-agent,skills — alt: remotion-superpowers,moneyprinterturbo
- `papermorph` [S|loc|M|+] — Skill que convierte libros en experiencias web animadas y narradas, con distintas rutas de voz y recursos visu — tags: programatico,skill,javascript
- `rea-video` [S|hyb|M|?] — Herramienta y skills para descomponer un video plano por plano y documentar cómo recrearlo en un archivo VIDEO — tags: programatico,agent-skills,ai-video,aigc-detection,claude-code,codex,ffmpeg,prompt-engineering
- `remotion` [L|loc|M|+] — Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. — tags: video,typescript — alt: moviepy,hyperframes
- `remotion-superpowers` [S|loc|E|+] — Orquestación de video con Remotion y servicios audiovisuales externos; requiere claves y revisar costes por et — tags: video,skills,coding-agent — alt: openmontage,video-use
- `skills-remotion` [S|loc|E|+] — Skills oficiales de Remotion para que tu agente de código cree videos con React. — tags: video,skills
- `srt-whiteboard-animation` [S|loc|M|?] — Skill para crear animaciones de pizarra con trazos y contenido organizados a partir de archivos de subtítulos  — tags: programatico,skill,python
- `video-shotcraft` [S|loc|M|+] — Skill para crear videos de producto editables con Remotion, composición de planos, movimiento y trabajo de son — tags: programatico,skill,typescript
- `video-use` [S|loc|E|?] — Edición con agentes y FFmpeg,con transcripción documentada mediante ElevenLabs Scribe. — tags: video,coding-agent,skills,python — alt: remotion-superpowers
- `videofy-minimal` [A|loc|E|+] — Aplicación local que transforma artículos de noticias en videos breves mediante guion, voz y un flujo de revis — tags: video,typescript — alt: moneyprinterturbo

### 31. Presentaciones, diagramas y explicación visual (8)
Detalle: `REPO_MENU_cats/31-presentaciones-diagramas-y-explicaci-n-visual.md`

- `archify` [S|loc|E|?] — Skill para convertir ideas, planes y bases de código en diagramas y visualizaciones HTML interactivas. — tags: diagramas,agent-skills,ai-agents,architecture-diagram,claude-code,claude-skills,codex,coding-agents — tools: claude-code,codex — alt: diagram-design
- `diagram-design` [S|loc|M|+] — Skill para que un agente cree diagramas explicativos con HTML y SVG, con criterios de composición y legibilida — tags: diagramas,skill,html — alt: archify
- `marp` [D|loc|E|?] — Entrada al ecosistema Marp de presentaciones Markdown; el CLI y extensión de editor se distribuyen por separad — tags: slides,typescript — alt: slidev,reveal.js
- `mermaid` [L|loc|E|?] — Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. — tags: docs,dataviz,typescript — alt: excalidraw
- `ppt-master` [S|hyb|E|?] — Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documento — tags: slides,python — alt: presenton
- `presenton` [A|hyb|E|+] — Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. — tags: slides,agents,typescript — prov: openai,google,local — alt: ppt-master
- `reveal.js` [L|loc|E|?] — Framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orad — tags: slides,javascript — alt: slidev,marp
- `slidev` [A|loc|E|+] — Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. — tags: slides,typescript — alt: marp,reveal.js

### 32. Navegadores y automatización web (11)
Detalle: `REPO_MENU_cats/32-navegadores-y-automatizaci-n-web.md`

- `agent-browser` [A|loc|E|+] — CLI de navegador de Vercel que entrega árboles de accesibilidad y referencias de elementos para agentes. — tags: navegador,rust — alt: playwright-cli
- `awesome-chrome-devtools` [D|loc|E|?] — Directorio de herramientas, clientes y recursos del ecosistema de Chrome DevTools y Chrome DevTools Protocol. — tags: navegador,awesome,awesome-list
- `browser-harness` [R|loc|E|?] — Arnés mínimo para que Claude Code, Codex o Cursor usen tu Chrome real con tu sesión iniciada. — tags: browser,coding-agent,python — alt: playwright-mcp,chrome-devtools-mcp,browser-use
- `browser-use` [L|hyb|M|?] — Librería Python para que los LLM usen un navegador real y actúen en páginas sin selectores fijos. — tags: automation,browser,python — alt: computer-use-preview,stagehand,skyvern,playwright-mcp,browser-harness
- `lightpanda` [R|loc|E|?] — Navegador headless escrito en Zig para IA y automatización, mucho más ligero que Chrome. — tags: browser,scraping
- `playwright` [L|hyb|M|+] — Framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola A — tags: automation,browser,typescript — alt: puppeteer,selenium
- `playwright-cli` [S|hyb|E|+] — Interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador  — tags: browser,typescript — alt: agent-browser
- `puppeteer` [L|loc|E|+] — Librería de Google para controlar Chrome y Firefox desde Node.js. — tags: browser,scraping,typescript — alt: playwright,selenium
- `selenium` [L|loc|M|?] — Framework veterano de automatización de navegadores con soporte para casi todos los lenguajes. — tags: browser,java,python — alt: playwright,puppeteer
- `skyvern` [P|hyb|M|+] — Automatiza flujos en el navegador con LLM y visión, sin selectores frágiles. — tags: browser,automation,python — prov: openai,anthropic — alt: browser-use,stagehand,computer-use-preview
- `stagehand` [L|hyb|E|+] — SDK de Browserbase para automatizar el navegador mezclando código con acciones en lenguaje natural. — tags: browser,agents,typescript — prov: openai,anthropic — alt: browser-use,skyvern

---

## Cómo interpretar la instalación

- Usa la entrada seleccionada del README o la guía original de cada ficha; no deduzcas paquetes por el nombre del repo.
- Un bloque puede ser un comando de terminal, configuración, código o una instrucción dentro del agente: conserva su contexto.
- Para skills y MCP sigue el método documentado para tu cliente; no copies la misma configuración a todos los agentes.
- Revisa cuenta, API, servicios, licencia y modelos locales como decisiones separadas.
- Marca `?` → revisa la instalación original; clonar no equivale a instalar.

> La revisión es documental. Ni el comando ni la primera prueba se ejecutaron en los proyectos de terceros.
