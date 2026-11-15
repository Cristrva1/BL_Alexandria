[Inicio](../README.md) · [Rutas por objetivo](../rutas.md) · [Acceso y costes](../acceso.md)

# Memoria, RAG y búsqueda de conocimiento

Memoria persistente, sistemas RAG y bases vectoriales. La memoria mantiene contexto; RAG recupera documentos; una base vectorial almacena el índice de búsqueda.

23 repos · 3 secciones

## Puntos de partida

Opciones editoriales para empezar a comparar. Elige por tu objetivo y acceso; no por las estrellas.

| Repo | Qué hace | Acceso básico |
|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | API de IA opcional |
| [RAGFlow](../fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | Depende de la ruta elegida |
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | Sin API de IA en la ruta básica |

## Secciones

- [Memoria persistente para agentes](#memoria-persistente-para-agentes) — 11 repos
- [RAG y motores de conocimiento](#rag-y-motores-de-conocimiento) — 6 repos
- [Bases vectoriales y búsqueda semántica](#bases-vectoriales-y-búsqueda-semántica) — 6 repos

## Memoria persistente para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | usas Claude Code a diario y repites contexto entre sesiones | API de IA opcional |
| [mem0](../fichas/mem0.md) | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | quieres memoria estándar lista con integraciones amplias | Depende de la ruta elegida |
| [mempalace](../fichas/mempalace.md) | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | la privacidad es prioridad y no quieres llamadas a API | Sin API de IA en la ruta básica |
| [OpenViking](../fichas/openviking.md) | Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. | buscas esta función: Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. | API de IA opcional |
| [cognee](../fichas/cognee.md) | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. | quieres memoria basada en grafo con poco esfuerzo | Depende de la ruta elegida |
| [Graphiti](../fichas/graphiti.md) | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. | necesitas memoria que cambie con el tiempo y se pueda consultar | Depende de la ruta elegida |
| [supermemory](../fichas/supermemory.md) | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. | quieres una API de memoria lista para tu app | Depende de la ruta elegida |
| [agentmemory](../fichas/agentmemory.md) | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. | cambias de asistente y quieres una memoria común entre ellos | Depende de la ruta elegida |
| [Letta](../fichas/letta.md) | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). | quieres agentes con memoria de largo plazo gestionada | Depende de la ruta elegida |
| [Engram](../fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | quieres memoria local simple para cualquier agente | Sin API de IA en la ruta básica |
| [dsh-noema](../fichas/dsh-noema.md) | Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. | buscas esta función: Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. | Sin API de IA en la ruta básica |

## RAG y motores de conocimiento

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [RAGFlow](../fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | tus documentos son complejos y necesitas citas fiables | Depende de la ruta elegida |
| [LightRAG](../fichas/lightrag.md) | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | quieres RAG con grafo sin el coste de GraphRAG | Depende de la ruta elegida |
| [PageIndex](../fichas/pageindex.md) | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. | tus documentos son largos y con estructura clara | API de IA opcional |
| [graphrag](../fichas/graphrag.md) | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. | tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | Depende de la ruta elegida |
| [onyx](../fichas/onyx.md) | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. | buscas esta función: Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. | API de IA opcional |
| [agentic-rag-for-dummies](../fichas/agentic-rag-for-dummies.md) | Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama. | buscas esta función: Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama. | API de IA opcional |

## Bases vectoriales y búsqueda semántica

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | quieres una base vectorial dedicada y rápida | Sin API de IA en la ruta básica |
| [Milvus](../fichas/milvus.md) | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | esperas volúmenes muy grandes de vectores | Sin API de IA en la ruta básica |
| [Faiss](../fichas/faiss.md) | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. | necesitas índices vectoriales en memoria y máximo control | Sin API de IA en la ruta básica |
| [Chroma](../fichas/chroma.md) | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. | empiezas con RAG y quieres lo más simple | Sin API de IA en la ruta básica |
| [pgvector](../fichas/pgvector.md) | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. | ya usas PostgreSQL y quieres vectores | Sin API de IA en la ruta básica |
| [turbovec](../fichas/turbovec.md) | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. | necesitas vector search veloz y embebido sin desplegar una DB | Sin API de IA en la ruta básica |

## Recetas relacionadas

- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
