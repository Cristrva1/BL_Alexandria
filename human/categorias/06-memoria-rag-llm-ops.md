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
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | Sin clave propia de API de IA en la ruta básica |

## Secciones

- [Memoria persistente para agentes](#memoria-persistente-para-agentes) — 11 repos
- [RAG y motores de conocimiento](#rag-y-motores-de-conocimiento) — 6 repos
- [Bases vectoriales y búsqueda semántica](#bases-vectoriales-y-búsqueda-semántica) — 6 repos

## Memoria persistente para agentes

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [claude-mem](../fichas/claude-mem.md) | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | Tu objetivo encaja con estos ejemplos: Conservar decisiones entre sesiones; Recuperar el motivo de un cambio de código | API de IA opcional |
| [mem0](../fichas/mem0.md) | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | Tu objetivo encaja con estos ejemplos: Recordar preferencias de atención; Mantener contexto de una app entre conversaciones | Depende de la ruta elegida |
| [mempalace](../fichas/mempalace.md) | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | Tu objetivo encaja con estos ejemplos: Recuperar decisiones antiguas; Consultar archivos de contexto sin resúmenes destructivos | API de IA opcional |
| [OpenViking](../fichas/openviking.md) | Base de contexto para agentes que organiza memoria, documentos y skills y permite consultar esa información. | Tu objetivo encaja con estos ejemplos: Conservar contexto de un proyecto; Consultar conocimientos y skills desde un almacén común | Depende de la ruta elegida |
| [cognee](../fichas/cognee.md) | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. | Tu objetivo encaja con estos ejemplos: Construir memoria de documentos; Recuperar contexto desde Claude Code o Codex | API de IA opcional |
| [Graphiti](../fichas/graphiti.md) | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. | Tu objetivo encaja con estos ejemplos: Representar cambios de una relación comercial; Conservar hechos de conversaciones con fechas | Depende de la ruta elegida |
| [supermemory](../fichas/supermemory.md) | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. | Tu objetivo encaja con estos ejemplos: Conservar contexto entre agentes; Buscar documentos y recuerdos de un proyecto | Depende de la ruta elegida |
| [agentmemory](../fichas/agentmemory.md) | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. | Tu objetivo encaja con estos ejemplos: Compartir contexto entre Claude Code y Codex; Consultar decisiones por proyecto | API de IA opcional |
| [Letta](../fichas/letta.md) | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). | Tu objetivo encaja con estos ejemplos: Estudiar un agente con memoria persistente; Crear un asistente que conserve preferencias | Depende de la ruta elegida |
| [Engram](../fichas/engram.md) | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | Tu objetivo encaja con estos ejemplos: Recordar decisiones técnicas; Hacer una entrega de contexto entre sesiones | Sin clave propia de API de IA en la ruta básica |
| [dsh-noema](../fichas/dsh-noema.md) | Plugin de memoria persistente para DeepSeek Harness con herramientas de consulta y opciones de configuración. | Tu objetivo encaja con estos ejemplos: Dar memoria a DeepSeek Harness; Importar una nota propia de otro agente | Sin clave propia de API de IA en la ruta básica |

## RAG y motores de conocimiento

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [RAGFlow](../fichas/ragflow.md) | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | Tu objetivo encaja con estos ejemplos: Consultar manuales de una organización; Combinar documentos en una base de conocimiento | Depende de la ruta elegida |
| [LightRAG](../fichas/lightrag.md) | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | Tu objetivo encaja con estos ejemplos: Consultar relaciones entre conceptos; Combinar búsqueda de grafos y vectores | Depende de la ruta elegida |
| [PageIndex](../fichas/pageindex.md) | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. | Tu objetivo encaja con estos ejemplos: Consultar informes largos por su estructura; Encontrar una sección de un contrato | Depende de la ruta elegida |
| [graphrag](../fichas/graphrag.md) | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. | Tu objetivo encaja con estos ejemplos: Estudiar relaciones de un corpus; Comparar búsqueda local y resumen global | Depende de la ruta elegida |
| [onyx](../fichas/onyx.md) | Plataforma de chat y búsqueda con IA sobre fuentes de una organización, con conectores y control de acceso. | Tu objetivo encaja con estos ejemplos: Buscar conocimiento de equipo; Dar contexto organizacional a un agente de código | Depende de la ruta elegida |
| [agentic-rag-for-dummies](../fichas/agentic-rag-for-dummies.md) | Ejemplo de RAG con agentes y LangGraph para consultar documentos, con una ruta local basada en Ollama. | Tu objetivo encaja con estos ejemplos: Aprender RAG por pasos; Comparar un pipeline local con otro proveedor | Depende de la ruta elegida |

## Bases vectoriales y búsqueda semántica

| Repo | Para qué sirve | Elígelo si… | API de IA |
|---|---|---|---|
| [Qdrant](../fichas/qdrant.md) | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | Tu objetivo encaja con estos ejemplos: Guardar embeddings de documentos; Combinar similitud y filtros de metadatos | Sin clave propia de API de IA en la ruta básica |
| [Milvus](../fichas/milvus.md) | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala | Sin clave propia de API de IA en la ruta básica |
| [Faiss](../fichas/faiss.md) | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. | Tu objetivo encaja con estos ejemplos: Comparar embeddings de imágenes; Experimentar con índices y compresión | Sin clave propia de API de IA en la ruta básica |
| [Chroma](../fichas/chroma.md) | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. | Tu objetivo encaja con estos ejemplos: Prototipar búsqueda semántica local; Filtrar fragmentos por metadatos | Sin clave propia de API de IA en la ruta básica |
| [pgvector](../fichas/pgvector.md) | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. | Tu objetivo encaja con estos ejemplos: Buscar similitud junto a datos SQL; Filtrar resultados vectoriales por columnas del negocio | Sin clave propia de API de IA en la ruta básica |
| [turbovec](../fichas/turbovec.md) | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. | Tu objetivo encaja con estos ejemplos: Explorar índices vectoriales embebidos; Reducir memoria de una búsqueda local | Sin clave propia de API de IA en la ruta básica |

## Recetas relacionadas

- [Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.

[Comparar alternativas](../comparativas/README.md) · [Cómo empezar](../instalar.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
