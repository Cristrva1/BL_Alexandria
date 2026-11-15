[Inicio](README.md) · [Cómo elegir](elegir.md) · [Acceso y costes](acceso.md)

# ¿Qué quieres conseguir?

Empieza por un resultado. Los repos de entrada son opciones para comparar, no una lista que debas instalar completa.

## Programar con un agente

Elegir una herramienta de desarrollo y mejorar su flujo sin construir un agente desde cero.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Codex CLI](fichas/codex.md) | Agente de código ligero de OpenAI para la terminal, escrito en Rust y open source. | API de IA opcional |
| [Claude Code](fichas/claude-code.md) | Agente de código de Anthropic que trabaja en tu terminal, IDE o la web y entiende todo tu repositorio. | API de IA opcional |
| [OpenCode](fichas/opencode.md) | Agente de código open source para la terminal, compatible con más de 75 proveedores y modelos locales. | Depende de la ruta elegida |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=programar)

## Automatizar tareas y conectar apps

Diseñar flujos con disparadores, acciones y seguimiento.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [n8n](fichas/n8n.md) | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. | API de IA opcional |
| [activepieces](fichas/activepieces.md) | Plataforma open-source de automatización con IA, alternativa extensible a Zapier que conecta apps mediante flujos low-code y "pieces" reutilizables. | API de IA opcional |
| [Node-RED](fichas/node-red.md) | Editor visual de flujos por eventos para IoT, APIs y automatizaciones ligeras en Node.js. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=automatizar)

## Atender clientes por WhatsApp

Conectar el canal, decidir el flujo y pasar a una persona cuando haga falta.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [evolution-api](fichas/evolution-api.md) | API REST para automatizar WhatsApp y otros canales desde tus aplicaciones, con multi-instancia y webhooks. | Sin API de IA en la ruta básica |
| [WAHA](fichas/waha.md) | API REST de WhatsApp en un contenedor Docker, con varios motores y panel web. | Sin API de IA en la ruta básica |
| [chatwoot](fichas/chatwoot.md) | Plataforma open-source de soporte al cliente que unifica conversaciones de múltiples canales (WhatsApp, web, email, redes) en una sola bandeja de entrada. | API de IA opcional |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=whatsapp)

## Preguntar a documentos

Extraer el contenido y elegir una solución de búsqueda o RAG.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Docling](fichas/docling.md) | Librería de IBM que convierte PDF, DOCX, PPTX e imágenes en Markdown o JSON listos para IA. | API de IA opcional |
| [AnythingLLM](fichas/anything-llm.md) | App todo en uno para chatear con tus documentos y usar agentes con modelos locales o en la nube. | API de IA opcional |
| [RAGFlow](fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | Depende de la ruta elegida |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=documentos)

## Investigar un tema con fuentes

Combinar búsqueda y síntesis con trazabilidad de las fuentes.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [local-deep-research](fichas/local-deep-research.md) | Agente de investigación que combina buscadores, documentos y modelos locales o remotos para elaborar informes con fuentes. | Depende de la ruta elegida |
| [gpt-researcher](fichas/gpt-researcher.md) | Agente autónomo que investiga en línea y consolida reportes citados y estructurados. | Depende de la ruta elegida |
| [deer-flow](fichas/deer-flow.md) | Super-agente open-source que orquesta sub-agentes, memoria y sandboxes con skills extensibles. | Depende de la ruta elegida |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=investigar)

## Usar IA con modelos locales

Elegir un motor, un modelo y una interfaz que funcionen con tu equipo.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Ollama](fichas/ollama.md) | La forma más fácil de descargar y correr LLM en tu máquina, con API compatible con OpenAI. | Sin API de IA en la ruta básica |
| [Jan](fichas/jan.md) | Aplicación de escritorio para conversar con modelos locales y configurar proveedores remotos desde una misma interfaz. | API de IA opcional |
| [Open WebUI](fichas/open-webui.md) | Interfaz tipo ChatGPT auto-hospedada para Ollama y APIs compatibles con OpenAI, con RAG, voz y herramientas. | API de IA opcional |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=local)

## Crear una web o aplicación

Elegir componentes y añadir IA solo si el producto la necesita.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [ui](fichas/ui.md) | Colección de componentes copy-paste para React/Tailwind (shadcn/ui) que vives dentro de tu repo en lugar de instalar como dependencia cerrada. | Sin API de IA en la ruta básica |
| [tailwindcss](fichas/tailwindcss.md) | Framework CSS utility-first para construir interfaces rápido y consistente aplicando clases atómicas directamente en el marcado. | Sin API de IA en la ruta básica |
| [assistant-ui](fichas/assistant-ui.md) | Librería React y TypeScript para interfaces de chat con IA de calidad producción. | Depende de la ruta elegida |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=web)

## Crear o editar videos

Elegir entre editar material, programar escenas o generar clips.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [remotion](fichas/remotion.md) | Framework de React para crear videos por código y renderizar composiciones con contenido y tiempos definidos. | Sin API de IA en la ruta básica |
| [MoviePy](fichas/moviepy.md) | Librería Python para editar video por código: cortes, concatenaciones, títulos, composición por capas y efectos. | Sin API de IA en la ruta básica |
| [FFmpeg](fichas/ffmpeg.md) | Conjunto de librerías y CLI para convertir, cortar, filtrar y transmitir audio y video en casi cualquier formato. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=video)

## Transcribir audio a texto

Obtener texto o subtítulos a partir de una grabación.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [whisper.cpp](fichas/whisper-cpp.md) | Port de Whisper de OpenAI en C/C++ para transcribir audio rápido en CPU, Mac y móviles. | Sin API de IA en la ruta básica |
| [faster-whisper](fichas/faster-whisper.md) | Runtime de transcripción que ejecuta Whisper con CTranslate2 y opciones de CPU, GPU y cuantización. | Sin API de IA en la ruta básica |
| [whisperX](fichas/whisperx.md) | Pipeline de transcripción que añade alineación temporal de palabras y funciones de separación de hablantes. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=voz)

## Crear voz a partir de texto

Convertir un guion en narración con una ruta local o un servicio.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Kokoro](fichas/kokoro.md) | Modelo y biblioteca de texto a voz para generar narración localmente con distintas voces e idiomas compatibles. | Sin API de IA en la ruta básica |
| [supertonic](fichas/supertonic.md) | Motor de texto a voz que ofrece modelos y ejemplos para sintetizar audio en dispositivos y navegadores compatibles. | Sin API de IA en la ruta básica |
| [edge-tts](fichas/edge-tts.md) | Biblioteca y CLI de Python para sintetizar voz con el servicio en línea usado por Microsoft Edge. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=narrar)

## Generar o mejorar imágenes

Elegir una interfaz y revisar modelos, pesos y requisitos de GPU.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [ComfyUI](fichas/comfyui.md) | Motor local para crear pipelines de generación de imagen y video con IA mediante un grafo de nodos. | Sin API de IA en la ruta básica |
| [Fooocus](fichas/fooocus.md) | Herramienta de generación de imagen sobre SDXL pensada para dar buenos resultados con mínima configuración, ocultando parámetros técnicos tras presets inteligentes. | Sin API de IA en la ruta básica |
| [rembg](fichas/rembg.md) | Herramienta para quitar el fondo de imágenes en local, por CLI, librería o servidor. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=imagenes)

## Crear una presentación

Decidir si necesitas PowerPoint editable o diapositivas web.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [ppt-master](fichas/ppt-master.md) | Herramientas e instrucciones para que un agente cree presentaciones PowerPoint editables a partir de documentos. | Sin API de IA en la ruta básica |
| [Presenton](fichas/presenton.md) | Generador de presentaciones con IA, open source y con API, alternativa a Gamma o Beautiful.ai. | Depende de la ruta elegida |
| [Slidev](fichas/slidev.md) | Presentaciones para desarrolladores escritas en Markdown, con código en vivo y componentes Vue. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=presentaciones)

## Dibujar un diagrama

Explicar una idea con un dibujo, un esquema o un diagrama por código.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Excalidraw](fichas/excalidraw.md) | Pizarra virtual open source para diagramas con estilo dibujado a mano, colaborativa. | Sin API de IA en la ruta básica |
| [Mermaid](fichas/mermaid.md) | Genera diagramas de flujo, secuencia, Gantt y más a partir de texto similar a Markdown. | Sin API de IA en la ruta básica |
| [tldraw](fichas/tldraw.md) | SDK para construir apps de lienzo infinito en React, como pizarras y herramientas de diagramas. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=diagramas)

## Explorar datos y crear dashboards

Elegir una herramienta de BI o una librería de gráficos.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [metabase](fichas/metabase.md) | Herramienta de dashboards y BI para explorar métricas de negocio conectando directamente a tus bases de datos sin escribir SQL. | Sin API de IA en la ruta básica |
| [Apache Superset](fichas/superset.md) | Plataforma de exploración y visualización de datos de Apache, alternativa abierta a Tableau. | Sin API de IA en la ruta básica |
| [streamlit](fichas/streamlit.md) | Framework para levantar apps internas y prototipos de datos desde Python con solo unas líneas de script, sin tocar HTML ni JS. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=datos)

## Dar herramientas a mi agente

Buscar un servidor existente antes de programar un conector.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Context7](fichas/context7.md) | Servidor MCP que trae documentación actualizada y por versión de librerías al contexto del agente. | Sin API de IA en la ruta básica |
| [Playwright MCP](fichas/playwright-mcp.md) | Servidor MCP oficial de Microsoft que permite a los agentes navegar y operar páginas con Playwright. | Sin API de IA en la ruta básica |
| [GitHub MCP Server](fichas/github-mcp-server.md) | Servidor MCP oficial de GitHub para que los agentes lean repos, gestionen issues y PRs y revisen código. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=mcp)

## Mejorar Claude Code o Codex

Añadir instrucciones concretas al agente y conservar un conjunto pequeño.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [superpowers](fichas/superpowers.md) | Metodología completa de desarrollo para agentes construida sobre skills composables más instrucciones que aseguran que el agente realmente las invoque. | Sin API de IA en la ruta básica |
| [Agent Skills (Addy Osmani)](fichas/agent-skills.md) | Colección de Addy Osmani con skills de ingeniería para especificar, planificar, construir, verificar y revisar software con agentes. | Sin API de IA en la ruta básica |
| [impeccable](fichas/impeccable.md) | Guía de diseño para agentes de código (1 skill, 23 comandos, iteración en browser y 44 detectores de "tells" de UI por IA) que empuja al agente hacia frontends con criterio. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=skills)

## Aprender a construir con IA

Empezar por un curso o ejemplo antes de desplegar una plataforma.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [Generative AI for Beginners](fichas/generative-ai-for-beginners.md) | Curso de Microsoft para aprender los conceptos y construir ejemplos de aplicaciones con inteligencia artificial generativa. | Sin API de IA en la ruta básica |
| [ai-engineering-hub](fichas/ai-engineering-hub.md) | Colección de tutoriales y proyectos prácticos sobre LLM, RAG, agentes y aplicaciones de inteligencia artificial. | Sin API de IA en la ruta básica |
| [LLMs from Scratch](fichas/llms-from-scratch.md) | Código del libro de Sebastian Raschka para implementar un LLM tipo ChatGPT en PyTorch paso a paso. | Sin API de IA en la ruta básica |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=aprender)

## Investigar mercados y estrategias

Consultar herramientas y ejemplos financieros distinguiendo análisis, backtesting y ejecución.

| Punto de partida | Qué hace | Acceso básico |
|---|---|---|
| [qlib](fichas/qlib.md) | Plataforma de Microsoft para investigación cuantitativa con datos, modelos y evaluación de estrategias. | Sin API de IA en la ruta básica |
| [dexter](fichas/dexter.md) | Agente de investigación financiera que planifica consultas, obtiene datos de mercado y revisa sus análisis. | Depende de la ruta elegida |
| [TradingAgents](fichas/tradingagents.md) | Framework experimental que organiza agentes de análisis financiero, debate y evaluación de decisiones de trading. | Depende de la ruta elegida |

[Ver la ruta en el explorador](../docs/index.html#/explorar?goal=finanzas)
