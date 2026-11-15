# 3. Construir agentes y coordinar equipos de IA — detalle de repos

> Abre este archivo SOLO si tienes finalistas en esta categoría.
> Cada entrada: desc, stack, instalación, choose/avoid, combina/compite.

## `adk-python`
role=library · exec=hybrid · setup=easy · mcp=False · prov=google,openai,anthropic · tags=agents,python

**Qué es:** Define agentes y sistemas multiagente con herramientas, memoria y evaluación, con interfaz web de pruebas incluida. Se despliega fácil en Google Cloud.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/google/adk-python

**Instalación** [+]: `pip install google-adk`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** trabajas con Gemini o Google Cloud
**Evita si:** tu stack es OpenAI; mira `openai-agents-python`
**Combina con:** `gemini-cli`, `fastmcp`
**Alternativas (elige una):** `langgraph`, `openai-agents-python`

## `ag2`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Modela conversaciones entre varios agentes que se delegan tareas hasta resolver un objetivo.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/ag2ai/ag2

**Instalación** [+]: `pip install ag2`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes multiagente serio en Python
**Evita si:** te basta un agente único o quieres orquestación visual
**Combina con:** `langchain`, `langfuse`
**Alternativas (elige una):** `autogen`

## `agent-framework`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic · tags=agents,python

**Qué es:** Une la simplicidad de AutoGen con las capacidades empresariales de Semantic Kernel: workflows con estado, observabilidad y despliegue en Azure.
**Stack:** Python, C#, .NET
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/microsoft/agent-framework

**Instalación** [+]: `pip install agent-framework`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** trabajas en el ecosistema Microsoft o .NET
**Evita si:** quieres el ecosistema open source más grande; mira `langgraph`
**Alternativas (elige una):** `autogen`, `semantic-kernel`

## `agno`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=agents,memory,python

**Qué es:** Construye agentes con memoria, RAG y herramientas, y sírvelos como API con su plataforma. Antes se llamaba Phidata.
**Stack:** Python, FastAPI
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/agno-agi/agno

**Instalación** [?]: `Seguir la instalación original: https://github.com/agno-agi/agno/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un framework de agentes con memoria y API lista
**Evita si:** necesitas grafos explícitos y controlables; mira `langgraph`
**Combina con:** `qdrant`, `mem0`
**Alternativas (elige una):** `crewai`

## `autogen`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=agents,python

**Qué es:** Popularizó los sistemas multiagente que conversan para resolver tareas. Microsoft recomienda usar Agent Framework para proyectos nuevos.
**Stack:** Python, .NET
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/microsoft/autogen

**Instalación** [?]: `Seguir la instalación original: https://github.com/microsoft/autogen/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** mantienes un proyecto que ya usa AutoGen
**Evita si:** empiezas algo nuevo; mira `agent-framework`
**Combina con:** `litellm`
**Alternativas (elige una):** `agent-framework`, `ag2`, `crewai`

## `autogpt`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=openai,anthropic · tags=agents,automation,python

**Qué es:** El famoso proyecto de agentes autónomos evolucionó a una plataforma con editor de bloques, marketplace y servidor para agentes que corren en segundo plano.
**Stack:** Python, TypeScript, Next.js, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. El proveedor y la función elegidos determinan si hacen falta credenciales de IA.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/Significant-Gravitas/AutoGPT

**Instalación** [?]: `Seguir la instalación original: https://github.com/Significant-Gravitas/AutoGPT/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres agentes continuos con un editor visual propio
**Evita si:** buscas algo ligero y fácil de operar; mira `sim` o `flowise`
**Combina con:** `n8n`
**Alternativas (elige una):** `sim`, `langflow`, `flowise`

## `awesome-langgraph`
role=directory · exec=cloud · setup=easy · mcp=False · prov=— · tags=automation,agents,javascript

**Qué es:** Es una lista curada, no una herramienta ejecutable.
**Stack:** Markdown / Python-JS (LangGraph)
**Acceso y costes:**
- API de IA: Sin API de IA en la ruta básica. Consultar el catálogo o material no llama a un modelo. Los ejemplos enlazados tienen requisitos propios.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. Leer una referencia no ejecuta un modelo.
- Coste: Sin pago a un modelo en la ruta básica. La consulta del material no consume una API de IA; no incluye el coste de ejecutar sus ejemplos.
- Equipo: Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/vonzosten/awesome-LangGraph

**Instalación** [?]: `Consultar el material original; elegir un ejemplo antes de instalar.`
_Una referencia no se instala como un servicio único._

**Elige si:** construyes con LangGraph y quieres patrones de referencia
**Evita si:** no usas ese ecosistema
**Combina con:** `langchain`

## `claude-agent-sdk-python`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=py,framework,python

**Qué es:** SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: API de IA opcional. El SDK utiliza Claude Code. Comprueba su autenticación: una sesión del plan y una API key son rutas distintas.
- Claude Code: Acceso oficial con sesión del plan
- Codex: Integración no documentada
- Modelos locales: La función básica no necesita un modelo. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: El coste depende del proveedor o la ruta. El uso consume el acceso de Claude configurado: límites del plan o créditos y facturación de API. El paquete del SDK no incluye una cuenta ni uso ilimitado.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/anthropics/claude-agent-sdk-python

**Instalación** [+]: `pip install claude-agent-sdk`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** buscas esta función: SDK oficial de Python para integrar el bucle de Claude Code, herramientas, sesiones y hooks en una aplicación propia.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `crewai`
role=library · exec=cloud · setup=easy · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Cada agente recibe un rol y objetivo, y el equipo coopera o se reparte el trabajo de forma secuencial o jerárquica.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/crewAIInc/crewAI

**Instalación** [?]: `Seguir la instalación original: https://github.com/crewAIInc/crewAI/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres velocidad y un modelo mental simple de "equipo"
**Evita si:** necesitas control de bajo nivel o orquestación muy custom
**Combina con:** `langchain`, `mem0`
**Alternativas (elige una):** `autogen`, `langgraph`, `agno`, `metagpt`

## `deepagents`
role=runtime · exec=hybrid · setup=easy · mcp=False · prov=anthropic,openai · tags=agents,python

**Qué es:** Da a cualquier modelo las capacidades de los agentes profundos (planificar, delegar, usar archivos) sin construirlas tú. Cada pieza se puede extender o reemplazar.
**Stack:** Python, LangGraph
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/langchain-ai/deepagents

**Instalación** [+]: `uv add deepagents`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un agente potente sin diseñar el bucle desde cero
**Evita si:** necesitas control total del grafo; usa `langgraph` directamente
**Combina con:** `langgraph`, `langfuse`
**Alternativas (elige una):** `openai-agents-python`

## `dify`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,agents,python,docker

**Qué es:** Combina orquestación de prompts, RAG, agentes, workflows y observabilidad en un mismo producto autoalojable.
**Stack:** Python/TS, React, PostgreSQL, Redis, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langgenius/dify

**Instalación** [?]: `Seguir la instalación original: https://github.com/langgenius/dify/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres una app IA completa autoalojada
**Evita si:** solo necesitas una librería o un prototipo puntual
**Combina con:** `langflow`, `flowise`
**Alternativas (elige una):** `sim`, `ragflow`

## `dspy`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=prompts,evaluation,python

**Qué es:** Defines módulos con firmas de entrada y salida y DSPy optimiza automáticamente los prompts y ejemplos con tus métricas. Útil para pipelines que deben mejorar con datos.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/stanfordnlp/dspy

**Instalación** [+]: `pip install dspy`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres optimizar prompts de forma sistemática con datos
**Evita si:** solo necesitas una llamada simple al modelo
**Combina con:** `ragas`, `mlflow`
**Alternativas (elige una):** `promptfoo`

## `flowise`
role=app · exec=hybrid · setup=easy · mcp=False · prov=— · tags=automation,agents,typescript,docker

**Qué es:** Constructor visual para diseñar aplicaciones de IA conectando modelos, herramientas, memoria y fuentes de datos. La instalación de Flowise y el acceso al modelo son decisiones separadas.
**Stack:** Node.js/TypeScript, React
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/FlowiseAI/Flowise

**Instalación** [+]: `npm install -g flowise`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres un prototipo visual ya, en stack JS
**Evita si:** necesitas plataforma completa con RAG/observabilidad (dify)
**Combina con:** `dify`, `langflow`
**Alternativas (elige una):** `sim`, `autogpt`

## `haystack`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=rag,agents,python

**Qué es:** Compone pipelines modulares de recuperación, generación y agentes con componentes intercambiables. Muy usado en búsqueda empresarial.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/deepset-ai/haystack

**Instalación** [+]: `pip install haystack-ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres pipelines de RAG explícitos y listos para producción
**Evita si:** buscas el ecosistema más grande de integraciones; mira `llama-index`
**Combina con:** `qdrant`, `docling`
**Alternativas (elige una):** `llama-index`, `langchain`

## `hermes-agent-self-evolution`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=experimentos,python

**Qué es:** Herramientas para optimizar skills, prompts y código de Hermes Agent mediante búsqueda evolutiva con DSPy y GEPA. Evalúa variantes de texto, analiza trazas y selecciona mejoras sin reentrenar pesos de un modelo.
**Stack:** Python, pyproject.toml
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/NousResearch/hermes-agent-self-evolution

**Instalación** [?]: `Seguir la instalación original: https://github.com/NousResearch/hermes-agent-self-evolution/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres experimentar con mejoras de Hermes medidas sobre un conjunto de evaluación
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Combina con:** `hermes-agent`

## `jev-fraud`
role=library · exec=hybrid · setup=medium · mcp=False · prov=— · tags=experimentos,template,typescript

**Qué es:** Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.
**Stack:** TypeScript, package.json
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta descrita necesita credenciales o acceso a un proveedor de IA independiente del agente que ayude a instalarla.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. La función básica no depende de un modelo de lenguaje. No se presenta como un asistente de IA autónomo.
- Coste: Consumo de APIs o servicios. Consultar cuotas, créditos y tarifas de los proveedores antes de ejecutar. El código no incluye ese consumo.
- Equipo: Equipo normal; revisar dependencias. Comprueba sistema operativo, memoria, disco y dependencias de la distribución elegida.
**Repo:** https://github.com/Nutlope/jev-fraud

**Instalación** [?]: `Seguir la instalación original: https://github.com/Nutlope/jev-fraud/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** buscas esta función: Demostración de clasificación con modelos y servicios de IA para estudiar un flujo de detección de fraude.
**Evita si:** buscas una aplicación lista y no quieres preparar un proyecto de código

## `langchain`
role=library · exec=cloud · setup=medium · mcp=False · prov=— · tags=agents,automation,python

**Qué es:** Ofrece abstracciones y conectores para casi cualquier modelo, base de datos vectorial y fuente de datos.
**Stack:** Python/JS/TS
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain-ai/langchain

**Instalación** [+]: `uv add langchain`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres la base estándar con máximas integraciones
**Evita si:** prefieres mínima abstracción o un solo proveedor sin cambiar
**Combina con:** `langflow`, `langfuse`, `litellm`
**Alternativas (elige una):** `llama-index`, `haystack`, `semantic-kernel`

## `langchain4j`
role=library · exec=hybrid · setup=medium · mcp=True · prov=— · tags=ts,anthropic,chatgpt,chroma,embeddings,gemini,gpt,huggingface

**Qué es:** Biblioteca de Java para integrar LLM, herramientas, agentes, RAG y almacenes vectoriales en aplicaciones de la JVM. Ofrece interfaces comunes para proveedores y conectores y se integra con frameworks de Java.
**Stack:** Java
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain4j/langchain4j

**Instalación** [?]: `Seguir la instalación original: https://github.com/langchain4j/langchain4j/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** tu aplicación usa Java y necesita integrar modelos o recuperación de documentos
**Evita si:** un flujo determinista resuelve el problema sin un agente

## `langflow`
role=app · exec=hybrid · setup=medium · mcp=False · prov=— · tags=automation,agents,python,docker

**Qué es:** Permite arrastrar y conectar componentes en un lienzo y exportarlos como API o código Python.
**Stack:** Python, React, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langflow-ai/langflow

**Instalación** [+]: `pip install langflow`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** prefieres construir en visual sobre LangChain
**Evita si:** quieres todo en código o no usas LangChain
**Combina con:** `langchain`, `dify`
**Alternativas (elige una):** `sim`, `autogpt`

## `langgraph`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,google,local · tags=agents,python

**Qué es:** Modela agentes y flujos multiagente como grafos de nodos con estado compartido y checkpoints. Pensado para agentes de producción que deben ser controlables y recuperables.
**Stack:** Python, LangChain
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain-ai/langgraph

**Instalación** [+]: `pip install -U langgraph`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** necesitas agentes con estado, control fino y persistencia
**Evita si:** quieres algo mínimo para un agente simple; mira `smolagents`
**Combina con:** `langchain`, `langfuse`
**Alternativas (elige una):** `crewai`, `openai-agents-python`, `pydantic-ai`, `langgraph-supervisor-py`, `adk-python`

## `langgraph-supervisor-py`
role=library · exec=hybrid · setup=easy · mcp=False · prov=— · tags=agents,python

**Qué es:** Facilitaba el patrón supervisor en sistemas multiagente. LangChain ahora recomienda implementar ese patrón directamente con herramientas.
**Stack:** Python, LangGraph
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain-ai/langgraph-supervisor-py

**Instalación** [+]: `pip install langgraph-supervisor`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** mantienes código que ya la usa
**Evita si:** empiezas un proyecto nuevo; usa el patrón con herramientas en `langgraph`
**Alternativas (elige una):** `langgraph`

## `langgraphjs`
role=runtime · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,typescript

**Qué es:** Lleva el modelo de grafos con estado, checkpoints y human-in-the-loop de LangGraph al ecosistema JavaScript.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/langchain-ai/langgraphjs

**Instalación** [+]: `npm install @langchain/langgraph @langchain/core`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres el modelo de LangGraph en TypeScript
**Evita si:** buscas una experiencia TS más integrada; mira `mastra`
**Combina con:** `langfuse`
**Alternativas (elige una):** `mastra`, `vercel-ai`

## `llama-index`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,local · tags=rag,agents,python

**Qué es:** Ofrece cargadores para cientos de fuentes, índices, motores de consulta y agentes centrados en documentos. Su plataforma LlamaParse procesa PDFs complejos.
**Stack:** Python, TypeScript
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/run-llama/llama_index

**Instalación** [+]: `pip install llama-index`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu proyecto gira alrededor de RAG sobre tus documentos
**Evita si:** necesitas orquestación general de agentes; mira `langgraph`
**Combina con:** `qdrant`, `docling`, `ragas`
**Alternativas (elige una):** `haystack`, `langchain`

## `llm-council`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=— · tags=agents,python

**Qué es:** Cada modelo aporta una respuesta y luego se contrastan para llegar a un consenso.
**Stack:** Python, React, FastAPI, PostgreSQL
**Acceso y costes:**
- API de IA: API de IA necesaria. La ruta documentada necesita credenciales de un proveedor de IA o servicio externo.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: Consumo de APIs o servicios. Revisar el plan, créditos, cuotas y facturación del proveedor antes de ejecutar.
- Equipo: Requisitos por confirmar. Consultar los requisitos del README y de los componentes que actives.
**Repo:** https://github.com/karpathy/llm-council

**Instalación** [?]: `Seguir la instalación original: https://github.com/karpathy/llm-council/blob/master/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres consenso entre modelos o comparar proveedores
**Evita si:** te basta un único LLM o el coste multi-modelo no es asumible
**Combina con:** `litellm`

## `mastra`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai,anthropic,google,local · tags=agents,rag,typescript

**Qué es:** Reúne en un solo paquete agentes con memoria, workflows con estado, RAG, evals y un playground local. Pensado para equipos web que trabajan en TypeScript.
**Stack:** TypeScript, Node.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/mastra-ai/mastra

**Instalación** [+]: `npm create mastra@latest`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu equipo trabaja en TypeScript y quiere agentes completos
**Evita si:** trabajas en Python; mira `langgraph` o `pydantic-ai`
**Combina con:** `copilotkit`, `langfuse`
**Alternativas (elige una):** `langgraphjs`, `vercel-ai`

## `metagpt`
role=runtime · exec=cloud · setup=medium · mcp=False · prov=— · tags=py,agent,gpt,llm,metagpt,multi-agent,python

**Qué es:** Framework de agentes que representa roles de un equipo de software para coordinar tareas de desarrollo. Asigna responsabilidades y artefactos a agentes que colaboran sobre un encargo.
**Stack:** Python, Docker
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/FoundationAgents/MetaGPT

**Instalación** [+]: `pip install --upgrade metagpt`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** quieres estudiar un flujo multiagente basado en roles de desarrollo
**Evita si:** un flujo determinista resuelve el problema sin un agente
**Alternativas (elige una):** `crewai`

## `mirofish`
role=platform · exec=hybrid · setup=heavy · mcp=False · prov=— · tags=agents,python

**Qué es:** Permite simular dinámicas sociales en un "sandbox". Proyecto de nicho.
**Stack:** Python/web, Docker, PostgreSQL
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/666ghj/MiroFish

**Instalación** [?]: `Seguir la instalación original: https://github.com/666ghj/MiroFish/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** simulas futuros/escenarios con muchos actores
**Evita si:** necesitas tareas deterministas o resultados reproducibles
**Combina con:** `openevolve`

## `openai-agents-python`
role=library · exec=hybrid · setup=easy · mcp=True · prov=openai · tags=agents,python

**Qué es:** Define agentes con instrucciones y herramientas, pasa el control entre ellos y añade validaciones. Funciona con modelos de OpenAI y otros compatibles.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/openai/openai-agents-python

**Instalación** [+]: `pip install openai-agents`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** usas OpenAI y quieres agentes multiagente con poco código
**Evita si:** necesitas control de estado avanzado; mira `langgraph`
**Combina con:** `openai-python`, `fastmcp`
**Alternativas (elige una):** `pydantic-ai`, `langgraph`, `smolagents`, `deepagents`, `adk-python`

## `openevolve`
role=runtime · exec=cloud · setup=heavy · mcp=False · prov=— · tags=automation,agents,python

**Qué es:** Genera, evalúa y muta candidatos de código a lo largo de múltiples generaciones.
**Stack:** Python, PyTorch/numpy, Rust
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/algorithmicsuperintelligence/openevolve

**Instalación** [+]: `pip install openevolve`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** optimizas problemas algorítmicos donde cabe explorar muchas variantes
**Evita si:** haces tareas de texto comunes o buscas respuesta inmediata
**Combina con:** `llm-council`

## `pydantic-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=agents,python

**Qué es:** Construye agentes con salidas validadas, herramientas tipadas e inyección de dependencias, al estilo FastAPI. Incluye evaluación y observabilidad con Logfire.
**Stack:** Python, Pydantic
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/pydantic/pydantic-ai

**Instalación** [?]: `Seguir la instalación original: https://github.com/pydantic/pydantic-ai/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres agentes tipados y validados en Python
**Evita si:** necesitas grafos complejos con persistencia; mira `langgraph`
**Combina con:** `langfuse`, `fastmcp`
**Alternativas (elige una):** `openai-agents-python`, `smolagents`, `langgraph`

## `semantic-kernel`
role=library · exec=hybrid · setup=medium · mcp=False · prov=openai · tags=agents,python

**Qué es:** Pensado para empresas que ya usan .NET o Java y quieren añadir IA con patrones conocidos. Su evolución para agentes es Microsoft Agent Framework.
**Stack:** C#, Python, Java
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/microsoft/semantic-kernel

**Instalación** [+]: `pip install semantic-kernel`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** tu app es .NET o Java y quieres IA integrada
**Evita si:** empiezas un sistema de agentes nuevo; mira `agent-framework`
**Alternativas (elige una):** `agent-framework`, `langchain`

## `sim`
role=platform · exec=hybrid · setup=medium · mcp=False · prov=openai,anthropic,local · tags=agents,automation,typescript

**Qué es:** Diseña agentes conectando bloques en un canvas, prueba en vivo y despliega como API o chat. Open source y auto-hospedable.
**Stack:** TypeScript, Next.js, PostgreSQL
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/simstudioai/sim

**Instalación** [?]: `Seguir la instalación original: https://github.com/simstudioai/sim/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un constructor visual de agentes moderno y abierto
**Evita si:** prefieres automatización general con cientos de apps; mira `n8n`
**Combina con:** `ollama`, `langfuse`
**Alternativas (elige una):** `flowise`, `langflow`, `dify`, `autogpt`

## `smolagents`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,local · tags=agents,python

**Qué es:** Sus agentes expresan las acciones como código en vez de JSON, lo que reduce pasos y errores. El núcleo cabe en unas mil líneas.
**Stack:** Python
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelos locales documentados. La ruta local está documentada; hay que instalar o descargar un modelo compatible.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. El tamaño y cuantización del modelo determinan RAM, VRAM y disco. No se promete rendimiento sin una prueba.
**Repo:** https://github.com/huggingface/smolagents

**Instalación** [?]: `Seguir la instalación original: https://github.com/huggingface/smolagents/blob/main/README.md`
_No se adivina el paquete ni se ejecuta un despliegue por el nombre del repo._

**Elige si:** quieres un agente simple y transparente en Python
**Evita si:** necesitas flujos con estado y aprobación humana; mira `langgraph`
**Combina con:** `e2b`, `transformers`
**Alternativas (elige una):** `pydantic-ai`, `openai-agents-python`

## `vercel-ai`
role=library · exec=hybrid · setup=easy · mcp=False · prov=openai,anthropic,google,local · tags=agents,ui,typescript,react

**Qué es:** Unifica la llamada a decenas de proveedores con una API común y trae hooks de React para chat con streaming. Es la base de muchos frameworks de agentes en TS.
**Stack:** TypeScript, React, Next.js
**Acceso y costes:**
- API de IA: Depende de la ruta elegida. Configura el modelo o proveedor antes de ejecutar. No asumir que la suscripción del agente cubre las llamadas de esta app.
- Claude Code: Integración no documentada
- Codex: Integración no documentada
- Modelos locales: Modelo local no documentado. No se confirma un backend local solo porque la aplicación se instale en tu equipo.
- Coste: El coste depende del proveedor o la ruta. Revisar modelo, conectores, alojamiento y licencia; no se publican importes estimados sin fuente.
- Equipo: Memoria y GPU según el modelo. Con un proveedor remoto importa el servidor de la app; con un modelo local, su RAM, GPU y disco.
**Repo:** https://github.com/vercel/ai

**Instalación** [+]: `npm install ai`
_Comando documentado en la fuente revisada; no equivale a una prueba de instalación._

**Elige si:** construyes una app web con IA en TypeScript
**Evita si:** necesitas agentes complejos con memoria y workflows; mira `mastra`
**Combina con:** `ui`, `assistant-ui`
**Alternativas (elige una):** `langgraphjs`, `mastra`
