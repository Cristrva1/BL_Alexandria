
### 🎨 ui-ux-pro-max-skill
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** conjunto de skills que dotan al asistente de código de inteligencia de diseño UI/UX y estilos avanzados, para que las interfaces que genera dejen de verse a "plantilla". Resuelve el punto débil habitual del código asistido por IA: la jerarquía visual y el acabado.
**Por qué destaca:** aporta criterio de layout, tipografía y composición además de código, algo que los LLMs por sí solos no manejan bien. Se integra con asistentes populares (Claude Code, Codex, Cursor) vía una CLI propia y skills copiables.
**Cómo funciona:** las skills inyectan guías de diseño (espaciado, jerarquía, motion) en el contexto del asistente, y la CLI `uipro-cli` (Node) orquesta la aplicación de esos criterios sobre el código generado, con reglas concretas para Tailwind/CSS.
**Instalación:** clona el repo y sigue su README; instala la CLI vía Node (`npx` o instalación local) y copia las skills al directorio de skills de tu asistente. Requiere Node.js y un asistente compatible con skills.
**Casos:** mejorar layouts y jerarquía visual de UIs generadas por IA · acabado profesional con Tailwind/CSS · iterar diseño sin handoff manual con un diseñador.
**Stack:** Node.js (uipro-cli), TypeScript/React — **Modelo/API:** agnóstico; funciona con cualquier asistente que cargue skills (Claude Code, Codex, Cursor).
**Elige si:** generas UI con IA y el resultado se ve genérico o despulido — **Evita si:** no trabajas frontend o ya tienes un sistema de diseño impuesto.
**Combina con:** [taste-skill](#-taste-skill) · [impeccable](#-impeccable) · [tailwindcss](#-tailwindcss)
**Repo:** [GitHub](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)

### 🍷 taste-skill
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skills "anti-slop" para producir frontends premium (layout, tipografía, motion y espaciado) más skills de generación de imagen para crear mood boards de referencia. Ataca el acabado "de plantilla" que delata a las UIs generadas por IA.
**Por qué destaca:** aporta criterio de diseño además de código, y opcionalmente genera boards visuales (web, mobile, brand) para anclar el estilo antes de programar. Es portable entre asistentes (Codex, Cursor, Claude Code) y de foco estético.
**Cómo funciona:** las skills inyectan guías de gusto visual en el contexto del asistente y, cuando se activan las de imagen, llaman a un generador (ChatGPT Images u otro) para producir boards de referencia que el modelo usa como guía.
**Instalación:** clona el repo y copia las skills a tu directorio de skills (Codex, Cursor o Claude Code); las de imagen requieren un generador disponible y su correspondiente acceso/API.
**Casos:** subir el gusto de UIs construidas por IA · boards de referencia (web/mobile/brand) antes de codificar · alinear estética entre diseñador y agente.
**Stack:** Markdown/skills — **Modelo/API:** Codex, Cursor, Claude Code; las skills de imagen usan generadores como ChatGPT Images.
**Elige si:** quieres frontends con gusto y no te basta con UI funcional — **Evita si:** ya tienes un design system cerrado o no usas generadores de imagen.
**Combina con:** [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill) · [impeccable](#-impeccable)
**Repo:** [GitHub](https://github.com/Leonxlnx/taste-skill)

### ✏️ skills_emil
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering). Resuelve el handoff diseño↔código, no solo la estética final.
**Por qué destaca:** pone el foco en la traducción de diseño a implementación (tokens, consistencia, decisiones compartidas), un ángulo menos cubierto por otras skills de UI que miran solo el resultado visual.
**Cómo funciona:** se entrega como un `SKILL.md` (skill `emil-design-eng`) que el asistente carga para guiar decisiones de diseño-implementación: estructura de componentes, naming, tokens y patrones coherentes entre Figma y código.
**Instalación:** copia el `SKILL.md` al directorio de skills de tu asistente (Claude Code, Codex, Cursor); es referencia local del autor, así que consulta la fuente original para la versión más reciente.
**Casos:** mejorar el handoff diseño↔ingeniería · resultados UI más consistentes entre Figma y código · alinear naming y tokens en un equipo.
**Stack:** Markdown (skills), TypeScript/React — **Modelo/API:** agnóstico; cualquier asistente que cargue skills.
**Elige si:** trabajas diseño+dev en equipo y sufres el handoff — **Evita si:** buscas componentes listos o trabajas solo.
**Combina con:** [design.md](#-designmd) · [ui-ux-pro-max-skill](#-ui-ux-pro-max-skill)
**Repo:** [GitHub](https://github.com/emilkowalski/skills/blob/main/skills/emil-design-eng/SKILL.md)

### 🛡️ SkillSpector
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** herramienta para auditar la seguridad de skills de agentes y detectar patrones potencialmente riesgosos (comandos peligrosos, exfiltración, prompts ocultos) antes de instalarlas. Resuelve el riesgo de ejecutar skills de terceros sin revisión.
**Por qué destaca:** aporta una capa de seguridad muy necesaria sobre catálogos enormes de skills de terceros, y proviene de NVIDIA, lo que le da respaldo institucional. Es agnóstica al asistente, así que sirve para skills de Claude Code, Codex, Cursor, etc.
**Cómo funciona:** analiza los archivos de la skill en busca de comandos shell peligrosos, llamadas de red sospechosas o instrucciones ocultas, y reporta los hallazgos en un resumen accionable sin ejecutar nada.
**Instalación:** clona el repo e instala sus dependencias (Python/Node) según el README; ejecútalo apuntando al directorio de skills que quieras auditar. Requiere Python y/o Node según el modo de escaneo.
**Casos:** auditar skills de terceros antes de instalarlas · detectar comandos peligrosos o exfiltración · revisar catálogos descargados en lote.
**Stack:** Python/Node, Docker — **Modelo/API:** agnóstico; no invoca LLMs, solo analiza archivos.
**Elige si:** instalas skills externas o curas catálogos — **Evita si:** solo usas skills propias de confianza.
**Combina con:** [antigravity-awesome-skills](#-antigravity-awesome-skills)
**Repo:** [GitHub](https://github.com/NVIDIA/SkillSpector)

### 🧑 humanizer
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill para Claude Code y OpenCode que elimina las señales típicas ("tells") de la escritura generada por IA para que el texto suene más natural. Resuelve el problema de publicar prosa que delata su origen de modelo.
**Por qué destaca:** es simple y de foco único, lo que la hace efectiva y fácil de adoptar para pulir prosa sin reescribir todo el flujo. Funciona como una capa de post-procesado de estilo sobre cualquier salida de LLM.
**Cómo funciona:** aplica reglas de reescritura sobre el texto del LLM para quitar muletillas, cadencias predecibles y patrones reconocibles de IA, devolviendo una versión más cercana al lenguaje humano.
**Instalación:** clona el repo y copia el `SKILL.md` al directorio de skills de Claude Code u OpenCode. Requiere uno de esos asistentes (o cualquier runtime que cargue skills).
**Casos:** redactar correos/posts que no suenen a IA · pulir borradores de LLM antes de publicar · humanizar respuestas de customer support.
**Stack:** Markdown/skill — **Modelo/API:** Claude Code, OpenCode; agnóstico al proveedor subyacente del LLM.
**Elige si:** publicas prosa generada por IA y quieres evitar el "tono IA" — **Evita si:** escribes a mano o el registro formal no es problema.
**Combina con:** [stop-slop](#-stop-slop)
**Repo:** [GitHub](https://github.com/blader/humanizer)

### 🧹 stop-slop
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🎨 skill/prompt · Setup 🟢 fácil
**Qué es:** skill que enseña al modelo a eliminar patrones y "tells" de la prosa generada por IA, mejorando ritmo y estilo. Resuelve el "slop": frases formulaicas, listas redundantes y cadencias reconocibles que delatan al LLM.
**Por qué destaca:** aporta reglas concretas y accionables contra el slop, útiles con cualquier LLM y no atadas a un asistente concreto. Es complementaria a [humanizer](#-humanizer), aunque ambas solapan en parte.
**Cómo funciona:** define instrucciones de estilo que el asistente aplica al reescribir, evitando frases y cadencias predecibles (aperturas tópicas, transiciones de relleno, enumeraciones automáticas).
**Instalación:** clona el repo y copia el `SKILL.md` al directorio de skills de tu asistente, o úsalo como instrucción de estilo pegada en el system prompt. No requiere dependencias más allá del propio asistente.
**Casos:** limpiar frases y ritmos predecibles · mejorar estilo del LLM en posts y correos · pulir documentación generada por IA.
**Stack:** Markdown/skill — **Modelo/API:** cualquier LLM; agnóstico al proveedor.
**Elige si:** quieres prosa más natural y te molesta el tono IA — **Evita si:** ya usas [humanizer](#-humanizer) (solapan) o escribes a mano.
**Combina con:** [humanizer](#-humanizer)
**Repo:** [GitHub](https://github.com/hardikpandya/stop-slop)

---

## 3. Frameworks & Orquestación de Agentes

Plataformas para construir sistemas multiagente, research autónomo y flujos low-code de IA.

### 🔍 Escaneo rápido

| Repo | Qué es | Ejec. | Setup | Elige si… |
|---|---|---|---|---|
| [ag2](#-ag2) | Framework multiagente maduro (heredero de AutoGen) | ☁️ | 🟡 | Construyes sistemas multiagente en prod |
| [crewAI](#-crewai) | Equipos de agentes con roles y tareas | ☁️ | 🟢 | Quieres avanzar rápido con "crews" |
| [langchain](#-langchain) | Framework base de apps LLM (Python/JS) | ☁️ | 🟡 | Necesitas el estándar de orquestación |
| [langflow](#-langflow) | Constructor visual de flujos LLM sobre LangChain | 🔀 | 🟡 | Prefieres iterar componentes en visual |
| [dify](#-dify) | Plataforma integral de apps IA (backend+UI) | 🔀 | 🟡 | Quieres backend+UI listos para apps |
| [Flowise](#-flowise) | Builder visual drag-and-drop de pipelines LLM | 🔀 | 🟢 | Prototipas pipelines sin código |
| [OpenHands](#-openhands) | Agentes que ejecutan en entornos dev sandbox | 🔀 | 🟡 | Quieres un agente que programe/ejecute |
| [deer-flow](#-deer-flow) | Super-agente con sub-agentes y sandbox (ByteDance) | 🔀 | 🟡 | Buscas orquestación potente extensible |
| [NeMo-Agent-Toolkit](#-nemo-agent-toolkit) | Toolkit de agentes de NVIDIA (NIM) | 🔀 | 🔴 | Estás en stack NVIDIA/empresa |
| [hermes-agent](#-hermes-agent) | Entorno desktop/CLI de agentes locales (Nous) | 🏠 | 🟡 | Ejecutas agentes locales con razonamiento |
| [openevolve](#-openevolve) | Agente de código evolutivo (estilo AlphaEvolve) | ☁️ | 🔴 | Optimizas algoritmos por evolución |
| [gpt-researcher](#-gpt-researcher) | Agente de research autónomo con citas | 🔀 | 🟡 | Necesitas reportes citados profundos |
| [autoresearch](#-autoresearch) | Research iterativo experimental (Karpathy) | 🔀 | 🟡 | Exploras automatización de investigación |
| [deer-flow](#-deer-flow) | (ver arriba) | 🔀 | 🟡 | — |
| [ruflo](#-ruflo) | Swarm multiagente (Rust) para Claude/Codex | 🔀 | 🔴 | Coordinas 100+ agentes con memoria |
| [multica](#-multica) | Plataforma humanos+agentes lado a lado | 🔀 | 🟡 | Mezclas equipo humano y agentes |
| [MiroFish](#-mirofish) | Motor de predicción multiagente (simulación) | 🔀 | 🔴 | Simulas escenarios/futuros con agentes |
| [llm-council](#-llm-council) | "Consejo" de varios LLMs deliberando | 🔀 | 🟡 | Quieres respuestas por consenso multi-modelo |
| [awesome-LangGraph](#-awesome-langgraph) | Recursos curados del ecosistema LangGraph | 📂 | 🟢 | Construyes grafos cíclicos de agentes |

### ⚖️ ¿Cuál elegir? — Frameworks de agentes

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **langchain** | Base general de apps LLM y RAG | Ecosistema enorme, estándar de facto, Python+JS | Quieres algo ligero sin abstracción o solo un agente simple |
| **ag2** | Multiagente colaborativo serio en prod | Patrones de colaboración maduros (heredero de AutoGen) | Solo necesitas un agente único o control fino de bajo nivel |
| **crewAI** | Equipos con roles y tareas, prototipo rápido | DX ágil para "crews", curva suave | Necesitas control de bajo nivel o orquestación muy custom |
| **OpenHands** | Agente que codifica y ejecuta en sandbox | Acciones reales (edita código, corre comandos, navega) | Solo quieres chat/RAG o no puedes correr Docker |
| **deer-flow** | Orquestación con sub-agentes y sandbox | Super-agente extensible por skills, respaldo ByteDance | Buscas algo minimalista o sin Docker |

### ⚖️ ¿Cuál elegir? — Low-code / visual de IA

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **dify** | App IA completa (backend+UI+RAG+agentes) | Plataforma integral autoalojable lista para prod | Solo necesitas una librería o un prototipo puntual |
| **langflow** | Iterar componentes de agente en visual | Lienzo sobre LangChain, exporta a API/código | Quieres todo en código o no usas LangChain |
| **Flowise** | Prototipo rápido de pipeline drag-and-drop | Sencillo, basado en LangChain.js, widget embebible | Necesitas plataforma completa con RAG/observabilidad ([dify](#-dify)) |

### 🤝 ag2
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework maduro para sistemas multiagente con patrones de colaboración (heredero directo de AutoGen). Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.
**Por qué destaca:** uno de los frameworks multiagente de referencia, con amplia adopción y comunidad activa heredada de AutoGen. Es totalmente open-source y aporta patrones de conversación (secuencial, anidado, grupo) ya probados en producción.
**Cómo funciona:** define agentes conversacionales (asistente, ejecutor de código, usuario) que intercambian mensajes según patrones predefinidos; corre sobre Python y se conecta a APIs de LLM vía variables de entorno.
**Instalación:** `pip install ag2` (o `pyautogen` para el nombre legacy). Requiere una clave de API de LLM (OpenAI, Anthropic u otro) configurada por entorno.
**Casos:** equipos de agentes que se reparten tareas · flujos de decisión estructurados · agentes que escriben y ejecutan código en bucle.
**Stack:** Python — **Modelo/API:** OpenAI, Anthropic, Gemini, locales (Ollama); agnóstico vía variables de entorno.
**Elige si:** construyes multiagente serio en Python — **Evita si:** te basta un agente único o quieres orquestación visual.
**Combina con:** [langchain](#-langchain) · [langfuse](#-langfuse)
**Repo:** [GitHub](https://github.com/ag2ai/ag2)

### 👥 crewAI
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.
**Por qué destaca:** muy popular por su curva de aprendizaje suave; es de las formas más rápidas de montar un equipo de agentes funcional. Es independiente de LangChain y aporta un modelo mental claro (agentes, tareas, crew) que se lee casi como prosa.
**Cómo funciona:** declaras agentes (rol, meta, herramientas) y tareas, y CrewAI orquesta su ejecución secuencial o jerárquica; está escrito en Python y delega el LLM al proveedor que configures.
**Instalación:** `pip install crewai` (o `crewai[tools]` para el set de herramientas integradas). Requiere una clave de API de LLM por entorno.
**Casos:** avanzar rápido en flujos de agentes · prototipos colaborativos · pipelines de research/redacción repartidos por rol.
**Stack:** Python — **Modelo/API:** OpenAI, Anthropic, Gemini, locales; agnóstico vía variables de entorno.
**Elige si:** quieres velocidad y un modelo mental simple de "equipo" — **Evita si:** necesitas control de bajo nivel o orquestación muy custom.
**Combina con:** [langchain](#-langchain) · [mem0](#-mem0)
**Repo:** [GitHub](https://github.com/crewAIInc/crewAI)

### 🦜 langchain
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.
**Por qué destaca:** estándar de facto del ecosistema LLM, con la comunidad e integraciones más grandes del sector. Su valor está en future-proofing: cambiar de modelo o vector store suele ser mover un parámetro, no reescribir código.
**Cómo funciona:** encadena componentes (prompts, modelos, retrievers, tools) en pipelines o agentes; disponible en Python y JS/TS, con LangGraph para grafos cíclicos con estado.
**Instalación:** `pip install langchain` o `npm install langchain`. Requiere la clave del proveedor de LLM que vayas a usar (OpenAI, Anthropic, etc.).
**Casos:** orquestar LLM + herramientas + memoria · base de casi cualquier app de IA · RAG sobre documentos propios.
**Stack:** Python/JS/TS — **Modelo/API:** prácticamente todos (OpenAI, Anthropic, Google, locales vía Ollama).
**Elige si:** quieres la base estándar con máximas integraciones — **Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar.
**Combina con:** [langflow](#-langflow) · [langfuse](#-langfuse) · [litellm](#-litellm)
**Repo:** [GitHub](https://github.com/langchain-ai/langchain)

### 🔗 langflow
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.
**Por qué destaca:** une la potencia del ecosistema LangChain con una interfaz visual, muy valorado para prototipar sin escribir todo el código. Al generar LangChain real por debajo, lo que construyes en visual es portable a código.
**Cómo funciona:** cada nodo del lienzo envuelve un componente LangChain (LLM, retriever, tool, prompt); el flujo se ejecuta como un grafo y se expone vía API. Corre sobre Python con frontend web (React).
**Instalación:** `pip install langflow` o vía Docker. Requiere un proveedor de LLM configurado por entorno para los componentes que lo usen.
**Casos:** iterar componentes de agente sin código · prototipar pipelines RAG · enseñar LangChain a perfiles no técnicos.
**Stack:** Python, React, Docker — **Modelo/API:** múltiples; agnóstico vía LangChain.
**Elige si:** prefieres construir en visual sobre LangChain — **Evita si:** quieres todo en código o no usas LangChain.
**Combina con:** [langchain](#-langchain) · [dify](#-dify)
**Repo:** [GitHub](https://github.com/langflow-ai/langflow)

### 🧱 dify
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.
**Por qué destaca:** todo-en-uno muy popular para llevar apps de IA a producción sin ensamblar piezas sueltas. Cubre desde el chatbot con RAG hasta workflows visuales y agentes, con gestión de usuarios y API propia.
**Cómo funciona:** define apps (chatbot, agente, workflow) desde un panel web; el backend en Python orquesta modelos y herramientas sobre PostgreSQL/Redis, y se despliega con Docker Compose.
**Instalación:** `docker compose up` desde el repo (o cloud gestionado de Dify). Requiere Docker y al menos una clave de proveedor de LLM.
**Casos:** desplegar un chatbot/asistente con RAG · apps IA para clientes · workflows visuales con herramientas propias.
**Stack:** Python/TS, React, PostgreSQL, Redis, Docker — **Modelo/API:** OpenAI, Anthropic, Google, locales; agnóstico vía variables de entorno.
**Elige si:** quieres una app IA completa autoalojada — **Evita si:** solo necesitas una librería o un prototipo puntual.
**Combina con:** [langflow](#-langflow) · [Flowise](#-flowise)
**Repo:** [GitHub](https://github.com/langgenius/dify)

### 🌊 Flowise
**Etiquetas:** Ejecución 🔀 híbrido · Rol 🖥️ app/UI · Setup 🟢 fácil
**Qué es:** builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible.
**Por qué destaca:** muy adoptado para prototipar flujos LLM en minutos sin escribir código. Al estar basado en LangChain.js, hereda sus conectores y se instala con un solo comando de npm.
**Cómo funciona:** cada nodo encapsula un componente (LLM, retriever, tool, memoria); el grafo se ejecuta en un backend Node.js y se sirve por API o widget. Persiste credenciales y conversaciones en SQLite/PostgreSQL.
**Instalación:** `npm install -g flowise && npx flowise start` o vía Docker. Requiere Node.js y las claves de los proveedores de LLM que uses.
**Casos:** prototipar un flujo LLM rápido · demos sin código · widget de chat embebible en una web.
**Stack:** Node.js/TypeScript, React — **Modelo/API:** múltiples; agnóstico vía LangChain.js.
**Elige si:** quieres un prototipo visual ya, en stack JS — **Evita si:** necesitas plataforma completa con RAG/observabilidad ([dify](#-dify)).
**Combina con:** [dify](#-dify) · [langflow](#-langflow)
**Repo:** [GitHub](https://github.com/FlowiseAI/Flowise)

### 🙌 OpenHands
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox.
**Por qué destaca:** uno de los proyectos open-source de agentes de programación más populares, con foco en acciones reales en lugar de solo respuestas. Soporta varios runtimes (local, remoto, cloud) y agentes compatibles con ACP.
**Cómo funciona:** un bucle agente-acción-observación ejecuta tareas dentro de un contenedor Docker aislado; backend en Python con UI web, y el agente opera sobre el filesystem, shell y navegador del sandbox.
**Instalación:** `docker run` de la imagen oficial (o `pip install openhands-ai` para el modo CLI). Requiere Docker y una clave de proveedor de LLM.
**Casos:** agente que edita código, corre comandos y navega · automatizar tareas dev · resolver issues end-to-end en un repo.
**Stack:** Python/TS, Docker — **Modelo/API:** OpenAI, Anthropic, Gemini, locales; agnóstico vía variables de entorno.
**Elige si:** quieres un agente que "haga", no solo hable — **Evita si:** solo necesitas chat/RAG o no puedes correr Docker.
**Limitaciones:** el sandbox Docker consume recursos y la ejecución de código arbitrario exige cuidar el aislamiento.
**Combina con:** [ECC](#-ecc) · [sandbox](#-sandbox)
**Repo:** [GitHub](https://github.com/All-Hands-AI/OpenHands)

### 🦌 deer-flow
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas complejas delegando en agentes especializados.
**Por qué destaca:** orquestación potente y extensible; alcanzó gran visibilidad (#1 en GitHub Trending en su lanzamiento v2) y cuenta con el respaldo de ByteDance. Su diseño por skills lo hace ampliable sin tocar el núcleo.
**Cómo funciona:** un orquestador reparte sub-tareas a agentes con herramientas y sandbox, integrando memoria entre pasos; implementado en Python/TS sobre LangChain.
**Instalación:** `git clone` del repo y arranque con sus scripts (o Docker). Requiere claves de proveedor de LLM y, para el sandbox, Docker.
**Casos:** research profundo · tareas complejas multi-paso con herramientas · flujos extensibles vía skills propias.
**Stack:** Python/TS, LangChain, Docker — **Modelo/API:** múltiples; agnóstico vía variables de entorno.
**Elige si:** quieres un orquestador completo y extensible — **Evita si:** buscas algo minimalista o sin Docker.
**Combina con:** [gpt-researcher](#-gpt-researcher) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/bytedance/deer-flow)

### 🟩 NeMo-Agent-Toolkit
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🔴 pesado
**Qué es:** toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial.
**Por qué destaca:** respaldo y rendimiento de NVIDIA, orientado a despliegues empresariales sobre su stack de modelos NIM e infra GPU. Incluye evaluación y guardrails, no solo orquestación.
**Cómo funciona:** compone agentes y herramientas mediante perfiles configurables y los conecta a modelos NVIDIA NIM u otros compatibles (OpenAI-style); librería Python (Apache-2.0) con servidor FastAPI.
**Instalación:** `pip install nvidia-nat` (o `git clone` del repo). Para sacar provecho real necesitas acceso a NIM/NGC o GPUs NVIDIA; de ahí el setup 🔴.
**Casos:** agentes empresariales en stack NVIDIA · pipelines con modelos propios tras un firewall · RAG con guardrails y evaluación.
**Stack:** Python, FastAPI (Apache-2.0) — **Modelo/API:** NVIDIA NIM y compatibles OpenAI.
**Elige si:** trabajas con infra NVIDIA o necesitas guardrails/eval empresarial — **Evita si:** quieres algo ligero y agnóstico.
**Combina con:** [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit)

### ☤ hermes-agent
**Etiquetas:** Ejecución 🏠 local-first · Rol 🖥️ app/UI · Setup 🟡 medio
**Qué es:** entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local.
**Por qué destaca:** aprovecha el razonamiento estructurado de los modelos Hermes y prioriza la ejecución local frente a depender de la nube. Su rasgo distintivo es un learning loop: el agente crea skills desde la experiencia y persiste conocimiento entre sesiones.
**Cómo funciona:** una app de escritorio (Tauri) coordina agentes con backend Python que invocan modelos Hermes locales o APIs comerciales como fallback, guardando memoria y skills autoaprendidas.
**Instalación:** `git clone` y build con Tauri/Cargo (más dependencias Python). Para modo local puro necesitas pesos de Hermes y una GPU razonable; sin GPU puede usar APIs comerciales.
**Casos:** delegar tareas en sandbox local · panel de control de escritorio (Tauri) · agente que acumula skills con el uso.
**Stack:** Rust (Tauri), TypeScript, Python — **Modelo/API:** Hermes-3-Llama-3 local + APIs comerciales (OpenAI, Anthropic) como fallback.
**Elige si:** quieres agentes locales con UI y memoria persistente — **Evita si:** prefieres orquestación en nube o no quieres compilar Tauri.
**Limitaciones:** el build de Tauri y los pesos locales elevan la barrera de entrada frente a una solución hosted.
**Combina con:** [ECC](#-ecc) · [odysseus](#-odysseus)
**Repo:** [GitHub](https://github.com/NousResearch/hermes-agent)

### 🧬 openevolve
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 🧩 motor/runtime · Setup 🔴 pesado
**Qué es:** agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
**Por qué destaca:** supera la generación en un solo paso al explorar el espacio de soluciones, encontrando algoritmos inéditos (inspirado en AlphaEvolve de Google). Es el proyecto open-source que más cerca está de replicar ese enfoque.
**Cómo funciona:** un bucle evolutivo usa el LLM como operador de mutación y una función de evaluación como fitness; implementado en Python con numpy/PyTorch y componentes en Rust para velocidad.
**Instalación:** `pip install openevolve` (o `git clone` del repo). Requiere un proveedor de LLM de frontera (Claude/GPT-4o) y, según el problema, cómputo no trivial para evaluar muchas generaciones.
**Casos:** empaquetado geométrico · optimización de carteras · mejorar scripts en tiempo real · descubrir heurísticas nuevas.
**Stack:** Python, PyTorch/numpy, Rust — **Modelo/API:** modelos de frontera creativos (Claude, GPT-4o); agnóstico vía variables de entorno.
**Elige si:** optimizas problemas algorítmicos donde cabe explorar muchas variantes — **Evita si:** haces tareas de texto comunes o buscas respuesta inmediata.
**Limitaciones:** consume muchos tokens de LLM y cómputo por generación; no es práctico para tareas triviales.
**Combina con:** [llm-council](#-llm-council)
**Repo:** [GitHub](https://github.com/algorithmicsuperintelligence/openevolve)

### 🔍 gpt-researcher
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, busca fuentes y redacta un informe con referencias.
**Por qué destaca:** muy popular para research profundo; automatiza horas de búsqueda recopilando y citando lo más relevante. Su arquitectura planificador-buscador-redactor es un patrón de referencia para research con agentes.
**Cómo funciona:** un agente planificador genera consultas, agentes de búsqueda recopilan fuentes web (vía Tavily y otros) y un redactor sintetiza el reporte; backend Python (FastAPI) con frontend Next.js.
**Instalación:** `pip install gpt-researcher` o vía Docker. Requiere una clave de LLM y, según configuración, una clave de búsqueda web (Tavily).
**Casos:** análisis de un tema con fuentes · reportes en PDF/Markdown · briefing automático antes de una decisión.
**Stack:** Python, Next.js, FastAPI — **Modelo/API:** GPT-4o, Claude, Gemini + locales; agnóstico vía variables de entorno.
**Elige si:** necesitas research profundo citado — **Evita si:** solo quieres una respuesta corta o un chat simple.
**Combina con:** [firecrawl](#-firecrawl) · [browser-use](#-browser-use) · receta [Research profundo](#-3-agente-de-research-profundo)
**Repo:** [GitHub](https://github.com/assafelovic/gpt-researcher)

### 🔬 autoresearch
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proyecto pequeño y exploratorio de Karpathy, más que una herramienta pulida.
**Por qué destaca:** propuesta sencilla para experimentar con investigación autónoma en varias pasadas; valioso como punto de partida y referencia didáctica más que como producto cerrado.
**Cómo funciona:** repite ciclos de búsqueda y refinamiento sobre un tema, refinando consultas con cada iteración; implementado en Python con llamadas a LLM y búsqueda web.
**Instalación:** `git clone` del repo y ejecución de sus scripts en Python (consulta el README). Requiere una clave de LLM y acceso a búsqueda web.
**Casos:** loops de búsqueda y refinamiento · exploración de un tema en varias pasadas · base para montar tu propio agente de research.
**Stack:** Python — **Modelo/API:** múltiples; agnóstico vía variables de entorno.
**Elige si:** experimentas con research iterativo o quieres un punto de partida — **Evita si:** quieres salida pulida y lista ([gpt-researcher](#-gpt-researcher)).
**Combina con:** [gpt-researcher](#-gpt-researcher) · [crawl4ai](#-crawl4ai)
**Repo:** [GitHub](https://github.com/karpathy/autoresearch)

### 🐝 ruflo
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala.
**Por qué destaca:** motor en Rust con embeddings, memoria persistente y plugins, orientado a coordinación masiva de agentes con seguridad de nivel enterprise. Es de nicho pero ambicioso y aprovecha el rendimiento de Rust para la orquestación.
**Cómo funciona:** un coordinador en Rust reparte trabajo entre agentes, comparte memoria federada (embeddings) y comunica equipos; se apoya en los CLIs de Claude Code y Codex como ejecutores.
**Instalación:** `cargo install` o build desde fuente con `git clone` (consulta el README). Requiere tener instalados los CLIs de agentes (Claude Code/Codex) y sus claves.
**Casos:** swarms de agentes especializados · memoria autoaprendida y comms entre equipos · paralelizar tareas de codificación a escala.
**Stack:** Rust — **Modelo/API:** Claude Code, Codex (vía sus CLIs).
**Elige si:** orquestas muchos agentes a escala y quieres rendimiento — **Evita si:** solo necesitas 1-2 agentes o no usas Claude Code/Codex.
**Limitaciones:** setup pesado (Rust + CLIs de agentes) y caso de uso estrecho; no es una librería de uso general.
**Combina con:** [mem0](#-mem0) · [ECC](#-ecc)
**Repo:** [GitHub](https://github.com/ruvnet/ruflo)

### 🧑‍🤝‍🧑 multica
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho.
**Por qué destaca:** propone equipos mixtos humano+agente en un flujo común, en lugar de automatización totalmente headless. El ángulo es operativo: agentes como "compañeros de equipo" con contexto compartido.
**Cómo funciona:** según lo descrito, ofrece un entorno web donde humanos y agentes comparten tareas y contexto; pila web/TypeScript con backend persistente.
**Instalación:** consulta el README del repo (`git clone` / instalación web). Requiere claves de proveedor de LLM para los agentes.
**Casos:** equipos mixtos humano+agente · operación con agentes como colaboradores · delegar tareas repetitivas a agentes dentro de un flujo humano.
**Stack:** web/TS, Docker, PostgreSQL — **Modelo/API:** múltiples; agnóstico vía variables de entorno.
**Elige si:** mezclas trabajo humano y agentes en un mismo flujo — **Evita si:** quieres automatización 100% headless o un producto maduro.
**Limitaciones:** proyecto de nicho y madurez limitada; conviene validar estado antes de apostar por él.
**Combina con:** [ruflo](#-ruflo) · [chatwoot](#-chatwoot)
**Repo:** [GitHub](https://github.com/multica-ai/multica)

### 🐟 MiroFish
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🔴 pesado
**Qué es:** motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
**Por qué destaca:** simula futuros con agentes que tienen personalidad, memoria y lógica que evolucionan, ofreciendo una "vista de dios" del escenario. El enfoque de simulación multiagente lo distingue de los frameworks orientados a tareas.
**Cómo funciona:** según lo descrito, instancia muchos agentes con perfiles y memoria que interactúan en un mundo simulado para estimar resultados; pila Python/web con persistencia.
**Instalación:** consulta el README del repo (`git clone` y ejecución en Python). Requiere claves de LLM para los agentes y cómputo no trivial para simulaciones grandes (de ahí el setup 🔴).
**Casos:** simular impacto de una noticia/política · predecir tendencias en un "sandbox" social · what-if sobre escenarios con muchos actores.
**Stack:** Python/web, Docker, PostgreSQL — **Modelo/API:** múltiples; agnóstico vía variables de entorno.
**Elige si:** simulas futuros/escenarios con muchos actores — **Evita si:** necesitas tareas deterministas o resultados reproducibles.
**Limitaciones:** proyecto de nicho, coste de LLM alto por la cantidad de agentes y resultados no deterministas.
**Combina con:** [openevolve](#-openevolve)
**Repo:** [GitHub](https://github.com/666ghj/MiroFish)

### 🏛️ llm-council
**Etiquetas:** Ejecución 🔀 híbrido · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
**Por qué destaca:** combina perspectivas de varios modelos para reducir el sesgo de uno solo; propuesta sencilla y didáctica popularizada por Karpathy. Sirve tanto para obtener mejores respuestas como para comparar modelos.
**Cómo funciona:** envía la consulta a varios LLMs, los hace revisar las respuestas de los demás y agrega un resultado de consenso; app ligera en Python/web con backend FastAPI.
**Instalación:** `git clone` del repo y ejecución según su README. Requiere claves de varios proveedores de LLM (OpenAI, Anthropic, Google, xAI) para que el consejo tenga variedad.
**Casos:** respuestas por consenso multi-modelo · reducir sesgo de un solo modelo · comparar modelos en preguntas reales.
**Stack:** Python, React, FastAPI, PostgreSQL — **Modelo/API:** múltiples LLMs (OpenAI, Anthropic, Google, xAI Grok).
**Elige si:** quieres consenso entre modelos o comparar proveedores — **Evita si:** te basta un único LLM o el coste multi-modelo no es asumible.
**Limitaciones:** cada consulta se multiplica por el nº de modelos del consejo, elevando coste y latencia.
**Combina con:** [litellm](#-litellm)
**Repo:** [GitHub](https://github.com/karpathy/llm-council)

### 🕸️ awesome-LangGraph
**Etiquetas:** Ejecución ☁️ API/cloud · Rol 📂 directorio/recurso · Setup 🟢 fácil
**Qué es:** repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no una herramienta ejecutable.
**Por qué destaca:** índice organizado por áreas (RAG, web, finanzas, salud, seguridad) que facilita encontrar patrones y proyectos de referencia para LangGraph. Útil como punto de partida antes de diseñar un grafo de agentes.
**Cómo funciona:** una lista "awesome" en Markdown con enlaces a proyectos, plantillas y tutoriales del ecosistema LangGraph, clasificados por caso de uso.
**Instalación:** no requiere instalación; se consulta el repo (o `git clone` para uso offline).
**Casos:** estructurar grafos cíclicos de agentes · políticas de enrutamiento y estado · encontrar plantillas de RAG/multiagente.
**Stack:** Markdown / Python-JS (LangGraph) — **Modelo/API:** N/A (recurso).
**Elige si:** construyes con LangGraph y quieres patrones de referencia — **Evita si:** no usas ese ecosistema.
**Combina con:** [langchain](#-langchain)
**Repo:** [GitHub](https://github.com/von-development/awesome-LangGraph)

---

## 4. Scraping, Búsqueda & Research Web

Crawling, extracción estructurada y navegación web con LLMs.

### 🔍 Escaneo rápido

| Repo | Qué es | Lenguaje | Setup | Elige si… |
|---|---|---|---|---|
| [firecrawl](#-firecrawl) | API search+scrape para agentes (Markdown/JSON) | TS/API | 🟡 | Quieres web → Markdown/JSON listo para LLM |
| [crawl4ai](#-crawl4ai) | Crawling a gran escala orientado a IA | Python | 🟡 | Recolectas grandes volúmenes barato |
| [scrapy](#-scrapy) | Framework clásico y maduro de scraping | Python | 🟡 | Necesitas un crawler maduro y robusto |
| [crawlee](#-crawlee) | Framework de crawling moderno con antibloqueo | Node.js | 🟡 | Scrapeas con Node y antibloqueo |
| [crawlee-python](#-crawlee-python) | Crawlee llevado a Python | Python | 🟡 | Quieres Crawlee pero en Python |
| [Scrapling](#-scrapling) | Scraping adaptativo anti-bloqueo | Python | 🟡 | Las páginas cambian o te bloquean |
| [scrapely](#-scrapely) | Extracción por ejemplos (sin reglas) | Python | 🟢 | Extraes por plantilla aprendida |
| [llm-scraper](#-llm-scraper) | Web → datos estructurados con LLM + Zod | TS | 🟢 | Defines un esquema y el LLM lo llena |
| [Scrapegraph-ai](#-scrapegraph-ai) | Scraping por grafos + LLM ("by prompt") | Python | 🟡 | Combinas extracción y estructura semántica |
| [playwright](#-playwright) | Automatización/testing de navegador | TS/Python | 🟡 | Necesitas control preciso del browser |
| [playwright-cli](#-playwright-cli) | Playwright como CLI + skills | TS | 🟢 | Tu agente automatiza web vía CLI |
| [browser-use](#-browser-use) | Navegación web por visión para LLM | Python | 🟡 | El agente "ve" la pantalla y actúa |
| [instaloader](#-instaloader) | Descarga de datos de Instagram | Python | 🟢 | Extraes contenido/metadata de IG |
| [snscrape](#-snscrape) | Scraper de redes sociales | Python | 🟢 | Recolectas posts sin API oficial |

### ⚖️ ¿Cuál elegir? — Crawling/scraping

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **firecrawl** | Alimentar agentes/RAG con web limpia | Salida lista para LLM (MD/JSON), API hosted + MCP | Solo necesitas un crawler crudo o sin presupuesto de API |
| **crawl4ai** | Volumen alto orientado a IA, self-host | Gratuito, open-source, salida lista para IA | Quieres scraping puntual simple o API hosted sin operar |
| **scrapy** | Crawler robusto y maduro a escala | Ecosistema, control total, base instalada masiva | No quieres curva de framework ni salida lista para LLM |
| **crawlee** / **crawlee-python** | Antibloqueo moderno (Node o Python) | Rotación/proxies/sesiones integrados, mantenido por Apify | Te sirve scrapy clásico o no necesitas evasión de bloqueos |
| **Scrapling** | Sitios que cambian de estructura o bloquean | Selectores adaptativos auto-reparables | El sitio es estable y simple, o no necesitas stealth |

### ⚖️ ¿Cuál elegir? — Web estructurada con LLM / navegación

| Repo | Cuándo usarlo | Ventaja clave | Evítalo si… |
|---|---|---|---|
| **llm-scraper** | Quieres un esquema tipado (Zod) relleno por LLM | Salida validada, integración directa con Playwright | Prefieres extracción semántica por grafos o trabajas en Python |
| **Scrapegraph-ai** | Extracción semántica "by prompt" en Python | Combina scraping + razonamiento, multi-proveedor | Te basta un esquema simple o el coste de LLM por página es alto |
| **browser-use** | El agente debe navegar como humano | Control visual, sin selectores fijos | Necesitas reproducibilidad determinista o sin coste de visión |
| **playwright** / **playwright-cli** | Control determinista del browser | Reproducible, multiplataforma, auto-waits | Quieres que el agente decida por visión ([browser-use](#-browser-use)) |

### 🔥 firecrawl
**Etiquetas:** Ejecución ☁️ API/cloud · MCP 🔌 · Rol ⚙️ plataforma · Setup 🟡 medio
**Qué es:** plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript.
**Por qué destaca:** se ha vuelto la opción de referencia para alimentar pipelines RAG y agentes con web limpia; muy adoptada y con integración MCP de primera clase. Su salida Markdown/JSON normalizada ahorra el paso de limpiar HTML.
**Cómo funciona:** renderiza la página (incluido JS), normaliza el HTML y lo convierte a Markdown/JSON; expone endpoints scrape/crawl/search/map vía API REST y SDKs, más un servidor MCP para que los agentes lo usen como herramienta.
**Instalación:** API hosted con clave (`npm i @mendable/firecrawl-js` o `pip install firecrawl-py`); también self-host con Docker. Requiere una clave de API (gratuita con límite, de pago a escala) o infra para self-host.
**Casos:** convertir páginas complejas en contexto limpio · search + crawl para research · alimentar RAG con documentación de sitios dinámicos.
**Stack:** API/SDK (TS/Python), hosted o self-host, Docker — **Modelo/API:** MCP y agentes; no atado a un proveedor de LLM.
**Elige si:** alimentas agentes/RAG con web y quieres salida limpia — **Evita si:** solo quieres HTML crudo o el presupuesto de API no encaja.
**Limitaciones:** la API hosted de pago escala por páginas; el self-host requiere operar Redis, workers y Chromium.
**Combina con:** [gpt-researcher](#-gpt-researcher) · [crawl4ai](#-crawl4ai) · receta [Research profundo](#-3-agente-de-research-profundo)
**Repo:** [GitHub](https://github.com/firecrawl/firecrawl)

### 🕷️ crawl4ai
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA.
**Por qué destaca:** una de las alternativas open-source más populares a las APIs de pago; gratuita, self-host y muy activa en la comunidad de scraping para LLMs. Su salida Markdown/JSON limpia compite directamente con firecrawl sin coste de API.
**Cómo funciona:** usa Playwright para controlar un navegador headless, ejecuta el render asíncrono y limpia el resultado a Markdown/JSON con estrategias de extracción configurables (incluido LLM-extraction opcional).
**Instalación:** `pip install crawl4ai` seguido de `crawl4ai-setup` para instalar los navegadores de Playwright. Requiere Chromium (lo instala el setup) y, para LLM-extraction, una clave de proveedor.
**Casos:** pipeline que recolecta muchas páginas para análisis · salida lista para IA · alternativa self-host a firecrawl a escala.
**Stack:** Python, Playwright — **Modelo/API:** agnóstico; la extracción con LLM es opcional y configurable por entorno.
**Elige si:** necesitas volumen barato y self-host — **Evita si:** quieres una API hosted simple sin operar navegadores ([firecrawl](#-firecrawl)).
**Combina con:** [firecrawl](#-firecrawl) · [gpt-researcher](#-gpt-researcher)
**Repo:** [GitHub](https://github.com/unclecode/crawl4ai)

### 🐍 scrapy
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala.
**Por qué destaca:** estándar de facto del scraping en Python desde hace más de una década, con enorme ecosistema de extensiones y base instalada masiva. Su robustez y extensibilidad lo mantienen vigente pese a su edad.
**Cómo funciona:** define spiders que emiten requests asíncronas sobre el motor Twisted, procesa respuestas con selectores (CSS/XPath) y pasa los items por pipelines de limpieza/almacenamiento.
**Instalación:** `pip install scrapy`; el comando `scrapy startproject` genera el andamiaje del proyecto. Requiere Python y, según el target, rotación de proxies/headers para evitar bloqueos.
**Casos:** spiders robustos · pipelines de extracción a gran escala · feeds estructurados (JSON/CSV) hacia un data warehouse.
**Stack:** Python (Twisted) — **Modelo/API:** N/A (no usa LLM).
**Elige si:** quieres un crawler sólido y configurable a escala — **Evita si:** buscas salida lista para LLM o algo puntual sin curva de framework.
**Combina con:** [scrapely](#-scrapely) · [crawlee-python](#-crawlee-python)
**Repo:** [GitHub](https://github.com/scrapy/scrapy)

### 🦗 crawlee
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework moderno de crawling para Node.js con antibloqueo integrado, que unifica scraping de HTTP y de navegador bajo una misma API con colas y reintentos.
**Por qué destaca:** mantenido por Apify, es la referencia de crawling en el ecosistema JavaScript y trae evasión de bloqueos lista de fábrica. Su unificación HTTP+navegador evita mantener dos stacks separados.
**Cómo funciona:** gestiona una cola de URLs y un pool autoescalable de crawlers (Cheerio para HTTP o Playwright/Puppeteer para navegador), con rotación de proxies y huellas para evitar baneos.
**Instalación:** `npm i crawlee` o, para empezar, `npx crawlee create`. Requiere Node.js y, para el modo navegador, los binarios de Playwright/Puppeteer.
**Casos:** scraping a escala con rotación de proxies · colas y reintentos · crawlers que combinan HTTP rápido y navegador para JS pesado.
**Stack:** Node.js/TypeScript — **Modelo/API:** N/A (no usa LLM).
**Elige si:** scrapeas con Node y necesitas antibloqueo — **Evita si:** trabajas en Python ([crawlee-python](#-crawlee-python)) o no necesitas evasión.
**Combina con:** [playwright](#-playwright)
**Repo:** [GitHub](https://github.com/apify/crawlee)

### 🦗 crawlee-python
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python.
**Por qué destaca:** acerca las ventajas del Crawlee de Node a quienes ya viven en Python, con respaldo oficial de Apify y adopción en crecimiento. Encaja naturalmente con pandas, notebooks y pipelines de datos.
**Cómo funciona:** ofrece crawlers basados en BeautifulSoup/HTTPX o en Playwright, con una cola de requests unificada, autoescalado y gestión de sesiones y proxies.
**Instalación:** `pip install crawlee` (extras como `crawlee[playwright]` para el modo navegador). Requiere Python y, para el modo navegador, los binarios de Playwright.
**Casos:** crawling moderno con antibloqueo en Python · integrar con stack de datos Python · alternativa a scrapy con evasión integrada.
**Stack:** Python — **Modelo/API:** N/A (no usa LLM).
**Elige si:** quieres Crawlee en Python con antibloqueo — **Evita si:** ya usas scrapy y te basta, o no necesitas evasión.
**Combina con:** [scrapy](#-scrapy) · [playwright](#-playwright)
**Repo:** [GitHub](https://github.com/apify/crawlee-python)

### 🩹 Scrapling
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia.
**Por qué destaca:** proyecto en alza por su enfoque "auto-reparable" de selectores, que evita reescribir scrapers cada vez que el sitio se actualiza. Sus fetchers sigilosos imitan navegadores reales para sortear bloqueos.
**Cómo funciona:** rastrea atributos y posiciones de los elementos para reencontrarlos tras cambios en el DOM, con fetchers sigilosos (Camoufox/Playwright) que imitan navegadores reales para evadir detección.
**Instalación:** `pip install scrapling` (con `scrapling install` para los navegadores del modo sigiloso). Requiere Python y, para el modo stealth, los binarios de navegador que instala el subcomando.
**Casos:** páginas que cambian de estructura · evadir bloqueos sin reescribir selectores · scraping resiliente sobre sitios volátiles.
**Stack:** Python — **Modelo/API:** N/A (no usa LLM).
**Elige si:** los sitios cambian o te bloquean a menudo — **Evita si:** el target es estable y simple, o no necesitas stealth.
**Combina con:** [scrapy](#-scrapy)
**Repo:** [GitHub](https://github.com/D4Vinci/Scrapling)

### 📐 scrapely
**Etiquetas:** Ejecución 🏠 local-first · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales.
**Por qué destaca:** pieza histórica del ecosistema Scrapy; nicho y poco activa hoy, pero útil cuando se quiere extraer "por demostración" en lugar de programar selectores. Su enfoque by-example sigue siendo didáctico.
**Cómo funciona:** se le da una URL de ejemplo con los datos marcados, induce una plantilla mediante alineación de HTML y la aplica a nuevas páginas con la misma estructura.
**Instalación:** `pip install scrapely`. Requiere Python; sin dependencias pesadas.
**Casos:** extraer campos repetidos sin escribir reglas · scraping por plantilla aprendida · prototipar extracción sobre familias de páginas homogéneas.
**Stack:** Python — **Modelo/API:** N/A (no usa LLM).
**Elige si:** prefieres enseñar por ejemplos y el sitio es homogéneo — **Evita si:** necesitas un crawler completo o el proyecto exige mantenimiento activo.
**Limitaciones:** mantenimiento poco activo; conviene validar compatibilidad con Python actual antes de apostar por ella.
**Combina con:** [scrapy](#-scrapy)
**Repo:** [GitHub](https://github.com/scrapy/scrapely)

### 🧾 llm-scraper
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟢 fácil
**Qué es:** librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído.
**Por qué destaca:** popular por su simplicidad: salida tipada y validada sin escribir parsers, integrándose directamente con Playwright y los SDKs de LLM. El uso de Zod garantiza tipos correctos en tiempo de compilación.
**Cómo funciona:** carga la página con Playwright, la pasa a texto/markdown y pide al LLM que devuelva un objeto conforme al esquema Zod, garantizando tipos correctos y validación en runtime.
**Instalación:** `npm i llm-scraper playwright` y la SDK del proveedor de LLM elegido. Requiere Node.js, los binarios de Playwright y una clave de API de LLM.
**Casos:** extraer datos tipados de sitios · automatizar datasets estructurados · poblar una API/DB desde páginas sin backend propio.
**Stack:** TypeScript, Playwright, Zod — **Modelo/API:** LLMs vía SDK (OpenAI, Anthropic, etc.); agnóstico vía variables de entorno.
**Elige si:** quieres salida tipada y validada en stack TS — **Evita si:** prefieres extracción semántica por grafos ([Scrapegraph-ai](#-scrapegraph-ai)) o trabajas en Python.
**Combina con:** [playwright](#-playwright) · [firecrawl](#-firecrawl)
**Repo:** [GitHub](https://github.com/mishushakov/llm-scraper)

### 🕸️ Scrapegraph-ai
**Etiquetas:** Ejecución 🔀 híbrido · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping.
**Por qué destaca:** muy popular por permitir scraping "by prompt", combinando extracción con razonamiento del modelo y soporte para múltiples proveedores. Su filosofía "You Only Scrape Once" resume el valor: una descripción, un grafo.
**Cómo funciona:** construye un grafo dirigido de nodos (fetch, parse, generación con LLM) que recorre la página y produce el resultado estructurado pedido, usando LangGraph por debajo.
**Instalación:** `pip install scrapegraphai` más `playwright install` para el render dinámico. Requiere una clave de proveedor de LLM y los binarios de Playwright.
**Casos:** extracción semántica de sitios · datasets útiles para IA · scraping sin selectores, solo describiendo los campos.
**Stack:** Python, LangChain/LangGraph, Playwright — **Modelo/API:** múltiples LLMs (OpenAI, Anthropic, locales vía Ollama); agnóstico vía variables de entorno.
**Elige si:** quieres estructura semántica "by prompt" en Python — **Evita si:** te basta un esquema simple ([llm-scraper](#-llm-scraper)) o el coste de LLM por página es alto.
**Combina con:** [crawl4ai](#-crawl4ai) · [graphrag](#-graphrag)
**Repo:** [GitHub](https://github.com/ScrapeGraphAI/Scrapegraph-ai)

### 🎭 playwright
**Etiquetas:** Ejecución 🔀 híbrido · MCP 🔌 · Rol 📚 librería/SDK · Setup 🟡 medio
**Qué es:** framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje.
**Por qué destaca:** se ha convertido en el estándar moderno de automatización de browser, desplazando a Selenium/Puppeteer por su fiabilidad y su auto-espera de elementos. Microsoft lo mantiene y tiene bindings para Node.js, Python, Java y .NET.
**Cómo funciona:** lanza navegadores reales en modo headless o con UI y los controla por protocolo (CDP), con waits automáticos, interceptación de red y captura de DOM/screenshots/traces.
**Instalación:** `npm i playwright` o `pip install playwright`, seguido de `playwright install` para los navegadores. Requiere descargar los binarios de Chromium/Firefox/WebKit (~varios cientos de MB).
**Casos:** testing E2E · scraping dinámico · scripting reproducible · herramienta de agentes vía MCP.
**Stack:** Node.js o Python (también Java/.NET) — **Modelo/API:** se integra con MCP y agentes; no usa LLM por sí mismo.
**Elige si:** necesitas control preciso y reproducible del browser — **Evita si:** quieres que el agente navegue por visión ([browser-use](#-browser-use)) o no necesitas un navegador real.
**Combina con:** [browser-use](#-browser-use) · [crawlee](#-crawlee)
**Repo:** [GitHub](https://github.com/microsoft/playwright)
