[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Qdrant

> Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 35.6k | Apache-2.0 | Rust | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🟢 fácil

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin API de IA en la ruta básica. La función básica es software convencional; no necesita un LLM. Las integraciones añadidas pueden requerir servicios. |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. La herramienta procesa o gestiona datos sin un modelo de lenguaje en su función básica. |
| Coste | Sin pago a un modelo en la ruta básica. Sin consumo de un modelo para la función básica. El alojamiento, servicios conectados y licencia se revisan aparte. |
| Equipo | Equipo normal; revisar dependencias. Consultar los requisitos del README y de los componentes que actives. |

El agente puede ayudarte a instalarlo. Una sesión del agente solo ejecuta esta aplicación si existe una integración documentada.

## Qué puedes hacer con él

Guarda embeddings con metadatos y los busca con filtros rápidos, a escala. Muy usada como memoria de RAG y agentes.

## Por qué destaca

Rápida, fácil de desplegar y con buena API; opción por defecto en muchos stacks.

## Cómo funciona

Índices HNSW con filtrado sobre payloads, cuantización y almacenamiento en disco.

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

1. Elige la ruta del README: paquete, aplicación o despliegue desde fuente.
2. Prepara sus dependencias y configura el modelo o las credenciales indicadas en Acceso y costes.
3. Ejecuta el ejemplo mínimo documentado y verifica el resultado antes de ampliar el proyecto.

[Instrucciones originales de instalación](https://github.com/qdrant/qdrant/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Qdrant para mi objetivo y necesito pasos guiados. Lee https://github.com/qdrant/qdrant/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Casos de uso

- Memoria vectorial para RAG
- Búsqueda semántica de productos
- Deduplicación por similitud

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| quieres una base vectorial dedicada y rápida | ya tienes PostgreSQL y poco volumen; mira `pgvector` |

## Stack y modelos

- **Stack:** Rust, Docker
- **Etiquetas:** `vector-db` `rag` `rust` `docker`
- **Modo de instalación sugerido:** 📖 **Referencia** — léelo o clónalo; no lo instales de entrada

## Combina con

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [LlamaIndex](llama-index.md) | 52.9k | Framework para conectar LLM con tus datos: ingesta, indexación, RAG y agentes sobre documentos. |
| [langchain](langchain.md) | 150k | Framework base para construir aplicaciones con LLMs (cadenas, agentes, RAG, herramientas). |
| [n8n](n8n.md) | 211k | Plataforma de automatización de workflows que integra APIs, servicios y procesos de negocio con IA mediante un editor visual basado en nodos. |

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Milvus](milvus.md) | 46.7k | Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |
| [pgvector](pgvector.md) | 23.7k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. |
| [Faiss](faiss.md) | 41.7k | Librería de Meta para búsqueda de similitud y clustering de vectores densos, en CPU y GPU. |

## Enlaces

- 🐙 GitHub: [qdrant/qdrant](https://github.com/qdrant/qdrant)
- 🌐 Web: <https://qdrant.tech>
- 🧪 Receta: [RAG sobre tus documentos](../playbooks/rag-sobre-documentos.md)

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-14. Lectura de documentación; no prueba de instalación o ejecución.

- [Fuente 1](https://github.com/qdrant/qdrant/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
