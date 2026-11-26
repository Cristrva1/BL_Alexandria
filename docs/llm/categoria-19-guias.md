# Alexandría para agentes · Guías, cursos y cookbooks

Categoría 19 «Aprender IA y escribir mejores prompts» › subcategoría `guias`. 14 repos. Generado el 2026-11-24 desde `INDICE_IA.json` e `INDICE_IA.detalle.json` (Biblioteca de Alexandría, Binarias Labs).
Explorador en línea: https://cristrva1.github.io/BL_Alexandria/#/explorar?cat=19&sub=guias · Ficha de cada repo: `https://cristrva1.github.io/BL_Alexandria/#/repo/<id>`

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
| `awesome-llm-apps` | Colección de más de 100 apps de ejemplo listas para ejecutar: agentes, equipos… | 1 Básico | 75 | Apache-2.0 (OSI permisiva) | recomendado |
| `loop-engineering` | Patrones, plantillas y CLI para diseñar bucles de trabajo con agentes de código… | 1 Básico | 67 | MIT (OSI permisiva) | sin grupo |
| `ai-agents-for-beginners` | Curso de Microsoft con 18 lecciones (texto, video y código Python) para empezar… | 1 Básico | 65 | MIT (OSI permisiva) | recomendado |
| `generative-ai-for-beginners` | Curso de Microsoft para aprender los conceptos y construir ejemplos de… | 1 Básico | 65 | MIT (OSI permisiva) | alternativa |
| `500-ai-agents-projects` | Colección de casos de uso y agentes autocontenidos, junto con enlaces a… | 1 Básico | 61 | MIT (OSI permisiva) | sin grupo |
| `agents-course` | Curso oficial y gratuito de agentes de IA de Hugging Face: de los fundamentos a… | 1 Básico | 58 | Apache-2.0 (OSI permisiva) | sin grupo |
| `ai-engineering-hub` | Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y… | 1 Básico | 58 | MIT (OSI permisiva) | sin grupo |
| `openai-cookbook` | Ejemplos y guías oficiales en notebooks para usar la API de OpenAI en casos… | 1 Básico | 58 | MIT (OSI permisiva) | alternativa |
| `claude-cookbooks` | Recetario oficial de Anthropic con notebooks de Python para la API de Claude… | 1 Básico | 53 | MIT (OSI permisiva) | alternativa |
| `claude-quickstarts` | Ejemplos oficiales de Anthropic para construir aplicaciones con Claude… | 1 Básico | 53 | MIT (OSI permisiva) | sin grupo |
| `12-factor-agents` | Guía de 12 principios de ingeniería para construir agentes con LLM fiables en… | 1 Básico | 50 | Apache-2.0 (OSI permisiva) | sin grupo |
| `agents-towards-production` | Colección de 28 tutoriales con código para llevar agentes de IA a producción… | 1 Básico | 49 | Licencia propia no comercial (source-available) | sin grupo |
| `awesome-harness-engineering` | Directorio de herramientas y patrones para diseñar el entorno, memoria… | 1 Básico | 49 | CC0-1.0 (OSI permisiva) | sin grupo |
| `context-engineering` | Guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la… | 1 Básico | 44 | MIT (OSI permisiva) | sin grupo |

Puntuación 0-100: adopción 25, mantenimiento 25, licencia 15, madurez 10, respaldo 10, encaje 10, seguridad 5. Papel: posición en su grupo de similares; «sin grupo» = no hay otro repo equivalente en el catálogo.

## Fichas

### Awesome LLM Apps (`awesome-llm-apps`)

- **Repo:** https://github.com/Shubhamsaboo/awesome-llm-apps · Apache-2.0 · nivel 1 · 75/100 · recomendado en «Cookbooks y ejemplos de apps con LLM»
- **Qué es:** Colección (Apache-2.0) de @Shubhamsaboo con más de 100 plantillas open source de agentes, skills de agente y apps RAG. Es muy popular (~145k estrellas) y se actualiza a diario.
- **Cuándo elegirlo:** Casos: Aprender con un asistente de viajes; Estudiar un RAG con Llama local.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; entorno y proveedor específicos del ejemplo elegido; hardware prerequisites; API de IA: opcional; Navegador; entorno y proveedor específicos del ejemplo elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `npx skills add https://github.com/Shubhamsaboo/awesome-llm-apps/tree/main/agent_skills/project-graveyard` — fuente: https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Escoge una app de RAG local y revisa su README y requisitos antes de descargar modelos Éxito: Sabes qué archivos, modelo y servicio necesita esa app concreta
- **Combina con:** `streamlit` [25/apps], `openai-agents-python` [3/py], `adk-python` [3/py], `firecrawl` [4/crawlers]
- **Alternativas:** `openai-cookbook`, `claude-cookbooks`
- **Riesgos y avisos:** Alternativas (elige una): openai-cookbook, claude-cookbooks. Documenta skills para Claude Code y Codex; no todas las apps son skills ni tienen idéntica compatibilidad o instalación.

### Loop Engineering (`loop-engineering`)

- **Repo:** https://github.com/cobusgreyling/loop-engineering · MIT · nivel 1 · 67/100
- **Qué es:** Biblioteca de patrones (MIT) de Cobus Greyling para operar agentes de programación alrededor de un repositorio mediante 'bucles' en lugar de prompts sueltos. Es activa (v1.6.0) y reciente.
- **Cuándo elegirlo:** Casos: Diseñar un ciclo de revisión de issues; Estimar el coste de un bucle antes de automatizarlo.
- **Requisitos:** nivel 1: preparación sencilla, se instala dentro de un agente (skill, plugin o MCP); Node; proyecto de prueba; Claude Code o Codex configurado; hardware prerequisites; API de IA: no; Node; proyecto de prueba; Claude Code o Codex configurado.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/cobusgreyling/loop-engineering/blob/main/README.md

  ```bash
  npx @cobusgreyling/loop init . --pattern daily-triage --tool claude
  npx @cobusgreyling/loop doctor .
  ```
- **Primera prueba propuesta (no ejecutada):** Genera la plantilla de daily-triage en una carpeta de prueba y ejecuta doctor antes de activar acciones Éxito: Puedes revisar la configuración y los avisos del diagnóstico
- **Combina con:** `claude-code` [20/terminal], `codex` [20/terminal], `opencode` [20/terminal], `awesome-harness-engineering`
- **Riesgos y avisos:** Sin alternativas declaradas. claude-code, codex y opencode son alternativas entre sí: elige uno por bucle. La primera semana se plantea solo con informes; Claude y Codex están documentados y Antigravity no figura como adaptador.

### AI Agents for Beginners (`ai-agents-for-beginners`)

- **Repo:** https://github.com/microsoft/ai-agents-for-beginners · MIT · nivel 1 · 65/100 · recomendado en «Cursos de Microsoft para principiantes»
- **Qué es:** Curso gratuito de Microsoft (MIT) para empezar a construir agentes de IA. Tiene unas 18 lecciones con texto, vídeo y código Python, y está traducido a más de 50 idiomas. Es activo y muy popular (~80k estrellas).
- **Cuándo elegirlo:** Casos: Aprender patrones de agentes; Estudiar herramientas y memoria con ejemplos.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Python y cuenta Azure para los ejercicios principales; hardware prerequisites; API de IA: opcional; Navegador; Python y cuenta Azure para los ejercicios principales.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/microsoft/ai-agents-for-beginners/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la primera lección y dibuja las herramientas y decisiones de un agente de consultas ficticio Éxito: Puedes distinguir el agente de una llamada única al modelo
- **Combina con:** `agent-framework` [3/ts], `generative-ai-for-beginners`, `mcp-for-beginners` [5/directorios]
- **Alternativas:** `generative-ai-for-beginners`
- **Riesgos y avisos:** Sin alternativas declaradas. Requiere cuenta de Azure para los ejemplos tal como están. El README actual usa Agent Framework y Foundry Agent Service V2; algunos ejemplos aceptan otros proveedores compatibles y no se presupone ejecución local.

### Generative AI for Beginners (`generative-ai-for-beginners`)

- **Repo:** https://github.com/microsoft/generative-ai-for-beginners · MIT · nivel 1 · 65/100 · alternativa en «Cursos de Microsoft para principiantes»
- **Qué es:** Curso gratuito de Microsoft (MIT) para aprender a construir aplicaciones de IA generativa, ahora en su versión 3. Es muy popular (~124k estrellas), se mantiene activo y está traducido a más de 50 idiomas mediante Co-op Translator.
- **Cuándo elegirlo:** Casos: Empezar a construir una app generativa; Comparar nube con Foundry Local.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Python para los laboratorios; proveedor o Foundry Local según lección; hardware prerequisites; API de IA: opcional; Navegador; Python para los laboratorios; proveedor o Foundry Local según lección.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/microsoft/generative-ai-for-beginners/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee la introducción y elige un ejemplo de generación de texto antes de preparar su entorno específico Éxito: Puedes distinguir modelo, aplicación y proveedor y localizar las dependencias de ese ejemplo
- **Combina con:** `ai-agents-for-beginners`, `mcp-for-beginners` [5/directorios], `openai-cookbook`
- **Alternativas:** `ai-agents-for-beginners`, `llm-course`
- **Riesgos y avisos:** Alternativas (elige una): llm-course. Aviso: algunas lecciones dependían de GitHub Models, retirado a finales de julio de 2026; usa Microsoft Foundry Models o…. No todas las lecciones comparten dependencias ni admiten el mismo proveedor; la ruta local documentada no convierte todos los ejemplos a local.

### 500-AI-Agents-Projects (`500-ai-agents-projects`)

- **Repo:** https://github.com/ashishpatel26/500-AI-Agents-Projects · MIT · nivel 1 · 61/100
- **Qué es:** Colección (MIT) de @ashishpatel26 con más de 500 casos de uso y proyectos de agentes de IA, organizados por industria y framework. Es activa (último push en noviembre de 2026) y popular (~40k estrellas).
- **Cuándo elegirlo:** Casos: Encontrar una idea de agente para un sector; Comparar un ejemplo local con uno por API.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; dependencias y proveedor de un agente elegido; hardware prerequisites; API de IA: opcional; Navegador; dependencias y proveedor de un agente elegido.
- **Instalación (documentada en la fuente; no ejecutada):** `git clone https://github.com/ashishpatel26/500-AI-Agents-Projects.git` — fuente: https://github.com/ashishpatel26/500-AI-Agents-Projects/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona el agente de investigación web y revisa su .env.example sin añadir credenciales todavía Éxito: Puedes enumerar fuentes de datos, modelo y permisos necesarios
- **Combina con:** `crewai` [3/py], `langgraph` [3/py], `agno` [3/py]
- **Riesgos y avisos:** Sin alternativas declaradas. crewai, langgraph y agno son alternativas entre sí: elige uno por proyecto. Actualmente incluye agentes autocontenidos además de enlaces externos; mencionar un proyecto de Claude Code no hace compatible todo el directorio.

### Hugging Face Agents Course (`agents-course`)

- **Repo:** https://github.com/huggingface/agents-course · Apache-2.0 · nivel 1 · 58/100
- **Qué es:** Curso de código abierto (Apache-2.0) de Hugging Face. Muy popular; contenido estable con unidades extra añadidas con el tiempo.
- **Cuándo elegirlo:** Casos: aprender a construir agentes con distintos frameworks de forma guiada; obtener un certificado tras un proyecto evaluado automáticamente.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; MDX; API de IA: no.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/huggingface/agents-course/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Abre la unidad 1 en hf.co/learn/agents-course y ejecuta su cuaderno de ejemplo. Éxito: Construyes un agente sencillo que usa una herramienta.
- **Combina con:** `smolagents` [3/py], `langgraph` [3/py], `llama-index` [3/py], `langfuse` [23/observabilidad]
- **Riesgos y avisos:** Algunos ejercicios usan la API de inferencia de Hugging Face, con límites en cuentas gratuitas.

### ai-engineering-hub (`ai-engineering-hub`)

- **Repo:** https://github.com/patchy631/ai-engineering-hub · MIT · nivel 1 · 58/100
- **Qué es:** Colección (MIT) de @patchy631 con tutoriales y más de 93 proyectos de ingeniería de IA: 22 de nivel principiante, 48 intermedios y 23 avanzados. Es activa (último push en noviembre de 2026) y está asociada a una newsletter.
- **Cuándo elegirlo:** Casos: Aprender RAG con Ollama; Comparar técnicas de ajuste fino.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; README específico del tutorial; modelo local o proveedor; hardware prerequisites; API de IA: opcional; Python; README específico del tutorial; modelo local o proveedor.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/patchy631/ai-engineering-hub/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige Simple RAG Workflow y dibuja ingestión, recuperación y generación Éxito: Puedes identificar dónde se almacenan documentos y dónde se usa el modelo
- **Combina con:** `crewai` [3/py], `llama-index` [3/py], `firecrawl` [4/crawlers], `ollama` [8/motores]
- **Riesgos y avisos:** Sin alternativas declaradas. Las comparaciones con Claude Code son contenido educativo y no una integración instalada del catálogo.

### OpenAI Cookbook (`openai-cookbook`)

- **Repo:** https://github.com/openai/openai-cookbook · MIT · nivel 1 · 58/100 · alternativa en «Cookbooks y ejemplos de apps con LLM»
- **Qué es:** Recetario oficial de OpenAI (MIT) con ejemplos de código y guías para tareas comunes con su API. Se navega en cookbook.openai.com. Es activo (último push en noviembre de 2026) y maduro.
- **Cuándo elegirlo:** Casos: Extraer campos de un texto; Aprender a evaluar respuestas de una aplicación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Python y API key de OpenAI si ejecutas notebooks; hardware prerequisites; API de IA: opcional; Navegador; Python y API key de OpenAI si ejecutas notebooks.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/openai/openai-cookbook/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Elige una receta de salida estructurada y revisa su esquema antes de ejecutar una entrada breve Éxito: Puedes identificar la petición, respuesta esperada y consumo de la receta
- **Combina con:** `openai-python` [7/herramientas], `openai-agents-python` [3/py], `promptfoo` [23/observabilidad], `generative-ai-for-beginners`
- **Alternativas:** `awesome-llm-apps`, `claude-cookbooks`
- **Riesgos y avisos:** Alternativas (elige una): claude-cookbooks, awesome-llm-apps. Es un recetario oficial de API; no es un paquete de plugins ni una promesa de acceso mediante suscripción.

### Claude Cookbooks (`claude-cookbooks`)

- **Repo:** https://github.com/anthropics/claude-cookbooks · MIT · nivel 1 · 53/100 · alternativa en «Cookbooks y ejemplos de apps con LLM»
- **Qué es:** Recetario oficial de Anthropic (MIT) con notebooks y guías para construir con la API de Claude. Antes se llamaba anthropic-cookbook, nombre que aún aparece en muchos enlaces del README. Es activo (último push en noviembre de 2026).
- **Cuándo elegirlo:** Casos: Clasificar tickets ficticios; Estudiar llamadas a herramientas.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; Python y clave Anthropic para ejecutar ejemplos; hardware prerequisites; API de IA: opcional; Navegador; Python y clave Anthropic para ejecutar ejemplos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/anthropics/claude-cookbooks/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee una receta de extracción y adapta sus datos a un párrafo ficticio Éxito: Entiendes qué se envía al modelo y qué respuesta se valida
- **Combina con:** `prompt-engineering-guide` [19/prompts], `claude-agent-sdk-python` [3/py], `promptfoo` [23/observabilidad]
- **Alternativas:** `awesome-llm-apps`, `openai-cookbook`
- **Riesgos y avisos:** Alternativas (elige una): openai-cookbook, awesome-llm-apps. Combinación anterior con anthropic-skills sustituida por claude-agent-sdk-python (más directa). La suscripción de Claude Code no sustituye automáticamente la clave API pedida por estos notebooks.

### claude-quickstarts (`claude-quickstarts`)

- **Repo:** https://github.com/anthropics/claude-quickstarts · MIT · nivel 1 · 53/100
- **Qué es:** Colección oficial de Anthropic (MIT) de proyectos de inicio para construir aplicaciones con la API de Claude. Es activa (último push en noviembre de 2026) y se amplía con las novedades de la plataforma.
- **Cuándo elegirlo:** Casos: Prototipar soporte con Claude; Estudiar una demo de uso de computadora.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo; hardware prerequisites; API de IA: opcional; Python o TypeScript según proyecto; clave Anthropic; servicios del ejemplo.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/anthropics/claude-quickstarts/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Escoge Customer Support Agent y revisa las herramientas que permite antes de enviar una consulta ficticia Éxito: Puedes identificar acciones del agente y datos enviados a la API
- **Combina con:** `claude-agent-sdk-python` [3/py], `copilotkit` [9/ia-ui], `e2b` [22/infra]
- **Riesgos y avisos:** Sin alternativas declaradas. Incluye un ejemplo MCP para Managed Agents pero no todos los quickstarts son conectores; la demo de computadora requiere un entorno aislado de prueba.

### 12-Factor Agents (`12-factor-agents`)

- **Repo:** https://github.com/humanlayer/12-factor-agents · Apache-2.0 · nivel 1 · 50/100
- **Qué es:** Guía de 12 principios para construir aplicaciones con LLM fiables, escrita por Dex (HumanLayer) a imagen de las '12 Factor Apps'. El código es Apache 2.0 y el contenido CC BY-SA 4.0 (GitHub lo marca NOASSERTION).
- **Cuándo elegirlo:** Casos: Revisar un diseño antes de programar; Estudiar recuperación de errores en agentes.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; flujo de agente dibujado; hardware prerequisites; API de IA: no; Navegador; flujo de agente dibujado.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/humanlayer/12-factor-agents/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Aplica el principio de controlar el flujo a un agente imaginario de soporte y señala dónde pedir intervención humana Éxito: Obtienes un diagrama con pasos deterministas y decisiones del modelo
- **Combina con:** `context-engineering`, `langgraph` [3/py], `vercel-ai` [3/ts], `awesome-harness-engineering`
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. El bloque de pseudocódigo es ilustrativo y no un instalador ejecutable; la licencia de contenido es CC BY-SA.

### Agents Towards Production (`agents-towards-production`)

- **Repo:** https://github.com/NirDiamant/agents-towards-production · Licencia propia no comercial · nivel 1 · 49/100
- **Qué es:** Colección de tutoriales de @NirDiamant para llevar agentes de IA a producción. **Licencia no comercial personalizada** (GitHub la marca NOASSERTION): no es open source en sentido OSI. Es muy activa y el README promociona un libro del autor.
- **Cuándo elegirlo:** Casos: Aprender a desplegar un agente; Comparar un servicio LLM con Ollama on-prem.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Python; dependencias por tutorial; servicios o GPU según ejercicio; hardware prerequisites; API de IA: opcional; Python; dependencias por tutorial; servicios o GPU según ejercicio.
- **Instalación (documentada en la fuente; no ejecutada):** fuente https://github.com/NirDiamant/agents-towards-production/blob/main/README.md

  ```bash
  git clone https://github.com/NirDiamant/agents-towards-production.git
  cd agents-towards-production
  ```
- **Primera prueba propuesta (no ejecutada):** Elige un tutorial de observabilidad y enumera sus entradas, trazas y criterios de evaluación Éxito: Puedes reconocer qué evidencia permitiría diagnosticar un fallo
- **Combina con:** `langgraph` [3/py], `mem0` [6/memoria], `ollama` [8/motores]
- **Riesgos y avisos:** Open-core o uso comercial limitado: parte de las funciones o datos son de pago. Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Licencia no comercial: revisa el LICENSE antes de reutilizar el código en un producto. Contenido parcialmente patrocinado. La colección declara licencia personalizada no comercial; cada tutorial tiene entorno propio y no acredita un despliegue productivo por seguirlo.

### awesome-harness-engineering (`awesome-harness-engineering`)

- **Repo:** https://github.com/ai-boost/awesome-harness-engineering · CC0-1.0 · nivel 1 · 49/100
- **Qué es:** Lista curada (CC0) de recursos, patrones y plantillas para diseñar 'harnesses' de agentes de IA, es decir, el andamiaje alrededor del modelo. La mantiene ai-boost, acepta patrocinios y está traducida a 9 idiomas.
- **Cuándo elegirlo:** Casos: Diseñar el entorno de un agente; Encontrar recursos de evaluación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; flujo de agente de referencia; hardware prerequisites; API de IA: no; Navegador; flujo de agente de referencia.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/ai-boost/awesome-harness-engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Selecciona las secciones de permisos y evaluación y redacta tres preguntas para revisar tu agente Éxito: Puedes separar ejecución, memoria, observabilidad y control de permisos
- **Combina con:** `12-factor-agents`, `loop-engineering`, `claude-code` [20/terminal]
- **Riesgos y avisos:** Licencia confirmada leyendo LICENSE el 2026-11-16 (GitHub: NOASSERTION). Sin alternativas declaradas. Es una selección de referencias que incluye Claude Code y Codex; no un paquete único de skills ni garantía de compatibilidad de todos sus enlaces.

### Context-Engineering (`context-engineering`)

- **Repo:** https://github.com/jasontang-ai/Context-Engineering · MIT · nivel 1 · 44/100
- **Qué es:** Guía y curso en construcción (MIT) sobre 'ingeniería de contexto', inspirada en la definición de Andrej Karpathy. El repositorio cambió de dueño, de davidkimai/Context-Engineering a jasontang-ai/Context-Engineering, y el README todavía…
- **Cuándo elegirlo:** Casos: Preparar contexto para una tarea larga; Estudiar memoria y recuperación.
- **Requisitos:** nivel 1: material de consulta: se lee, no se instala; Navegador; agente si utilizas los comandos; hardware prerequisites; API de IA: no; Navegador; agente si utilizas los comandos.
- **Instalación:** sin comando en el catálogo; ver README oficial. Fuente: https://github.com/jasontang-ai/Context-Engineering/blob/main/README.md
- **Primera prueba propuesta (no ejecutada):** Lee el mapa de contexto y reduce un encargo a objetivo, datos pertinentes y límites Éxito: Puedes justificar qué datos incluyes y cuáles omites
- **Combina con:** `12-factor-agents`, `prompt-engineering-guide` [19/prompts], `headroom` [23/tokens]
- **Riesgos y avisos:** Sin alternativas declaradas. Hallazgo: el catálogo debería documentar el cambio de dueño (davidkimai → jasontang-ai). El curso está en construcción y declara comandos para Claude Code y Codex; los resultados de artículos citados no validan por sí solos todas sus propuestas.

## Cómo referenciarlo desde AGENTS.md o CLAUDE.md

Guarda este archivo como `docs/alexandria/categoria-19-guias.md` y añade:

```markdown
## Herramientas externas
Antes de proponer herramientas de «Guías, cursos y cookbooks», lee `docs/alexandria/categoria-19-guias.md` y sigue sus
«Instrucciones para el agente». No instales ni ejecutes nada de esa lista sin mi aprobación explícita.
```

En Claude Code también sirve una importación directa en `CLAUDE.md`: `@docs/alexandria/categoria-19-guias.md` (carga el archivo en cada sesión; úsala solo si el tema es central en el proyecto).
