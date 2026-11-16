[🏠 Inicio](../README.md) › [🧬 Memoria, RAG y búsqueda de conocimiento](../categorias/06-memoria-rag-llm-ops.md) › Bases vectoriales y búsqueda semántica

# 🧮 Milvus

> Base de datos vectorial nativa de la nube para búsqueda a escala de miles de millones de vectores.

| Popularidad en GitHub | Licencia | Lenguaje | Añadido a Alexandria |
|---|---|---|---|
| 46.7k | Apache-2.0 | Go | 2026-11-10 |

**Ejecución** 🏠 local · **Rol** 🧩 motor/runtime · **Setup** 🔴 pesado

## ¿Qué es?

Base de datos vectorial de alto rendimiento y escalable, escrita en Go y C++, proyecto de la LF AI & Data Foundation bajo Apache 2.0. Madura y muy activa (v3.0.6), con versión gestionada en Zilliz Cloud.

## ¿Qué hace?

Organiza y busca grandes volúmenes de datos no estructurados (texto, imágenes, multimodal) por similitud vectorial, con soporte de los principales tipos de índice, búsqueda de texto completo con BM25 mediante vectores dispersos y búsqueda híbrida. Sirve desde prototipos hasta despliegues distribuidos de miles de millones de vectores.

## ¿Cómo lo hace?

Arquitectura distribuida nativa de Kubernetes que separa cómputo y almacenamiento, con aceleración por CPU y GPU. Se usa con el SDK `pymilvus` (`MilvusClient`); Milvus Lite (`pymilvus[milvus-lite]`) crea una base local en un archivo para empezar, y para servidor se despliega en Docker (standalone) o en Kubernetes.

## ¿Con qué otros repos se combina?

| Repo | Para qué juntarlos | Orden de instalación y cuidados |
|---|---|---|
| [AnythingLLM](anything-llm.md) | Base vectorial soportada por AnythingLLM. | Milvus primero; configura su URL en AnythingLLM antes de ingerir documentos. |
| [LightRAG](lightrag.md) | Backend de almacenamiento vectorial soportado. | Milvus primero; fija el modelo de embeddings antes de indexar. |
| [LlamaIndex](llama-index.md) | Integración documentada en la web de Milvus. | Instala el paquete de integración de LlamaIndex y apunta a Milvus Lite o al servidor. |

**Notas:** Alternativas (elige una): qdrant, chroma, pgvector.

Estado en GitHub: activo · último push 2026-11-16 · última versión publicada v3.0.6 (2026-11-11) · licencia declarada Apache-2.0 (consultado el 2026-11-15).

<sub>Descripción redactada a partir de la documentación del autor (revisada el 2026-11-15); no se instaló ni ejecutó. Fuentes: [1](https://github.com/milvus-io/milvus/blob/master/README.md) · [2](https://milvus.io/docs/integrate_with_llamaindex.md)</sub>

## Acceso, coste y equipo

[Cómo interpretar estas rutas](../acceso.md)

| Pregunta | Respuesta |
|---|---|
| API de IA | Sin clave propia de API de IA en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte |
| Claude Code | Integración no documentada |
| Codex | Integración no documentada |
| Antigravity | Integración no documentada |
| Modelos locales | La función básica no necesita un modelo. pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar |
| Coste | Sin pago a un modelo en la ruta básica. No exige LLM; infraestructura y generación de vectores se presupuestan aparte |
| Equipo | Preparación según la ruta elegida. Python para cliente; servidor o modo local según guía; vectores de prueba |

pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar

## Cómo empezar

Requiere preparación técnica. [Entender los términos](../vocabulario.md).

**Antes de empezar:**

- Python para cliente
- servidor o modo local según guía
- vectores de prueba

1. Abre la guía original enlazada y elige tu sistema y la ruta de aplicación,plugin o código fuente que corresponda.
2. Prepara los requisitos de la lista y sigue esa ruta paso a paso en un entorno de prueba. Esta ficha no propone un comando cuando no se seleccionó uno verificable.

Instalación revisada en documentos; no ejecutada por Alexandría. Los comandos conservan la sintaxis del autor: adapta la activación del entorno y las variables a tu sistema.

[Instrucciones originales de instalación](https://github.com/milvus-io/milvus/blob/master/README.md)

**Si necesitas ayuda paso a paso**, copia este encargo en tu asistente:

> Quiero usar Milvus para mi objetivo y necesito pasos guiados. Lee https://github.com/milvus-io/milvus/blob/master/README.md. Pregunta mi sistema operativo, comprueba cuenta, costes y dependencias y guíame una acción a la vez hasta una primera prueba pequeña. Distingue tu ayuda para instalar del acceso al modelo que usará la aplicación.

## Tu primera prueba

Crea una colección, inserta tres vectores y busca uno cercano.

**Qué comprobar:** Puedes contrastar el vecino y los metadatos devueltos.

Prueba propuesta para ti; Alexandría no la ejecutó en este proyecto.

## Casos de uso

- Buscar productos por similitud
- Indexar embeddings a gran escala

## ¿Es para ti?

| ✅ Elígelo si… | ⛔ Evítalo si… |
|---|---|
| Tu objetivo encaja con estos ejemplos: Buscar productos por similitud; Indexar embeddings a gran escala | Necesitas funciones o garantías fuera del alcance descrito; revisa los límites y requisitos antes de elegirlo |

**Limitaciones:** pymilvus es el cliente y no toda la infraestructura del servidor; elige explícitamente el modo antes de instalar

## Stack y modelos

- **Stack:** Python para cliente; servidor o modo local según guía; vectores de prueba
- **Etiquetas:** `vector-db` `rag` `go` `docker`
- **Modo de instalación sugerido:** ⏳ **Diferir** — pesado: solo si llega a finalista

## Alternativas (elige una)

| Repo | ⭐ | Qué hace |
|---|---:|---|
| [Qdrant](qdrant.md) | 35.6k | Base de datos vectorial de alto rendimiento escrita en Rust, con filtros y búsqueda híbrida. |
| [Chroma](chroma.md) | 29.7k | Base de datos de búsqueda para IA, la más sencilla para empezar con embeddings en local. |
| [pgvector](pgvector.md) | 23.7k | Extensión de PostgreSQL para búsqueda de similitud vectorial junto a tus datos relacionales. |

## Enlaces

- 🐙 GitHub: [milvus-io/milvus](https://github.com/milvus-io/milvus)
- 🌐 Web: <https://milvus.io>

## Fuentes y alcance de revisión

Acceso revisado el 2026-11-15. Lectura de documentación; no prueba de instalación o ejecución.

Categoría confirmada en la revisión individual. Ejemplos ilustrativos; compatibilidad documental.

- [Fuente 1](https://github.com/milvus-io/milvus/blob/master/README.md)

---

<sub>Generado por `uv run repo-intelligence guide build` desde `INDICE_IA.json` + `INDICE_IA.detalle.json`. No edites este archivo a mano. Datos de GitHub verificados el 2026-11-14.</sub>
