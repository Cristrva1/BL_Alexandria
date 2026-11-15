[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Memoria, conocimiento y operación de IA

Guarda memoria, consulta documentos con RAG, sirve modelos y evalúa resultados. Una base vectorial y un sistema RAG completo resuelven capas distintas.

35 repos · 6 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | API de IA opcional |
| [RAGFlow](../fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | Depende de la ruta elegida |
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | Sin API de IA en la ruta básica |
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | Sin API de IA en la ruta básica |
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | API de IA opcional |
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | Depende de la ruta elegida |

## Secciones

- [Memoria persistente para agentes](#memoria-persistente-para-agentes) — 9 repos
- [RAG y motores de conocimiento](#rag-y-motores-de-conocimiento) — 4 repos
- [Bases vectoriales y búsqueda semántica](#bases-vectoriales-y-búsqueda-semántica) — 6 repos
- [Serving y gateways de LLM](#serving-y-gateways-de-llm) — 5 repos
- [Ahorro de contexto y tokens](#ahorro-de-contexto-y-tokens) — 2 repos
- [Observabilidad, evaluación y guardrails](#observabilidad-evaluación-y-guardrails) — 9 repos

## Memoria persistente para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | usas Claude Code a diario y repites contexto entre sesiones | API de IA opcional |
| [mem0](../fichas/mem0.md) | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | quieres memoria estándar lista con integraciones amplias | Depende de la ruta elegida |
| [mempalace](../fichas/mempalace.md) | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | la privacidad es prioridad y no quieres llamadas a API | Sin API de IA en la ruta básica |
| [cognee](../fichas/cognee.md) | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. | quieres memoria basada en grafo con poco esfuerzo | Depende de la ruta elegida |
| [Graphiti](../fichas/graphiti.md) | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. | necesitas memoria que cambie con el tiempo y se pueda consultar | Depende de la ruta elegida |
| [supermemory](../fichas/supermemory.md) | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. | quieres una API de memoria lista para tu app | Depende de la ruta elegida |
| [agentmemory](../fichas/agentmemory.md) | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. | cambias de asistente y quieres una memoria común entre ellos | Depende de la ruta elegida |
| [Letta](../fichas/letta.md) | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). | quieres agentes con memoria de largo plazo gestionada | Depende de la ruta elegida |
| [Engram](../fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | quieres memoria local simple para cualquier agente | Sin API de IA en la ruta básica |

## RAG y motores de conocimiento

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [RAGFlow](../fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | tus documentos son complejos y necesitas citas fiables | Depende de la ruta elegida |
| [LightRAG](../fichas/lightrag.md) | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | quieres RAG con grafo sin el coste de GraphRAG | Depende de la ruta elegida |
| [PageIndex](../fichas/pageindex.md) | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. | tus documentos son largos y con estructura clara | API de IA opcional |
| [graphrag](../fichas/graphrag.md) | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. | tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | Depende de la ruta elegida |

## Bases vectoriales y búsqueda semántica

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | quieres una base vectorial dedicada y rápida | Sin API de IA en la ruta básica |
| [Milvus](../fichas/milvus.md) | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | esperas volúmenes muy grandes de vectores | Sin API de IA en la ruta básica |
| [Faiss](../fichas/faiss.md) | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. | necesitas índices vectoriales en memoria y máximo control | Sin API de IA en la ruta básica |
| [Chroma](../fichas/chroma.md) | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. | empiezas con RAG y quieres lo más simple | Sin API de IA en la ruta básica |
| [pgvector](../fichas/pgvector.md) | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. | ya usas PostgreSQL y quieres vectores | Sin API de IA en la ruta básica |
| [turbovec](../fichas/turbovec.md) | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. | necesitas vector search veloz y embebido sin desplegar una DB | Sin API de IA en la ruta básica |

## Serving y gateways de LLM

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [vLLM](../fichas/vllm.md) | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | necesitas servir LLM abiertos a muchos usuarios en GPU | Sin API de IA en la ruta básica |
| [litellm](../fichas/litellm.md) | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | trabajas con múltiples modelos o quieres fallback/control de costos | Depende de la ruta elegida |
| [SGLang](../fichas/sglang.md) | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | buscas el máximo rendimiento en servicio de LLM | Sin API de IA en la ruta básica |
| [TensorRT-LLM](../fichas/tensorrt-llm.md) | Herramientas de NVIDIA para optimizar y desplegar inferencia de modelos de lenguaje con kernels y runtimes especializados. | despliegas LLM en GPU NVIDIA y necesitas optimizar la inferencia | Sin API de IA en la ruta básica |
| [backdoor](../fichas/backdoor.md) | Proxy de terceros que adapta proveedores de modelos para usarlos con el flujo de herramientas de Claude Code. | quieres estudiar cómo conectar otros modelos al harness de Claude Code | Depende de la ruta elegida |

## Ahorro de contexto y tokens

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [headroom](../fichas/headroom.md) | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | te quedas sin contexto en sesiones largas | API de IA opcional |
| [rtk](../fichas/rtk.md) | Proxy de terminal que compacta salidas de comandos para reducir el contexto que consumen los agentes de código. | tu agente consume demasiado contexto leyendo salidas extensas de terminal | API de IA opcional |

## Observabilidad, evaluación y guardrails

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [promptfoo](../fichas/promptfoo.md) | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | quieres pruebas automáticas de prompts y seguridad | Depende de la ruta elegida |
| [langfuse](../fichas/langfuse.md) | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | operas agentes en serio y necesitas trazas/costes/eval | API de IA opcional |
| [MLflow](../fichas/mlflow.md) | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | tu equipo hace ML clásico y LLM y quiere una sola plataforma | API de IA opcional |
| [loguru](../fichas/loguru.md) | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | quieres logging fácil y legible en Python sin pelear con stdlib | Sin API de IA en la ruta básica |
| [Opik](../fichas/opik.md) | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | quieres observabilidad y evaluación en un solo producto abierto | API de IA opcional |
| [DeepEval](../fichas/deepeval.md) | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | quieres tests de LLM en Python como pytest | Depende de la ruta elegida |
| [Ragas](../fichas/ragas.md) | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | evalúas un sistema RAG | Depende de la ruta elegida |
| [Phoenix](../fichas/phoenix.md) | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | quieres observabilidad basada en OpenTelemetry | API de IA opcional |
| [NeMo Guardrails](../fichas/guardrails.md) | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | necesitas políticas de seguridad en un chatbot | Depende de la ruta elegida |

## Recetas relacionadas

- [Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.
- [Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
