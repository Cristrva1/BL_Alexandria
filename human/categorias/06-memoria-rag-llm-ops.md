[🏠 Inicio](../README.md) · [📚 Catálogo](../../Catalogo.md) · [⬅️ 5. MCP & Conectividad](05-mcp-conectividad.md) · [7. Inteligencia de Código, Datos & Entrenamiento ➡️](07-inteligencia-de-c-digo-datos-entrenamiento.md)

# 🧬 6. Memoria, RAG & LLM Ops

> Memoria persistente para agentes, RAG, bases vectoriales, serving y gateways de LLM, ahorro de tokens y observabilidad.

**32 repos** · 6 subcategorías · ⭐ 1.3M estrellas en total · 🆕 20 sugeridos nuevos

## ⭐ Imprescindibles

Si solo vas a mirar unos pocos, empieza por estos:

| Repo | ⭐ | Qué hace | Instalación |
|---|---:|---|---|
| [claude-mem](../fichas/claude-mem.md) | 116k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | `/plugin marketplace add thedotmack/claude-mem` |
| [RAGFlow](../fichas/ragflow.md) | 94k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | `git clone https://github.com/infiniflow/ragflow && cd ragflow/docker && docker compose up -d` |
| [Qdrant](../fichas/qdrant.md) | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | `docker run -p 6333:6333 qdrant/qdrant` |
| [vLLM](../fichas/vllm.md) | 96.7k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | `pip install vllm` |
| [headroom](../fichas/headroom.md) | 79.3k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | `pip` |
| [promptfoo](../fichas/promptfoo.md) | 27k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | `npx promptfoo@latest init` |

## 🧭 Subcategorías

- [Memoria persistente para agentes](#memoria-persistente-para-agentes) — 9 repos
- [RAG y motores de conocimiento](#rag-y-motores-de-conocimiento) — 4 repos
- [Bases vectoriales y búsqueda semántica](#bases-vectoriales-y-búsqueda-semántica) — 6 repos
- [Serving y gateways de LLM](#serving-y-gateways-de-llm) — 3 repos
- [Ahorro de contexto y tokens](#ahorro-de-contexto-y-tokens) — 1 repos
- [Observabilidad, evaluación y guardrails](#observabilidad-evaluación-y-guardrails) — 9 repos

## Memoria persistente para agentes

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [claude-mem](../fichas/claude-mem.md) 🆕 | 116k | Plugin que da memoria persistente entre sesiones a Claude Code y otros agentes, comprimida con IA. | usas Claude Code a diario y repites contexto entre sesiones | 🟢 |
| [mem0](../fichas/mem0.md) | 68.7k | Capa de memoria persistente para agentes y apps de IA que guarda, recupera y actualiza recuerdos del usuario y de la sesión de forma incremental. | quieres memoria estándar lista con integraciones amplias | 🟢 |
| [mempalace](../fichas/mempalace.md) | 60.5k | Memoria de IA local-first con almacenamiento verbatim y backend conectable, pensada para alto recall sin enviar datos a servicios externos. | la privacidad es prioridad y no quieres llamadas a API | 🟢 |
| [cognee](../fichas/cognee.md) 🆕 | 33.2k | Plataforma de memoria para agentes que combina grafos de conocimiento y vectores, usable con modelos pequeños. | quieres memoria basada en grafo con poco esfuerzo | 🟢 |
| [Graphiti](../fichas/graphiti.md) 🆕 | 32.7k | Librería de Zep para construir grafos de conocimiento temporales en tiempo real para agentes. | necesitas memoria que cambie con el tiempo y se pueda consultar | 🟡 |
| [supermemory](../fichas/supermemory.md) 🆕 | 31.6k | Motor de memoria y contexto muy rápido, con API para apps de IA y app propia, ejecutable en local. | quieres una API de memoria lista para tu app | 🟢 |
| [agentmemory](../fichas/agentmemory.md) | 30.3k | Memoria persistente para agentes de código (Claude Code, Copilot CLI, Cursor, Gemini CLI, Codex…), construida sobre el motor iii y expuesta como capa común entre clientes. | cambias de asistente y quieres una memoria común entre ellos | 🟢 |
| [Letta](../fichas/letta.md) 🆕 | 25.4k | Plataforma para agentes con estado y memoria avanzada que aprenden con el tiempo (antes MemGPT). | quieres agentes con memoria de largo plazo gestionada | 🟡 |
| [Engram](../fichas/engram.md) | 7.9k | Memoria persistente para agentes de código en un solo binario Go con SQLite, MCP, API y TUI. | quieres memoria local simple para cualquier agente | 🟢 |

## RAG y motores de conocimiento

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [RAGFlow](../fichas/ragflow.md) 🆕 | 94k | Motor de RAG con comprensión profunda de documentos, citas y agentes, auto-hospedable. | tus documentos son complejos y necesitas citas fiables | 🔴 |
| [LightRAG](../fichas/lightrag.md) 🆕 | 40.6k | RAG simple y rápido que combina grafo de conocimiento y vectores, de la Universidad de Hong Kong. | quieres RAG con grafo sin el coste de GraphRAG | 🟡 |
| [PageIndex](../fichas/pageindex.md) 🆕 | 40.3k | Índice de documentos para RAG sin vectores, basado en razonamiento sobre una tabla de contenidos. | tus documentos son largos y con estructura clara | 🟢 |
| [graphrag](../fichas/graphrag.md) | 36.6k | Sistema de RAG de Microsoft que recupera información sobre un grafo de conocimiento extraído del corpus, en lugar de buscar solo fragmentos sueltos por similitud. | tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | 🟡 |

## Bases vectoriales y búsqueda semántica

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [Qdrant](../fichas/qdrant.md) 🆕 | 35.5k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. | quieres una base vectorial dedicada y rápida | 🟢 |
| [Milvus](../fichas/milvus.md) 🆕 | 46.6k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. | esperas volúmenes muy grandes de vectores | 🔴 |
| [Faiss](../fichas/faiss.md) 🆕 | 41.3k | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. | necesitas índices vectoriales en memoria y máximo control | 🟡 |
| [Chroma](../fichas/chroma.md) 🆕 | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. | empiezas con RAG y quieres lo más simple | 🟢 |
| [pgvector](../fichas/pgvector.md) 🆕 | 23.6k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. | ya usas PostgreSQL y quieres vectores | 🟢 |
| [turbovec](../fichas/turbovec.md) | 17.5k | Librería de búsqueda vectorial rápida basada en la cuantización TurboQuant, pensada como capa de recuperación embebida. | necesitas vector search veloz y embebido sin desplegar una DB | 🟢 |

## Serving y gateways de LLM

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [vLLM](../fichas/vllm.md) | 96.7k | Motor de inferencia y servicio de LLM de alto rendimiento y uso eficiente de memoria en GPU. | necesitas servir LLM abiertos a muchos usuarios en GPU | 🔴 |
| [litellm](../fichas/litellm.md) | 63k | Gateway/SDK que unifica el acceso a 100+ proveedores de LLM bajo una sola interfaz compatible con el formato de OpenAI. | trabajas con múltiples modelos o quieres fallback/control de costos | 🟢 |
| [SGLang](../fichas/sglang.md) 🆕 | 38.7k | Framework de servicio de alto rendimiento para LLM y modelos multimodales. | buscas el máximo rendimiento en servicio de LLM | 🔴 |

## Ahorro de contexto y tokens

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [headroom](../fichas/headroom.md) | 79.3k | Utilidad para compactar contexto y aprovechar mejor la ventana del modelo, condensando texto largo sin perder lo esencial. | te quedas sin contexto en sesiones largas | 🟢 |

## Observabilidad, evaluación y guardrails

| Repo | ⭐ | Qué hace | Ideal si… | Setup |
|---|---:|---|---|:---:|
| ⭐ [promptfoo](../fichas/promptfoo.md) 🆕 | 27k | CLI para probar prompts, agentes y RAG, comparar modelos y hacer red teaming de seguridad. | quieres pruebas automáticas de prompts y seguridad | 🟢 |
| [langfuse](../fichas/langfuse.md) | 37.3k | Plataforma open-source de observabilidad, trazas y evaluación para apps LLM, con vista detallada de cada llamada y agente. | operas agentes en serio y necesitas trazas/costes/eval | 🟡 |
| [MLflow](../fichas/mlflow.md) 🆕 | 28.7k | Plataforma open source para el ciclo de vida de modelos de ML y apps de LLM: experimentos, trazas y registro. | tu equipo hace ML clásico y LLM y quiere una sola plataforma | 🟢 |
| [loguru](../fichas/loguru.md) | 24.2k | Librería de logging para Python centrada en la simplicidad ("logging that doesn't suck"), lista para usar sin configuración previa. | quieres logging fácil y legible en Python sin pelear con stdlib | 🟢 |
| [Opik](../fichas/opik.md) 🆕 | 23.3k | Plataforma de Comet para depurar, evaluar y monitorear apps de LLM, RAG y agentes. | quieres observabilidad y evaluación en un solo producto abierto | 🟡 |
| [DeepEval](../fichas/deepeval.md) 🆕 | 19.4k | Framework de evaluación de LLM al estilo pytest, con decenas de métricas listas. | quieres tests de LLM en Python como pytest | 🟢 |
| [Ragas](../fichas/ragas.md) 🆕 | 16.3k | Librería para evaluar aplicaciones de LLM y RAG con métricas objetivas y datos de prueba sintéticos. | evalúas un sistema RAG | 🟢 |
| [Phoenix](../fichas/phoenix.md) 🆕 | 12.2k | Plataforma open source de Arize para observar, trazar y evaluar apps de LLM, con OpenTelemetry. | quieres observabilidad basada en OpenTelemetry | 🟢 |
| [NeMo Guardrails](../fichas/guardrails.md) | 7.5k | Toolkit de NVIDIA para añadir barreras programables a sistemas conversacionales con LLM. | necesitas políticas de seguridad en un chatbot | 🟡 |

## ⚖️ ¿Cuál elegir?

Repos que cumplen la misma función: elige uno por grupo.

### claude-mem, RAGFlow, mem0, LightRAG, PageIndex, graphrag, cognee

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [claude-mem](../fichas/claude-mem.md) | 116k | usas Claude Code a diario y repites contexto entre sesiones | necesitas memoria para una app propia; mira `mem0` |
| [RAGFlow](../fichas/ragflow.md) | 94k | tus documentos son complejos y necesitas citas fiables | quieres algo ligero en un portátil; mira `anything-llm` |
| [mem0](../fichas/mem0.md) | 68.7k | quieres memoria estándar lista con integraciones amplias | necesitas todo local sin llamadas a API (mempalace) o control total del almacenamiento |
| [LightRAG](../fichas/lightrag.md) | 40.6k | quieres RAG con grafo sin el coste de GraphRAG | no necesitas relaciones entre entidades; usa RAG vectorial con `llama-index` |
| [PageIndex](../fichas/pageindex.md) | 40.3k | tus documentos son largos y con estructura clara | tienes miles de documentos cortos; usa búsqueda vectorial |
| [graphrag](../fichas/graphrag.md) | 36.6k | tu corpus tiene relaciones ricas y el RAG por fragmentos se queda corto | un RAG simple basta o el coste de indexado con LLM es prohibitivo |
| [cognee](../fichas/cognee.md) | 33.2k | quieres memoria basada en grafo con poco esfuerzo | necesitas un grafo temporal en tiempo real; mira `graphiti` |

### Qdrant, Milvus, Faiss, Chroma, pgvector

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [Qdrant](../fichas/qdrant.md) | 35.5k | quieres una base vectorial dedicada y rápida | ya tienes PostgreSQL y poco volumen; mira `pgvector` |
| [Milvus](../fichas/milvus.md) | 46.6k | esperas volúmenes muy grandes de vectores | tu proyecto es pequeño; mira `chroma` o `qdrant` |
| [Faiss](../fichas/faiss.md) | 41.3k | necesitas índices vectoriales en memoria y máximo control | quieres persistencia y API listas; mira `qdrant` |
| [Chroma](../fichas/chroma.md) | 29.7k | empiezas con RAG y quieres lo más simple | necesitas gran escala y filtros complejos; mira `qdrant` o `milvus` |
| [pgvector](../fichas/pgvector.md) | 23.6k | ya usas PostgreSQL y quieres vectores | tienes volúmenes muy grandes; mira `milvus` |

### vLLM, SGLang

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [vLLM](../fichas/vllm.md) | 96.7k | necesitas servir LLM abiertos a muchos usuarios en GPU | solo los usas tú en un portátil; mira `ollama` |
| [SGLang](../fichas/sglang.md) | 38.7k | buscas el máximo rendimiento en servicio de LLM | quieres la opción más documentada; mira `vllm` |

### promptfoo, DeepEval, Ragas

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [promptfoo](../fichas/promptfoo.md) | 27k | quieres pruebas automáticas de prompts y seguridad | necesitas observabilidad en producción; mira `langfuse` |
| [DeepEval](../fichas/deepeval.md) | 19.4k | quieres tests de LLM en Python como pytest | prefieres configurar en YAML y comparar modelos; mira `promptfoo` |
| [Ragas](../fichas/ragas.md) | 16.3k | evalúas un sistema RAG | necesitas red teaming de seguridad; mira `promptfoo` |

### langfuse, MLflow, Opik, Phoenix

| Repo | ⭐ | Elígelo si… | Evítalo si… |
|---|---:|---|---|
| [langfuse](../fichas/langfuse.md) | 37.3k | operas agentes en serio y necesitas trazas/costes/eval | haces prototipos triviales o no quieres operar el backend |
| [MLflow](../fichas/mlflow.md) | 28.7k | tu equipo hace ML clásico y LLM y quiere una sola plataforma | solo trazas LLM y quieres algo más ligero; mira `langfuse` |
| [Opik](../fichas/opik.md) | 23.3k | quieres observabilidad y evaluación en un solo producto abierto | prefieres la opción más extendida; mira `langfuse` |
| [Phoenix](../fichas/phoenix.md) | 12.2k | quieres observabilidad basada en OpenTelemetry | buscas la plataforma más usada; mira `langfuse` |

## 🧪 Recetas que usan esta categoría

- [🔎 Agente de research profundo](../playbooks/agente-de-research-profundo.md) — Investigar un tema en la web y entregar un informe estructurado con fuentes citadas.
- [🏠 Workspace privado local soberano](../playbooks/workspace-privado-local-soberano.md) — Tener chat, documentos y memoria de IA en tu propia máquina, sin enviar datos a terceros.
- [🦙 ChatGPT privado con modelos locales](../playbooks/chatgpt-privado-local.md) — Tener un chat tipo ChatGPT para ti o tu equipo con modelos que corren en tu máquina o servidor.
- [📎 RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md) — Preguntarle a tus PDFs, manuales y bases de conocimiento con respuestas citadas.
- [🛠️ Agente de código potenciado](../playbooks/agente-de-codigo-potenciado.md) — Sacar el máximo a Claude Code, Codex u opencode con método, contexto actualizado y memoria.
- [📞 Agente de voz en tiempo real](../playbooks/agente-de-voz.md) — Un asistente que escucha y responde por voz con baja latencia, en web o por teléfono.

## 🏷️ Leyenda

⭐ imprescindible · 🆕 sugerido nuevo (aún no clonado en tu biblioteca) · Setup: 🟢 fácil · 🟡 medio · 🔴 pesado (GPU o varios servicios).

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-05.</sub>
