# Guia de la biblioteca

Generado: 2026-06-23T19:18:00.148096+00:00

Esta guia se regenera con `uv run repo-intelligence guide build`.

## Lectura rapida

- [Catalogo.md](Catalogo.md): tabla plana de repos.
- [human/README.md](human/README.md): guia humana navegable.
- [human/fichas/](human/fichas/): ficha individual por repo.
- [human/comparativas/](human/comparativas/): alternativas y solapamientos.
- [human/playbooks/](human/playbooks/): recetas end-to-end.
- [ai_index/REPOS.scan.json](ai_index/REPOS.scan.json): indice compacto para IA.

## Como usar esta guia

1. Empieza por una categoria o playbook.
2. Elige como maximo 3 repos finalistas por funcion.
3. Abre solo las fichas de esos finalistas.
4. Instala solo lo marcado como global, local del proyecto o Docker local.
5. Deja los catalogos de skills como referencia salvo que una ficha indique lo contrario.

## Playbooks

- [Bot de WhatsApp con IA](human/playbooks/bot-de-whatsapp-con-ia.md): atención/ventas automatizada por WhatsApp con un agente LLM.
- [Pipeline de Reels / video corto](human/playbooks/pipeline-de-reels-video-corto.md): convertir contenido en video corto con voz y subtítulos.
- [Agente de research profundo](human/playbooks/agente-de-research-profundo.md): investigación citada y estructurada a partir de la web.
- [Workspace privado local soberano](human/playbooks/workspace-privado-local-soberano.md): asistente todo-en-uno sin fuga de datos.
- [Análisis de repos grandes](human/playbooks/analisis-de-repos-grandes.md): que un asistente entienda una base de código enorme barato.
- [Marketing de agencia](human/playbooks/marketing-de-agencia.md): operar campañas y contenido a escala.
- [Web app moderna con IA](human/playbooks/web-app-moderna-con-ia.md): construir frontend pulido rápido.
- [Construir una app/servidor MCP](human/playbooks/construir-una-appservidor-mcp.md): exponer datos o herramientas propias a asistentes.
- [Documentos → presentaciones](human/playbooks/documentos-presentaciones.md): pasar texto/informes a slides editables.

## Categorias

### 1. [Automatización, Mensajería & CRM](human/categorias/01-automatizaci-n-mensajer-a-crm.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [twenty-main](human/fichas/twenty-main.md) | defer | deferred | CRM open-source orientado a desarrolladores, alternativa moderna y personalizable a Salesforce/HubSpot que modela tu negocio mediante objetos y campos propios. |
| [evolution-api](human/fichas/evolution-api.md) | defer | deferred | API REST robusta que actúa como middleware para automatizar WhatsApp y mensajería multicanal, exponiendo el envío/recepción de mensajes a tus aplicaciones. |
| [OpenWA](human/fichas/openwa.md) | reference | reference_only | gateway/SDK abierto para conectar y automatizar cuentas de WhatsApp de forma directa desde código, sin infraestructura pesada. |
| [whatsapp-agentkit](human/fichas/whatsapp-agentkit.md) | reference | reference_only | plantilla guiada que construye un agente conversacional de WhatsApp en menos de 30 minutos sin necesidad de programar, partiendo de preguntas sobre tu negocio. |
| [activepieces](human/fichas/activepieces.md) | reference | reference_only | plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y piezas reutilizables. |
| [n8n](human/fichas/n8n.md) | reference | reference_only | plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |
| [n8n_io](human/fichas/n8n-io.md) | reference | reference_only | copia local del repositorio oficial de n8n (mismo proyecto que [n8n](#-n8n)), mantenida como referencia o espejo del código fuente. |
| [huginn](human/fichas/huginn.md) | reference | reference_only | sistema de agentes self-hosted para automatizar tareas online y reaccionar a eventos, a menudo descrito como un "IFTTT/Zapier que controlas tú". |
| [mautic](human/fichas/mautic.md) | defer | deferred | plataforma open-source de marketing automation y segmentación de audiencias, alternativa soberana a suites comerciales como HubSpot o Marketo. |
| [chatwoot](human/fichas/chatwoot.md) | defer | deferred | plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. |
| [listmonk](human/fichas/listmonk.md) | reference | reference_only | gestor self-hosted de newsletters y listas de correo de alto rendimiento, pensado para envíos masivos sin depender de un SaaS. |
| [novu](human/fichas/novu.md) | reference | reference_only | infraestructura open-source de notificaciones que centraliza la comunicación multicanal (email, SMS, push y chat) desde un único backend. |

### 2. [Skills, Prompts & Guías de Agente](human/categorias/02-skills-prompts-gu-as-de-agente.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [andrej-karpathy-skills](human/fichas/andrej-karpathy-skills.md) | reference | reference_only | guía de 4 principios (inspirada en las ideas de Andrej Karpathy sobre asistentes de código) que define cómo debe responder un agente para maximizar utilidad y reducir verbosidad innecesaria. |
| [antigravity-awesome-skills](human/fichas/antigravity-awesome-skills.md) | reference | reference_only | catálogo masivo con más de 1.678 habilidades (`SKILL.md`) categorizadas por dominio (desarrollo, QA, DevOps, seguridad, marketing) listas para instalar en distintos asistentes. |
| [awesome-agent-skills](human/fichas/awesome-agent-skills.md) | reference | reference_only | colección curada de habilidades oficiales y comunitarias publicadas por marcas líderes (Anthropic, Google, Stripe, Netlify…) como referencia de calidad para agentes. |
| [awesome-claude-code](human/fichas/awesome-claude-code.md) | reference | reference_only | lista "awesome" curada de scripts, agentes, hooks, slash commands y extensiones específicos del ecosistema de Claude Code. |
| [superpowers](human/fichas/superpowers.md) | reference | reference_only | metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. |
| [skills](human/fichas/skills.md) | reference | reference_only | colección de skills de referencia mantenida por el proyecto aihero.dev / Total TypeScript, pensada como ejemplos limpios y bien construidos. |
| [claude-plugins-official](human/fichas/claude-plugins-official.md) | reference | reference_only | plugins y extensiones oficiales para Claude, distribuidos junto al repositorio de Claude Code de Anthropic. |
| [agents-towards-production](human/fichas/agents-towards-production.md) | reference | reference_only | playbook open-source con tutoriales end-to-end para llevar agentes GenAI de prototipo a producto real, cubriendo el ciclo completo de producción. |
| [Context-Engineering](human/fichas/context-engineering.md) | reference | reference_only | guía y curso práctico sobre "ingeniería de contexto", es decir, llenar la ventana de contexto con la información justa que el modelo necesita para el siguiente paso. |
| [agent-toolkit](human/fichas/agent-toolkit.md) | reference | reference_only | conjunto de skills opinadas para mejorar la eficiencia diaria con Claude Code en tareas de desarrollo, documentación y planificación. |
| [n8n-skills](human/fichas/n8n-skills.md) | reference | reference_only | conjunto de 14 skills estructuradas para Claude Code orientadas a construir flujos de n8n correctos, evitando errores al generar su JSON. |
| [marketingskills](human/fichas/marketingskills.md) | reference | reference_only | colección de skills de marketing que cubren conversión, copywriting, SEO, analítica y growth para usar con agentes de código. |
| [agency-agents](human/fichas/agency-agents.md) | reference | reference_only | conjunto de playbooks y agentes especializados (incluye un Digital Marketing Pro) diseñados para operar una agencia multicanal a escala. |
| [geo-seo-claude](human/fichas/geo-seo-claude.md) | reference | reference_only | skill GEO-first con soporte SEO clásico para optimizar la visibilidad de sitios ante motores de búsqueda con IA (Generative Engine Optimization). |
| [prompt-master](human/fichas/prompt-master.md) | reference | reference_only | skill que ayuda a redactar prompts precisos para cualquier herramienta de IA, buscando el mejor resultado sin desperdiciar tokens. |
| [ui-ux-pro-max-skill](human/fichas/ui-ux-pro-max-skill.md) | reference | reference_only | habilidades que dotan al asistente de inteligencia de diseño UI/UX y estilos avanzados para producir interfaces más profesionales. |
| [taste-skill](human/fichas/taste-skill.md) | reference | reference_only | skills "anti-slop" para producir frontends premium (layout, tipografía, motion) más skills de generación de imagen para crear mood boards de referencia. |
| [skills_emil](human/fichas/skills-emil.md) | reference | reference_only | colección de skills enfocada en diseño de interfaces y en mejorar la colaboración entre diseñador y desarrollador (design engineering). |
| [SkillSpector](human/fichas/skillspector.md) | reference | reference_only | herramienta para auditar la seguridad de skills y detectar patrones potencialmente riesgosos antes de instalarlas. |
| [humanizer](human/fichas/humanizer.md) | reference | reference_only | skill para Claude Code/OpenCode que elimina las señales típicas ("tells") de la escritura generada por IA para que el texto suene más natural. |
| [stop-slop](human/fichas/stop-slop.md) | reference | reference_only | skill que enseña al modelo a eliminar patrones y "tells" de la prosa generada por IA, mejorando ritmo y estilo. |

### 3. [Frameworks & Orquestación de Agentes](human/categorias/03-frameworks-orquestaci-n-de-agentes.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [ag2](human/fichas/ag2.md) | reference | reference_only | framework maduro para sistemas multiagente con patrones de colaboración (heredero de AutoGen). Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo. |
| [crewAI](human/fichas/crewai.md) | reference | reference_only | framework para orquestar "crews" de agentes con roles y tareas. Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica. |
| [langchain](human/fichas/langchain.md) | reference | reference_only | framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos. |
| [langflow](human/fichas/langflow.md) | reference | reference_only | constructor visual de flujos LLM/agentes construido sobre LangChain. Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código. |
| [dify](human/fichas/dify.md) | reference | reference_only | plataforma integral para construir apps de IA con backend y UI listos. Combina orquestación de prompts, RAG, agentes y observabilidad en un mismo producto autoalojable. |
| [Flowise](human/fichas/flowise.md) | reference | reference_only | builder visual drag-and-drop para pipelines LLM. Permite montar chatflows y agentes conectando nodos y exponerlos como API o widget embebible. |
| [OpenHands](human/fichas/openhands.md) | reference | reference_only | plataforma de agentes que ejecutan acciones reales en entornos de desarrollo (ex-OpenDevin). El agente puede leer y editar código, correr comandos y navegar la web dentro de un sandbox. |
| [deer-flow](human/fichas/deer-flow.md) | reference | reference_only | super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. Coordina tareas complejas delegando en agentes especializados. |
| [NeMo-Agent-Toolkit](human/fichas/nemo-agent-toolkit.md) | defer | deferred | toolkit de NVIDIA para construir y operar agentes (antes parte de NeMo). Aporta componentes para conectar, evaluar y desplegar agentes en infraestructura empresarial. |
| [hermes-agent](human/fichas/hermes-agent.md) | reference | reference_only | entorno desktop/CLI de Nous Research para ejecutar agentes locales eficientes. Ofrece un panel de control de escritorio para delegar tareas a agentes que corren en una sandbox local. |
| [openevolve](human/fichas/openevolve.md) | defer | deferred | agente de codificación evolutivo que optimiza algoritmos por simulación genética. Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones. |
| [gpt-researcher](human/fichas/gpt-researcher.md) | reference | reference_only | agente autónomo que investiga en línea y consolida reportes citados y estructurados. Planifica sub-preguntas, busca fuentes y redacta un informe con referencias. |
| [autoresearch](human/fichas/autoresearch.md) | reference | reference_only | enfoque experimental para automatizar investigación iterativa mediante bucles de búsqueda y refinamiento. Proyecto pequeño y exploratorio más que una herramienta pulida. |
| [ruflo](human/fichas/ruflo.md) | defer | deferred | harness multiagente en Rust para Claude Code y Codex que coordina 100+ agentes con memoria federada (ex-Claude Flow). Orquesta swarms de agentes especializados a escala. |
| [multica](human/fichas/multica.md) | reference | reference_only | plataforma para que humanos y agentes trabajen lado a lado ("tus próximas 10 contrataciones no serán humanas"). Integra colaboradores humanos y agentes en un mismo espacio de trabajo. Proyecto de nicho. |
| [MiroFish](human/fichas/mirofish.md) | defer | deferred | motor de inteligencia colectiva/predicción que construye mundos digitales con miles de agentes para anticipar escenarios. Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho. |
| [llm-council](human/fichas/llm-council.md) | reference | reference_only | "consejo" donde varios LLMs deliberan y se evalúan entre sí para responder. Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso. |
| [awesome-LangGraph](human/fichas/awesome-langgraph.md) | reference | reference_only | repositorio de recursos, librerías y arquitecturas del ecosistema LangGraph/LangChain. Es una lista curada, no una herramienta ejecutable. |

### 4. [Scraping, Búsqueda & Research Web](human/categorias/04-scraping-b-squeda-research-web.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [firecrawl](human/fichas/firecrawl.md) | reference | reference_only | plataforma y API para buscar, scrapear, mapear e interactuar con la web a escala, devolviendo contenido limpio y apto para agentes desde sitios complejos con JavaScript. |
| [crawl4ai](human/fichas/crawl4ai.md) | use_now | local_project | librería open-source de crawling y extracción web a gran escala con foco en fiabilidad, velocidad y costo, pensada explícitamente para generar datos listos para IA. |
| [scrapy](human/fichas/scrapy.md) | reference | reference_only | framework clásico y maduro de scraping y crawling en Python, con arquitectura asíncrona, pipelines de procesamiento y soporte para spiders complejos a gran escala. |
| [crawlee](human/fichas/crawlee.md) | reference | reference_only | framework moderno de crawling para Node.js con antibloqueo integrado, unifico scraping de HTTP y de navegador bajo una misma API con colas y reintentos. |
| [crawlee-python](human/fichas/crawlee-python.md) | reference | reference_only | versión Python de Crawlee que lleva el mismo modelo de colas, antibloqueo y crawlers HTTP/navegador al ecosistema de datos de Python. |
| [Scrapling](human/fichas/scrapling.md) | reference | reference_only | librería de scraping adaptativo y anti-bloqueo en Python que tolera cambios de estructura del sitio y reubica los elementos cuando el HTML cambia. |
| [scrapely](human/fichas/scrapely.md) | reference | reference_only | librería de extracción por ejemplos que aprende plantillas a partir de páginas anotadas y luego extrae los mismos campos de páginas similares sin reglas manuales. |
| [llm-scraper](human/fichas/llm-scraper.md) | reference | reference_only | librería TypeScript que convierte cualquier página web en datos estructurados definiendo un esquema Zod que el LLM rellena a partir del contenido extraído. |
| [Scrapegraph-ai](human/fichas/scrapegraph-ai.md) | reference | reference_only | framework de scraping en Python basado en grafos potenciado por LLM, donde describes en lenguaje natural qué extraer y el pipeline arma el flujo de scraping. |
| [playwright](human/fichas/playwright.md) | reference | reference_only | framework de Microsoft para automatización y testing de navegadores Chromium, Firefox y WebKit, con una sola API multiplataforma y soporte multi-lenguaje. |
| [playwright-cli](human/fichas/playwright-cli.md) | reference | reference_only | interfaz CLI de Playwright expuesta como SKILLs para agentes de código, que les deja automatizar el navegador con comandos en lugar de cargar esquemas masivos en el contexto. |
| [browser-use](human/fichas/browser-use.md) | reference | reference_only | biblioteca que da a los LLMs la capacidad de usar navegadores reales con interfaz para modelos de visión, dejando que el agente perciba la pantalla y actúe sin selectores fijos. |
| [instaloader](human/fichas/instaloader.md) | reference | reference_only | herramienta y librería Python para descargar fotos, videos, stories, leyendas y metadata pública de perfiles, hashtags y feeds de Instagram. |
| [snscrape](human/fichas/snscrape.md) | reference | reference_only | scraper de redes sociales (Twitter/X, Reddit, Telegram, etc.) que recolecta posts y perfiles sin necesidad de APIs oficiales ni claves. |

### 5. [MCP & Conectividad](human/categorias/05-mcp-conectividad.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [mcp](human/fichas/mcp.md) | reference | reference_only | núcleo del Model Context Protocol (spec y SDKs oficiales) para que herramientas, datos y clientes de IA interoperen bajo un mismo estándar abierto. |
| [mcp-use](human/fichas/mcp-use.md) | reference | reference_only | framework fullstack para construir MCP Apps y MCP Servers en TypeScript o Python, con utilidades para pasar de un prototipo local a una app desplegable. |
| [servers](human/fichas/servers.md) | reference | reference_only | colección oficial de implementaciones de referencia de servidores MCP mantenida por el steering group, con enlaces a servidores de la comunidad. |
| [awesome-mcp-servers](human/fichas/awesome-mcp-servers.md) | reference | reference_only | directorio curado de la comunidad que cataloga por categorías cientos de servidores MCP reutilizables, listos para conectar. |
| [mcp-neo4j](human/fichas/mcp-neo4j.md) | reference | reference_only | conjunto de servidores MCP oficiales para conectar bases de datos de grafos Neo4j a asistentes de IA, con soporte de despliegue en cloud. |
| [n8n-mcp](human/fichas/n8n-mcp.md) | reference | reference_only | servidor MCP que expone a la IA la documentación y los esquemas de los más de 1.845 nodos de n8n para ayudar a construir y depurar flujos. |
| [public-apis](human/fichas/public-apis.md) | reference | reference_only | directorio masivo y muy popular que lista por categorías miles de APIs públicas gratuitas para usar en proyectos. |

### 6. [Memoria, LLM Ops & Observabilidad](human/categorias/06-memoria-llm-ops-observabilidad.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [mem0](human/fichas/mem0.md) | reference | reference_only | capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. |
| [agentmemory](human/fichas/agentmemory.md) | reference | reference_only | memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. |
| [mempalace](human/fichas/mempalace.md) | reference | reference_only | memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. |
| [turbovec](human/fichas/turbovec.md) | reference | reference_only | librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. |
| [litellm](human/fichas/litellm.md) | reference | reference_only | gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. |
| [langfuse](human/fichas/langfuse.md) | reference | reference_only | plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. |
| [llmfit](human/fichas/llmfit.md) | reference | reference_only | herramienta para evaluar y medir el "fit" y la calidad de LLMs en una tarea concreta, orientada a comparar modelos con datos. |
| [headroom](human/fichas/headroom.md) | reference | reference_only | utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. |
| [sandbox](human/fichas/sandbox.md) | reference | reference_only | entorno sandbox all-in-one para agentes que reúne navegador, terminal, archivos, VSCode, Jupyter y MCP en un mismo espacio aislado. |
| [loguru](human/fichas/loguru.md) | reference | reference_only | librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. |

### 7. [Inteligencia de Código, Datos & Entrenamiento](human/categorias/07-inteligencia-de-c-digo-datos-entrenamiento.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [codegraph](human/fichas/codegraph.md) | reference | reference_only | CLI que indexa tu código y da a los asistentes de IA inteligencia semántica 100% local, permitiéndoles entender la estructura y el flujo de un repo sin leer archivo por archivo ni gastar llamadas a herramientas. |
| [graphify](human/fichas/graphify.md) | reference | reference_only | generador de grafos de conocimiento para proyectos locales que mapea código, PDFs, imágenes y video en diagramas interactivos, revelando cómo se conectan las piezas de un sistema. |
| [graphrag](human/fichas/graphrag.md) | reference | reference_only | sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. |
| [GitNexus](human/fichas/gitnexus.md) | use_now | global | herramienta visual para explorar y entender repositorios Git, mostrando estructura y relaciones para acelerar el onboarding en una base de código nueva. |
| [DeepSeek-Coder](human/fichas/deepseek-coder.md) | defer | deferred | familia de modelos open-source especializados en código, entrenados sobre grandes corpus de programación para generar, completar y revisar software. |
| [nanoGPT](human/fichas/nanogpt.md) | reference | reference_only | implementación mínima y limpia de Andrej Karpathy para entrenar y afinar GPTs, pensada para que el código quepa en la cabeza y se entienda de extremo a extremo. |
| [nanochat](human/fichas/nanochat.md) | reference | reference_only | pipeline full-stack mínimo de Andrej Karpathy para entrenar un "ChatGPT" de principio a fin, cubriendo desde el preentrenamiento hasta el chat servible. |
| [llm.c](human/fichas/llmc.md) | defer | deferred | implementación de entrenamiento de LLMs en C/CUDA puro de Andrej Karpathy, sin PyTorch ni frameworks pesados, para ver el cómputo al desnudo. |
| [how-to-train-your-gpt](human/fichas/how-to-train-your-gpt.md) | reference | reference_only | guía/tutorial práctico para entrenar un GPT paso a paso, pensado como material de estudio más que como librería de producción. |
| [cosmos](human/fichas/cosmos.md) | defer | deferred | plataforma de "world foundation models" de NVIDIA para IA física y embodiment, capaz de generar mundos y datos sintéticos para entrenar agentes y robots. |
| [data-science-ipython-notebooks](human/fichas/data-science-ipython-notebooks.md) | reference | reference_only | gran colección de notebooks de ciencia de datos y machine learning que cubre desde pandas y NumPy hasta deep learning y big data, con ejemplos listos para ejecutar. |
| [awesome-bigdata](human/fichas/awesome-bigdata.md) | reference | reference_only | directorio curado de frameworks, bases de datos y herramientas de big data, organizado por categorías para descubrir el ecosistema de datos a escala. |
| [openai-python](human/fichas/openai-python.md) | reference | reference_only | SDK oficial de OpenAI para Python, que expone de forma tipada y cómoda la API (chat, embeddings, imágenes, audio) y es la base habitual para apps que usan sus modelos. |

### 8. [Workspaces de IA Local & Notebooks](human/categorias/08-workspaces-de-ia-local-notebooks.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [ECC](human/fichas/ecc.md) | defer | deferred | sistema operativo/arnés unificado para desarrollar, ejecutar y desplegar en local agentes de IA de alto rendimiento de forma segura, sirviendo de capa intermedia entre el modelo y tu sistema. |
| [odysseus](human/fichas/odysseus.md) | defer | deferred | workspace auto-hospedado que unifica chats, research, documentos, correo, calendario y tareas operados por agentes locales, a modo de centro administrativo personal privado. |
| [open-notebook](human/fichas/open-notebook.md) | reference | reference_only | clon open-source y privado de Google NotebookLM para procesar notas y fuentes locales (PDFs, webs, texto) y generar resúmenes, chats y audios sin salir de tu equipo. |
| [notebooklm-py](human/fichas/notebooklm-py.md) | reference | reference_only | API Python no oficial para interactuar programáticamente con NotebookLM de Google, controlando notebooks, fuentes y generación de notas desde código. |
| [notebooklm-mcp-cli](human/fichas/notebooklm-mcp-cli.md) | reference | reference_only | CLI interactivo y servidor MCP para NotebookLM de Google, pensado para operar notebooks en la nube desde terminal o desde clientes compatibles con MCP. |

### 9. [Diseño, UI & Frontend](human/categorias/09-dise-o-ui-frontend.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [open-design](human/fichas/open-design.md) | reference | reference_only | editor/workspace de diseño colaborativo asistido por IA que genera, maqueta y anima interfaces a partir de instrucciones en lenguaje natural; alternativa libre a Claude Design Artifacts. |
| [penpot](human/fichas/penpot.md) | defer | deferred | plataforma open-source de diseño y prototipado colaborativo, pensada para equipos de producto y diseño que quieren soberanía sobre sus archivos. |
| [plasmic](human/fichas/plasmic.md) | reference | reference_only | builder visual para apps y sitios conectado a tu propia base de código, que permite diseñar y publicar sin perder el control del código real. |
| [design.md](human/fichas/designmd.md) | reference | reference_only | especificación de formato para describir una identidad visual a agentes de código (tokens YAML + prosa), de modo que el agente herede un sistema de diseño coherente. |
| [impeccable](human/fichas/impeccable.md) | reference | reference_only | guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. |
| [tailwindcss](human/fichas/tailwindcss.md) | reference | reference_only | framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. |
| [magicui](human/fichas/magicui.md) | reference | reference_only | librería de componentes UI visualmente atractivos (animaciones, efectos, secciones) para montar interfaces modernas con buen acabado desde el inicio. |
| [heroui](human/fichas/heroui.md) | reference | reference_only | librería de componentes React accesibles y lista para producción (React Aria + Tailwind), orientada a SaaS, dashboards y landings consistentes. |
| [ui (shadcn)](human/fichas/ui-shadcn.md) | reference | reference_only | colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. |
| [normalize.css](human/fichas/normalizecss.md) | reference | reference_only | hoja de estilos que normaliza los defaults entre navegadores para partir de una base de rendering uniforme. |
| [GSAP](human/fichas/gsap.md) | reference | reference_only | librería de animación de alto rendimiento para la web, capaz de orquestar timelines complejos y efectos sincronizados. |
| [motion](human/fichas/motion.md) | reference | reference_only | librería de animación declarativa para React/JS (antes Framer Motion) que añade transiciones y microinteracciones con muy poco código. |
| [three.js](human/fichas/threejs.md) | reference | reference_only | motor 3D (WebGL) para renderizar gráficos y escenas interactivas directamente en el navegador. |
| [react-three-fiber](human/fichas/react-three-fiber.md) | reference | reference_only | renderer de React para three.js que expresa escenas 3D como componentes declarativos y reactivos. |
| [swr](human/fichas/swr.md) | reference | reference_only | librería de data fetching para React (stale-while-revalidate) que sirve datos cacheados al instante y los revalida en segundo plano. |

### 10. [Analítica & Visualización](human/categorias/10-anal-tica-visualizaci-n.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [posthog](human/fichas/posthog.md) | defer | deferred | plataforma de product analytics y eventos para entender el comportamiento de usuarios, con funnels, session replay y feature flags en una sola suite. |
| [metabase](human/fichas/metabase.md) | reference | reference_only | herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. |
| [dash](human/fichas/dash.md) | reference | reference_only | framework para construir aplicaciones analíticas interactivas en Python combinando gráficos Plotly con componentes de UI reactivos. |
| [echarts](human/fichas/echarts.md) | reference | reference_only | librería de visualización potente para gráficos y dashboards web (proyecto Apache), con decenas de tipos de gráfico y soporte de grandes volúmenes de datos. |
| [uPlot](human/fichas/uplot.md) | reference | reference_only | librería ultraligera para gráficos de series temporales capaz de pintar cientos de miles de puntos sin penalizar el rendimiento. |
| [streamlit](human/fichas/streamlit.md) | reference | reference_only | framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. |
| [awesome-dataviz](human/fichas/awesome-dataviz.md) | reference | reference_only | directorio curado de herramientas, librerías y recursos de visualización de datos recopilados por la comunidad. |

### 11. [Generación de Imagen & Visión](human/categorias/11-generaci-n-de-imagen-visi-n.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [ComfyUI](human/fichas/comfyui.md) | defer | deferred | motor local modular para crear pipelines visuales de generación con IA mediante un grafo de nodos, donde cada paso (carga de modelo, sampling, postproceso) es un bloque conectable y reutilizable. |
| [stable-diffusion-webui](human/fichas/stable-diffusion-webui.md) | defer | deferred | interfaz web local de referencia para Stable Diffusion (AUTOMATIC1111), que expone txt2img, img2img, inpainting y cientos de extensiones desde el navegador. |
| [Fooocus](human/fichas/fooocus.md) | reference | reference_only | herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. |
| [InvokeAI](human/fichas/invokeai.md) | defer | deferred | suite profesional y unificada para Stable Diffusion que combina una UI pulida con canvas, capas, inpainting y gestión de modelos y workflows. |
| [diffusers](human/fichas/diffusers.md) | defer | deferred | librería de Hugging Face para construir y ejecutar pipelines de modelos de difusión (imagen, video, audio) desde código, con APIs estandarizadas para schedulers y modelos. |
| [ControlNet](human/fichas/controlnet.md) | defer | deferred | método y modelos para condicionar la generación text-to-image con señales externas como poses, bordes, profundidad o mapas de segmentación, fijando la estructura del resultado. |
| [sd-webui-controlnet](human/fichas/sd-webui-controlnet.md) | defer | deferred | extensión que integra el control estructural de ControlNet directamente en Stable Diffusion WebUI, con preprocesadores para poses, bordes, profundidad y más. |
| [ComfyUI_IPAdapter_plus](human/fichas/comfyui-ipadapter-plus.md) | defer | deferred | conjunto de nodos para ComfyUI que implementa IPAdapter, permitiendo condicionar la generación con una imagen de referencia para transferir estilo o identidad. |
| [GFPGAN](human/fichas/gfpgan.md) | reference | reference_only | algoritmo de restauración facial que reconstruye rostros degradados o de baja calidad usando priors generativos (GAN) preentrenados. |
| [Real-ESRGAN](human/fichas/real-esrgan.md) | reference | reference_only | herramienta de superresolución y restauración para imágenes reales que reescala y limpia material de baja calidad sin rehacerlo. |
| [LivePortrait](human/fichas/liveportrait.md) | defer | deferred | sistema eficiente para animar retratos estáticos, transfiriendo el movimiento facial de un video de referencia a una sola imagen de origen. |
| [Deep-Live-Cam](human/fichas/deep-live-cam.md) | defer | deferred | herramienta de face swap y deepfake en tiempo real a partir de una sola imagen, aplicable a webcam o video con salvaguardas de uso. |
| [face_recognition](human/fichas/face-recognition.md) | reference | reference_only | librería de Python sencilla para detección y reconocimiento facial, con una API de alto nivel para localizar, comparar e identificar caras en imágenes. |
| [Open-Generative-AI](human/fichas/open-generative-ai.md) | reference | reference_only | plataforma alternativa libre a servicios premium de video/imagen que agrupa más de 200 modelos generativos accesibles desde terminal o integrados con agentes. |
| [fluxer](human/fichas/fluxer.md) | reference | reference_only | plataforma generativa emergente con foco en audio y video mejorados, ofrecida como cliente Canary web/desktop; su API y self-host aún están en finalización. |

### 12. [Audio, Voz & Video](human/categorias/12-audio-voz-video.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [whisper](human/fichas/whisper.md) | reference | reference_only | modelo de reconocimiento de voz y traducción de audio multilingüe de OpenAI, estándar de la industria que transcribe casi cualquier idioma con un solo modelo. |
| [faster-whisper](human/fichas/faster-whisper.md) | reference | reference_only | reimplementación de Whisper sobre CTranslate2 que transcribe mucho más rápido y con menor consumo de memoria, manteniendo la misma precisión. |
| [whisperX](human/fichas/whisperx.md) | reference | reference_only | extensión de Whisper que añade alineación temporal a nivel de palabra y diarización de hablantes, ideal para subtitulado profesional. |
| [supertonic](human/fichas/supertonic.md) | reference | reference_only | motor TTS multilingüe ultrarrápido de Supertone que sintetiza voz directamente en el dispositivo, incluso en el navegador vía WebGPU. |
| [VoxCPM](human/fichas/voxcpm.md) | defer | deferred | sistema TTS de alta fidelidad de OpenBMB que prescinde del tokenizador tradicional para lograr una prosodia y fluidez muy naturales, con clonación de voz. |
| [TTS](human/fichas/tts.md) | reference | reference_only | toolkit open-source de Coqui para síntesis de voz local y multilingüe, con decenas de modelos preentrenados y clonación de voz. |
| [OmniVoice-Studio](human/fichas/omnivoice-studio.md) | reference | reference_only | suite de voz de escritorio open-source planteada como alternativa a ElevenLabs, con dictado en tiempo real, clonación zero-shot y doblaje de video en hasta 646 idiomas, todo local. |
| [lossless-cut](human/fichas/lossless-cut.md) | reference | reference_only | aplicación de escritorio para recortar, fusionar y reorganizar video/audio sin recodificar, conservando la calidad original. |
| [moviepy](human/fichas/moviepy.md) | reference | reference_only | librería Python para edición de video programática: cortar, concatenar, superponer texto, subtítulos y audio, y exportar el resultado. |
| [remotion](human/fichas/remotion.md) | reference | reference_only | framework para crear videos por código usando React, definiendo cada frame como un componente y renderizando a MP4. |
| [videofy_minimal](human/fichas/videofy-minimal.md) | reference | reference_only | herramienta minimalista (de Schibsted) que convierte contenido textual en videos cortos de forma local, sin pipeline complejo. |
| [OpenCut](human/fichas/opencut.md) | reference | reference_only | editor de video open-source con UI moderna, planteado como alternativa libre tipo CapCut, usable en web o escritorio. |
| [openscreen](human/fichas/openscreen.md) | reference | reference_only | herramienta ligera de grabación de pantalla para screencasts y demos; el proyecto original está archivado y continúa mediante un fork comunitario. |
| [Youtube2Webpage](human/fichas/youtube2webpage.md) | reference | reference_only | script en Perl que genera una página web legible a partir de un video de YouTube, intercalando la transcripción de subtítulos con capturas de pantalla del momento citado. |
| [hyperframes](human/fichas/hyperframes.md) | reference | reference_only | framework npm para generar animaciones frame a frame de forma programática desde código. |

### 13. [Documentos & Presentaciones](human/categorias/13-documentos-presentaciones.md)

| Repo | Decision | Instalacion | Resumen |
|---|---|---|---|
| [markitdown](human/fichas/markitdown.md) | use_now | local_project | utilidad Python de Microsoft que convierte archivos complejos (PDF, Word, Excel, PowerPoint, HTML, imágenes, audio) a Markdown limpio optimizado para que los LLMs lo consuman. |
| [ppt-master](human/fichas/ppt-master.md) | reference | reference_only | generador que transforma documentos de texto en presentaciones PowerPoint (.pptx) editables nativas, listas para abrir y ajustar en Office. |
| [pdfcraft](human/fichas/pdfcraft.md) | reference | reference_only | conjunto de herramientas PDF gratuitas, privadas y basadas en navegador para combinar, dividir, comprimir y convertir archivos sin instalar nada. |
| [reveal.js](human/fichas/revealjs.md) | reference | reference_only | framework veterano para crear presentaciones (slides) en HTML, con transiciones, temas, fragmentos y modo orador integrados. |

